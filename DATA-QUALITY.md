# Data-quality notes & known issues

This file tracks known consistency issues in the dataset. It supports transparency and reuse (FAIR). See [SCHEMA.md](SCHEMA.md) for the intended structure.

_Status: all **~171** live notes carry `type` + `noteID` + `status` (YAML-validated). Superseded/archived material lives under the gitignored `_archive/`. **The vault is edited/synced live, so counts drift.**_

> **Rename (2026-07-03):** what the paper calls a *research report* now lives in the `source/` folder as `type: source`; the relational link field was renamed `report:`/`reviewof:` → `sourceReport:` across cases, memos, and reviews.

## 1. Ambiguous wikilinks — resolved

The paper/report/case name triples (e.g. `Aspartame`, `SORA model`) and the duplicate person notes are **resolved** (redundant reports and non-memo cases archived; `data/people/` merged into `data/posters/`; and the `data/papers/` folder — which duplicated `source/` — was removed during a sync, recoverable from git).

**Duplicate site notes — resolved (2026-07-05):** 10 flat root-level `data/sites/` notes (github, mastodon, pubpeer, retractionwatch, twitter, reddit, hackernews, blog, bluesky, and a second Statistical Modeling blog note) duplicated the taxonomy-subfolder copies with separate `noteID`s, dating to the initial import. The frontmatter-only root copies were archived to `_archive/duplicate-sites/`; the taxonomy copies (which carry the inbound links) are canonical. `blog - Statistical Modeling` now carries the long blog name as aliases.

**Site/setting name clashes — resolved (2026-07-05):** the 6 `data/settings/` notes (`blog`, `bluesky`, `hackernews`, `mastodon`, `reddit`, `twitter`) were empty stubs whose names clashed with `data/sites/` notes. They were archived to `_archive/settings-superseded/`; the generic site notes now double as the platform type, and every formerly ambiguous `[[name]]` link resolves uniquely to its site note (verified). No name clashes remain in the live vault.

## 2. Fragmented / duplicate case names — resolved

- **Power analysis (Bishop / G\*Power):** ✅ merged into a single case `Incorrect power analysis in G-Power` (renamed from `…G*Power` in v2, because Windows does not allow `*` in filenames; the old name is kept as an alias); the former names `Multiple incorrect power analyses in G*Power` and `Power analysis critique` are kept as **aliases**, and the duplicate notes moved to `_archive/cases-merged/`.
- **Social-media / AI-image clusters:** ✅ the duplicate/fragment case notes were archived (they were not coded in a memo — see §3).

## 3. Cases — scope after cleanup

`analysis/cases/` holds **12 cases**: the **10 distinct cases reported in the preprint** (Patel & Chan 2026; the paper's case titles are stored as `aliases`, with *Metascience Preregistration* and *Cassava Sciences Fraud* each used across two themes) plus **2 additional memo-coded cases** (`Culturally Biased SPSP Poster`, `Time-restricted Feeding`). Cases with no memo/paper connection were archived:

- `_archive/orphan-cases/` — 98 fully-isolated empty stubs.
- `_archive/cases-no-memo/` — 11 cases that had links but no memo coding.
- `_archive/cases-merged/` — 2 Bishop power-analysis duplicates (folded into the canonical case).

Remaining cases are mostly `status: stub` — the human analytic write-up lives in the memos, not the case note. As of 2026-07-05, each case note carries a preprint-placement line (whether/where it appears in Patel & Chan 2026) and an orange, footnoted AI-generated summary (`[^claude-case]`), plus bidirectional `sites` ↔ `cases` links.

## 4. Coding vocabulary — `#inpeer/` only in the live vault

The earlier `#zoo/…` → `#inpeer/…` migration is effectively complete for the live dataset: **82 notes use `#inpeer/`, 0 use a top-level `#zoo/`** (a `#misc/zoo/…` working-notes branch remains; see the codebook's *Tags outside the coding tree*). Remaining `#zoo/` tags exist only on archived notes.

## 5. Provenance gaps

- Many notes lack a `created` timestamp; only source-captured notes reliably carry `created`/`source`/`permalink`.
- **Capture URLs backfilled (2026-07-05):** 35 of 36 `review` / `appraisal` / `commentary` notes now carry a `source` (original URL) — most recovered from the capture bodies, 5 via web search (flagged in `TODO.md` for spot-checking). The one gap is `gelman blog langer` (empty stub, ambiguous target — see `TODO.md`). Archived `permalink`s remain rare (2 notes); adding archive.today/Wayback links is still worthwhile for the social-media captures.

## 6. Sources (research reports) — residual verification

See `TODO.md` for open items: the `@ferguson2024social` venue/DOI, the duplicate `@wang2012reducing`/`@wang2012reducinga` citekeys, and first-author-only author lists. (`@dadamo` and `@bartik` were archived as orphan sources.) Note several reviewed works are **retracted** or carry an **Expression of Concern** (flagged in each source's `publicationStatus`).

## 7. Archived material (gitignored, kept locally)

| Folder                              | Count | What                                                                 |
| ----------------------------------- | ----- | -------------------------------------------------------------------- |
| `_archive/orphan-cases/`            | 98    | fully-isolated empty case stubs                                      |
| `_archive/cases-no-memo/`           | 11    | cases not coded in a memo                                            |
| `_archive/cases-merged/`            | 2     | Bishop power-analysis duplicates                                     |
| `_archive/redundant-named-reports/` | 9     | named reports duplicating `source/`/paper notes                      |
| `_archive/appraisals-superseded/`   | 8     | old-vocabulary appraisal duplicates                                  |
| `_archive/redundant-people/`        | 7     | `data/people/` copies merged into `data/posters/`                    |
| `_archive/unlinked-study-authors/`  | 8     | study authors with no reviewers/cases/memos                          |
| `_archive/orphan-sources/`          | 4     | sources with no live author/case/review                              |
| `_archive/blank-orphan-reports/`    | 4     | blank, unlinked `@citekey` reports                                   |
| `_archive/blank-orphan-papers/`     | 1     | blank, unlinked paper                                                |
| `_archive/duplicate-sites/`         | 10    | flat root-level site notes duplicating the taxonomy-subfolder copies |
| `_archive/settings-superseded/`     | 6     | empty platform-type stubs; generic site notes now carry this role    |

## 8. Missing images

17 screenshots embedded 18 times in notes are not in this dataset, so those embeds show as broken. They were not found in the authors' working copies when checked on 2026-11-02. The surrounding text remains, and the supplementary materials (S3) describe how captures were saved.

Missing files: `Pasted image 20240308164926`, `Pasted image 20240308170108`, `Pasted image 20240905193510`, and `Screenshot` files dated 2024-09-05 (17.40.30, 19.38.18, 19.38.38), 2024-09-12 (18.58.31), 2024-09-28 (22.21.02, 22.40.58), 2024-11-05 (15.14.35, 15.15.32, 19.07.10), 2024-11-06 (18.10.22), 2024-11-07 (14.03.36), 2024-11-09 (19.59.15, 20.56.56), and 2024-11-11 (19.34.17).

## 9. Unresolved wikilinks

By a scripted count on 2026-11-02, about 359 of 938 wikilinks in the notes (case-insensitive, counting aliases, excluding image embeds) point to no note. Many are leftovers from the Roam Research import in memo text, such as daily-note dates and block references, or point to people without a note, such as study co-authors. They are left as written to preserve the memos as the record of the analysis.

## 10. Thin review notes

Three of the 34 notes in `data/reviews/` hold almost no content: `gelman blog langer`, `fried twitter wu`, and `hullman blog Protzko`. Their target or source URL is listed in `TODO.md` where one needs checking.

## 11. Dataset versus paper counts

- **Study authors:** the paper reports 21. This vault has 13 live notes, and 8 more with no links are in `_archive/unlinked-study-authors/`, which accounts for the difference.
- **Codes:** the paper and supplementary materials report 1,080 codes. This vault has 455 (`CODEBOOK.md`). The difference is not yet explained; see `TODO.md`.
- **Websites:** the paper reports sixteen distinct websites and the vault has 20 site notes, some of them generic platform categories. The difference is not yet itemized.

