"""Digests of closed GitHub issues -> troubleshooting units (mode S: own words, link to the issue).

Usage: python issues2ku.py <stage2/issues-out> <units/issues>

Open issues and pyOCD's discussions go the same way: an entry with "open": true says so in its unit.

Every file in <stage2/issues-out> is a JSON list written after stage2/issues_prompt.md:
  {issue, tool, title, symptoms[], cause, fix, applies_to{}, versions, resolution, confidence}
Each entry becomes units/issues/<repo>/iss-<repo>-<number>.md with status draft. The body is the
digest's own text; the only verbatim text is tool output (symptoms). A symptom becomes a pattern
for exact matching when enough of it is fixed text: quoted names, numbers, addresses and paths
are wildcards, a log prefix such as "0001234 C " is dropped.
"""
import json
import re
import sys
from pathlib import Path

DOMAIN = {"pyocd": "debug", "gdb": "debug", "cmsis-debugger": "debug", "csolution": "project", "cbuild": "project",
          "cmsis-solution": "project", "cpackget": "pack", "packchk": "pack", "svdconv": "pack",
          "cmsis-core": "core", "cmsis-rtx": "rtos", "cmsis-view": "trace"}
TOOL_NAME = {"pyocd": "pyOCD", "gdb": "GDB", "cmsis-debugger": "CMSIS Debugger", "csolution": "csolution", "cbuild": "cbuild",
             "cmsis-solution": "CMSIS Solution", "cpackget": "cpackget", "packchk": "packchk", "svdconv": "svdconv",
             "cmsis-core": "CMSIS-Core", "cmsis-rtx": "RTX", "cmsis-view": "CMSIS-View"}
REPO_SHORT = {"pyOCD": "pyocd", "devtools": "devtools", "cmsis-toolbox": "toolbox", "cpackget": "cpackget",
              "vscode-cmsis-debugger": "dbg", "vscode-cmsis-solution": "sol", "CMSIS_6": "cmsis6", "CMSIS-RTX": "rtx",
              "CMSIS-View": "view"}
APPLIES_KEYS = {"device", "family", "board", "core", "component", "api", "pack", "toolchain", "compiler", "tool"}
VARIABLE = re.compile(r"'[^'\n]*'|\"[^\"\n]*\"|`[^`\n]*`|0x[0-9a-fA-F]+|(?:[A-Za-z]:)?(?:[\\/][\w.@+-]+){2,}[\\/]?|\b\d+(?:\.\d+)*\b")
# Log prefixes: pyOCD's "0001234 C " or "0001234:", Python logging's "WARNING:__main__:", cpackget's "ERRO ",
# a time stamp, or a bare "Error:".
LOG_PREFIX = re.compile(r"^\s*(?:\d{3,}:?\s+(?:[A-Z]\s+)?|(?:CRITICAL|ERROR|WARNING|INFO|DEBUG):[\w.]+:|(?:ERRO|WARN|INFO|DEBU)\s+|"
                        r"\[?\d{2}:\d{2}:\d{2}(?:\.\d+)?\]?\s+|(?:error|warning|info|debug)\s*[:|]\s*(?=\S))", re.I)
MIN_LITERAL = 20


def symptom_regex(symptom):
    """A pattern for the symptom line, or '' when too little of it is fixed text."""
    # The search strips "error csolution: " from a query line (messageLines), so the pattern must not need it.
    s = re.sub(r"^.*?\b(?:error|warning|info)\s+[\w.-]+:\s*", "", symptom.strip(), flags=re.I)
    s = LOG_PREFIX.sub("", s)
    s = re.sub(r"\s*\[[\w.]+\]\s*$", "", s)          # a trailing logger name such as [pyocd.__main__]
    parts, literal, pos = [], 0, 0
    for m in VARIABLE.finditer(s):
        lit = s[pos:m.start()]
        parts.append(re.escape(lit))
        literal += len(lit.strip())
        q = m.group(0)[0]
        parts.append(f"{q}.*?{q}" if q in "'\"`" else r"\S+")
        pos = m.end()
    lit = s[pos:]
    parts.append(re.escape(lit))
    literal += len(lit.strip())
    if literal < MIN_LITERAL:
        return ""
    rx = "".join(parts).strip()
    return re.sub(r"(\\ |\s)+", r"\\s+", rx)


def summary_of(text, words=40):
    first = re.split(r"(?<=[.!?])\s+(?=[A-Z<`'\"(])", " ".join(text.split()), maxsplit=1)[0]
    w = first.split()
    return first if len(w) <= words else " ".join(w[:words - 1]) + " …"


def unit(entry):
    m = re.match(r"https://github\.com/([^/]+)/([^/]+)/(issues|discussions)/(\d+)", entry["issue"])
    if not m:
        raise ValueError(f"not an issue URL: {entry['issue']}")
    owner, repo, kind, number = m.groups()
    number = number if kind == "issues" else f"d{number}"
    short = REPO_SHORT.get(repo, re.sub(r"[^a-z0-9]+", "-", repo.lower()))
    tool = entry.get("tool") or "other"
    symptoms = [s.strip() for s in entry.get("symptoms") or [] if isinstance(s, str) and s.strip()][:3]
    patterns = [p for p in (symptom_regex(s) for s in symptoms) if p]
    applies = {}
    for k, v in (entry.get("applies_to") or {}).items():
        vals = [str(x) for x in (v if isinstance(v, list) else [v]) if str(x).strip()]
        if k in APPLIES_KEYS and vals:
            applies[k] = vals
    if tool in DOMAIN:
        applies.setdefault("tool", [tool])
    body = []
    if symptoms:
        body.append("## Symptom\n\n" + "\n".join(f"`{s}`" for s in symptoms))
    body.append("## Cause\n\n" + entry["cause"].strip())
    body.append("## Fix\n\n" + entry["fix"].strip())
    facts = [f"Resolution: {entry.get('resolution', '')}"] if entry.get("resolution") else []
    if entry.get("versions"):
        facts.append(f"Versions: {entry['versions']}")
    if entry.get("open"):
        facts.append("The issue is still open: the fix is a workaround, a later release may change it.")
    facts.append(f"From [{owner}/{repo} {'discussion ' if kind == 'discussions' else '#'}{number.lstrip('d')}]({entry['issue']}), "
                 f"summarized in own words; confidence {entry.get('confidence', 'medium')}, not reviewed yet.")
    body.append("## Source\n\n" + "\n\n".join(facts))
    meta = dict(id=f"iss-{short}-{number}", type="troubleshooting", domain=DOMAIN.get(tool, "general"),
                title=f"{TOOL_NAME.get(tool, tool)}: {entry['title'].strip()}"[:160], summary=summary_of(entry["cause"]),
                status="draft", tool=tool, symptoms=symptoms, symptom_regex=patterns[0] if patterns else "",
                collection=f"issues-{short}", source=entry["issue"], doc_source=entry["issue"],
                resolution=entry.get("resolution", ""), versions=entry.get("versions", ""),
                issue_state="open" if entry.get("open") else "",
                confidence=entry.get("confidence", "medium"), cause_origin="issue-digest",
                applies_to=applies, license="own summary of a GitHub issue", mode="S")
    meta = {k: v for k, v in meta.items() if v not in ("", [], None, {})}
    return short, meta, "\n\n".join(body)


def main(src, out):
    src, out = Path(src), Path(out)
    for old in out.glob("*/*.md"):
        old.unlink()
    counts, seen = {}, set()
    for f in sorted(src.glob("*.json")):
        for entry in json.loads(f.read_text(encoding="utf-8")):
            if not (entry.get("cause") and entry.get("fix") and entry.get("title")):
                print(f"  {entry.get('issue')}: no cause, fix or title, skipped")
                continue
            short, meta, body = unit(entry)
            if meta["id"] in seen:
                continue
            seen.add(meta["id"])
            target = out / short / f"{meta['id']}.md"
            counts.setdefault(short, 0)
            target.parent.mkdir(parents=True, exist_ok=True)
            fm = "\n".join(f"{k}: {json.dumps(v, ensure_ascii=False)}" for k, v in meta.items())
            target.write_text(f"---\n{fm}\n---\n\n{body}\n", encoding="utf-8")
            counts[short] += 1
    for k, v in sorted(counts.items()):
        print(f"{k:12s} {v:4d} units")
    print(f"total        {sum(counts.values()):4d}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(*sys.argv[1:])
