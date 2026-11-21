export const SITE_NAME = 'Made Minds';
export const SITE_TITLE = 'A genealogy of the ideas behind AI';
export const MAP_DATE = '20 November 2026';

export const FAMILIES = [
  { id: 'transcendence', name: 'Transcendence', colour: '#C9F25B', text: 'The vision of a future beyond human limits.' },
  { id: 'risk', name: 'Risk', colour: '#F5A3BC', text: 'The fear that AI could end us, and the work to prevent it.' },
  { id: 'acceleration', name: 'Acceleration', colour: '#D8461C', text: 'The conviction that the answer is more technology, faster.' },
] as const;

/* The eras of the history of AI, newest first. Each history moment names one. */
export const ERAS = [
  { id: 'generative', name: 'The generative race', span: '2022 to now', from: 2022, text: 'Chatbots reach the public, the labs race to build ever larger data centres, and states start to write AI laws.' },
  { id: 'scale', name: 'Transformers and scale', span: '2017 to 2022', from: 2017, text: 'One architecture, the transformer, trained on ever more text and computing power.' },
  { id: 'deep-learning', name: 'Deep learning', span: '2012 to 2017', from: 2012, text: 'Neural networks return, running on graphics chips and large datasets, and beat people at Go.' },
  { id: 'learning', name: 'Learning from data', span: '1993 to 2012', from: 1993, text: 'Statistics takes over from hand-written rules, and machines beat champions at chess and quiz shows.' },
  { id: 'winters', name: 'Expert systems and the winters', span: '1974 to 1993', from: 1974, text: 'Rule-based expert systems boom in business, and funding for AI dries up twice.' },
  { id: 'birth', name: 'The birth of AI', span: '1943 to 1974', from: 1943, text: 'The field is named, and the first programs prove theorems, learn and talk.' },
  { id: 'reckoning', name: 'Reckoning machines', span: '1642 to 1943', from: 1642, text: 'Calculating machines, the logic of thought and the idea of a universal computer.' },
  { id: 'automata', name: 'Myths and automata', span: 'Antiquity to 1642', from: -10000, text: 'Myths of made beings, and the first machines that move by themselves.' },
] as const;
export const ERA_IDS = ERAS.map((e) => e.id) as [string, ...string[]];

/* The threads that run through the history of AI. Each moment names the one it belongs to most. */
export const THREADS = [
  { id: 'made-beings', name: 'Made beings' },
  { id: 'reasoning', name: 'Logic and calculation' },
  { id: 'symbols-networks', name: 'Symbols or networks' },
  { id: 'talking', name: 'Machines that talk' },
  { id: 'games', name: 'Machines at play' },
  { id: 'booms-winters', name: 'Booms and winters' },
  { id: 'compute', name: 'Chips and data' },
  { id: 'warnings', name: 'Warnings' },
  { id: 'law', name: 'Laws and states' },
] as const;
export const THREAD_IDS = THREADS.map((t) => t.id) as [string, ...string[]];
export const threadName = (id?: string) => THREADS.find((t) => t.id === id)?.name;

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

// The line under a movement's name: "Often called the doomers · includes the call to pause and Humanist AI".
// Strands are written in the case they are shown in (common nouns lower case, names such as Humanist AI capitalised).
const andList = (xs: string[]) => (xs.length < 2 ? xs.join('') : `${xs.slice(0, -1).join(', ')} and ${xs[xs.length - 1]}`);
export const strandsLine = (aka: string | undefined, includes: string[]) =>
  [aka, includes.length ? `${aka ? 'includes' : 'Includes'} ${andList(includes)}` : ''].filter(Boolean).join(' · ');

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
