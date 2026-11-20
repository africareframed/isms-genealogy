import { getCollection } from 'astro:content';
import { readdirSync, readFileSync } from 'node:fs';
import { parse } from 'yaml';
import { ERAS } from './site';

const hasItems = (folder: string) => {
  try {
    return readdirSync(folder)
      .filter((f) => f.endsWith('.yaml'))
      .some((f) => ((parse(readFileSync(`${folder}/${f}`, 'utf8')) ?? []) as unknown[]).length > 0);
  } catch {
    return false;
  }
};

/* An empty collection makes the build warn, so each one is read only once it holds items. */
export const getHistory = async () =>
  hasItems('src/data/history')
    ? (await getCollection('history')).sort(
        (a, b) => b.data.year - a.data.year || (b.data.month ?? 0) - (a.data.month ?? 0),
      )
    : [];

export const getWords = async () =>
  hasItems('src/data/words') ? (await getCollection('words')).sort((a, b) => (a.data.year ?? 0) - (b.data.year ?? 0)) : [];

/** The years an era covers: from its start up to the start of the next, newer one. */
export const eraBounds = (id: string) => {
  const i = ERAS.findIndex((e) => e.id === id);
  return { from: ERAS[i].from, to: i === 0 ? Infinity : ERAS[i - 1].from };
};

export const momentAnchor = (id: string) => `h-${id}`;
export const eraAnchor = (id: string) => `h-era-${id}`;
