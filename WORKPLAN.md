# Work plan

Every session starts here: find the first stage that is not done, do the next piece, update this file, commit, push. Rules are in `CLAUDE.md`.

## The new framework on the live site (owner's go, 25 Nov 2026, 14:43)

Twelve movements in six families, and the new movement page (tested on Neo-Luddism) for all twelve. The owner, 25 Nov: no more fact-checking in this run beyond what is already done; everything new stays `status: draft` and its page shows "Draft · to be checked"; a checker pass comes later (phase 5).

**Now:** phases 1, 2 and 4 live; the Doubt colour and all twelve movement cards (3.1, 3.2); the home page as an atlas of the movements. Next: 3.3 (the design guide: the new cards), then phase 5 (checker pass on the draft text, and the doc and the site agree).

### How to pick up (read this first, every session)

1. Read `CLAUDE.md`, then this section. The first unticked box is the next step. The **Now** line above names the phase and branch.
2. `git fetch origin`, check out the branch on the **Now** line (create it from `main` if it does not exist yet), run `git status`. Uncommitted changes belong to the first unticked step: finish it, or discard them (`git checkout -- . && git clean -fd src public`) and redo it.
3. One box is one commit. Tick the box and update the **Now** line in the same commit, then push at once (`git -c push.negotiate=true push -u origin <branch>`). `npm run build` must pass with no warnings before every commit.
4. Deploy (`npm run deploy`) only at the lines marked **Deploy**, after merging into `main`. Between those points the live site stays as it is, so a stop half-way never leaves it broken.
5. Sources: the doc "A new framing of the AI movements" (https://claude.ai/artifact/JZZanMGfFdDsTYLQWH2bHi). Its main tab is saved in `docs/framework/framing.md` (families, descriptions, values, fears, promises, first consequences, funding lines, quotes, strands). The Funding and Can serve grid tabs are read in the doc itself (docs connector), or saved next to it first with the doc's Export menu. The page rules (lenses, Interests order, lead-ins) are in `CLAUDE.md` and the doc's "Movement page" tab; Neo-Luddism (`src/content/isms/neo-luddism.md`) is the worked example.
6. Owner-gated, never blocking: every new image. Use the placeholder and go on; list what waits in "Waiting on the owner".
7. Add a line to the log at the end of each phase.

### The map, old to new

| New (order, family) | Id | From |
| --- | --- | --- |
| 01 Transhumanism (Transcend) | `transhumanism` | as now |
| 02 Singularitarianism (Transcend) | `singularitarianism` | as now |
| 03 Techno-optimism (Accelerate) | `techno-optimism` | as now, plus effective accelerationism as a strand; American Dynamism leaves it |
| 04 American Dynamism (Accelerate) | `american-dynamism` | new; its entries and figures move out of Techno-optimism |
| 05 AI safety (Prevent) | `ai-safety` | new; effective altruism and longtermism, Humanist AI and the alignment entries of Rationalism |
| 06 Pause (Prevent) | `pause` | new; Rationalism and the call to pause |
| 07 Pro-human (Protect) | `pro-human` | as now |
| 08 AI ethics (Protect) | `ai-ethics` | as now, without AI as normal technology |
| 09 Digital sovereignty (Reclaim) | `digital-sovereignty` | as now |
| 10 Neo-Luddism (Reclaim) | `neo-luddism` | as now; new page setup done |
| 11 Normal technology (Doubt) | `normal-technology` | new; the strand moves out of AI ethics |
| 12 AI skepticism (Doubt) | `ai-skepticism` | new; written from scratch (the hype critique, the neurosymbolic critique, the bubble thesis) |

Retired pages, kept as redirects: `effective-accelerationism.html` → `techno-optimism.html`, `rationalism.html` → `pause.html`, `effective-altruism.html` → `ai-safety.html` (to the home page's movements until the target page is ready). Neoreaction moves to the timeline and the vocabulary.

Families (ids, names, colours): `transcend` Transcend `#C9F25B`, `accelerate` Accelerate `#FF9F4F`, `prevent` Prevent `#F5A3BC`, `protect` Protect `#73C7F2`, `reclaim` Reclaim `#C3A6FF`, `doubt` Doubt `#2EE6C8` (turquoise, owner 25 Nov 2026). Each family's line comes from the "What it wants" column in `docs/framework/framing.md`.

### Phase 0. Groundwork

- [x] Save the doc's main tab as `docs/framework/framing.md` (25 Nov)
- [x] This plan (25 Nov)

### Phase 1. Switch to six families and twelve movements (branch `framework/switch`)

All on one branch, so the live site changes once, when the whole switch is done.

- [x] 1.1 Families: `FAMILIES` in `src/lib/site.ts`, the family enum in `src/content.config.ts`, the `family` and `order` of every movement file (01–12), hero line "Transcend. Accelerate. Prevent. Protect. Reclaim. Doubt."
- [x] 1.2 Stub files for the five new movements (`ready: false`): title, family, order, summary, lead and includes from `framing.md`; entries and figures files where the build needs them. Their cards show "In preparation".
- [x] 1.3 Effective accelerationism into Techno-optimism: entries, figures, words, images and every reference (themes, words, history, people); the file removed; the strand line updated. Build catches broken references.
- [x] 1.4 American Dynamism out of Techno-optimism: its entries and figures move to `american-dynamism`.
- [x] 1.5 Rationalism into Pause, and its alignment entries into AI safety: entries, figures, words, images, references (history, themes, `about.astro`).
- [x] 1.6 Effective altruism into AI safety, with Humanist AI: entries, figures, words, images, references (history, themes, `people.yaml`).
- [x] 1.7 AI as normal technology out of AI ethics into `normal-technology`.
- [x] 1.8 Redirect pages for the three retired addresses (`public/`, meta refresh, `noindex`).
- [x] 1.9 Counts and wording: "ten movements" and "five families" in `index.astro`, `history.astro`, `method.astro`, `vocabulary.astro` and `people.astro`; the Movements header's introduction.
- [x] 1.10 `CLAUDE.md`: the framework section rewritten to the new map (families, movements, strands, order).
- [x] 1.11 Build, look at home, a movement page, vocabulary and People on a wide screen and a phone; merge into `main`; **Deploy**. Log line.

### Phase 2. The new page for every movement (one branch `page/<id>` each, since old `ism/*` branches still exist on GitHub; merge and **Deploy** after each)

For each movement, in this order: (a) lenses in its file from `framing.md`: values, fears, promises, first consequences (lower case, conditional), the quote ("In their own words"), `fundedBy` from the Funding tab, `canServeText` written by hand in the fixed order, `canServe` from the Can serve grid tab, `status: draft`; (b) the introduction's first sentence and the strands line checked against the family rule; (c) "Who disputes it" stays in the file, not shown; (d) build, look on a wide screen and a phone, merge, deploy, tick.

- [x] 10 Neo-Luddism (25 Nov, the template)
- [x] 01 Transhumanism
- [x] 02 Singularitarianism
- [x] 03 Techno-optimism (its timeline now has 31 entries with e/acc's; trimming to sixteen would delete checked entries, so that waits for the owner)
- [x] 07 Pro-human
- [x] 08 AI ethics
- [x] 09 Digital sovereignty
- [x] 05 AI safety (from the moved content: introduction, holders, the rest; `ready: true` when complete)
- [x] 06 Pause (likewise)
- [x] 04 American Dynamism (likewise; more entries if fewer than ten)
- [x] 11 Normal technology (likewise)
- [x] 12 AI skepticism (new: introduction, six holders, figures, ten to sixteen entries with real sources, words, lenses; `ready: true` when complete)

### Phase 3. Cards and colour (owner-gated)

- [x] 3.1 The Doubt colour (owner); then `FAMILIES`, cards and the design guide's tokens
- [x] 3.2 Cards for the five new movements. Pause and AI safety took over the Rationalism and EA cards (owner, 25 Nov: the paper clip and the arithmometer with 10⁵⁸, renamed `collage-pause` and `collage-ai-safety`). American Dynamism (the Y-12 Alpha racetrack), Normal technology (Edison's Jumbo dynamo) and AI skepticism (the mechanism of Vaucanson's presumed duck) from image batch 12, approved 25 Nov (17:46)
- [ ] 3.3 The design guide (artifact `4b7a91e1…`): cards, tokens, decisions

### Phase 4. Across the site

- [x] 4.1 Method page: the movement test, the four lenses, the derivation rules, interest not motive, the funding rules
- [x] 4.2 About page and the home page's section introductions
- [x] 4.3 Key-word pages: "How the movements see it" lines for the new movements, none left pointing at retired ones
- [x] 4.4 Vocabulary: words for the new movements (AI skepticism especially), tags moved from retired movements
- [x] 4.5 History of AI: each new movement's naming moment (`born`) and tags on moments
- [x] 4.6 People: filters and counts with twelve movements; the owner decides whether People stays in the menu
- [x] 4.7 Private preview artifact (stage 7)

### Phase 5. Checks (later, with the owner)

- [ ] 5.1 A checker that has not seen the drafting checks every draft line against its sources and sets `status: checked`
- [ ] 5.2 The doc and the site agree (lenses, funding, Can serve grid)

## Night of 22–23 November 2026 (owner's go at 23:49; he reads the result in the morning)

Tick each line as it is done, commit, push. A resumed session picks up at the first open line.

**Phase A** (branch `exp/phase-a`; tell the owner when done, by SendUserMessage)
- [x] Home page order: History of AI, Movements, Vocabulary (menu and hero links too)
- [x] Families in the order Transcendence, Acceleration, Risk; movements renumbered 01–06; hero "Transcend. Accelerate. Pause."
- [x] Acceleration in highlighter orange `#FF9F4F` (cards re-rendered; the site accent `#D8461C` and the History card stay)
- [x] EA card: the arithmometer (batch 10, public domain) with 10⁵⁸; "2045" moved to the Singularitarianism card; Transhumanism card without big type
- [x] CLAUDE.md, this file; build without warnings; screenshots; merged, pushed, deployed, preview artifact updated, owner told (23 Nov, 00:01). The design guide is updated once, at the end of the night run, for phase A and the Protection family together (tokens.json for the colours, 02-cards, 03-decisions, the card images)

- Owner, 00:41: keep 2014 FAT/ML as AI ethics' naming moment; add Magnifica Humanitas to the History of AI (untagged; checker on `check/weave`); no introduction for the History of AI header.

**Night run** (owner approved: the Protection family, highlighter blue `#73C7F2`, verb "Protect."). AFP photos are kept out of `public/` (anything there is published): they live in `/home/claude/img-work/batch09` and on the owner's Mac (`isms-genealogy-images/batch-09`) until he clears them.
- [x] Framework: family Protection after Risk; rule widened to "born in or against the tech world"; CLAUDE.md
- [x] AI ethics (includes AI as normal technology), branch `ism/ai-ethics`: drafted (2c0336f, 16 entries), checked (a9dbf8d), merged, ready
- [x] Pro-human, branch `ism/pro-human`: drafted (dff3602, 14 entries), checked (c4da67b), merged, ready. Humanist AI stays in Rationalism (owner, 22 Nov)
- [x] Collages: Protection = the water banner (Unsplash, batch 9) + the owner's Sanders still (cleared by the owner) + a "Sanders · Bannon · same stage" strip. AI ethics = the AFP head-cam photos (batch 9): the owner cleared them at 00:03 on 23 Nov, so they go live. Made on `exp/protection` (5a7b15d), with the hero "Protect." and "eight movements"
- [x] (00:40, checked 90af05a, merged) History moments tagged, new moments where missing; new words in the vocabulary; key-word lines where the new movements hold a view: drafted on exp/protection (ae0f2e1); checker running on branch `check/weave` (worktree /home/claude/wt-weave). After all three checks: merge the three branches into exp/protection, set `ready: true` on both, build, look, merge to main, deploy
- [x] (00:12) Design guide (artifact 4b7a91e1…, read its SKILL.md first): highlighter colours and Protection blue in tokens.json; 02-cards (EA arithmometer, 2045 on Singularitarianism, the two new cards); 03-decisions (22 Nov); card images; `lastChange` last
- [x] (00:45) The Protection family is live (main 71157cb, deployed)
- [x] (02:15) **Its words** (owner, 00:44–00:47): one row of pills on each movement page, linking to the vocabulary or a key-word page; "In the vocabulary" folded in. The two drafting agents were stopped by an interrupt, so the 32 missing listed words were drafted in the main session (`src/data/words/movement-words.yaml`), checked by a separate agent (all 32 checked), merged and deployed. Never delete a movement's listed words (owner). Still open: the 3–5 further relevant words per movement the owner asked for "if relevant".
- [x] (01:42–02:17) **History of AI, 2022 to now** (owner, 01:01–02:07), all checked and live: Anthropic's IPO; a constitution and a retirement; the maths story in three moments (a Millennium Prize problem, 8 Sep; mathematicians push back, Sep–Oct; the Riemann hypothesis, 20 Nov); "MechaHitler"; Gemini's Founding Fathers; agents at work; agents among themselves (OpenClaw, Moltbook); the swarm that hacked Hugging Face and after the swarm; the chip controls; authors against Anthropic; lawsuits over teenagers' deaths; the US–China dialogue on super intelligence. An optional `day` orders moments within a month. Palantir (2003) added in "Learning from data", with a new thread "Machines at war". Left out, for the owner: the Mythos/Fable export controls of June 2026 (reversed after 18 days); the Jacobian conjecture (July 2026).
- [x] (02:30) **AI in war** (owner, 02:00–02:07): the target factory (Gaza), the Iran war, drones that steer themselves (AI only), Palantir (2003); thread "Machines at war". All checked and live.
- [x] (04:08) **Longer moments for outsiders** (owner, 02:29–02:31; rules in CLAUDE.md): all eight eras rewritten, checked by separate agents and live, with the ten statement moments carried over. Merges done: the swarm attack; the Millennium Prize problems; the pro-human campaign; the ImageNet win with DNNresearch; Japan's Fifth Generation with Strategic Computing. Open: 1980-xcon keeps its earlier checked text, because the R1 paper (cdn.aaai.org) was not approved; its rewrite is in `/home/claude/hist-gaps/rewrite/05-winters.yaml` (draft) and needs that page or a cut of three claims.
- [x] (04:50) **Rogue agents and agent swarms** (owner, 04:20–04:28): the swarm moment renamed "Rogue agents hack Hugging Face" and widened to RubyGems, the 100+ organisations OpenAI notified and Tencent's agents (October); a new moment "Agent swarms become a weapon" (31 Aug 2026: PaperCut, Gambit, CyberXero, Trend Micro, Amazon's decoys). Checked by a separate agent and live. Warp left out (its "agent swarm" quote rests on one timeline only).
- [x] (03:08) **Statement moments**: the ten are checked and live, appended to the live era files. **When the rewritten staging files replace the live ones, carry these ten over** (their source is `/home/claude/hist-gaps/statements.yaml`; ids 2025-ai-2027, 2024-machines-of-loving-grace, 2023-hinton-leaves-google, 2017-putin-ai, 2015-autonomous-weapons-letter, 2000-why-the-future-doesnt-need-us, 1980-chinese-room, 1976-weizenbaum, 1972-dreyfus, 1970-early-promises).
- [x] (04:12) Built, checked on screen, deployed; private preview artifact updated (version 1795405644-442d). Left for later: the phone pass (stage 6b) and the People track (ideas, below).

## Stages

- [x] **1. Repository and skeleton.** Astro static site, design from the mockup, flat relative pages.
- [x] **2. Content structure.** Isms, themes, entries, figures, images; per-ism files; references checked at build.
- [x] **3. Isms.** For each: research agent drafts (branch `ism/<ism>`), checker agent verifies, merge, `ready: true`.
  - [x] Transhumanism — 14 entries, 12 figures, checked and merged (20 Nov)
  - [x] Singularitarianism (incl. successionism) — 14 entries, 11 figures, checked and merged
  - [x] Rationalism (incl. the call to pause) — 16 entries, 12 figures, checked and merged
  - [x] Effective altruism and longtermism — 16 entries, 10 figures, checked and merged
  - [x] Effective accelerationism (incl. neoreaction and the network state) — 16 entries, 10 figures, checked and merged
  - [x] Techno-optimism (incl. augmentation) — 16 entries, 12 figures, checked and merged
- [x] **4. Themes.** All seven written, checked and merged (20 Nov).
- [x] **4b. History of AI** (owner, 20 Nov: the third track, between the movements and the vocabulary). 97 moments in eight eras (`ERAS` in `src/lib/site.ts`), one file per era in `src/data/history/`, each with one of nine threads (`THREADS`), newest first, folding open on `history.html`. Drafted by three agents and checked by three others; 16 history words added to the vocabulary (`src/data/words/history-*.yaml`). Card: three machines at play, the Turk (1770), Kasparov (1997) and Lee Sedol (2016), a panorama from side to side, a quarter taller than a movement card so it reads as the biggest card (`HISTORY`, 2200 × 1000, 11:5; owner, 21 Nov; it was 11:4 at movement-card height), and a 4:5 version for phones and the page.
- [ ] **5. Images.** Every movement, key word and the History of AI has its collage card (batches 1–7). New cards follow the illustration guide: a session lists candidates as a batch in `docs/image-batches/batch-NN.md` (file, what it shows, file page, licence, size); the owner approves in the main conversation; only then is anything downloaded and the collage made there.
- [ ] **6. Checks.** WCAG 2.2 AA, speed, links, a source on every entry.
- [ ] **6b. Phone pass** (owner, 21 Nov: later). A hamburger menu on phones; until then the menu wraps onto a second line. Also: the history panorama is small on phones (consider its 4:5 page image there), and the sticky section menus on long pages.
- [ ] **7. Private preview.** Live and kept updated: run `npm run build:artifact`, then republish the `.html` files and `images/` of `dist-artifact/` (not `fonts/`) to artifact slug `608fc983-b11a-491d-82a9-146c41b7bb55` ("Radical Romance: A genealogy of the ideas behind AI"; get its current version with get_artifact first, and use `remove` for pages that no longer exist).
- [ ] **8. New key words** (owner, 20 Nov), one at a time, each drafted on a branch `keyword/<id>` by a research agent and checked by a separate agent, then merged with the next `order`: **Open weights** (9), **AGI** (10), **The pause** (11), **p(doom)** (12). Each needs a card: the research agent proposes one concrete object for it (see the illustration guide), and the session lists candidates as an image batch. Until the card is made the page shows without an image. Tag the history moments and movement entries that belong to the word (`themes:`), and add or update its vocabulary entry.
- [ ] **9. Keep the history and the vocabulary current.** New moments in the newest era (`src/data/history/01-generative.yaml`) for events since the last update, and new words as they enter the debate, each drafted and then checked by a separate agent. Keep each narrow; ask the owner before adding an era, a thread or a movement.

## Notes

- WebFetch cannot open Wikimedia Commons file pages. Image research on Commons is done in the main conversation with the built-in browser, which runs on the owner's Mac.
- Same-year entries: give `month` so they sort newest first.
- Alignment tags: the three held-back tags were added after `keywords` merged (20 Nov).
- The proxy refuses deleting remote branches (HTTP 403), so merged branches such as `keyword/alignment` stay on GitHub; the owner can delete them there.

## Ideas for later (owner)

- [x] (09:05) **People, stage 1** (owner's go, 08:46): 196 portraits cropped to 600 × 750 on the owner's Mac and copied into `public/portraits/`; `src/data/people/people.yaml` (212 people: the cleared portraits plus the figures, less Albanese and Tao, not named on the site for what they did); `src/lib/people.ts` works out movements, moments, timeline entries, words, era and threads; `people.html` with the grid by era, panels, Movement, Era and Thread filters, the explanation line and addresses; People in the home menu and hero; "Notable figures" renamed "People" with links; names in the history's "who" lines and the vocabulary's coiners link to their portraits; Method page section. On the preview for the owner to look at before it goes live.
- [x] (09:55) **People, stage 2** (started 09:08): lifespans, roles, labs, open letters and a note where the site has none, researched in ten batches by era (brief and batches in `/home/claude/hist-gaps/people/`, results in `facts/`), each checked by a separate agent; all 212 checked and in `src/data/people-facts/` (copied by `python3 scripts/people_facts.py <facts folder> <batches>`, checked entries only). The index is A to Z by surname (owner, 23 Nov). Stages 1 and 2 wait on the preview for the owner before they go live (branch `people-stage-1`). Checkers' calls to know: Kokotajlo's superintelligence signature cut (no second source); Tallinn's kept on one reprinted list; Tristan Harris's Google years cut (not AI work); Kaplan at OpenAI to 2020; Goodfellow leaving Google in 2025 rests on Wikipedia citing his LinkedIn. The pause and superintelligence signatory lists load only by script: a later pass in the built-in browser on the owner's Mac, if he approves the FLI site.
- [x] (24 Nov, 14:50) **Critics of hype and power** (owner, 24 Nov 14:33, after a review by another AI found them missing): Meredith Whittaker, Shannon Vallor, Evgeny Morozov, L. M. Sacasas, Ed Zitron, Cory Doctorow and Brian Merchant added as AI ethics's people and to the People page (218 people; the six new ones have no portrait yet, the owner to supply); words Borg Complex, solutionism, enshittification, rot economy, the AI mirror; "Who disputes it" lines for Techno-optimism (Morozov's A.G.I.-ism, Zitron's bubble) and Rationalism (Vallor). Drafts and checker's notes in `/home/claude/hist-gaps/critics/`, people facts in batch 11; all checked by a separate agent. On the preview with stages 1–2 (branch `people-stage-1`). Kjærulff and Analogiseringsstyrelsen wait for stage 7 (beyond the US and Britain). Then (24 Nov, 15:55; owner: "Let's include her") Jill Lepore: an AI ethics person, the word "the Artificial State" (2026), a "Who disputes it" line on Effective accelerationism and the History of AI moment "The People Machine" (Simulmatics, 1959; Lepore named in its source only, so her era stays 2026), all checked; 219 people. Then (owner, 24 Nov 16:08, "push it live when done") the fifth family **Reclaim** (#C3A6FF): **09 Neo-Luddism** (16 entries, 10 people, 7 words; card: the stocking frame, Felkin 1867) and **10 Digital sovereignty** (15 entries, 12 people, 10 words; card: the first web server, Commons photo 2005), drafted and checked by separate agents (staging in `/home/claude/hist-gaps/reclaim/`, copied by `reclaim/integrate.py`); **American Dynamism** as a strand of Techno-optimism (entry 2022, Boyle and Karp, the word; its timeline now has 17 entries). Image batch 11 approved by the owner (CERN's own 1990 photo sits behind a bot check, so the Commons photo was used). People now 238. Checkers' calls: the analogue revival is the weaker Neo-Luddism strand (TechRadar, July 2026); the enshittification retag to Digital sovereignty was dropped as weak; no source ties Khan, Wu or Brandeis to digital sovereignty by name (they come in through the anti-monopoly strand); Analogiseringsstyrelsen and Kjærulff found nowhere. Merged into main and deployed on 24 Nov 2026, 20:10, with People stages 1–2, the critics and Lepore.
- **People: the plan** (owner, 23 Nov 2026, 08:43): https://claude.ai/artifact/ATKBAXCViTaAGX2jhpDwGr. Decided: the name People; one page, no page per person; group filters Movement, Role, Era, Thread, Lab, Open letters; switches Crossed camps, Funders, Quit or fired, Predictions, p(doom); no Honours, gender, ethnicity or nationality; explanation line with hover preview; connections and dated camp shifts; a bubble view as an experiment after the grid. Seven stages, each live once checked.
- **People** (owner, 23 Nov 2026, 02:56; not started, after the history rewrite): a fourth track, menu History of AI, Movements, People, Vocabulary. Join up what exists (the figures on movement pages, the people in history moments, the vocabulary's coiners), showing who crosses camps. To settle first: a rule for who gets in; public roles and documented statements only, critics where it matters; portraits, which the owner is gathering himself with their licence data (Wikimedia Commons: public domain or free licences, credited), and whether they get the collage treatment. This would reverse the 20 Nov no-portraits rule, the owner's call. At 04:45 the owner reported the portraits ready: 213 files with `portraits.csv` (name, file, Commons page, licence, author, credit, date, size) in his connected folder `isms-genealogy-images/portraits/`, not yet in the repository. Licences: public domain 47, CC0 6, CC licences 119, "Attribution" 2, fair use 8, external web source 31. **The owner cleared every file in the folder (04:50)**, so none needs a rights check; Checked against their sources (05:05; not by face): 12 need replacing (9 show the wrong person or a flag, 3 are book covers or a slide), 6 need cropping, 2 need a note or a second look; list in `isms-genealogy-images/portrait-check/portrait-check.csv`, contact sheets beside it.

## Waiting on the owner

- Long timelines after the merges (the guide is ten to sixteen): Techno-optimism 31 entries, AI safety 20. Trim, or keep the strands' history whole?

- Whether People stays in the menu once movement pages show their people as portraits (phase 4.6).

- Whether images under a non-commercial licence (CC BY-NC, e.g. the British Museum's Gilgamesh tablet, a Barlach lithograph) are acceptable.

- Image batch approvals (sent as lists when ready). Batches 6, 7 and 8 were approved and used (Watt's governor for Alignment; von Kempelen's Turk for the History of AI; Deep Blue at the Computer History Museum for its moment).
- The domain (mademinds.org: owner checks and buys it), and when to allow search engines (remove the noindex tag).
- Hosting (owner, 21 Nov: later): move the site from GitHub Pages to Cloudflare, likely Workers static assets serving `dist/` (no adapter needed for a static Astro build), with the domain mademinds.org. Needs the owner's Cloudflare account and explicit go; no session starts it on its own.
- Before launch: delete the dev grid switch (owner, 21 Nov: the "Grid" button and G key in `src/layouts/Base.astro`, and the "DEV ONLY" block at the end of `src/styles/site.css`). The name Made Minds was decided on 20 November 2026.

## How a session continues the build

The site now has three tracks: **Movements** (the six, done), **History of AI** (97 moments, done) and **Vocabulary** (key words with cards and pages, plus the plain word list). What remains is stages 8 and 9, image batches for new cards, and the checks in stage 6. The framework, the design, the illustration style, the home page and its copy are the owner's: a session never changes them on its own.

1. `git fetch origin`. Look for branches with drafts (`keyword/*`, `history/*`, `words/*`, `ism/*`). A branch with `status: draft` items needs a checker that has not seen the drafting (`docs/agent-brief.md`). It opens every source, fixes or removes what does not hold, and sets `status: checked`. Then merge `main` into the branch, build with no warnings, merge into `main`, push.
2. Otherwise draft the next key word in stage 8 with a research agent in its own worktree (`git worktree add -b keyword/<id> ../wt-<id> main`, then `ln -s "$PWD/node_modules" ../wt-<id>/node_modules`), using the key-word brief in `docs/agent-brief.md`. Do not merge a draft: it is checked first, in this run or the next.
3. When stage 8 is done, add new history moments or words (stage 9) with the history brief, then check them.
4. Collect the image candidates the agents propose into one batch file in `docs/image-batches/`. Never download, never make or change a collage: that happens in the main conversation after the owner says yes.
5. Republish the private preview (stage 7). Scheduled runs do not run `npm run deploy`: the live site is updated in the owner's conversation, after the owner has seen the preview.
6. Tick this file, add a line to the log, commit, push. Fetch before every push, because the owner's conversation also pushes to `main`.

## Log

- 2026-11-25: Hero edited by the owner (19:14): new axes form around the machine "and the Big Tech behind it"; "an archaic dread" instead of fears (the word is the lenses' and the families'); the line on the range of futures is gone, since the family introductions carry it.

- 2026-11-25: Each family row on the home page now opens with a short introduction instead of one line (owner, 19:10): what its two movements share, then how they differ (who crosses; whom it serves; whether it can be made safe in time; what they defend first; build our own or refuse; ordinary or oversold). Written from the movements' own lenses.

- 2026-11-25: Family headings on the home page made large (owner, 19:08): name and colour square at 48 px on columns 1–6, the family's line on 7–12, as the old Movements header and its introduction were.

- 2026-11-25: Hero (owner, 19:05): no more "today they are movements"; a new paragraph asks what these positions become as they meet political power while the world order is remade, and who will hold power in the future. Four paragraphs now.

- 2026-11-25: Hero: the breakthrough of large language models "stirred wonder and archaic fears" (owner, 19:00).

- 2026-11-25: Hero, second paragraph (owner, 18:59): the breakthrough of large language models brought positions that had long been fringe into the mainstream; today they are movements.

- 2026-11-25: Hero text polished (owner, 18:55): one tense with the scene ("The day before"), "the machine" for one of the repeated "AI"s, a lighter list of what a movement has, and a last paragraph that closes on the tales and their roots. The subtitle waits.

- 2026-11-25: The site is renamed **Radical Romance** (owner, 18:31); Made Minds is dropped altogether. `SITE_NAME`, the hero, the preview artifact's title and the illustration guide's title follow. The subtitle stays "A genealogy of the ideas behind AI". The repository and the GitHub Pages address are unchanged.

- 2026-11-25: Hero: the futures now run from machines that succeed us to a world that barely changes, and the ideas are "many older than the computer, some as old as myth" (owner, 18:26).

- 2026-11-25: Hero text reframed as an investigation (owner, 18:21): new axes forming around AI, all rooted in history; the ideas strange, and strangely familiar; Made Minds as an investigation into them.

- 2026-11-25: The subtitle and the map date are back above the headline (owner, 18:14). The "Movements" heading is gone from the home page; its introduction (what a movement is, how the families run) is fused into the hero's text.

- 2026-11-25: The hero's top line (subtitle and map date) and the six family verbs are gone from the home page (owner, 18:09). The big headline is now "ChatGPT felt like year zero. It wasn't." The subtitle stays in the browser tab; the families still head their rows.

- 2026-11-25: Home hero rewritten with the owner (18:05): it opens in medias res at the Pro-Human Assembly (Washington, 15 September 2026, Sanders and Bannon on one stage), then Trump's "hoax" the day before and the old lines between left and right being redrawn; the movements behind the new lines and the futures they want; "ChatGPT felt like year zero. It wasn't." closes it, with each page tracing its genealogy. Facts from the checked History of AI moment "The pro-human campaign".

- 2026-11-25: The home page is an atlas of the movements only (owner, 17:40 and 17:54): the History of AI card is parked (switched off in `index.astro`), the key-word cards move to the top of the vocabulary page, and both pages stay in the menu. The subtitle stays. The hero's text now frames the atlas: the camps were already there, they compete over what AI is and what future it should bring, twelve in six families, and each idea's genealogy. Back links read "All movements".

- 2026-11-25: Cards for the last three movements, from image batch 12 (owner's yes, 17:46): American Dynamism is an Alpha racetrack at Y-12, Oak Ridge (c. 1944) with 2024 · a Manhattan Project for AGI; Normal technology is Edison's Jumbo dynamo (1882) with 2025 · AI as normal technology; AI skepticism is the mechanism of a duck presumed to be Vaucanson's (before 1880) with 2021 · On the Dangers of Stochastic Parrots. All twelve movements now have cards.

- 2026-11-25: Pause and AI safety took over the old Rationalism and Effective altruism cards (owner): the Gem paper clip with the paperclip maximiser, and the arithmometer with Bostrom's 10⁵⁸ future lives. Both stay pink, as before. Files and engine ids renamed to `collage-pause` and `collage-ai-safety`.

- 2026-11-25: Doubt is highlighter turquoise `#2EE6C8` (owner). The placeholder yellow sat closer to Transcend's lime than any other two family colours (and almost matched it for colour-blind readers); turquoise is the gap in the set, furthest from all five. Set in `FAMILIES`, `scripts/collages.py`, `CLAUDE.md` and `framing.md`; the design guide's family tokens are renamed to the six families, with `family-doubt` added.

- 2026-11-25: Phase 4 done and live: the method and about pages explain the lenses and the twelve movements; key-word lines for American Dynamism (Compute), Normal technology (Abundance) and AI skepticism (Scaling laws); four new words (Chinese room, octopus test, general-purpose technology, productivity paradox, all draft) and three retagged (American Dynamism, rot economy, AI winter); history moments tagged with American Dynamism, AI safety and AI skepticism; naming moments for American Dynamism, Pause and Normal technology. AI safety and AI skepticism have no naming moment: no entry records the name being coined. The People filter shows all twelve, each with people. Private preview republished (version 1795616499-d021).

- 2026-11-25: Phase 2 done: all twelve movements have the new page (lenses with Promises and Interests, the quote opening People, portrait tiles). AI safety, Pause, American Dynamism, Normal technology and AI skepticism are live; American Dynamism (16 entries), Normal technology (11) and AI skepticism (12) got new timelines, and 13 names were added to the People page. All new text is draft. The five new movements still have no cards (phase 3).

- 2026-11-25: Phase 1 of the new framework is live (owner's go, 14:48): six families named by verbs (Doubt in a placeholder yellow), twelve movements numbered 01–12, the map dated 25 November 2026. Effective accelerationism is a strand of Techno-optimism; Rationalism and Effective altruism are strands of Pause and AI safety; American Dynamism and Normal technology have their own files; AI skepticism is a stub. The five new movements show "In preparation" without cards until phases 2 and 3. Retired addresses redirect.

- 2026-11-25: New movement-page setup tested on Neo-Luddism only (owner). Who holds it now follows the introduction; the movement's quote opens the People section (owner). Then the lenses as labelled rows on 4 + 8: Values (filled chips in the family colour), Fears (outlined chips), Promises (with the first consequences after "If <movement>'s demands became law tomorrow,"), and Interests: one row, the funding first (fact, `fundedBy`), then who its demands could serve (the site's reasoning, `canServeText`, after a bold "Its demands could serve"); funders are named only in the first part, beneficiaries only in the second. The seven-actor matrix stays in the file (`canServe`) for the actor view, not on the page: the owner found it too simplistic as a list. He also tried a spread layout and turned it down: the hierarchy became unclear. People on the page are the People page's own portrait tiles, opening the same panel (`src/components/PersonCard.astro`, now shared by both pages; the People page output is unchanged). The owner may take People out of the menu later. The new text is draft until checked. "Who disputes it" is no longer shown when an ism has `lenses`; its text stays in the file. The framework behind it (twelve movements in six families) lives in the owner's doc "A new framing of the AI movements" (https://claude.ai/artifact/JZZanMGfFdDsTYLQWH2bHi) and is not yet applied to the rest of the site.

- 2026-11-21: Vocabulary gets technical terms (owner): a "Technical terms" filter beside the families (`technical: true` on a word), ten existing words tagged, and 23 new words in `src/data/words/technical.yaml`, from neural network (1943) to reasoning model (2024), checked the same night; the checker corrected 17 of them against their sources. Training, inference and benchmark left out as separate words: ordinary words with no traceable first use.

- 2026-11-21: The section menu's underline now follows scrolling on every page with a menu (owner). Its script ran before the sections existed and stopped; it now runs after load and tracks scroll position. Bold width reserved so the menu never shifts.

- 2026-11-21: Humanist AI added as a strand of Rationalism (owner): card line, Microsoft AI as a holder, a 2026 timeline entry, three words (Tool AI, humanist superintelligence, Humanist AI) and a History of AI moment, all draft until checked. Rationalism now has 17 timeline entries, one over the guide of sixteen. Strand lines now keep their own capitals.

- 2026-11-21: Click-to-remove taken off the History card pieces (owner): a click on the image always opens the history.

- 2026-11-21: History card motion starts earlier (owner): the square moves from the moment the card enters and locks once it is fully in view; the five pieces land before it starts to leave, checked on five screen sizes.

- 2026-11-21: History card pieces follow scroll position, reversible (owner): each piece about 6% of the screen apart after the click point, so readers can scroll back and forth; the square stays a one-way ratchet.

- 2026-11-21: History card pieces now arrive in an even beat right after the click (owner): 0.18 s, then every 0.42 s. Before, each waited for more scrolling and felt broken.

- 2026-11-21: History card glitches replaced by pieces that stay (owner): after the square clicks into place, five chosen squares of the second state arrive with scrolling and stay; a click takes one away. Calmer and less confusing than flicker.

- 2026-11-21: History card animation calmed and ordered (owner): the square locks first, then Deep Blue takes Kasparov's face, then four or five single squares per pass, never on a face.

- 2026-11-21: Hover stutter removed from the History card (owner): it moves only when the reader scrolls.

- 2026-11-21: History card animation live as an experiment (owner): squares glitch on scroll from a second state of the card, a black square ratchets into place one way only, still at rest, off for reduced motion. Script and layer in `src/pages/index.astro` and `site.css`, marked EXPERIMENT; second states `collage-history-b`, `collage-history-tall-b`; the home page's vertical card is `collage-history-tall-home`.

- 2026-11-21: History card made taller, 11:4 to 11:5 (owner): at movement-card height its three subjects came out smaller than the single objects above it. 2:1 was tried and crowded the panels.

- 2026-11-21: History of AI card redesigned (owner): three machines at play, the Turk (1770), Kasparov walking away from Deep Blue (1997) and Lee Sedol against AlphaGo (2016), no big type, labels along the bottom; grey, paper and orange. A vertical version for phones and the history page, and three variations as images on those moments in the timeline (the Turk's hidden player, Deep Blue's towers from batch 8, Lee Sedol). The two stills are an owner exception to the no-people rule, cleared by the owner as fair use; both are screenshots from the official live streams of the matches. Engine: fragments can be cut out along the grid (`keep`), and a field can carry its own colour.

- 2026-11-21: The scheduled task's instructions and this procedure rewritten for the new direction (three tracks, key words, history, image batches only, no deploy from scheduled runs). The scheduled task is paused until the owner resumes it.

- 2026-11-20: History of AI merged and live: 97 checked moments (antiquity to 2026) and 16 history words, from three drafting agents and three separate checkers (corrections listed in their commits on `history/*`). The owner suggested Longview's podcast The Last Invention as a lead; it gave the threads, with symbols against networks the most frequent. Google's 2012 cat network moved to the deep-learning file. Section menu on the history page uses the years of each era.

- 2026-11-20: History of AI started (owner): `history` collection and eras, `history.html` with an era index and folding moments, each era showing the movements named in it and the vocabulary words coined in it; a full-width card on the home page between the movements and the vocabulary (shown once moments exist); menu Movements · History of AI · Vocabulary; "In the history of AI" on movement and key-word pages, built from tags. Each movement's naming moment is set with `born`. Alignment card made from batch 6 (Watt's governor, 1788, with Wiener's 1960 words). Collage engine: colour fields no longer wrap round to the opposite edge. Illustration guide updated: the six movement cards and Alignment added, key-word names, family colours as tokens.

- 2026-11-20 (scheduled run): Key word **Alignment** drafted, checked by a separate agent and merged (`order: 8`, card image to come; 6 history entries tagged, 3 held back, see Notes). Checker removed Russell's reported denial of coining the word (single unverifiable source; the vocabulary entry for "alignment" still carries it) and moved the DAIR statement out (better on The pause). Image batch 6 listed for its card. Preview republished (version 24); not deployed to GitHub Pages.

- 2026-11-20: Collage set made for all 13 cards; Abundance rebuilt around an electricity meter (batch 3, 1 image, CC BY-SA 4.0).
- 2026-11-20: Key-word pages merged (drafted, then checked by a separate agent): Scaling laws, Compute, Abundance, Augmentation, Facial recognition, Citizens' assemblies, Luddite. Old theme URLs (power, scale, the-tool, rights-and-dignity, self-determination, critique) are gone. Next key words with new cards: Open weights, Alignment, AGI, The pause, p(doom). Update the illustration guide's card names to the new words.
- 2026-11-20: Vocabulary merged: 40 words, each checked against sources by a separate agent (several dates corrected, e.g. p(doom) by 2009). Vocabulary page with family filter; home shows the illustrated words, then the plain list.
- 2026-11-20: Image batch 5 approved and used: Rationalism is the 1893 Gem paper clip (public domain) with the 2003 paperclip maximiser; Effective altruism is stacked bed nets (CC BY 2.0, DFAT) with GiveWell's $5 a net and $5,500 per life saved. All six ism cards now follow the guide, in both formats. The heap of paperclips was downloaded but not used. The "Six movements" heading is hidden (owner).
- 2026-11-20: Ism cards rebuilt by the illustration guide, with page images: Transhumanism (Flood Tablet + 2045, label date corrected to 7th century BCE), Singularitarianism (IAS machine + Ulam 1958), Techno-optimism (Hoover Dam, no BUILD; handed over two years early), e/acc kept plus a page image. Rationalism and Effective altruism wait for image batch 5.
- 2026-11-20: Owner decisions: themes become narrow key words plus a vocabulary (questions dropped as too broad, no critics section); notable figures shown as a folding index of names, no portraits. Questions agent stopped before writing; vocabulary agent continues (branch `words`).
- 2026-11-20: Home restructured (owner): the six as movements in three family rows, numbered 01–06; no filter above them; themes shown as questions; the critics and the vocabulary get their own sections (filter on the vocabulary). Agents drafting the question pages (branch `questions`) and the vocabulary (branch `words`).
- 2026-11-20: Vertical page images (4:5, 1200 × 1500) for the seven themes, shown at the top of each theme page (`pageImage`). Fixed stretched photos on The tool, Rights and dignity, Critique and Power; the engine now warns when a box stretches its crop (ism cards still have some, to fix in their rework).
- 2026-11-20: Illustration guide made as a design system, "Made Minds Illustration", from the seven theme cards and the owner's feedback. Ism cards to be reworked next, then added.
- 2026-11-20: Site named Made Minds (owner). Power and Rights and dignity collages rebuilt around objects (batch 4: four NVIDIA H100 cards, CC BY 3.0; a London police facial-recognition camera, CC BY-SA 4.0). Then, at the owner's request, fewer big numbers: Power is the chips alone (label: the 2022 US licence for H100 sales to China); Rights and dignity shows EU. Then no big type on Abundance or Rights and dignity either: type stays only where it comes from another time than the object (2045, 10²⁵, e/acc, BUILD).
- 2026-11-20: Image batch 2 (3 card images) downloaded; every ism card now has an image. Home grid rows aligned.
- 2026-11-20: Transhumanism checked and merged; every ism and theme is now checked.
- 2026-11-20: Owner approved going public: repository public, GitHub Pages live from `gh-pages` (noindex for now).
- 2026-11-20: Themes Power, The tool, Scale, Abundance checked and merged.
- 2026-11-20: Themes Rights and dignity, Self-determination, Critique checked and merged.
- 2026-11-20: Image batch 1 downloaded and on the site (17 images).
- 2026-11-20: Techno-optimism checked and merged. All six isms done.
- 2026-11-20: Effective accelerationism checked and merged.
- 2026-11-20: Effective altruism checked and merged; card summary narrowed to longtermists.
- 2026-11-20: The last three isms drafted; checks running.
- 2026-11-20: Singularitarianism checked and merged. Research agents started for the last three isms.
- 2026-11-20: Rationalism checked and merged (Wiener root set to attributed; Barlach NC image swapped for Barth, public domain). Image batch 1 approved; download blocked by allowlist.
- 2026-11-20: Rationalism drafted by a research agent; check started. Month field added.
- 2026-11-20: Skeleton, content structure, Transhumanism and Abundance drafted from the mockup. Repository created.
