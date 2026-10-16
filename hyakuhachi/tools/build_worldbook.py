#!/usr/bin/env python3
"""Compile the Hyakuhachi bible into a SillyTavern World Info JSON file.

Every `## ` section of every bible/*.md file becomes one always-on (constant)
entry, verbatim, so the worldbook is a lossless copy of the bible.

Usage: python3 tools/build_worldbook.py
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BIBLE = ROOT / "bible"
OUT = ROOT / "worldbook" / "hyakuhachi.json"


def sections(md: str):
    """Yield (title, body) for each `## ` section; the `# ` file title is dropped."""
    title, lines = None, []
    for line in md.splitlines():
        if line.startswith("## "):
            if title is not None:
                yield title, "\n".join(lines).strip()
            title, lines = line[3:].strip(), []
        elif title is not None:
            lines.append(line)
    if title is not None:
        yield title, "\n".join(lines).strip()


def entry(uid: int, file_no: str, title: str, body: str) -> dict:
    return {
        "uid": uid,
        "key": [],
        "keysecondary": [],
        "comment": f"{file_no} · {title}",
        "content": f"[Hyakuhachi Lore: {title}]\n{body}",
        "constant": True,
        "vectorized": False,
        "selective": True,
        "selectiveLogic": 0,
        "addMemo": True,
        # Higher order = inserted later in the prompt; keeps bible reading order.
        "order": 100 + uid,
        "position": 0,
        "disable": False,
        "ignoreBudget": True,
        "excludeRecursion": False,
        "preventRecursion": True,
        "delayUntilRecursion": False,
        "probability": 100,
        "useProbability": True,
        "depth": 4,
        "group": "",
        "groupOverride": False,
        "groupWeight": 100,
        "scanDepth": None,
        "caseSensitive": None,
        "matchWholeWords": None,
        "useGroupScoring": None,
        "automationId": "",
        "role": None,
        "sticky": 0,
        "cooldown": 0,
        "delay": 0,
        "displayIndex": uid,
    }


def main():
    entries, words = {}, 0
    for path in sorted(BIBLE.glob("*.md")):
        file_no = re.match(r"\d+", path.name).group(0)
        for title, body in sections(path.read_text(encoding="utf-8")):
            uid = len(entries)
            entries[str(uid)] = entry(uid, file_no, title, body)
            words += len(body.split())
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps({"entries": entries}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{len(entries)} entries, ~{words} words (~{round(words * 1.4 / 1000)}k tokens) -> {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
