# A genealogy of the isms behind artificial intelligence

Instructions for every Claude session and agent working in this repository. Read `WORKPLAN.md` next: it says what is done and what comes next.

## The project

A website, built first to pitch funders for an exhibition. It maps the isms of the AI industry and traces each one back in time. Owner: Thomas (GitHub account `africareframed`). The site is called **Made Minds** (owner, 20 November 2026), always with the subtitle "A genealogy of the isms behind artificial intelligence". The domain mademinds.org is the owner's to check and buy.

**Never open, read, clone or change `africareframed/africareframed-site` or any other repository.** Only this one.

## The framework (decided, do not change without the owner)

- **An ism** is mapped when it is a whole view of AI (what it is, where it is heading, what to do), born in the tech world, and named by its own people, with founding texts, vocabulary and institutions to trace.
- **Six isms in three families:**
  - Transcendence: Transhumanism · Singularitarianism (includes successionism)
  - Risk: Rationalism (often called the doomers; includes the call to pause) · Effective altruism (includes longtermism)
  - Acceleration: Effective accelerationism (includes neoreaction and the network state) · Techno-optimism (includes augmentation)
- **Seven themes**, with no timeline of their own: Abundance (incl. post-work) · Power (AI nationalism, state-led AI, the populist right) · The tool (open-source AI) · Scale · Rights and dignity (rights-based regulation, religious voices) · Self-determination (data sovereignty, democratic plurality) · Critique (AI ethics, political economy, normal technology).
- **Ism page:** Introduction · Who holds it now · Notable figures · Its words · Its themes · Who disputes it · then the history, newest first, back to the oldest root.
- **Theme page:** Introduction · How the isms see it (one line per ism) · Strands · Its words · In the isms' histories (built automatically from theme tags) · Who disputes it.
- **Navigation:** grid → page → back to the grid. No sideways scrolling, no scroll-jacking. Theme tags are the only links between pages.
- Design follows the mockup (canvas "AI philosophies — website mockup"): white, Inter Tight + IBM Plex Mono, one accent `#D8461C`. Super clean, large type with presence, short texts.

## Where content lives

| What | File |
| --- | --- |
| Ism card, introduction, holders, words, themes, disputes | `src/content/isms/<ism>.md` (body = introduction) |
| Theme page | `src/content/themes/<theme>.md` |
| Timeline entries | `src/data/entries/<ism>.yaml` |
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
- **No portraits or photographs of real people** downloaded or added by Claude, whatever their licence. Figures get an empty portrait slot; the owner fills it.
- Record every image in `src/data/images/` with title, date, rights (`public-domain`, `open-licence` + licence, `cleared`, `to-check`) and `sourceUrl` of the page where the licence was read.
- Prefer Wikimedia Commons, the Library of Congress, the Internet Archive and museum open-access collections. Copyrighted items (book covers, press photos, film stills) stay `to-check` placeholders until the owner clears them.
- Downloads happen only after the owner approves a batch (a list of files with source, size and licence). They go to the owner's connected folder `isms-genealogy-images` and are then copied into `public/images/`.

### Collages (the house image style, from 20 Nov 2026)

The full recipe lives in the design system **Made Minds Illustration** (https://claude.ai/artifact/AKayCErJw2u8QYjb3bzDSN, slug `4b7a91e1-db02-4604-a0e6-7241adc16c37`): rules, the step-by-step recipe, the seven theme cards as references, the owner's decisions and the versions he turned down. Read its `project/README.md` and `project/01-recipe.md` before making or changing a collage. When the owner changes the style, update the guide first, then the engine. The six ism cards are not in it yet: they are reworked next, then added with their family colours.

Every ism and theme card is a collage made in code by `scripts/collages.py` (`python3 scripts/collages.py <id>`), from archive images already cleared. Rules: archive fragments only (objects, drawings, engravings, machines, charts; no title pages or text documents); fragments cut along a 100 px grid, with a few squares shifted, inverted or removed; two bold colour fields under them, slightly out of register; family colour for isms (Transcendence `#C9F25B`, Risk `#F5A3BC`, Acceleration `#D8461C`), grey for themes; type only when it carries meaning (a date, a word of the ism's own) and then always whole, never cut; small mono labels with year and source on paper strips. Guiding rule (owner, 20 Nov): one strong object, one exact fact, plenty of air, as in the Scale collage (the Perceptron with 10²⁵). Big type is rare (owner, 20 Nov): most cards have none, and type never captions its object (no "$500" by a chip, no "0 kWh" by a meter). It earns its place only when it comes from another time than the object, so the viewer closes the gap. A concrete object or a figure in action beats a symbol or an artwork. Each collage's record in `src/data/images/collages.yaml` names its sources and the licence that follows from them. Every card comes in two formats: the card for the grid (`collage-<id>`, 1500 × 1000 for themes) and a vertical page image (`collage-<id>-tall`, 1200 × 1500, 4:5) composed again for the top of its page and set as `pageImage`. Never stretch a photograph: the box keeps the crop's proportions (the engine warns).

## Build and check

```
npm install
npm run build      # must pass with no warnings before any commit
```

The build is flat `.html` files with relative links, so `dist/` works as a private preview artifact, on GitHub Pages or on a domain.

The owner made the site public on 20 November 2026: the repository is public and GitHub Pages serves the `gh-pages` branch at https://africareframed.github.io/isms-genealogy/. After merging into `main`, run `npm run deploy` to update it. Every page carries `noindex` until the owner launches it properly. Anything new that is public in a different way (a domain, search indexing, announcements) still needs the owner's explicit go.

## Git

Commit small, with clear messages. Agents working on one ism use a branch `ism/<ism>` and push it; the coordinating session merges into `main` after the build passes.
