#!/usr/bin/env python3
"""Build the coding audit trail from the vault's Markdown notes.

Reads every note in data/, analysis/ and source/, plus the tables in CODEBOOK.md.
Writes two CSV files to the vault root and prints a coverage summary:
  code-applications.csv  one row per #inpeer code applied: where it is, and its gloss if any
  codebook.csv           one row per CODEBOOK.md entry, with where its definition came from

Run from anywhere with Python 3.8+; it needs no packages and changes no notes:
  python3 scripts/code_audit.py
"""
import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# Other tag trees are working notes and are ignored, but a gloss never runs past one.
TAG = re.compile(r"(?<![\w/#])#(inpeer|misc|dg|cscw)((?:/[A-Za-z0-9_-]+)*)")
# Glosses are written as "This means that...", or as "#code means..." or "#code if...".
GLOSS = re.compile(r"(?:[Tt]his means|\bmeans that).*")
DIRECT_GLOSS = re.compile(r"^[\s:,-]*((?:means|if)\b.*)")
GLOSS_WINDOW = 3


def find_gloss(lines, index, tag_end):
    """Return the gloss after a code, on its line or the next two, stopping at the next code."""
    rest = lines[index][tag_end:]
    next_tag = TAG.search(rest)
    direct = DIRECT_GLOSS.match(rest[: next_tag.start()] if next_tag else rest)
    if direct:
        return direct.group(1).strip()
    window = [rest[: next_tag.start()] if next_tag else rest]
    # With several codes on one line, a gloss after them belongs to the last.
    if next_tag:
        return next((m.group(0).strip() for m in map(GLOSS.search, window) if m), "")
    for line in lines[index + 1 : index + GLOSS_WINDOW]:
        if TAG.search(line):
            break
        window.append(line)
    return next((m.group(0).strip() for m in map(GLOSS.search, window) if m), "")


def read_applications():
    rows = []
    for folder in ("data", "analysis", "source"):
        for path in sorted((ROOT / folder).rglob("*.md")):
            text = path.read_text(encoding="utf8")
            kind = re.search(r"^type: *(\S+)", text, re.M)
            lines = text.split("\n")
            for number, line in enumerate(lines, 1):
                for tag in TAG.finditer(line):
                    if tag.group(1) != "inpeer":
                        continue
                    rows.append({
                        "code": tag.group(0),
                        "note": path.relative_to(ROOT).as_posix(),
                        "line": number,
                        "note_type": kind.group(1) if kind else "",
                        "gloss": find_gloss(lines, number - 1, tag.end()),
                    })
    return rows


def read_codebook():
    rows = []
    level = 0
    for line in (ROOT / "CODEBOOK.md").read_text(encoding="utf8").split("\n"):
        heading = re.match(r"## Table \d+\. Level (\d+)", line)
        if heading:
            level = int(heading.group(1))
        if not re.match(r"\| \d+ \| `#inpeer", line):
            continue
        _, code, definition, rq, instances, example = line.strip(" |").split(" | ")
        source = "researcher_gloss" if definition.startswith("Researcher's gloss") else "drafted"
        rows.append({
            "code": code.strip("`"),
            "level": level,
            "definition_source": source,
            "definition": definition,
            "rq": rq,
            "instances": instances,
            "example": example,
        })
    return rows


def write_csv(name, rows):
    with open(ROOT / name, "w", newline="", encoding="utf8") as out:
        writer = csv.DictWriter(out, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


applications = read_applications()
codebook = read_codebook()
write_csv("code-applications.csv", applications)
write_csv("codebook.csv", codebook)

applied = {row["code"] for row in applications}
glossed = {row["code"] for row in applications if row["gloss"]}
print(f"#inpeer applications: {len(applications)}; with a gloss beside them: {sum(bool(r['gloss']) for r in applications)}")
print(f"#inpeer codes applied: {len(applied)}; glossed at least once: {len(glossed)}")
print(f"notes with #inpeer codes: {len({r['note'] for r in applications})}")
print(f"codebook entries: {len(codebook)}; researcher gloss: {sum(r['definition_source'] == 'researcher_gloss' for r in codebook)}")
