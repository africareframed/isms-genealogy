# A genealogy of the isms behind artificial intelligence

Instructions for every Claude session and agent working in this repository. Read `WORKPLAN.md` next: it says what is done and what comes next.

## The project

A website, built first to pitch funders for an exhibition. It maps the isms of the AI industry and traces each one back in time. Owner: Thomas (GitHub account `africareframed`). The site is called **Made Minds** (owner, 20 November 2026), always with the subtitle "A genealogy of the ideas behind AI" (changed on 20 November 2026 at the owner's request; it was "A genealogy of the isms behind artificial intelligence"). The domain mademinds.org is the owner's to check and buy.

**Never open, read, clone or change `africareframed/africareframed-site` or any other repository.** Only this one.

## The framework (decided, do not change without the owner)

- **An ism** is mapped when it is a whole view of AI (what it is, where it is heading, what to do), born in the tech world, and named by its own people, with founding texts, vocabulary and institutions to trace.
- **Six isms in three families**, in this order (owner, 22 Nov 2026: from the farthest future towards the present, from the most eager about the machine to the most wary; numbered 01–06 in this order):
  - Transcendence: Transhumanism · Singularitarianism (includes successionism)
  - Acceleration: Effective accelerationism (includes neoreaction and the network state) · Techno-optimism (includes augmentation)
  - Risk: Rationalism (often called the doomers; includes the call to pause and Humanist AI, owner 21 Nov 2026) · Effective altruism (includes longtermism)
- **Below the six: key words and the vocabulary** (owner, 20 Nov 2026). The broad themes are gone. Instead, narrow terms people hear again and again in the debate. Every term is in the **vocabulary** (`src/data/words/`: what it means, who coined it and when, which isms use it). About a dozen are **key words** with an illustrated card and their own page (`src/content/themes/`, the old theme files): Scaling laws (Perceptron card), Compute (H100 chips), Abundance (meter), Augmentation (mouse), Facial recognition (camera), Citizens' assemblies (kleroterion), Luddite (the Luddite engraving); to come with new cards: Open weights, Alignment, AGI, The pause, p(doom). No separate critics section: criticism sits in each page's "Who disputes it" and in narrow words of its own. More key words are added over time; each stays narrow.
- **Three tracks** (owner, 20 Nov 2026), in this order (owner, 22 Nov 2026): **History of AI** (what happened: machines, ideas, labs, money, laws; the ground all six react to), **Movements** (who believes what) and **Vocabulary** (the words they fight with). The menu shows these three in this order. The history links the other two by data: each moment is tagged with movements and key words; each era shows the movements named in it (`born` on each ism) and the words coined in it (by year); movement and key-word pages list "In the history of AI".
- **Headings say "movements"**; "isms" stays the working word in this file and the repository. The home page has three sections, each under a plain header of one word or name (History of AI, Movements, Vocabulary; owner, 20 Nov 2026, reordered 22 Nov 2026 so the history comes first): the **History of AI** as one panorama card (11:5, a quarter taller than a movement card so it reads as the biggest; the 4:5 version on phones), then the six in three family rows (01–06), then **Vocabulary**: the illustrated key words first, then the other words as a plain list leading to the full vocabulary page (the only place with a filter, by family). No explainers of how the site works: the design should make it clear (owner, 20 Nov 2026). The hero (owner, 21 Nov 2026, option A): the subtitle and the map date on one line over a thin rule; below it "Transcend. Accelerate. Pause." across the page (the families' order, owner 22 Nov 2026); under that, a bold standfirst on columns 1–5 ("ChatGPT … felt like year zero." with "It wasn't." on its own line), column 6 left empty, and three short paragraphs on columns 7–12, in line with the right-hand movement cards below, the last linking the three sections; the two columns stack under 900 px.
- **Ism page:** Introduction · Who holds it now · Notable figures · Its words · Its themes · Who disputes it · then the history, newest first, back to the oldest root.
- **History of AI page:** Introduction · the eras as an index · then, newest first, each era (name, span, one line, movements named in it, words from it) and its moments. A moment shows year, title and one line, and folds open to who, two to four sentences, the source and its tags. The deepest timeline on the site: about 80 moments, back to the oldest documented root.
- **Key-word page:** Introduction (what it means, who coined it) · How the movements see it (one line each, only where a movement has a view) · Strands · Related words · In the movements' histories (built from tags) · Who disputes it. The section menu lists only the sections a page has.
- **Navigation:** grid → page → back to the grid. No sideways scrolling, no scroll-jacking. Theme tags are the only links between pages.
- **Motion** (owner, 21 Nov 2026, live as an experiment on the History of AI card only): first one black square ratchets into place smoothly as the reader scrolls, one way only, from the moment the card's top edge enters the screen, and locks once the whole card is in view, so the reader sees the motion is theirs. After that, five chosen pieces of the card's second state (`collage-history-b`) each belong to a scroll position, close enough that all five land while the whole card is still on screen (at most 6% of the screen apart), so a scroll brings them 1, 2, 3 and scrolling back takes them away, last first; people can scroll back and forth to study them. A hard cut, no flicker. The pieces: Deep Blue over Kasparov's face, a grey slip beside the square, the man inside the Turk, an orange slip, a square of Lee Sedol. The whole image is the way into the history: a click anywhere on it, pieces included, opens the history page (owner: a second meaning for a click confused it). Nothing moves when the page is still, hover included; reduced motion gets the still card. Other cards stay still unless the owner says otherwise.
- Design follows the mockup (canvas "AI philosophies — website mockup"): white, Inter Tight + IBM Plex Mono, one accent `#D8461C`. Super clean, large type with presence, short texts.
- **One grid** (owner, 21 Nov 2026): 12 columns with one gutter inside the 1312 px container (`--g` 40 px; 32 px under 1100 px, 20 px under 640 px). Every layout is built from spans, so column edges fall on the same vertical lines on every page: movement rows 6 + 6, hero 5 + an empty column + 6, history card 5 + 7, page introductions 7 + 5, key-word cards and the era index 3 + 3 + 3 + 3, figures 4 + 4 + 4, the movements' rows on a key-word page 4 + 8. A span of n columns is `calc(var(--c) * n + var(--g) * (n - 1))`; equal splits use `repeat(n, 1fr)` with `column-gap: var(--g)`.

## Where content lives

| What | File |
| --- | --- |
| Ism card, introduction, holders, words, themes, disputes | `src/content/isms/<ism>.md` (body = introduction) |
| Theme page | `src/content/themes/<theme>.md` |
| Timeline entries | `src/data/entries/<ism>.yaml` |
| History of AI moments | `src/data/history/<nn>-<era>.yaml` (eras in `src/lib/site.ts`) |
| Notable figures | `src/data/figures/<ism>.yaml` |
| Images | `src/data/images/<ism>.yaml` (cards: `cards.yaml`) |
| Image files | `public/images/` |
| Portraits | `public/portraits/` (added by the owner only) |

Schemas are in `src/content.config.ts`; the build fails on a broken reference. Set `ready: true` on an ism or theme only when its page is complete. One file per ism means agents working on different isms never touch the same file.

## Writing rules

- British English. Plain words, sentences under 25 words, paragraphs of at most three sentences.
- Introduction: a lead sentence of what the ism holds today, then two short paragraphs that may reach into the past. Fulfilling, never long.
- Timeline entries: a title, who, and two to four sentences. Give `month` (1–12) when two entries share a year, so they sort newest first. Ten to sixteen entries per ism, from today back to its oldest documented root.
- Every entry has a real, specific source (author, title, publisher or venue, year) and, where possible, `sourceUrl` to a page you actually opened. Never invent a source.
- Mark each root's relation: `claimed` (the movement cites it as an ancestor), `attributed` (historians link it, the movement does not), `coined`, `definition`, `institutional-root`, `milestone`, `reacted-against`.
- Neutral and fair. Describe what people said and did; give critics their own section. No verdicts.
- Quotations: at most one per source, under 15 words. Paraphrase everything else.
- New text is `status: draft`. A separate checker agent, which has not seen the drafting, checks every claim against the sources and sets `status: checked` only when it holds.

## Image rules

- **Never AI-generated.** Human-made images only: documents, title pages, diagrams, machines, places, artworks, photographs of objects or events.
- **No portraits or photographs of real people**, whatever their licence (owner, 20 Nov 2026: too many people, too many images). Notable figures appear as names only: an index on each ism page where each name folds open to a short note and a link to its moment in the history. One exception (owner, 21 Nov 2026): the History of AI card and its timeline moments show Garry Kasparov (1997) and Lee Sedol (2016) from broadcast stills, which the owner cleared as fair use; no other images of people without the owner's say.
- Record every image in `src/data/images/` with title, date, rights (`public-domain`, `open-licence` + licence, `cleared`, `to-check`) and `sourceUrl` of the page where the licence was read. `licence` is the credit readers see in the caption, so it names the source, never who cleared it; clearance notes go in `note`, which is never shown (owner, 21 Nov 2026).
- Prefer Wikimedia Commons, the Library of Congress, the Internet Archive and museum open-access collections. Copyrighted items (book covers, press photos, film stills) stay `to-check` placeholders until the owner clears them.
- Downloads happen only after the owner approves a batch (a list of files with source, size and licence). They go to the owner's connected folder `isms-genealogy-images` and are then copied into `public/images/`.

### Collages (the house image style, from 20 Nov 2026)

**Why collage** (owner, 21 Nov 2026): AI is itself a kind of collage. Its training material is a collage of human knowledge, and in the AI's reality we are becoming a collage too. AI hides its seams; our collages show them: human-made fragments, cut along the grid, out of register, each with its year and source. This is the reason behind every rule below.

The full recipe lives in the design system **Made Minds Illustration** (https://claude.ai/artifact/AKayCErJw2u8QYjb3bzDSN, slug `4b7a91e1-db02-4604-a0e6-7241adc16c37`): rules, the step-by-step recipe, the seven theme cards as references, the owner's decisions and the versions he turned down. Read its `project/README.md` and `project/01-recipe.md` before making or changing a collage. When the owner changes the style, update the guide first, then the engine. It holds all fourteen cards (six movements in family colours, eight key words in grey), the History of AI card and its motion, and the family colours as tokens.

Every ism and theme card is a collage made in code by `scripts/collages.py` (`python3 scripts/collages.py <id>`), from archive images already cleared. Rules: archive fragments only (objects, drawings, engravings, machines, charts; no title pages or text documents); fragments cut along a 100 px grid, with a few squares shifted, inverted or removed; two bold colour fields under them, slightly out of register; family colour for isms, always a highlighter colour (owner, 22 Nov 2026: Transcendence `#C9F25B`, Acceleration `#FF9F4F`, Risk `#F5A3BC`; `#D8461C` stays the site's one accent and the History of AI card's orange), grey for themes; type only when it carries meaning (a date, a word of the ism's own) and then always whole, never cut; small mono labels with year and source on paper strips. Guiding rule (owner, 20 Nov): one strong object, one exact fact, plenty of air, as in the Scale collage (the Perceptron with 10²⁵). Big type is rare (owner, 20 Nov): most cards have none, and type never captions its object (no "$500" by a chip, no "0 kWh" by a meter). It earns its place only when it comes from another time than the object, so the viewer closes the gap. A concrete object or a figure in action beats a symbol or an artwork. Each collage's record in `src/data/images/collages.yaml` names its sources and the licence that follows from them. Every card comes in two formats: the card for the grid (`collage-<id>`, 1500 × 1000 for themes) and a vertical page image (`collage-<id>-tall`, 1200 × 1500, 4:5) composed again for the top of its page and set as `pageImage`. Never stretch a photograph: the box keeps the crop's proportions (the engine warns).

## Build and check

```
npm install
npm run build      # must pass with no warnings before any commit
```

The build is flat `.html` files with relative links, so `dist/` works as a private preview artifact, on GitHub Pages or on a domain.

The owner made the site public on 20 November 2026: the repository is public and GitHub Pages serves the `gh-pages` branch at https://africareframed.github.io/isms-genealogy/. After merging into `main`, run `npm run deploy` to update it. Every page carries `noindex` until the owner launches it properly. Anything new that is public in a different way (a domain, search indexing, announcements) still needs the owner's explicit go.

## Git

Commit small, with clear messages. Agents working on one ism use a branch `ism/<ism>` and push it; the coordinating session merges into `main` after the build passes.
