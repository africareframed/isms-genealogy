import { defineCollection, reference } from 'astro:content';
import { glob, type Loader } from 'astro/loaders';
import { z } from 'astro/zod';
import { readdir, readFile } from 'node:fs/promises';
import path from 'node:path';
import { parse } from 'yaml';
import { ERA_IDS, THREAD_IDS } from './lib/site';

const status = z.enum(['draft', 'checked']).default('draft');

/* Isms: one Markdown file each in src/content/isms. The body is the introduction. */
const isms = defineCollection({
  loader: glob({ pattern: '*.md', base: './src/content/isms' }),
  schema: z.object({
    title: z.string(),
    family: z.enum(['transcendence', 'acceleration', 'risk', 'protection']),
    order: z.number(),
    ready: z.boolean().default(false),
    summary: z.string(),
    includes: z.array(z.string()).default([]),
    aka: z.string().optional(),
    image: reference('images').optional(),
    pageImage: reference('images').optional(), // the vertical (4:5) image at the top of the page
    lead: z.string().optional(),
    holders: z.array(z.object({ name: z.string(), note: z.string() })).default([]),
    words: z.array(z.string()).default([]),
    themes: z.array(reference('themes')).default([]),
    disputes: z.string().optional(),
    born: reference('entries').optional(), // the moment the movement got its name, shown in the history of AI
    status,
  }),
});

/* Themes: one Markdown file each in src/content/themes. No timeline of their own. */
const themes = defineCollection({
  loader: glob({ pattern: '*.md', base: './src/content/themes' }),
  schema: z.object({
    title: z.string(), // the question, e.g. "Who controls it?"
    topic: z.string().optional(), // a one-word label above it, e.g. "Power"
    kind: z.enum(['question', 'critics']).default('question'),
    order: z.number(),
    ready: z.boolean().default(false),
    summary: z.string(),
    includes: z.array(z.string()).default([]),
    image: reference('images').optional(),
    pageImage: reference('images').optional(), // the vertical (4:5) image at the top of the page
    lead: z.string().optional(),
    isms: z.array(z.object({ ism: reference('isms'), text: z.string() })).default([]),
    strands: z
      .array(z.object({ name: z.string(), text: z.string(), source: z.string().optional() }))
      .default([]),
    words: z.array(z.string()).default([]),
    disputes: z.string().optional(),
    status,
  }),
});

/* Timeline entries: one YAML file per ism in src/data/entries, holding a list.
   Each entry's id becomes "<ism>/<id>". */
const entriesLoader: Loader = {
  name: 'entries-loader',
  load: async ({ store, parseData, generateDigest, logger }) => {
    store.clear();
    const dir = path.join(process.cwd(), 'src/data/entries');
    const files = (await readdir(dir)).filter((f) => f.endsWith('.yaml'));
    for (const f of files) {
      const doc = parse(await readFile(path.join(dir, f), 'utf8'));
      if (!doc?.ism || !Array.isArray(doc.entries)) {
        logger.warn(`${f}: expected "ism" and "entries"`);
        continue;
      }
      for (const raw of doc.entries) {
        const { id: localId, ...rest } = raw;
        const id = `${doc.ism}/${localId}`;
        const data = await parseData({ id, data: { ...rest, ism: doc.ism } });
        store.set({ id, data, digest: generateDigest(data) });
      }
    }
  },
};

const entries = defineCollection({
  loader: entriesLoader,
  schema: z.object({
    ism: reference('isms'),
    year: z.number().int(),
    month: z.number().int().min(1).max(12).optional(),
    yearLabel: z.string().optional(),
    title: z.string(),
    who: z.string().optional(),
    relation: z.enum([
      'milestone',
      'institutional-root',
      'definition',
      'coined',
      'claimed',
      'attributed',
      'reacted-against',
    ]),
    tagLabel: z.string().optional(),
    text: z.string(),
    source: z.string(),
    sourceUrl: z.string().optional(),
    themes: z.array(reference('themes')).default([]),
    image: reference('images').optional(),
    status,
  }),
});

/* Lists of items with ids, one or more YAML files per folder (one file per ism keeps
   parallel work free of merge conflicts). */
const listLoader = (folder: string): Loader => ({
  name: `list-loader:${folder}`,
  load: async ({ store, parseData, generateDigest, logger }) => {
    store.clear();
    const dir = path.join(process.cwd(), 'src/data', folder);
    for (const f of (await readdir(dir)).filter((x) => x.endsWith('.yaml')).sort()) {
      const list = parse(await readFile(path.join(dir, f), 'utf8')) ?? [];
      if (!Array.isArray(list)) {
        logger.warn(`${folder}/${f}: expected a list`);
        continue;
      }
      for (const { id, ...rest } of list) {
        if (store.has(id)) logger.warn(`${folder}/${f}: duplicate id "${id}"`);
        const data = await parseData({ id, data: rest });
        store.set({ id, data, digest: generateDigest(data) });
      }
    }
  },
});

/* Vocabulary: the movements' own words, src/data/words/*.yaml. */
const words = defineCollection({
  loader: listLoader('words'),
  schema: z.object({
    word: z.string(),
    definition: z.string(), // one or two plain sentences
    coinedBy: z.string().optional(), // who coined it or first used it in this sense
    year: z.number().optional(), // year of coinage or earliest documented use
    yearLabel: z.string().optional(), // e.g. "c. 1960" when the year is approximate
    origin: z.string(), // the source that documents the coinage or first use
    sourceUrl: z.string().optional(),
    isms: z.array(reference('isms')).default([]),
    technical: z.boolean().default(false), // a term for how AI is built or behaves: the 'Technical terms' filter
    status,
  }),
});

/* The history of AI: src/data/history/<nn>-<era>.yaml, one file per era. Newest first on the page.
   Years before the common era are negative, with a yearLabel such as "c. 750 BCE". */
const history = defineCollection({
  loader: listLoader('history'),
  schema: z.object({
    era: z.enum(ERA_IDS),
    thread: z.enum(THREAD_IDS).optional(), // the line of the story it belongs to most
    year: z.number().int(),
    month: z.number().int().min(1).max(12).optional(),
    // the day, only to order moments that share a year and month (newest first)
    day: z.number().int().min(1).max(31).optional(),
    yearLabel: z.string().optional(),
    title: z.string(),
    line: z.string(), // one short line shown before the moment is opened
    who: z.string().optional(),
    text: z.string(), // two to four sentences
    source: z.string(),
    sourceUrl: z.string().optional(),
    isms: z.array(reference('isms')).default([]), // movements this moment shaped or that reacted to it
    themes: z.array(reference('themes')).default([]), // key words
    image: reference('images').optional(),
    status,
  }),
});

/* Notable figures: src/data/figures/<ism>.yaml. Portraits are added by the project team only. */
const figures = defineCollection({
  loader: listLoader('figures'),
  schema: z.object({
    name: z.string(),
    lifespan: z.string().optional(),
    isms: z.array(reference('isms')),
    note: z.string(),
    entry: reference('entries').optional(),
    portrait: z.string().optional(),
    portraitCredit: z.string().optional(),
    portraitLicence: z.string().optional(),
  }),
});

/* Images: src/data/images/*.yaml. No file yet = a labelled placeholder. */
const images = defineCollection({
  loader: listLoader('images'),
  schema: z.object({
    title: z.string(),
    date: z.string().optional(),
    creator: z.string().optional(),
    holder: z.string().optional(),
    rights: z.enum(['public-domain', 'open-licence', 'cleared', 'to-check']),
    licence: z.string().optional(), // shown to readers as the credit
    note: z.string().optional(), // for the project only, never shown
    file: z.string().optional(),
    fit: z.enum(['cover', 'contain']).default('cover'),
    alt: z.string().optional(),
    sourceUrl: z.string().optional(),
  }),
});

/* People (owner, 23 Nov 2026): src/data/people/*.yaml, who is on the People page, with portrait and credit.
   Identity only; movements, moments and words are worked out from the rest of the site (src/lib/people.ts). */
const people = defineCollection({
  loader: listLoader('people'),
  schema: z.object({
    name: z.string(),
    aliases: z.array(z.string()).default([]), // other spellings used in the history and the vocabulary
    lifespan: z.string().optional(),
    portrait: z
      .object({
        file: z.string(), // in public/portraits, 600 x 750
        credit: z.string().optional(), // photographer or artist
        licence: z.string(), // shown to readers, naming the source
        sourceUrl: z.string().optional(),
        caveat: z.string().optional(), // e.g. a portrait whose sitter historians doubt
      })
      .optional(),
  }),
});

export const collections = { isms, themes, entries, figures, images, words, history, people };
