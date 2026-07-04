# Data-quality notes & known issues

This file tracks known consistency issues in the dataset. It supports transparency and reuse (FAIR). See [SCHEMA.md](SCHEMA.md) for the intended structure.

_Status: all **~188** live notes carry `type` + `noteID` + `status` (YAML-validated). Superseded/archived material lives under the gitignored `_archive/`. **The vault is edited/synced live, so counts drift.**_

> **Rename (2026-07-03):** what the paper calls a *research report* now lives in the `source/` folder as `type: source`; the relational link field was renamed `report:`/`reviewof:` → `sourceReport:` across cases, memos, and reviews.

## 1. Ambiguous wikilinks — platform note vs setting note

The paper/report/case name triples (e.g. `Aspartame`, `SORA model`) and the duplicate person notes are **resolved** (redundant reports and non-memo cases archived; `data/people/` merged into `data/posters/`; and the `data/papers/` folder — which duplicated `source/` — was removed during a sync, recoverable from git). What remains: **6 site/setting name clashes**, where a `data/settings/` note (platform *type*) shares a name with a `data/sites/` note (specific venue):

`blog` · `bluesky` · `hackernews` · `mastodon` · `reddit` · `twitter`

→ Distinct concepts (type vs instance). Consider renaming the setting notes (e.g. `blog (platform type)`) to break the clash.

## 2. Fragmented / duplicate case names — resolved

- **Power analysis (Bishop / G\*Power):** ✅ merged into a single case `Incorrect power analysis in G*Power`; the former names `Multiple incorrect power analyses in G*Power` and `Power analysis critique` are kept as **aliases**, and the duplicate notes moved to `_archive/cases-merged/`.
- **Social-media / AI-image clusters:** ✅ the duplicate/fragment case notes were archived (they were not coded in a memo — see §3).

## 3. Cases — scope after cleanup

`analysis/cases/` holds **12 cases**: the **10 distinct cases reported in the preprint** (Patel & Chan 2026; the paper's case titles are stored as `aliases`, with *Metascience Preregistration* and *Cassava Sciences Fraud* each used across two themes) plus **2 additional memo-coded cases** (`Culturally Biased SPSP Poster`, `Time-restricted Feeding`). Cases with no memo/paper connection were archived:

- `_archive/orphan-cases/` — 98 fully-isolated empty stubs.
- `_archive/cases-no-memo/` — 11 cases that had links but no memo coding.
- `_archive/cases-merged/` — 2 Bishop power-analysis duplicates (folded into the canonical case).

Remaining cases are mostly `status: stub` (they carry links but the analytic write-up lives in the memos, not the case note).

## 4. Coding vocabulary — `#inpeer/` only in the live vault

The earlier `#zoo/…` → `#inpeer/…` migration is effectively complete for the live dataset: **82 notes use `#inpeer/`, 0 use `#zoo/`**. Remaining `#zoo/` tags exist only on archived notes.

## 5. Provenance gaps

- Many notes lack a `created` timestamp; only source-captured notes reliably carry `created`/`source`/`permalink`.
- Ensure every `review` / `appraisal` / `commentary` retains its `source` (original URL) and, where possible, an archived `permalink`.

## 6. Sources (research reports) — residual verification

See `TODO.md` for open items: unverified `@dadamo` title, `@ferguson`/`@bartik` specifics, the duplicate `@wang2012reducing`/`@wang2012reducinga` citekeys, and first-author-only lists. Note several reviewed works are **retracted** or carry an **Expression of Concern** (flagged in each source's `publicationStatus`).

## 7. Archived material (gitignored, kept locally)

| Folder | Count | What |
|---|---|---|
| `_archive/orphan-cases/` | 98 | fully-isolated empty case stubs |
| `_archive/cases-no-memo/` | 11 | cases not coded in a memo |
| `_archive/cases-merged/` | 2 | Bishop power-analysis duplicates |
| `_archive/redundant-named-reports/` | 9 | named reports duplicating `source/`/paper notes |
| `_archive/appraisals-superseded/` | 8 | old-vocabulary appraisal duplicates |
| `_archive/redundant-people/` | 7 | `data/people/` copies merged into `data/posters/` |
| `_archive/unlinked-study-authors/` | 8 | study authors with no reviewers/cases/memos |
| `_archive/orphan-sources/` | 4 | sources with no live author/case/review |
| `_archive/blank-orphan-reports/` | 4 | blank, unlinked `@citekey` reports |
| `_archive/blank-orphan-papers/` | 1 | blank, unlinked paper |
