export const SITE_NAME = '[Working title]';
export const SITE_TITLE = 'A genealogy of the isms behind artificial intelligence';
export const MAP_DATE = '20 November 2026';

export const FAMILIES = [
  { id: 'transcendence', name: 'Transcendence', text: 'The vision of a future beyond human limits.' },
  { id: 'risk', name: 'Risk', text: 'The fear that AI could end us, and the work to prevent it.' },
  { id: 'acceleration', name: 'Acceleration', text: 'The conviction that the answer is more technology, faster.' },
] as const;

export const RELATIONS: Record<string, string> = {
  milestone: 'Milestone',
  'institutional-root': 'Institutional root',
  definition: 'Modern definition',
  coined: 'Claimed ancestor · coined the word',
  claimed: 'Claimed ancestor · cited',
  attributed: 'Attributed by historians',
  'reacted-against': 'Reacted against',
};

/** Pages sit flat at the root, so every link is relative and works under any base path. */
export const pageHref = (slug?: string) => (slug ? `${slug}.html` : 'index.html');

export const eraOf = (year: number) => (year >= 1800 ? `${Math.floor(year / 10) * 10}s` : 'Before 1800');
export const eraId = (era: string) => 'era-' + era.toLowerCase().replace(/\s+/g, '-');

export const yearText = (year: number, label?: string) =>
  label ?? (year < 0 ? `c. ${-year} BCE` : String(year));

export const rightsLabel = (rights: string, licence?: string) =>
  rights === 'public-domain'
    ? 'public domain'
    : rights === 'to-check'
      ? 'rights to check'
      : (licence ?? 'licensed');
