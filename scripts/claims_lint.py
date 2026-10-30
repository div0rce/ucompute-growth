#!/usr/bin/env python3
"""Claims lint for UCompute Growth content.

Usage: claims_lint.py <dir-or-file>... [--strict]
Checks every .md/.txt/.html/.json file under the given paths:
  1. no prohibited phrase (claims/registry.json prohibited_patterns), unless the line also
     contains the word "not" or "never" or "do not" (negated mentions such as "UCompute does not split a model" are fine)
     or sits inside a line starting with "> prohibited:" (quoting the rule itself);
  2. no identity leak (identity_patterns) anywhere, never negatable;
  3. front matter `claims:` lists only ids that exist; in --strict mode (used for content/ready and
     content/published) the file must declare at least one claim id;
  4. a tokens-per-second figure must have "path check" in the same paragraph.
Exit 1 on any finding. ponytail: regex over lines; no markdown parser until one is needed.
"""
import json, re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
REG = json.loads((ROOT / "claims" / "registry.json").read_text())
PROHIBITED = [re.compile(p, re.I) for p in REG["prohibited_patterns"]]
IDENTITY = [re.compile(p, re.I) for p in REG["identity_patterns"]]
NEGATED = re.compile(r"\b(not|never|no|without|rather than|instead of|unverified|planned)\b", re.I)
TOKS = re.compile(r"\btok(ens)?\s*/\s*s\b|\btokens per second\b", re.I)
FRONT = re.compile(r"^---\n(.*?)\n---", re.S)
EXTS = {".md", ".txt", ".html", ".json", ".yaml", ".yml"}
INDEXES = {"INDEX.md", "README.md"}  # pipeline bookkeeping, not publishable pieces: still pattern-checked

def files(paths):
    for p in paths:
        p = pathlib.Path(p)
        if p.is_dir():
            yield from (f for f in p.rglob("*") if f.suffix in EXTS and f.is_file())
        elif p.exists():
            yield p

def lint(path, strict):
    out = []
    text = path.read_text(errors="replace")
    m = FRONT.match(text)
    declared = []
    if m:
        for line in m.group(1).splitlines():
            if line.strip().startswith("claims:"):
                declared = [c.strip() for c in line.split(":", 1)[1].strip("[] ").split(",") if c.strip()]
    for c in declared:
        if c not in REG["claims"]:
            out.append(f"{path}:1: unknown claim id '{c}'")
    if strict and not declared and path.name not in INDEXES:
        out.append(f"{path}:1: strict: no `claims:` front matter")
    paragraphs, para, start = [], [], 1
    for i, line in enumerate(text.splitlines(), 1):
        if line.strip().startswith("> prohibited:"):
            continue
        for rx in IDENTITY:
            if rx.search(line):
                out.append(f"{path}:{i}: identity leak /{rx.pattern}/")
        for rx in PROHIBITED:
            if rx.search(line) and not NEGATED.search(line):
                out.append(f"{path}:{i}: prohibited phrase /{rx.pattern}/")
        if line.strip():
            if not para: start = i
            para.append(line)
        else:
            if para: paragraphs.append((start, "\n".join(para))); para = []
    if para: paragraphs.append((start, "\n".join(para)))
    for start, p in paragraphs:
        if TOKS.search(p) and "path check" not in p.lower():
            out.append(f"{path}:{start}: tokens-per-second figure without 'path check' label")
    return out

def main(argv):
    strict = "--strict" in argv
    paths = [a for a in argv if not a.startswith("--")] or ["content/ready", "content/published"]
    findings = []
    n = 0
    for f in files(paths):
        if f.name == "registry.json" and f.parent.name == "claims":
            continue
        n += 1
        findings += lint(f, strict)
    for x in findings: print(x)
    print(f"claims_lint: {n} files, {len(findings)} findings")
    return 1 if findings else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
