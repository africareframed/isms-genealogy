import { getCollection } from 'astro:content';
import { readdirSync } from 'node:fs';
import { getHistory, getWords, eraBounds } from './history';
import { ERAS, FAMILIES } from './site';

/* The People page (owner, 23 Nov 2026). Everything here is worked out from what the site already
   holds and has checked: a person's movements come from the notable figures, their moments from the
   History of AI and the movements' timelines, their words from the vocabulary. */

const esc = (s: string) => s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
/** A name, or any of its spellings, as a whole word: "Hinton" is not found in "Hintonia". */
export const namePattern = (names: string[]) =>
  new RegExp(`(?<![\\p{L}\\d-])(${[...names].sort((a, b) => b.length - a.length).map(esc).join('|')})(?![\\p{L}\\d-])`, 'u');
const plain = (name: string) => name.replace(/\s*\(.*?\)\s*/g, ' ').trim();

export const personAnchor = (id: string) => `p-${id}`;

const hasFacts = () => {
  try {
    return readdirSync('src/data/people-facts').some((f) => f.endsWith('.yaml'));
  } catch {
    return false;
  }
};

const eraOfYear = (year: number) => ERAS.find((e) => year >= eraBounds(e.id).from && year < eraBounds(e.id).to)?.id ?? ERAS[0].id;

export const getPeople = async () => {
  const people = await getCollection('people');
  const figures = await getCollection('figures');
  const isms = (await getCollection('isms')).sort((a, b) => a.data.order - b.data.order);
  const entries = await getCollection('entries');
  const moments = await getHistory();
  const words = await getWords();
  // checked facts only (scripts/people_facts.py copies nothing else); an empty folder would make the build warn
  const facts = new Map(
    (hasFacts() ? await getCollection('peopleFacts') : []).filter((f) => f.data.status === 'checked').map((f) => [f.id, f.data]),
  );
  const ismById = new Map(isms.map((i) => [i.id, i]));
  const familyOf = (ismId: string) => FAMILIES.find((f) => f.id === ismById.get(ismId)?.data.family);

  const list = people.map((p) => {
    const re = namePattern([p.data.name, ...p.data.aliases]);
    const figs = figures.filter((f) => re.test(plain(f.data.name)) && plain(f.data.name).match(re)?.[0].length === plain(f.data.name).length);
    // a moment counts when its "who" line or its text names the person
    const inHistory = moments.filter((m) => re.test(m.data.who ?? '') || re.test(m.data.text));
    const inTimelines = entries
      .filter((e) => re.test((e.data as { who?: string }).who ?? '') || re.test(e.data.text))
      .sort((a, b) => b.data.year - a.data.year);
    const coined = words.filter((w) => re.test(w.data.coinedBy ?? ''));
    const ismIds = [...new Set(figs.flatMap((f) => f.data.isms.map((r) => r.id)))].sort(
      (a, b) => (ismById.get(a)?.data.order ?? 99) - (ismById.get(b)?.data.order ?? 99),
    );
    // the era they made their mark in: their earliest moment whose "who" line names them (a mention in
    // another moment's text does not count, so Leibniz is not placed in Llull's century), else their
    // earliest moment of any kind, their earliest timeline entry, the entry their figure note points to,
    // or, for people with none of these (critics known for a word), the year they coined their first word
    const named = inHistory.filter((m) => re.test(m.data.who ?? ''));
    const firstMoment = named[named.length - 1] ?? inHistory[inHistory.length - 1];
    const figEntry = entries.find((e) => figs.some((f) => f.data.entry?.id === e.id));
    const firstEntry = inTimelines[inTimelines.length - 1] ?? figEntry;
    const coinedYears = coined.map((w) => w.data.year).filter((y): y is number => y !== undefined);
    const coinedYear = coinedYears.length ? Math.min(...coinedYears) : undefined;
    const firstYear = firstMoment?.data.year ?? firstEntry?.data.year ?? coinedYear;
    const era = firstMoment
      ? firstMoment.data.era
      : firstEntry
        ? eraOfYear(firstEntry.data.year)
        : coinedYear !== undefined
          ? eraOfYear(coinedYear)
          : undefined;
    const threads = [...new Set(inHistory.map((m) => m.data.thread).filter((t): t is string => Boolean(t)))];
    const fact = facts.get(p.id);
    return {
      id: p.id,
      name: p.data.name,
      lifespan: p.data.lifespan ?? figs.find((f) => f.data.lifespan)?.data.lifespan ?? fact?.lifespan,
      roles: fact?.roles ?? [],
      labs: fact?.labs ?? [],
      letters: fact?.letters ?? [],
      factNote: figs.length ? undefined : fact?.note,
      sources: fact?.sources ?? [],
      portrait: p.data.portrait,
      isms: ismIds,
      families: [...new Set(ismIds.map((i) => familyOf(i)?.id).filter((f): f is NonNullable<typeof f> => Boolean(f)))],
      notes: figs.map((f) => ({ ism: f.data.isms[0]?.id, note: f.data.note })),
      moments: inHistory,
      named, // the moments whose "who" line names them, newest first
      entries: inTimelines,
      words: coined,
      era,
      firstYear,
      threads,
    };
  });

  return list.sort((a, b) => (b.firstYear ?? 0) - (a.firstYear ?? 0) || a.name.localeCompare(b.name));
};

export type Person = Awaited<ReturnType<typeof getPeople>>[number];

/** Links names in a line of text to their tiles on the People page (the "who" line of a moment). */
export const linkNames = (text: string, people: { id: string; name: string; aliases?: string[] }[]) => {
  const parts: ({ text: string } | { text: string; id: string })[] = [];
  const named = people.map((p) => ({ id: p.id, re: namePattern([p.name, ...(p.aliases ?? [])]) }));
  let rest = text;
  while (rest.length) {
    let best: { at: number; len: number; id: string } | undefined;
    for (const n of named) {
      const m = n.re.exec(rest);
      if (m && (best === undefined || m.index < best.at || (m.index === best.at && m[0].length > best.len))) {
        best = { at: m.index, len: m[0].length, id: n.id };
      }
    }
    if (!best) {
      parts.push({ text: rest });
      break;
    }
    if (best.at > 0) parts.push({ text: rest.slice(0, best.at) });
    parts.push({ text: rest.slice(best.at, best.at + best.len), id: best.id });
    rest = rest.slice(best.at + best.len);
  }
  return parts;
};
