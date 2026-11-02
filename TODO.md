# TODO — items needing the human expert

## Open

### Sources (research reports) — residual verification

Located in `source/` (`type: source`, linked via `sourceReport:`). (`@dadamo`, `@bartik`, `@gaski`, `@AbrahmssonSara` were archived as orphan sources.)

- **`@ferguson2024social`** — two candidate 2024 Ferguson social-media meta-analyses; confirm which, add venue + DOI.
- **`@wang2012reducing` vs `@wang2012reducinga`** — duplicate citekeys for the same 2012 *J. Neuroscience* paper; consider merging.
- **Co-author completeness** — `@abou-Khalil` has first author only; `@protzko` links 3 key authors of a large consortium. Extend if needed.
- **Unresolved author links** — new co-authors (e.g. Moses Miller, Jacob Goldenberg, Noa Grobgeld) are `[[wikilinks]]` with no person note yet. Decide whether to create `person` notes for them.

### Reviewer bios — verify tentative identities

- **`Starkheiser`** — pseudonymous; no real-world bio found.
- ~~**`Syed Omar`** — tentative match to a KU cultural-psychology PhD student; not fully verified.~~
- ~~**`Kirsten T Elliot`** — moderate-confidence match (surname usually "Elliott").~~

### Data quality (see `DATA-QUALITY.md`)

- **Site URLs** — 2 generic category notes (`threaded commons/blogs/blog.md`, `threaded commons/podcast.md`) still have no `url` (may not need one). (The third, root-level `blog.md`, was archived as a duplicate.)

### Capture URLs — spot-check & residuals

- **Spot-check 5 web-recovered `source:` URLs** (added 2026-07-05 by Claude via web search; the rest were extracted from the capture bodies themselves):
  - `gelman statmodeling, mindlessness langer` → statmodeling 2024-03-06 "Mindlessness in the interpretation of a study on mindlessness"
  - `hullman blog Protzko` → statmodeling 2024-03-27 "The feel-good open science story versus the preregistration"
  - `liberman blog langer` → Language Log `?p=1396` "Generalization and truth"
  - `andre x.com, phone bans` → `x.com/andre_quentin/status/1783148596956635465`
  - `fried twitter wu` → `x.com/EikoFried/status/1773685102150644041` (matched via Zotero snapshot; note itself is an empty stub)
- **`gelman blog langer`** — empty stub with no metadata; ambiguous which Gelman–Langer post it meant (two other Gelman–Langer notes already exist). Decide: supply a URL, merge, or archive.
- **Archived permalinks** — only 2 notes carry a `permalink`; consider archiving the social-media captures (archive.today / Wayback) while they're still live.

### v2 release steps (need the authors' Figshare and GitHub accounts)

1. Review and merge this branch, then set `date-released` in `CITATION.cff` to the release date and tag the merge commit `v2.0.0`.
2. Build the zip with the command in the README's *Versions* section.
3. Publish a new version of Figshare record 33187710: replace the 179 files with the zip plus a copy of `README.md`.
4. Change the Figshare licence from CC BY 4.0 to CC0, to match `LICENSE`, and add the third-party exclusion from the README's *License* section to the description.
5. Add related materials on Figshare: the GitHub repository, the preprint (10.48550/arXiv.2604.16764), and the supplementary materials (10.6084/m9.figshare.32048553).
6. Confirm the `.v2` DOI link in the README resolves.

### Paper and supplement updates

- **Data availability statement** (paper, p. 96) still points to GitHub and says FAIR alignment is in progress. Cite the Figshare DOI in the text and reference list.
- **S6 in the supplementary materials** is still a placeholder ("expected in version 2"). Point it to `CODEBOOK.md`.
- **1,080 versus 455 codes.** Explain the difference in the paper or in `DATA-QUALITY.md` §11.
- **AI statement versus codebook.** The paper says no AI tools were used to analyze or interpret and that codes were defined with co-author JC. `CODEBOOK.md` has 269 AI-drafted definitions. Rewrite those definitions or update the statement.

### Annotation review

- Review the 269 definitions with `definition_source` = `drafted` in `codebook.csv`, starting with the 148 applied codes that have no gloss in the notes.

### Publishing

- ~~**Mint a dataset DOI** — connect the GitHub repo to Zenodo (or OSF or Figshare) and cut a release so the dataset has a persistent identifier; then add the DOI to `CITATION.cff` and `README.md`. Requires your account.~~
- ~~**arXiv ID** — the preprint wasn't findable on arXiv yet; when posted, add the arXiv ID/DOI to `CITATION.cff`'s `preferred-citation`.~~

## Completed

- ~~**`data/papers/` removal**~~ — confirmed intentional (notes duplicated `source/`); recoverable from git if ever needed.
- ~~**`paper:` → `sourceReport:` unification**~~ — all `paper:` fields converted; broken citekeys (`@protzko2024high`, `@zwebner2024can`, `@statistical`, `@gelmanhow`) fixed.

- ~~**`source/` rename**~~ — research reports are now `type: source` in `source/`; the link field `report:`/`reviewof:` was renamed to `sourceReport:` across cases/memos/reviews; 5 named-duplicate reports archived; README/SCHEMA/DATA-QUALITY updated.
- ~~**Report-location instability**~~ — resolved by adopting the auto-generated `source/` folder as the canonical home.
- ~~**Reviewer bios + URLs**~~ — real-individual posters (25 of 27 with a `url`) got a profile `url` and an orange, footnoted Claude-generated bio.
- ~~**Site URLs**~~ — 18 of 20 site notes have a `url`; 2 generic category notes need none.
- ~~**Duplicate site notes**~~ — 10 flat root-level `data/sites/` duplicates archived to `_archive/duplicate-sites/` (2026-07-05); taxonomy-subfolder copies are canonical.
- ~~**Site vs setting name clashes**~~ — resolved by archiving the 6 empty `data/settings/` stubs to `_archive/settings-superseded/` (2026-07-05); the generic site notes now double as the platform type and all `[[name]]` links resolve uniquely.
- ~~**Capture URLs**~~ — `source:` backfilled on 35 of 36 review/appraisal/commentary notes (2026-07-05); see spot-check item above.
- ~~**`CITATION.cff`**~~ — added (dataset + preprint preferred-citation, ORCIDs, CC0).
- ~~**Distinct review count**~~ — collapses to ~27 distinct review events.
- ~~**`@savin` author error**~~ — corrected to Ivan Savin & Jeroen van den Bergh.
- ~~**Named research reports**~~ — redundant named reports archived to `_archive/redundant-named-reports/`.
- ~~**Bibliographic content**~~ — all 9 live `source/` notes carry title, authors, venue, year, `publicationStatus` (retraction / Expression-of-Concern flags), and — except `@ferguson2024social` (open item) — a DOI/URL.
- ~~**Case pruning**~~ — reduced to the preprint's 10 cases (+2 extra); orphan/non-memo cases archived; 3 Bishop power-analysis cases merged (aliases retained).
- ~~**Case-memo / commentary metadata**~~ — relational properties (`sourceReport`, `reviews`, `cases`, `reviewers`, `authors`, `sites`, `source`) added.
- ~~**`#zoo/` → `#inpeer/` vocabulary**~~ — live vault uses `#inpeer/` only.
- ~~**Duplicate person notes**~~ — `data/people/` merged into `data/posters/`.
