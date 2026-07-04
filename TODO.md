# TODO — items needing the human expert

## Open

### ⚠️ `data/papers/` was deleted (confirm intent)

The 10 notes in `data/papers/` were removed from the working tree during a live sync — they duplicated the `source/` entries (same names). They **remain in git history and are recoverable** (`git checkout HEAD -- data/papers`). Confirm this consolidation is intended, or restore them.

### Sources (research reports) — residual verification

Located in `source/` (`type: source`, linked via `sourceReport:`).

- **`@dadamo2024Reversal`** — title UNVERIFIED. Confirm from DOI `10.3390/jpm14060641` (J. Personalized Medicine 14(6):641, 2024).
- **`@ferguson2024social`** — two candidate 2024 Ferguson social-media meta-analyses; confirm which, add venue + DOI.
- **`@bartik2024impact`** — confirm exact NBER working-paper number and author order (UBI/guaranteed-income study).
- **`@wang2012reducing` vs `@wang2012reducinga`** — duplicate citekeys for the same 2012 *J. Neuroscience* paper; consider merging.
- **Co-author completeness** — `@abou-Khalil` has first author only; `@protzko` links 3 key authors of a large consortium. Extend if needed.
- **Unresolved author links** — new co-authors (e.g. Moses Miller, Jacob Goldenberg, Elizabeth Rhodes) are `[[wikilinks]]` with no person note yet. Decide whether to create `person` notes for them.

### Reviewer bios — verify tentative identities

- **`Starkheiser`** — pseudonymous; no real-world bio found.
- **`Syed Omar`** — tentative match to a KU cultural-psychology PhD student; not fully verified.
- **`Kirsten T Elliot`** — moderate-confidence match (surname usually "Elliott").

### Data quality (see `DATA-QUALITY.md`)

- **Site vs setting name clashes** — 9 platform names (`blog`, `bluesky`, `pubpeer`, …) exist as both a `settings/` note and a `sites/` note, making `[[name]]` ambiguous. Consider renaming the setting notes.
- **Site URLs** — 3 generic category notes (`blog.md` ×2, `podcast.md`) still have no `url` (may not need one).
- **Legacy `paper:` field** — some reviews/posters link a source via a `paper:` field instead of `sourceReport:`; one citekey is broken (`lakens Twitter, Names Shape Faces` → `@zwebner2024can`, should be `@zwebnerCanNamesShape2024`). Unify to `sourceReport:` and fix the citekey.

## Completed

- ~~**`source/` rename**~~ — research reports are now `type: source` in `source/`; the link field `report:`/`reviewof:` was renamed to `sourceReport:` across cases/memos/reviews; 5 named-duplicate reports archived; README/SCHEMA/DATA-QUALITY updated.
- ~~**Report-location instability**~~ — resolved by adopting the auto-generated `source/` folder as the canonical home.
- ~~**Reviewer bios + URLs**~~ — 24 real-individual posters got a profile `url` and an orange, footnoted Claude-generated bio.
- ~~**Site URLs**~~ — 27 of 30 site notes have a `url`; 3 generic category notes need none.
- ~~**Distinct review count**~~ — collapses to ~27 distinct review events.
- ~~**`@savin` author error**~~ — corrected to Ivan Savin & Jeroen van den Bergh.
- ~~**Named research reports**~~ — redundant named reports archived to `_archive/redundant-named-reports/`.
- ~~**Bibliographic content**~~ — all 13 `source/` notes carry title, authors, venue, year, DOI/URL, `publicationStatus` (retraction / Expression-of-Concern flags).
- ~~**Case pruning**~~ — reduced to the preprint's 10 cases (+2 extra); orphan/non-memo cases archived; 3 Bishop power-analysis cases merged (aliases retained).
- ~~**Case-memo / commentary metadata**~~ — relational properties (`sourceReport`, `reviews`, `cases`, `reviewers`, `authors`, `sites`, `source`) added.
- ~~**`#zoo/` → `#inpeer/` vocabulary**~~ — live vault uses `#inpeer/` only.
- ~~**Duplicate person notes**~~ — `data/people/` merged into `data/posters/`.
