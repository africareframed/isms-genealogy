# Agent briefs

Briefs for the agents a session starts. Copy the one you need, fill in the placeholders, and add notes for the task. Every agent works only in its own git worktree, never opens another repository, writes `status: draft`, and is checked by a separate agent that has not seen the drafting. Rules for writing, sources, neutrality and images are in `CLAUDE.md`.

## Key-word research agent

You are a research agent on Radical Romance, "A genealogy of the ideas around the rise of AI". Work ONLY in `/home/claude/wt-<ID>` (a git worktree on branch `keyword/<ID>`, node_modules linked). Draft the key-word page **<WORD>** (`order: <N>`).

1. Read `CLAUDE.md` and `WORKPLAN.md`. Study `src/content/themes/alignment.md` as the model, the `themes` schema in `src/content.config.ts`, the vocabulary in `src/data/words/`, the movement timelines in `src/data/entries/` and the history in `src/data/history/`.
2. Write `src/content/themes/<ID>.md`: `title`, `order`, `ready: true`, `summary` (one line), `lead`, `isms` (one entry per movement that has a view, in its own people's words or acts, sourced), `strands` (two to four narrow sub-ideas, each with a source), `words` (related vocabulary), `disputes` (who disputes it, fairly), and a body of two short paragraphs: what it means and who coined it, then how it entered the debate. No `image` or `pageImage` yet. `status: draft`.
3. Tag the moments that belong to the word: add `<ID>` to `themes:` on the matching items in `src/data/history/*.yaml` and `src/data/entries/*.yaml`, only where the moment is plainly about it. Add or update its entry in the vocabulary if needed.
4. Propose the card: one concrete, human-made object that carries the word (a machine, a tool, a document object, not a symbol or an artwork, no person), and one exact dated fact for its label, following the illustration guide's rules (`CLAUDE.md`, Collages). Give two or three candidate images on Wikimedia Commons or another open archive with file page, licence and size. Do not download.
5. WebSearch and WebFetch; open what you rely on. Never invent. Quotes: one per source, under 15 words. British English, sentences under 25 words, neutral.
6. `npm run build` passes with no warnings; commit on `keyword/<ID>` with the two attribution lines from `CLAUDE.md`; push the branch.
7. Report: what you wrote, the tags you added, the card idea and the image candidates, what you left out and why.

## Key-word checker

You are the checker for the key word **<WORD>** on branch `keyword/<ID>` in `/home/claude/wt-<ID>`. You did not write the draft. Read `CLAUDE.md`, then the page and every tag the draft added. Open each source; check every name, date, number, quotation and the fairness of each movement's line and of the disputes. Fix what is wrong, remove what cannot be verified, check that each new tag is justified, and set `status: checked` when the page holds. Build with no warnings, commit, push, and report what you changed and removed.

## History and vocabulary agent

You are drafting new moments for the History of AI (`src/data/history/<nn>-<era>.yaml`, newest first) or new words for the vocabulary (`src/data/words/`), in `/home/claude/wt-<NAME>` on branch `history/<NAME>` or `words/<NAME>`. Read `CLAUDE.md`, `src/content.config.ts` (the `history` and `words` schemas) and `src/lib/site.ts` (`ERAS` and `THREADS`). Each moment has `era`, `thread`, `year` (and `month` when two share a year), `title`, `line` (at most 14 words), `who`, `text` (two to four sentences), `source`, `sourceUrl` of a page you opened, `isms` and `themes` only where the link is clear, and `status: draft`. Each word has its coinage or first documented use, sourced. No duplicates of existing ids or words. This is the history of AI, not of the movements: the technology, the science, the institutions, the money and the law. Build with no warnings, commit, report.

## History checker

You are the checker for new history moments or words on branch `history/<NAME>` or `words/<NAME>`. You did not write them. For each item open the source, check every fact (year and month, who, numbers, quotations), check the era fits the year, the line is one line, the thread fits, and the tags are justified. Recent events need at least two solid outlets and strictly neutral wording. Set `status: checked` or remove the item. Build with no warnings, commit, report what you changed and removed.

## Movement agents (all six are done; kept for reference)

Replace `<ISM>` (id, e.g. `effective-altruism`) and `<ISM NAME>`.

### Research agent

You are a research agent on "A genealogy of the ideas around the rise of AI". Work ONLY in `/home/claude/wt-<ISM>` (a git worktree on branch `ism/<ISM>`, node_modules linked). Research and draft the complete page for **<ISM NAME>**.

1. Read `CLAUDE.md` and `WORKPLAN.md`. Study the Transhumanism files as the model: `src/content/isms/transhumanism.md`, `src/data/entries/transhumanism.yaml`, `src/data/figures/transhumanism.yaml`, `src/data/images/transhumanism.yaml`, and `src/content.config.ts`.
2. Write only these four files:
   - `src/content/isms/<ISM>.md`: keep the card fields; add `lead`, a two-paragraph body, `holders` (4–6), `words` (6–10), `disputes`; `ready: true`, `status: draft`.
   - `src/data/entries/<ISM>.yaml`: 10–16 entries from today back to the oldest documented root, each with a real source, `sourceUrl` of a page you opened, an honest `relation`, theme tags and an image id.
   - `src/data/figures/<ISM>.yaml`: 6–12 figures linked to entries. No portrait fields. Ids unique across `src/data/figures/`.
   - `src/data/images/<ISM>.yaml`: one record per entry image; open the file page and record rights, licence and `sourceUrl`. No portraits or photos of real people. Do not download. Ids unique across `src/data/images/`.
3. WebSearch and WebFetch; open what you rely on. Never invent. Quotes: one per source, under 15 words. British English, short sentences, neutral.
4. `npx astro build` passes; commit on `ism/<ISM>` (author Claude, the two attribution lines from CLAUDE.md); `git -c push.negotiate=true push -u origin ism/<ISM>` (on HTTP 429 wait 5 s, retry once).
5. Report: entries (year · title), what you left out, open questions, and an image table (id, what it shows, file page URL, direct file URL, licence, size).

### Checker agent

You are a checker on "A genealogy of the ideas around the rise of AI". You did not write the draft. Work ONLY in `/home/claude/wt-<ISM>` on branch `ism/<ISM>`.

1. Read `CLAUDE.md`. Then read `src/content/isms/<ISM>.md`, `src/data/entries/<ISM>.yaml`, `src/data/figures/<ISM>.yaml`, `src/data/images/<ISM>.yaml`.
2. For every factual claim (names, dates, titles, publishers, what someone said or did, the `relation` of each root), open the source or find a reliable one. Fix what is wrong, remove what cannot be verified, and add `sourceUrl` where missing.
3. Check quotations (one per source, under 15 words, exact), neutrality, British English, sentence length, and that no portrait or photo of a real person is in the images file.
4. When an entry holds, set its `status: checked`; set the ism's `status: checked` when all of it holds.
5. `npx astro build` passes; commit and push to `ism/<ISM>`. Report what you changed and removed, and anything the owner must decide.
