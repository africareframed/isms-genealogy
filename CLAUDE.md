# A genealogy of the isms behind artificial intelligence

Instructions for every Claude session and agent working in this repository. Read `WORKPLAN.md` next: it says what is done and what comes next.

## The project

A website, built first to pitch funders for an exhibition. It maps the isms of the AI industry and traces each one back in time. Owner: Thomas (GitHub account `africareframed`). The working title of the site is still open: write `[Working title]`.

**Never open, read, clone or change `africareframed/africareframed-site` or any other repository.** Only this one.

## The framework (decided, do not change without the owner)

- **An ism** is mapped when it is a whole view of AI (what it is, where it is heading, what to do), born in the tech world, and named by its own people, with founding texts, vocabulary and institutions to trace.
- **Six isms in three families:**
  - Transcendence: Transhumanism · Singularitarianism (includes successionism)
  - Risk: Rationalism (includes the call to pause) · Effective altruism and longtermism
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
- Timeline entries: a title, who, and two to four sentences. Ten to sixteen entries per ism, from today back to its oldest documented root.
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

## Build and check

```
npm install
npm run build      # must pass with no warnings before any commit
```

The build is flat `.html` files with relative links, so `dist/` works as a private preview artifact, on GitHub Pages or on a domain. Going public needs the owner's explicit go.

## Git

Commit small, with clear messages. Agents working on one ism use a branch `ism/<ism>` and push it; the coordinating session merges into `main` after the build passes.
