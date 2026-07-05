# informal-peer-review

Repository of data and analyses from a digital ethnography of **informal peer review** — the public, post-publication scrutiny of scientific work that happens on blogs, PubPeer, and social media (Bluesky, X/Twitter) rather than through journals' formal review processes.

This repository is an [Obsidian](https://obsidian.md) vault. The notes are plain Markdown and can be read on GitHub or in any text editor, but they are richly cross-linked with `[[wikilinks]]` and coded with hierarchical tags, so they are best browsed in Obsidian (open this folder as a vault).

## What's here

The vault has three top-level folders: `data/` holds the source corpus (what was collected), `analysis/` holds the researcher's interpretive work (what was made of it), and `source/` holds the bibliographic notes for the works under review.

### `data/` — the corpus

Source material gathered for each case, lightly normalized into linked notes.

| Folder | Count | Contents |
| --- | --- | --- |
| `reviews/` | 34 | The informal peer-review artifacts themselves — blog posts, PubPeer threads, social-media critiques. **Also holds appraisals** (evaluations of specific papers/claims), distinguished by a `type: review` / `type: appraisal` field (22 reviews + 12 appraisals ≈ **27 distinct review events**). |
| `posters/` | 27 | People who post reviews, comments, and critiques (reviewers, commenters). Canonical home for reviewer notes. Nearly all (25/27) carry a profile `url` and a short bio; aggregate or pseudonymous accounts (e.g. `reddit users`) are the exceptions. |
| `authors/` | 14 | Study authors (`study authors/`, 13) and ethnography authors (`ethnography authors/`, 1) |
| `sites/` | 20 | Platforms/venues where review happens (PubPeer, particular blogs, GitHub, etc.), organized by interaction structure. The generic notes (`twitter`, `reddit`, `blog`, …) double as the platform *type*; the former separate `settings/` folder was archived. |
| `commentaries/` | 2 | Meta-commentary in which participants discuss informal peer review itself |

### `source/` — the works under review

| Folder | Count | Contents |
| --- | --- | --- |
| `source/` | 9 | Bibliographic notes (`type: source`) for the scientific works being scrutinized — a paper, preprint, or poster — keyed by a Zotero-style `@citekey`. The paper calls these *research reports*. Connected notes link to them via the `sourceReport:` property. |

### `analysis/` — the interpretive work

Analytic notes, memos, and the coding scheme produced while working the corpus.

| Folder | Count | Contents |
| --- | --- | --- |
| `cases/` | 12 | Per-case analytic notes — the preprint's 10 reported cases plus 2 extra memo-coded cases |
| `memos/Case Memos/` | 14 | Dated analytic memos worked case by case |
| `memos/Meta Memos/` | 31 | Reflexive research journal — `Meta - EOD` (end of day), `Meta - EOW` (end of week), `Meta - EOS` (end of session) |
| `memos/Commentaries/` | 8 | Memos on the commentary material |

_Totals as of the last cleanup pass — ~171 notes across the vault (excludes the local, gitignored `_archive/`). The vault is edited/synced live, so counts drift; see [SCHEMA.md](SCHEMA.md) for per-`type` counts and how to regenerate them._

## Method notes

- **Metadata schema.** Every note carries YAML frontmatter (`type`, `noteID`, `created`, `status`, `tags`) plus relational `[[wikilink]]` fields. See **[SCHEMA.md](SCHEMA.md)** for the full data dictionary and controlled vocabularies, and **[DATA-QUALITY.md](DATA-QUALITY.md)** for known consistency issues.
- **Coding scheme.** Analysis uses a hierarchical, tag-based codebook. Codes are nested paths describing the *who / why / how / where* of a review — e.g. `#inpeer/who/reviewer/roles/sleuth`, `#inpeer/how/practices/appraise/paper/frames/destructive`, `#inpeer/infrastructure/where/multimedia/pubpeer`. See **[CODEBOOK.md](CODEBOOK.md)** for the full codebook — every code at every level (Tables 1–11), with definitions, RQ mapping, instance counts, and grounded examples linked to vault notes.
- **Linking.** Cases, people, sources, sites, and reviews are connected with Obsidian `[[wikilinks]]` (in both frontmatter and body), so a source note links to its authors, the reviews of it, and the platforms where those reviews appeared.
- **Dates** in memo filenames follow `YYYY-MM-DD`.

## AI-use disclosure

Portions of this repository's **data curation** were performed with AI assistance, disclosed here for transparency:

- **Models:** Claude Opus 4.8 (Anthropic), 1M-context configuration; Claude Fable 5 (Anthropic).
- **Dates of use:** 2026-07-03 (Opus 4.8); 2026-07-05 (Fable 5).
- **What it did:** normalized YAML metadata across notes; consolidated/archived duplicates; added relational `[[wikilinks]]`; enriched `source/` bibliographic entries (titles, authors, DOIs, retraction flags) via web search; wrote reviewer bios and profile URLs; drafted the `SCHEMA.md` / `DATA-QUALITY.md` / `TODO.md` scaffolding; audited the vault against its documentation; backfilled original capture URLs (`source:`) on review/commentary notes (5 recovered via web search — flagged in `TODO.md` for spot-checking); added `CITATION.cff`; linked `sites/` ↔ `cases/` bidirectionally; wrote labeled case summaries (preprint placement + orange summary) in `analysis/cases/`; and drafted `CODEBOOK.md` (Level 1–3 code definitions grounded in the vault's own glosses and excerpts).
- **Labeling:** AI-generated **reviewer biographies** in `data/posters/` are shown in orange text with a `[^claude-bio]` footnote; AI-generated **case summaries** in `analysis/cases/` are shown in orange text with a `[^claude-case]` footnote. Other AI-assisted edits are structural (metadata/links) rather than interpretive.
- **Human oversight:** All AI output was reviewed and checked by **Jay Patel**. The analytic content (memos, coding, case interpretation) is the author's own.

## Notes on the repository

- `.obsidian/` holds vault configuration (themes, hotkeys, templates, settings). Installed **plugins are intentionally excluded** via `.gitignore` (`.obsidian/plugins/`) — they are large binaries and not part of the research data.
- Content is plain Markdown; no build step.

## Citation

See [CITATION.cff](CITATION.cff) — cite the dataset and the preprint (Patel & Chan, 2026, *You can just review things: A digital ethnography of informal peer review*).

## License

Released under [CC0 1.0 Universal](LICENSE) (public domain dedication).
