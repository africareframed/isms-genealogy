# Work plan

Every session starts here: find the first stage that is not done, do the next piece, update this file, commit, push. Rules are in `CLAUDE.md`.

## Stages

- [x] **1. Repository and skeleton.** Astro static site, design from the mockup, flat relative pages.
- [x] **2. Content structure.** Isms, themes, entries, figures, images; per-ism files; references checked at build.
- [ ] **3. Isms.** For each: research agent drafts (branch `ism/<ism>`), checker agent verifies, merge, `ready: true`.
  - [ ] Transhumanism — drafted from the mockup; needs checking and more figures' sources
  - [x] Singularitarianism (incl. successionism) — 14 entries, 11 figures, checked and merged
  - [x] Rationalism (incl. the call to pause) — 16 entries, 12 figures, checked and merged
  - [x] Effective altruism and longtermism — 16 entries, 10 figures, checked and merged
  - [x] Effective accelerationism (incl. neoreaction and the network state) — 16 entries, 10 figures, checked and merged
  - [ ] Techno-optimism (incl. augmentation) — drafted (16 entries) on `ism/techno-optimism`; checker running. If the branch still has `status: draft` entries at the next run, run a checker on it.
- [ ] **4. Themes.** Abundance drafted; then Power, The tool, Scale, Rights and dignity, Self-determination, Critique. Each needs one line per ism, strands, words, disputes.
- [ ] **5. Images.** Batch 1 (17 files) approved by the owner on 20 Nov but blocked: image hosts are not in the network allowlist; owner is adding them. Candidate lists per ism → owner approves a batch → download to the owner's folder → `public/images/`.
- [ ] **6. Checks.** WCAG 2.2 AA, speed, links, a source on every entry.
- [ ] **7. Private preview.** Live and kept updated: run `npm run build:artifact`, then republish the `.html` files of `dist-artifact/` (not `fonts/`) to artifact slug `608fc983-b11a-491d-82a9-146c41b7bb55` ("A genealogy of the isms behind AI — preview"; get its current version with get_artifact first).

## Notes

- WebFetch cannot open Wikimedia Commons file pages. Image research on Commons is done in the main conversation with the built-in browser, which runs on the owner's Mac.
- Same-year entries: give `month` so they sort newest first.

## Waiting on the owner

- Whether images under a non-commercial licence (CC BY-NC, e.g. the British Museum's Gilgamesh tablet, a Barlach lithograph) are acceptable.

- Image batch approvals (sent as lists when ready).
- Portraits for notable figures (owner adds them to `public/portraits/`).
- The working title, and the decision to go public.

## How a session continues the build

1. `git fetch origin` and look at `ism/*` branches. A branch whose ism has `status: draft` entries needs checking: run a checker agent that has not seen the drafting. It opens every source, fixes or removes what does not hold, and sets `status: checked`. Then build, merge into `main`, push, delete the branch.
2. Otherwise start the next unstarted ism in stage 3 with a research agent in its own worktree (`git worktree add -b ism/<ism> ../wt-<ism> main`, link node_modules), using the brief in `docs/agent-brief.md`.
3. After the isms, the themes (stage 4), each written from the finished isms.
4. Collect image candidates from the agents' reports into one list per few isms, and send it to the owner as a download batch.
5. Republish the preview, tick this file, add a line to the log, commit, push.

## Log

- 2026-11-20: Effective accelerationism checked and merged.
- 2026-11-20: Effective altruism checked and merged; card summary narrowed to longtermists.
- 2026-11-20: The last three isms drafted; checks running.
- 2026-11-20: Singularitarianism checked and merged. Research agents started for the last three isms.
- 2026-11-20: Rationalism checked and merged (Wiener root set to attributed; Barlach NC image swapped for Barth, public domain). Image batch 1 approved; download blocked by allowlist.
- 2026-11-20: Rationalism drafted by a research agent; check started. Month field added.
- 2026-11-20: Skeleton, content structure, Transhumanism and Abundance drafted from the mockup. Repository created.
