# informal-peer-review

This is a repository of data, analyses, and codebook from our digital ethnography of **informal peer review** — the public, publisher-independent scrutiny of scientific work that happens on blogs, PubPeer, and social media (Bluesky, X/Twitter).

This repository is an [Obsidian](https://obsidian.md) vault. The notes are plain Markdown (.md) and can be read on GitHub or in any text editor, but they are richly cross-linked with `[[wikilinks]]` and coded with hierarchical tags, so they are best browsed in the free Obsidian desktop application. Open this folder as a vault.

## At a glance

| | |
| --- | --- |
| **Paper** | Patel, J., & Chan, J. (2026). *You can just review things: A digital ethnography of informal peer review*. arXiv:2604.16764. <https://doi.org/10.48550/arXiv.2604.16764> |
| **This dataset (archived)** | <https://doi.org/10.6084/m9.figshare.33187710> (always resolves to the latest version; see [Versions](#versions)) |
| **Supplementary materials** | <https://doi.org/10.6084/m9.figshare.32048553> |
| **Working copy** | <https://github.com/oasisresearchlab/informal-peer-review> (a development copy that can change; cite the DOI) |
| **Authors** | Jay Patel (ORCID [0000-0003-1040-3607](https://orcid.org/0000-0003-1040-3607)) and Joel Chan (ORCID [0000-0003-3000-4160](https://orcid.org/0000-0003-3000-4160)), University of Maryland, College Park |
| **Contact** | Jay Patel, <patel93@hey.com> |
| **Funding** | None |
| **Ethics** | University of Maryland, College Park IRB, Exempt status, #2187204-1 (see [Ethics](#ethics)) |
| **Licence** | CC0 1.0 for the authors' own contributions; third-party material is excluded (see [License](#license)) |

## About the study

The paper asks four questions: (1) Who are informal peer reviewers? (2) Where do informal peer reviewers work? (3) How do informal peer reviewers evaluate scholarly reports? (4) What are the impacts of informal reviews on publishers, study authors, and others? It answers them with a cross-platform digital ethnography with active participant observation, reporting ten unique cases. This dataset is the audit trail behind that report: the captured material, the memos, the codes, and the codebook.

- **Fieldwork dates:** memos in this vault run from 2024-07-26 to 2024-11-12. The paper followed up on all cases after nine and twelve months.
- **Where the data come from:** English-language public posts on platforms including Twitter/X, Bluesky, Reddit, PubPeer, ResearchHub, and personal or collaborative blogs. Inclusion and exclusion criteria are in the supplementary materials (S2).
- **Software:** threads saved with Zotero 7 (supplementary materials, S3); memoed in Roam Research, macOS desktop app v0.0.22; coded in Obsidian v1.7.5 (S5).

## Getting started

1. Download the archived deposit or clone this repository. Keep the folder structure, because folders carry meaning (see [SCHEMA.md](SCHEMA.md)). On macOS, extract Figshare's zip with `tar -xf` rather than `unzip`, which stops partway on it.
2. Open the folder as a vault in Obsidian, or read the Markdown files in any text editor. Nothing needs to be installed or built. Community plugins are not included, so Obsidian may list them as missing; they are not needed to read the notes.
3. Follow the analysis in this order: [CODEBOOK.md](CODEBOOK.md), then `analysis/cases/`, then `analysis/memos/`, then the captured material in `data/`. The codebook includes a worked example that walks one finding back to its source post.
4. To rebuild the coding audit trail, run `python3 scripts/code_audit.py`. It reads the notes in `data/`, `analysis/`, and `source/` and the tables in `CODEBOOK.md`, and overwrites the two CSV files below. It needs Python 3 with no packages, takes a few seconds, and changes no notes. It was run on Python 3.14.

### Top-level files

| File | Purpose |
| --- | --- |
| [CODEBOOK.md](CODEBOOK.md) | Every code used in these notes, its definition, research question, count, and example, plus how the coding annotates the data. |
| `codebook.csv` | The same codebook entries as a table, with a `definition_source` column. Generated. |
| `code-applications.csv` | One row per code applied: code, note, line, note type, and adjacent gloss. Generated. |
| [SCHEMA.md](SCHEMA.md) | Data dictionary for note types, metadata fields, and controlled vocabularies. |
| [DATA-QUALITY.md](DATA-QUALITY.md) | Known gaps and consistency issues. |
| [TODO.md](TODO.md) | Open items, including anything not yet verified. |
| `scripts/code_audit.py` | Generates the two CSV files. |
| `attachments/` | Screenshots embedded in notes that could be recovered (see [DATA-QUALITY.md](DATA-QUALITY.md) §8). |
| [AI-PROMPTS.md](AI-PROMPTS.md) | Model details and verbatim prompts for the v2 changes. |
| [CITATION.cff](CITATION.cff) | Machine-readable citation. |

## What's here

The vault has three top-level folders: `data/` holds the source corpus (what was collected), `analysis/` holds the researcher's interpretive work (what was made of it), and `source/` holds the bibliographic notes for the works under review.

### `data/` — the corpus

Source material gathered for each case

| Folder          | Count | Contents                                                                                                                                                                                                                                                                                          |
| --------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `reviews/`      | 34    | The informal peer-review artifacts themselves — blog posts, PubPeer threads, social-media critiques. **Also holds appraisals** (evaluations of specific papers/claims), distinguished by a `type: review` / `type: appraisal` field (22 reviews + 12 appraisals ≈ **27 distinct review events**). |
| `posters/`      | 27    | People who post reviews, comments, and critiques (reviewers, commenters). Canonical home for reviewer notes. Nearly all (25/27) carry a profile `url` and a short bio; aggregate or pseudonymous accounts (e.g. `reddit users`) are the exceptions.                                               |
| `authors/`      | 14    | Study authors (`study authors/`, 13) and ethnography authors (`ethnography authors/`, 1)                                                                                                                                                                                                          |
| `sites/`        | 20    | Platforms/venues where review happens (PubPeer, particular blogs, GitHub, etc.), organized by interaction structure. The generic notes (`twitter`, `reddit`, `blog`, …) double as the platform *type*; the former separate `settings/` folder was archived.                                       |
| `commentaries/` | 2     | Meta-commentary in which participants discuss informal peer review itself                                                                                                                                                                                                                         |

### `source/` — the works under review

| Folder    | Count | Contents                                                                                                                                                                                                                                                      |
| --------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `source/` | 9     | Bibliographic notes (`type: source`) for the scientific works being scrutinized — a paper, preprint, or poster — keyed by a Zotero-style `@citekey`. The paper calls these *research reports*. Connected notes link to them via the `sourceReport:` property. |

### `analysis/` — the interpretive work

Analytic notes, memos, and the coding scheme produced while working the corpus.

| Folder                | Count | Contents                                                                                                          |
| --------------------- | ----- | ----------------------------------------------------------------------------------------------------------------- |
| `cases/`              | 12    | Per-case analytic notes — the preprint's 10 reported cases plus 2 extra memo-coded cases                          |
| `memos/Case Memos/`   | 14    | Dated analytic memos worked case by case                                                                          |
| `memos/Meta Memos/`   | 31    | Reflexive research journal — `Meta - EOD` (end of day), `Meta - EOW` (end of week), `Meta - EOS` (end of session) |
| `memos/Commentaries (contains many or no appraisals)/` | 8     | Memos on the commentary material                                                                                  |

_Totals as of the last cleanup pass — ~171 notes across the vault (excludes the local, gitignored `_archive/`). The vault is edited/synced live, so counts drift; see [SCHEMA.md](SCHEMA.md) for per-`type` counts and how to regenerate them._

## Method notes

- **Metadata schema.** Every note carries YAML frontmatter (`type`, `noteID`, `status`, plus `created` and `tags` where available) and relational `[[wikilink]]` fields. See **[SCHEMA.md](SCHEMA.md)** for the full data dictionary and controlled vocabularies, and **[DATA-QUALITY.md](DATA-QUALITY.md)** for known consistency issues.
- **Coding scheme.** Obsidian's tag pane shows 1,136 for `#inpeer` (`who` 353, `evdInfra` 348, `how` 343, `digitalEthnography` 47, `why` 45). That counts every use of a code, so codes repeat: 330 distinct codes were applied, or 455 with their parent nodes, and this dataset documents those 455. The paper's figure of 1,080 likely counted uses at an earlier point, not distinct codes. Other tag trees such as `#misc/…` and `#dg/…` are irrelevant to the analyses and are ignored. Analysis uses a hierarchical, tag-based codebook. Codes are nested paths describing the *who / why / how / where* of a review — e.g. `#inpeer/who/reviewer/roles/sleuth`, `#inpeer/how/practices/review/paper/frames/destructive`, `#inpeer/evdInfra/where/multimedia/bespoke/pubpeer`. See **[CODEBOOK.md](CODEBOOK.md)** for the full codebook — every code used in these notes, at every level (Tables 1–11), with definitions, RQ mapping, instance counts, and grounded examples linked to vault notes.
- **Linking.** Cases, people, sources, sites, and reviews are connected with Obsidian `[[wikilinks]]` (in both frontmatter and body), so a source note links to its authors, the reviews of it, and the platforms where those reviews appeared.
- **Dates** in memo filenames follow `YYYY-MM-DD`.

## AI-use disclosure

Portions of this repository's **data curation** were performed with AI assistance, disclosed here for transparency:

- **Models:** Claude Opus 4.8 (Anthropic), 1M-context configuration; Claude Fable 5 (Anthropic); Claude Opus 5.5 (Anthropic), model ID `claude-opus-5-5`, via Claude Code 2.1.316. Model details and verbatim prompts for that work are in [AI-PROMPTS.md](AI-PROMPTS.md).
- **Dates of use:** 2026-07-03 (Opus 4.8); 2026-07-05 (Fable 5); 2026-11-02 (Opus 5.5).
- **What it did:** normalized YAML metadata across notes; consolidated/archived duplicates; added relational `[[wikilinks]]`; enriched `source/` bibliographic entries (titles, authors, DOIs, retraction flags) via web search; wrote reviewer bios and profile URLs; drafted the `SCHEMA.md` / `DATA-QUALITY.md` / `TODO.md` scaffolding; audited the vault against its documentation; backfilled original capture URLs (`source:`) on review/commentary notes (5 recovered via web search — flagged in `TODO.md` for spot-checking); added `CITATION.cff`; linked `sites/` ↔ `cases/` bidirectionally; wrote labeled case summaries (preprint placement + orange summary) in `analysis/cases/`; and transformed the human-written notes and codes into `CODEBOOK.md` (cleaning and organization, with human verification), drafting definitions for codes with no gloss in the notes. Of its 455 definitions, 199 quote the researcher's own glosses and 256 were drafted from the code path and coded excerpts, all grounded in the vault's fully human-generated content; `codebook.csv` marks which is which. On 2026-11-02, Claude Opus 5.5 prepared the v2 release changes: file renames, this README's added sections, the licence scope statement, `scripts/code_audit.py`, the codebook's annotation section, and new `DATA-QUALITY.md` entries, drawing on the paper and supplementary materials. It restored four screenshots from a backup and located the source URLs for two review notes, flagged in `TODO.md` for spot-checking. It also re-matched glosses to codes in `CODEBOOK.md`: 36 definitions now quote the researcher's gloss for that code, and 15 that had quoted another code's gloss or a memo remark were redrafted. It did not change coding, and in memos it changed only references to the two renamed notes.
- **Labeling:** AI-generated **reviewer biographies** in `data/posters/` are shown in orange text with a `[^claude-bio]` footnote; AI-generated **case summaries** in `analysis/cases/` are shown in orange text with a `[^claude-case]` footnote. Apart from the drafted definitions, other AI-assisted edits are structural (metadata/links) rather than interpretive.
- **Human oversight:** AI output was reviewed and checked by **Jay Patel**, except the items still open in [TODO.md](TODO.md). The analytic content (memos, coding, case interpretation) is my own work.

## Notes on the repository

- `.obsidian/` holds vault configuration (themes, hotkeys, templates, settings). Installed **plugins are intentionally excluded** via `.gitignore` (`.obsidian/plugins/`) — they are large binaries and not part of the research data.
- Content is plain Markdown; no build step.
- Some hashtags inside captured posts and quoted memo text were converted to analysis tags during coding (for example, `#misc/zoo/bin/…`), so check the original URL before treating a hashtag in quoted text as verbatim.

## Ethics

The University of Maryland, College Park IRB determined this project exempt from IRB review on July 11, 2024 (#2187204-1; 45 CFR 46.104(d)(2)(ii), (4)(i)). The anonymized letter is in the [supplementary materials](https://doi.org/10.6084/m9.figshare.32048553), S1, along with the full ethical precautions.

- **Consent:** under the exempt determination, study members did not need to consent or receive orientation (S1).
- **Naming:** posts are public, so this dataset keeps account names and URLs rather than pseudonyms (S1). The paper explains that anonymization is not possible when quoting publicly available posts, and how potential harm was weighed (§4).
- **Anonymization:** one participant asked for a direct message to be anonymized. It is redacted in `analysis/memos/Case Memos/2024-10-10, Dishonest metascience Bak-Coleman.md`.
- **Corrections:** to correct or discuss material about you, contact Jay Patel at the address above.

## Versions

| Version | DOI | Date | Contents |
| --- | --- | --- | --- |
| v1 | [10.6084/m9.figshare.33187710.v1](https://doi.org/10.6084/m9.figshare.33187710.v1) | 2026-08-07 | First deposit. Its record listed CC BY 4.0 while its files stated CC0, and it left out `TODO.md`. |
| v2 | [10.6084/m9.figshare.33187710.v2](https://doi.org/10.6084/m9.figshare.33187710.v2) | At release | Adds ethics, contact, and licence-scope documentation, DOI links, and the coding audit trail. Details are in `git log`. |

Cite the version you used. To export the files for a deposit from the tagged commit into the folder above this one, run:

```
git archive --prefix=informal-peer-review-v2/ v2.0.0 | tar -x -C ..
```

## Citation

See [CITATION.cff](CITATION.cff) — cite the dataset and the preprint (Patel & Chan, 2026, *You can just review things: A digital ethnography of informal peer review*).

## License

The **authors' own contributions** are released under [CC0 1.0 Universal](LICENSE) (public domain dedication): memos, codes and glosses, the codebook, schema, documentation, scripts, and our notes about cases, people, sites, and sources.

**CC0 does not cover third-party material**, because it is not ours to release. This includes posts, comments, blog text, and other captured content in `data/reviews/` and `data/commentaries/`, the same material quoted in `analysis/memos/`, and third-party pages shown in `attachments/`. It remains under its authors' rights and each platform's terms, and is shared here as the record of our scholarly analysis. Check with the original author or platform before reusing it for anything else.
