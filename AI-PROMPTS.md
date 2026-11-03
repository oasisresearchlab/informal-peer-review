# AI prompts for the v2 release

This file records the prompts behind the 2026-11-02 changes to this dataset, as part of the AI-use disclosure in [README.md](README.md).

| | |
| --- | --- |
| **Model** | Claude Opus 5.5 (Anthropic) |
| **Model ID** | `claude-opus-5-5` |
| **Interface** | Claude Code 2.1.316, command-line tool on macOS, with subagents and web search and fetch tools in the same session |
| **Date of access** | 2026-11-02 |
| **Prompt author** | Jay Patel |

The prompts are verbatim, including typos, except that local file paths are replaced with `[local path: …]`. Each prompt was one step in a single session, and the model also read the files and pages named in them. Prompts from the earlier sessions (Claude Opus 4.8 on 2026-07-03 and Claude Fable 5 on 2026-07-05) are not recorded here.

## Prompts

1. > read https://eivimeycook.github.io/TADA-Wiki/index.html

2. > evaluate this repo keeping in mind there is a DOI of teh data and codebook on figshare: https://github.com/oasisresearchlab/informal-peer-review

3. > Fit the Transferable, Available, and Documented bits. The annotated bit is applicable. The codebook (this is a qualitative project) so translated the construct to fit with our ethnography. I have give you GH access to the repo, but create a branch for v2 for me to inspect before merging. I can manually check the five AI-recovered URLs. The ethics review bit can be found in the patel and chen paper and supplementary materials: [local path: patel-chan-2026.pdf]

4. > write that AI was used to transform human-written notes and codes into a codebook (cleaning and organization with human verification). The 1,080 codes were in the Obsidian repo for the project inpeer, but not every code from the coding tree (hierarchical) was actually needed in the study. Count codes again and if needed, we should update the codebook such that codes with human-annotated text appears in the code book. Forget identify notes. Lists here with misattributed definitions and URLs I need to check. And give me details on the 17 screenshots. Are those supposed to be the figures from the pdf patel and chan 2026? [local path: int-paper-jp-2026-08-07-v2.pdf] should have the AI disclosure updatred?

5. > It's ok to share the PubPeer image with my pseudonym. It make be that codes are not unique, appearing multiple times (hence 1080 total codes. Actually, in the local vault, iI now see 1136 codes total in inpeer/... [Image #1]. Include the latest prompts in the AI disclosure with model name, version, date-of-access, etc. misc/... and dg/... codes are irrelevant for our analyses and should be ignored. Restore the three safe screenshots. Find the jussim Substack posts on the biased poster and the original gelman post on Langer from his blog. I'll check the URLs myself while you do this for accuracy.

   Image #1 was a screenshot of the Obsidian tag pane showing `inpeer` 1136, `misc` 194, and `dg` 13.

6. > I checked the urls and they passed. I verified your output so that's completed for the todo.  Keep the vacuousStudy code. The orca-cases local vault may have the 326 missing images.
