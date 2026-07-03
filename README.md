# informal-peer-review

Repository of data and analyses from a digital ethnography of **informal peer review** — the public, post-publication scrutiny of scientific work that happens on blogs, PubPeer, and social media (Bluesky, X/Twitter) rather than through journals' formal review processes.

This repository is an [Obsidian](https://obsidian.md) vault. The notes are plain Markdown and can be read on GitHub or in any text editor, but they are richly cross-linked with `[[wikilinks]]` and coded with hierarchical tags, so they are best browsed in Obsidian (open this folder as a vault).

## What's here

The vault is split into two top-level folders: `data/` holds the source corpus (what was collected), and `analysis/` holds the researcher's interpretive work (what was made of it).

### `data/` — the corpus

Source material gathered for each case, lightly normalized into linked notes.

| Folder | Contents |
| --- | --- |
| `papers/` | The scientific papers and preprints being scrutinized |
| `authors/` | Authors of those papers |
| `reviews/` | The informal peer-review artifacts themselves — blog posts, PubPeer threads, social-media critiques |
| `posters (reviewers, commenters)/` | People who post reviews, comments, and critiques |
| `people/` | Individual-person notes (reviewers, authors, commenters) |
| `sites/` | Specific platforms/venues where review happens (PubPeer, particular blogs, GitHub, etc.) |
| `settings/` | Platform *types* and their affordances (blog, bluesky, twitter, …) |
| `appraisals/` | Collected evaluations of specific papers/claims |
| `commentaries/` | Meta-commentary in which participants discuss informal peer review itself |
| `research reports/` | Bibliographic reference notes, keyed by Zotero-style `@citekey` |
| `cases/` | Case landing notes (see also `analysis/cases/`) |

### `analysis/` — the interpretive work

Analytic notes, memos, and the coding scheme produced while working the corpus.

| Folder | Contents |
| --- | --- |
| `cases/` | Per-case analytic notes, one per instance of informal peer review |
| `appraisals/` | Analytic appraisals |
| `memos/Case Memos/` | Dated analytic memos worked case by case |
| `memos/Meta Memos/` | Reflexive research journal — `Meta - EOD` (end of day), `Meta - EOW` (end of week), `Meta - EOS` (end of session) |
| `memos/Commentaries/` | Memos on the commentary material |
| `memos/Codebook/` | The coding scheme (see below) |

## Method notes

- **Coding scheme.** Analysis uses a hierarchical, tag-based codebook. Codes are nested paths that describe the *who / why / how / where* of a review — e.g. `review/who/reviewer/roles/sleuth`, `review/how/practices/appraise/paper/frames/destructive`, `review/infrastructure/where/multimedia/pubpeer` — alongside a `zoo/…` branch for the surrounding social and institutional context. The `Codebook` note regenerates the live tag list from the vault.
- **Linking.** Cases, people, papers, sites, and reviews are connected with Obsidian `[[wikilinks]]`, so a paper note links to its authors, the reviews of it, and the platforms where those reviews appeared.
- **Dates** in memo filenames follow `YYYY-MM-DD`.

## Notes on the repository

- `.obsidian/` holds vault configuration (themes, hotkeys, templates, settings). Installed **plugins are intentionally excluded** via `.gitignore` (`.obsidian/plugins/`) — they are large binaries and not part of the research data.
- Content is plain Markdown; no build step.

## License

Released under [CC0 1.0 Universal](LICENSE) (public domain dedication).
