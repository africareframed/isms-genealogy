# Work plan

Every session starts here: find the first stage that is not done, do the next piece, update this file, commit, push. Rules are in `CLAUDE.md`.

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
- [ ] **4b. History of AI** (owner, 20 Nov: the third track, between the movements and the vocabulary). About 80 moments in eight eras (`ERAS` in `src/lib/site.ts`), one file per era in `src/data/history/`, newest first, each folding open on `history.html`. Three drafting agents (branches `history/recent`, `history/middle`, `history/early`, local to the coordinating conversation) also add history words to `src/data/words/history-*.yaml`; then a separate checker. Card image: von Kempelen's Turk (batch 7) with 1997, the year Deep Blue beat Kasparov; full-width card 1600 × 900 (`HISTORY` in the engine) and a 4:5 page image.
- [ ] **5. Images.** Batch 1 (17 files) approved and downloaded 20 Nov into the owner's folder (batch-01/), resized to 1800 px JPEGs in public/images/, records filled. Network access now allows these hosts. Candidate lists per ism → owner approves a batch → download to the owner's folder → `public/images/`.
- [ ] **6. Checks.** WCAG 2.2 AA, speed, links, a source on every entry.
- [ ] **7. Private preview.** Live and kept updated: run `npm run build:artifact`, then republish the `.html` files and `images/` of `dist-artifact/` (not `fonts/`) to artifact slug `608fc983-b11a-491d-82a9-146c41b7bb55` ("A genealogy of the isms behind AI — preview"; get its current version with get_artifact first).

## Notes

- WebFetch cannot open Wikimedia Commons file pages. Image research on Commons is done in the main conversation with the built-in browser, which runs on the owner's Mac.
- Same-year entries: give `month` so they sort newest first.
- Alignment tags: the three held-back tags were added after `keywords` merged (20 Nov).
- The proxy refuses deleting remote branches (HTTP 403), so merged branches such as `keyword/alignment` stay on GitHub; the owner can delete them there.

## Waiting on the owner

- Whether images under a non-commercial licence (CC BY-NC, e.g. the British Museum's Gilgamesh tablet, a Barlach lithograph) are acceptable.

- Image batch approvals (sent as lists when ready). Batches 6 and 7 were approved and used (Watt's governor for Alignment; von Kempelen's Turk with 1997 for the History of AI).
- The domain (mademinds.org: owner checks and buys it), and when to allow search engines (remove the noindex tag). The name Made Minds was decided on 20 November 2026.

## How a session continues the build

1. `git fetch origin` and look at `ism/*` branches. A branch whose ism has `status: draft` entries needs checking: run a checker agent that has not seen the drafting. It opens every source, fixes or removes what does not hold, and sets `status: checked`. Then build, merge into `main`, push, delete the branch.
2. Otherwise start the next unstarted ism in stage 3 with a research agent in its own worktree (`git worktree add -b ism/<ism> ../wt-<ism> main`, link node_modules), using the brief in `docs/agent-brief.md`.
3. After the isms, the themes (stage 4), each written from the finished isms.
4. Collect image candidates from the agents' reports into one list per few isms, and send it to the owner as a download batch.
5. Run `npm run deploy` to update the live site, republish the preview, tick this file, add a line to the log, commit, push.

## Log

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
