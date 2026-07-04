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
| `posters/` | 27 | People who post reviews, comments, and critiques (reviewers, commenters). Canonical home for reviewer notes. Each carries a profile `url` and a short bio. |
| `authors/` | 14 | Study authors (`study authors/`, 13) and ethnography authors (`ethnography authors/`, 1) |
| `sites/` | 30 | Specific platforms/venues where review happens (PubPeer, particular blogs, GitHub, etc.) |
| `settings/` | 6 | Platform *types* grouped by their affordances (blog, bluesky, twitter, …) |
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
| `memos/Codebook/` | 1 | The coding scheme (see below) |

_Totals as of the last cleanup pass — ~188 notes across the vault (excludes the local, gitignored `_archive/`). The vault is edited/synced live, so counts drift; see [SCHEMA.md](SCHEMA.md) for per-`type` counts and how to regenerate them._

## Method notes

- **Metadata schema.** Every note carries YAML frontmatter (`type`, `noteID`, `created`, `status`, `tags`) plus relational `[[wikilink]]` fields. See **[SCHEMA.md](SCHEMA.md)** for the full data dictionary and controlled vocabularies, and **[DATA-QUALITY.md](DATA-QUALITY.md)** for known consistency issues.
- **Coding scheme.** Analysis uses a hierarchical, tag-based codebook. Codes are nested paths describing the *who / why / how / where* of a review — e.g. `#inpeer/who/reviewer/roles/sleuth`, `#inpeer/how/practices/appraise/paper/frames/destructive`, `#inpeer/infrastructure/where/multimedia/pubpeer`. The `Codebook` note regenerates the live tag list from the vault.
- **Linking.** Cases, people, sources, sites, and reviews are connected with Obsidian `[[wikilinks]]` (in both frontmatter and body), so a source note links to its authors, the reviews of it, and the platforms where those reviews appeared.
- **Dates** in memo filenames follow `YYYY-MM-DD`.

## AI-use disclosure

Portions of this repository's **data curation** were performed with AI assistance, disclosed here for transparency:

- **Model:** Claude Opus 4.8 (Anthropic), 1M-context configuration.
- **Date of use:** 2026-07-03.
- **What it did:** normalized YAML metadata across notes; consolidated/archived duplicates; added relational `[[wikilinks]]`; enriched `source/` bibliographic entries (titles, authors, DOIs, retraction flags) via web search; wrote reviewer bios and profile URLs; and drafted the `SCHEMA.md` / `DATA-QUALITY.md` / `TODO.md` scaffolding.
- **Labeling:** AI-generated **reviewer biographies** in `data/posters/` are shown in orange text with a `[^claude-bio]` footnote. Other AI-assisted edits are structural (metadata/links) rather than interpretive.
- **Human oversight:** All AI output was reviewed and checked by **Jay Patel**. The analytic content (memos, coding, case interpretation) is the author's own.

## Notes on the repository

- `.obsidian/` holds vault configuration (themes, hotkeys, templates, settings). Installed **plugins are intentionally excluded** via `.gitignore` (`.obsidian/plugins/`) — they are large binaries and not part of the research data.
- Content is plain Markdown; no build step.

## License

Released under [CC0 1.0 Universal](LICENSE) (public domain dedication).
