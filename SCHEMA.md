# Data dictionary & metadata schema

This document defines the core terms, note types, metadata (YAML frontmatter) fields, and controlled vocabularies used in this dataset. It is the reference for keeping the vault consistent and machine-readable (FAIR: *Findable* / *Interoperable* / *Reusable*).

## Core definitions

The dataset is built from five interlocking entities:

| Term | Note type / folder | Count | Definition |
|---|---|---|---|
| **Source** | `type: source` — `source/` | 9 | The original scholarly work being scrutinized (a "research report"): a paper, preprint, poster, book, or other research output. The *object* under review. Keyed by a Zotero-style `@citekey`. |
| **Study authors** | `type: person` — `data/authors/study authors/` | 13 | The people who produced a source — i.e., the authors of the work being reviewed. |
| **Review** | `type: review` / `appraisal` — `data/reviews/` | 34 | A single instance of *informal peer review*: a public post, thread, or comment that evaluates a source, published outside formal journal review (on a blog, PubPeer, or social media). An **appraisal** is a review whose focus is judging the work's quality/validity. The 34 files (22 reviews + 12 appraisals) collapse to **~27 distinct review events**. |
| **Reviewer** | `type: person` — `data/posters/` | 27 | A person who authors a review — the informal peer reviewer or commenter (a.k.a. "poster"). |
| **Case** | `type: case` — `analysis/cases/` | 12 | One episode of informal peer review: a source *together with* the review(s) of it, the reviewer(s) who wrote them, and the venue(s) where they appeared. The **unit of analysis**. |

A reviewer (poster) writes a review about a source (a research report) on a site like PubPeer or Bluesky. This constitutes an informal peer review case on a site publicly. The study authors of the source may or may not respond to the informal peer review.

> **Naming note:** what the paper calls a *research report* is stored as `type: source` in the `source/` folder (which the vault's sync auto-generates). The relational field that links a case/review/memo to its source is **`sourceReport:`** (the field name `source:` was already taken for capture URLs).

## Scope: what is in the paper vs. the dataset

- **The paper** describes **10 cases in detail**. Of these, roughly **2 cases inform more than one analytic theme** (a case can be discussed under multiple themes).
- **The broader analysis** is informed by **34 review artifacts** (22 `review` + 12 `appraisal` notes in `data/reviews/`) that collapse to **~27 distinct review events**. Multi-part series count once per reviewer + target (e.g. Bik's Science Integrity posts on Wang → 1; each degrowth thread → 1 per reviewer).
- The vault also retains **12 case notes** (the preprint's 10 reported cases plus 2 extra memo-coded cases), **9 sources**, **27 reviewers**, and **13 study authors** after cleanup. Cases not coded in a memo were archived to `_archive/cases-no-memo/` (earlier orphan stubs to `_archive/orphan-cases/`); see `DATA-QUALITY.md`.

Conventions:
- **Frontmatter** is YAML between `---` fences at the very top of every note.
- **Relational fields hold Obsidian `[[wikilinks]]`** to other notes (single value, or a YAML list for many). This is how records link to each other.
- **Dates** are ISO-8601 (`YYYY-MM-DDThh:mm:ss`, or `YYYY-MM-DD` for day-only).
- **Identifiers** use `noteID` — a UUID that persists even if the note is renamed.
- **Tags** use the project taxonomy, primarily the `#inpeer/…` hierarchy (see *Coding taxonomy* below).

## Fields on every note

| Field | Required | Description |
|---|---|---|
| `type` | yes | The note type — one of the values in the table below. |
| `noteID` | yes | UUID, stable across renames. |
| `created` | yes | ISO-8601 timestamp the record was created/captured. |
| `status` | yes | `complete` = written up; `stub` = placeholder needing content. |
| `tags` | no | List of taxonomy tags (may also appear inline as `#inpeer/…`). |

## Note types

Counts are as of the last cleanup pass (**total: 172 notes**; excludes the gitignored `_archive/`). Regenerate after changes — see *Maintaining totals* below.

| `type` | Folder | Count | What it represents | Key relational fields |
|---|---|---|---|---|
| `review` | `data/reviews/` | 22 | An informal peer-review artifact (blog post, PubPeer thread, social-media critique). | `sourceReport` → source · `author` → person · `site` → site · `memos` → memo(s) · `source`, `permalink` (URLs) · `casetype` |
| `appraisal` | `data/reviews/` | 12 | An evaluation of a specific paper/claim (a review focused on judging quality). Lives alongside reviews; distinguished by `type`. | `sourceReport` → source · `appraiser`/`author` → person · `source` (URL) |
| `source` | `source/` | 9 | Bibliographic note for the original study (research report), keyed `@authorYearTitle`. | `authors` → person(s) · `url` · `publicationStatus` · `cases` · `appraiser` |
| `person` | `data/posters/` (reviewers/commenters), `data/authors/` (study & ethnography authors) | 41 | An individual: reviewer, commenter, or study author. | `url` · `credentials` · `community` · `domain` |
| `site` | `data/sites/…` | 20 | A venue where review happens (a blog, PubPeer, a Bluesky account), organized in interaction-structure subfolders (see *Site taxonomy*). Generic notes (`twitter`, `reddit`, `blog`, …) double as the platform *type* — the former `type: setting` notes in `data/settings/` were archived (they were empty stubs whose names clashed with these). Flat root-level duplicates were also archived. | `cases` → case(s) · `url` |
| `case` | `analysis/cases/` | 12 | One instance of informal peer review, tying together a source, its reviews, people, and sites. | `sourceReport` · `reviews` · `people` · `sites` · `memos` · `casetype` |
| `memo` | `analysis/memos/…` | 53 | Analytic or reflexive memo. Subtypes by folder: Case Memos, Meta Memos (EOD/EOW/EOS), Commentaries. | `sourceReport` · `reviews` · `cases` · `reviewers` · `authors` · `sites` · `source` |
| `commentary` | `data/commentaries/` | 2 | Participant meta-commentary about informal peer review itself. | `reviewers` → person · `cases` · `sites` · `source` |
| `reference` | `analysis/memos/Codebook/` | 1 | The coding-scheme template that regenerates the live tag list. | — |

> Note on people: `data/posters/` (reviewers/commenters) and `data/authors/` (`study authors` / `ethnography authors`) both use `type: person`; the folder and the `community`/`domain` fields carry the role distinction. The former redundant `data/people/` folder was merged into `data/posters/`.

> Note on the removed `paper` type: an earlier `type: paper` / `data/papers/` folder held named notes that duplicated the `source/` entries; that folder was removed during consolidation (its notes are recoverable from git history if needed).

### Maintaining totals

The counts above and in *Core definitions* are a snapshot (the vault is edited/synced live). To regenerate:

```
grep -rh '^type:' data analysis source --include='*.md' | sort | uniq -c
```

## Site taxonomy

Sites are organized by interaction structure under `data/sites/`:
`flat network`, `threaded commons` (e.g. `blogs`), `threaded network` (e.g. `bluesky`), `threaded space` (e.g. `reddit`). The subfolder placement plus the generic platform notes (`twitter`, `reddit`, `blog`, …) carry the platform-type information that the archived `data/settings/` notes used to represent.

## Controlled vocabularies

- **`status`**: `complete` · `stub`
- **`casetype`**: `central` (extend as needed; document new values here)
- **`publicationStatus`**: a base status — `published` · `preprint` · `unpublished` — optionally followed by `; ` and a qualifier noting a retraction or Expression of Concern (e.g. `published; RETRACTED Sept 2024`, `published; Expression of Concern`). Machines filtering this field should match on substrings, not exact values.
- **`type`**: the values in the Note types table above.

## Coding taxonomy (tags)

Analytic coding uses a hierarchical tag tree. The **current/primary** namespace is `#inpeer/…`, organized by the dimensions of a review — e.g.:

- `#inpeer/who/reviewer/roles/…` — who reviews (sleuth, hero, expert, …)
- `#inpeer/why/motives/…` — why they review
- `#inpeer/how/practices/…` — how review is done (e.g. `…/appraise/paper/frames/destructive`)
- `#inpeer/infrastructure/where/…` — where review happens (platforms/multimedia)

A retained secondary branch, `#zoo/…`, captures surrounding social/institutional context and some earlier coding; only `#inpeer/` tags remain in the live vault.

The live list of tags in the vault can be regenerated from `analysis/memos/Codebook/`.

## Provenance

For source-captured records (reviews, appraisals, commentaries), retain the original capture URL (`source`/`url`) and, where available, a `permalink` to an archived copy (e.g. archive.ph). This preserves the chain back to the observed material.
