export const SITE_NAME = 'Radical Romance'; // owner, 25 Nov 2026: Made Minds dropped altogether
export const SITE_TITLE = 'A genealogy of the ideas around the rise of AI'; // owner, 25 Nov 2026; it was 'A genealogy of the ideas behind AI'
export const MAP_DATE = '25 November 2026';

export const FAMILIES = [
  // Six families of two movements each (owner, 25 Nov 2026: the new framework, doc "A new framing of the AI
  // movements"), named by a verb for what they want done, ordered from the largest claims about what AI will
  // become to the smallest. Family colours are highlighter colours. `intro` heads the family's row on the home page
  // (owner, 25 Nov 2026): it opens with the family's name and what defines it, never "Both", then how its
  // two movements differ.
  { id: 'transcend', name: 'Transcend', colour: '#C9F25B', text: 'The vision of a future beyond human limits.',
    intro: 'Transcend is the vision of a future beyond human limits, with AI as the way across. Its movements differ over who crosses. Transhumanism would free people from ageing and the limits of body and mind; Singularitarianism expects machines to surpass us and carry history past prediction.' },
  { id: 'accelerate', name: 'Accelerate', colour: '#FF9F4F', text: 'The conviction that the answer is more technology, faster.',
    intro: 'Accelerate is the conviction that the answer is more technology, faster, and that slowing down is the greater danger. Its movements differ over whom it serves. Techno-optimism trusts markets to make everyone richer; American Dynamism builds national strength for a race with China.' },
  { id: 'prevent', name: 'Prevent', colour: '#F5A3BC', text: 'The work to stop AI from ending us.',
    intro: 'Prevent is the work to stop AI from ending us, should a machine more capable than we are slip out of control. Its movements differ over whether it can be made safe in time. AI safety works to align and govern it as it is built; Pause holds it cannot, and would stop superintelligence being built.' },
  { id: 'protect', name: 'Protect', colour: '#73C7F2', text: 'The demand to shield people now, with limits and liability for the builders.',
    intro: 'Protect is the demand to shield people living now, not a humanity that may come, and to make the builders answer for harm. Its movements differ in what they defend first. Pro-human defends work, children and humans in charge; AI ethics demands justice against bias, surveillance and hidden labour.' },
  { id: 'reclaim', name: 'Reclaim', colour: '#C3A6FF', text: 'The resolve to change who owns and decides: to build our own, or to refuse.',
    intro: 'Reclaim is the resolve to change who owns AI and who decides about it. Its movements give two answers: build our own, or refuse. Digital sovereignty would build alternatives in public hands; Neo-Luddism claims the right to refuse, and workers\' say over which machines come in.' },
  // Doubt is highlighter turquoise (owner, 25 Nov 2026): the gap in the set, furthest from the other five.
  { id: 'doubt', name: 'Doubt', colour: '#2EE6C8', text: 'The case that AI is less than its makers claim.',
    intro: 'Doubt is the case that AI is less than its makers claim, and that policy should start from evidence. Its movements differ over how much of it is real. Normal technology sees a powerful but ordinary tool, spreading slowly like electricity; AI skepticism sees imitation without understanding, and money sunk into a bubble.' },
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
  { id: 'war', name: 'Machines at war' }, // owner, 23 Nov 2026: AI in war, from Palantir to the drone war
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

/* People (owner, 23 Nov 2026): the tags researched and checked for each person (src/data/people-facts/). */
export const ROLES = [
  { id: 'researcher', name: 'Researcher or engineer', line: 'people known in this story for research or engineering' },
  { id: 'founder', name: 'Founder or executive', line: 'people who founded or ran a company, lab or organisation' },
  { id: 'writer', name: 'Philosopher or writer', line: 'philosophers, authors, journalists and futurists' },
  { id: 'critic', name: 'Critic or campaigner', line: 'critics of AI, activists and campaign organisers' },
  { id: 'official', name: 'Politician or official', line: 'politicians, officials, military and religious leaders acting in public life' },
  { id: 'judge', name: 'Judge', line: 'judges whose rulings shape AI' },
] as const;
export const ROLE_IDS = ROLES.map((r) => r.id) as unknown as [string, ...string[]];
export const LABS = [
  { id: 'openai', name: 'OpenAI' },
  { id: 'google', name: 'Google and DeepMind' },
  { id: 'anthropic', name: 'Anthropic' },
  { id: 'meta', name: 'Meta' },
  { id: 'microsoft', name: 'Microsoft' },
  { id: 'palantir', name: 'Palantir' },
] as const;
export const LAB_IDS = LABS.map((l) => l.id) as unknown as [string, ...string[]];
export const LETTERS = [
  { id: 'pause-2023', name: 'The pause letter', when: 'March 2023', line: "the Future of Life Institute's call to pause the training of AI systems more powerful than GPT-4" },
  { id: 'extinction-2023', name: 'The extinction statement', when: 'May 2023', line: "the Center for AI Safety's one sentence ranking extinction risk from AI with pandemics and nuclear war" },
  { id: 'superintelligence-2025', name: 'The superintelligence statement', when: 'October 2025', line: 'the call to ban superintelligence until it can be built safely and has public support' },
] as const;
export const LETTER_IDS = LETTERS.map((l) => l.id) as unknown as [string, ...string[]];
