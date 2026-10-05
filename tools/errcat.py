#!/usr/bin/env python3
"""errcat: extrahiert Meldungstexte aus Open-CMSIS-Pack/devtools als Troubleshooting-Drafts.

Quellen (alle Apache-2.0, Modus V):
  packchk  tools/packchk/src/PackChk_Msgs.cpp   + Tabelle in tools/packchk/README.md
  svdconv  tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp + Tabelle in SVDConv/README.md
  csolution tools/projmgr/src/*.cpp (ProjMgrLogger::Get().Error/Warn)

cause/fix werden nur aus den README-Tabellen uebernommen. Fuer csolution gibt es keine
Doku-Tabelle: dort steht nur die ausloesende Bedingung aus dem Quelltext (trigger_code),
cause und fix bleiben leer und sind Aufgabe des Reviews.

Aufruf: python errcat.py <devtools> <out-dir>
"""
import json, re, subprocess, sys
from pathlib import Path

REPO = "Open-CMSIS-Pack/devtools"
LEVELS = {"ERROR": "error", "WARNING": "warning"}


def to_regex(template, var=r"%[A-Z0-9_]+%"):
    parts = re.split(f"({var})", template)
    rx = "".join(".+?" if re.fullmatch(var, p) else re.escape(p).replace("\\ ", " ") for p in parts)
    return "^" + rx.strip() + "$" if rx.strip() else ""


def literal_core(template, var=r"%[A-Z0-9_]+%"):
    """Laengstes festes Textstueck, geht als exakter String in BM25."""
    parts = [p.strip(" :'\"") for p in re.split(var, template)]
    return max(parts, key=len) if parts else ""


def title_text(template, var=r"%[A-Z0-9_]+%", limit=100):
    """The message as a title: variables as '…', cut at a word after `limit` characters."""
    t = re.sub(r"\s+", " ", re.sub(var, "…", template)).strip()
    if len(t) > limit:
        t = t[:limit].rsplit(" ", 1)[0] + " …"
    return t


def msg_table(path):
    rx = re.compile(r'\{\s*"(M\d+)",\s*\{\s*MsgLevel::LEVEL_(\w+)\s*,\s*\w+\s*,\s*((?:"(?:[^"\\]|\\.)*"\s*\\?\s*)+)\}')
    out = {}
    for m in rx.finditer(Path(path).read_text(encoding="utf-8", errors="replace")):
        text = "".join(re.findall(r'"((?:[^"\\]|\\.)*)"', m.group(3)))
        text = text.encode().decode("unicode_escape").replace("\n", " ").strip()
        out[m.group(1)] = (m.group(2), text)
    return out


def readme_table(path):
    out = {}
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        m = re.match(r"\|\s*(M\d+)\s*\|\s*(\w+)\s*\|(.*?)\|(.*?)\|?\s*$", line)
        if m:
            out[m.group(1)] = dict(type=m.group(2), text=m.group(3).strip(), details=m.group(4).strip())
    return out


def coded(tool, src, readme, repo, commit):
    tab, doc = msg_table(src), readme_table(readme)
    units = []
    for code, (lvl, text) in tab.items():
        if lvl not in LEVELS or not text:
            continue
        d = doc.get(code, {})
        units.append(dict(
            id=f"ts-{tool}-{code.lower()}", tool=tool, code=code, severity=LEVELS[lvl],
            title=f"{tool} {code}: {title_text(text)}",
            symptoms=[code, text], symptom_regex=to_regex(text),
            cause=d.get("details", ""), fix="",
            documented=bool(d), source=f"{REPO}@{commit}:{Path(src).relative_to(repo)}",
            doc_source=f"{REPO}@{commit}:{Path(readme).relative_to(repo)}" if d else ""))
    return units


def call_args(text, start):
    """Argumentliste ab der oeffnenden Klammer bis zur passenden schliessenden."""
    depth, i, instr = 0, start, False
    while i < len(text):
        c = text[i]
        if instr:
            if c == "\\":
                i += 1
            elif c == '"':
                instr = False
        elif c == '"':
            instr = True
        elif c == "(":
            depth += 1
        elif c == ")":
            depth -= 1
            if depth == 0:
                return text[start + 1:i]
        i += 1
    return ""


def first_arg(args):
    depth, instr, i = 0, False, 0
    while i < len(args):
        c = args[i]
        if instr:
            if c == "\\":
                i += 1
            elif c == '"':
                instr = False
        elif c == '"':
            instr = True
        elif c in "([{":
            depth += 1
        elif c in ")]}":
            depth -= 1
        elif c == "," and depth == 0:
            return args[:i]
        i += 1
    return args


def template_of(expr):
    """'"foo '" + x + "' bar"' -> "foo '<x>' bar". Reine Variablen -> None."""
    pieces = re.split(r'("(?:[^"\\]|\\.)*")', expr)
    out, has_lit = [], False
    for p in pieces:
        if p.startswith('"'):
            out.append(p[1:-1].encode().decode("unicode_escape"))
            has_lit = True
        elif p.strip(" +\n\t"):
            out.append("%VAR%")
    t = re.sub(r"(%VAR%)+", "%VAR%", "".join(out)).strip()
    return t if has_lit and re.sub(r"%VAR%|\W", "", t) else None


def projmgr(repo, commit):
    seen, units = {}, []
    for f in sorted((repo / "tools/projmgr/src").glob("*.cpp")):
        text = f.read_text(encoding="utf-8", errors="replace")
        for m in re.finditer(r"ProjMgrLogger::Get\(\)\.(Error|Warn)\s*\(", text):
            expr = first_arg(call_args(text, m.end() - 1))
            t = template_of(expr)
            if not t:
                continue
            line = text.count("\n", 0, m.start()) + 1
            # ausloesende Bedingung: letzte if-Zeile in den 6 Zeilen davor
            ctx = text[:m.start()].splitlines()[-6:]
            cond = next((c.strip() for c in reversed(ctx) if re.match(r"\s*(\}\s*else\s*)?if\s*\(", c)), "")
            key = (m.group(1), t)
            if key in seen:
                seen[key]["locations"].append(f"{f.name}:{line}")
                continue
            u = dict(
                id="", tool="csolution", code="", severity="error" if m.group(1) == "Error" else "warning",
                title=f"csolution: {title_text(t, r'%VAR%')}",
                symptoms=[t.replace("%VAR%", "<…>")], symptom_regex=to_regex(t, r"%VAR%"),
                cause="", fix="", trigger_code=cond, documented=False,
                source=f"{REPO}@{commit}:tools/projmgr/src/{f.name}:{line}", locations=[f"{f.name}:{line}"])
            seen[key] = u
            units.append(u)
    used = {}
    for u in units:
        base = "ts-csolution-" + (re.sub(r"[^a-z0-9]+", "-", literal_core(u["symptoms"][0].replace("<…>", "%VAR%"), r"%VAR%").lower()).strip("-")[:48] or "msg")
        used[base] = used.get(base, 0) + 1
        u["id"] = base if used[base] == 1 else f"{base}-{used[base]}"
    return units


def write(units, out):
    out.mkdir(parents=True, exist_ok=True)
    for u in units:
        body = []
        body.append("## Symptom\n\n" + "\n".join(f"`{s}`" for s in u["symptoms"]))
        body.append("## Cause\n\n" + (u["cause"] or "_open: to be written in the review_"))
        body.append("## Fix\n\n" + (u["fix"] or ("_see Cause_" if u["cause"] else "_open: to be written in the review_")))
        if u.get("trigger_code"):
            body.append("## Trigger in the source\n\n```cpp\n" + u["trigger_code"] + "\n```")
        meta = dict(id=u["id"], type="troubleshooting", domain="error-catalog", title=u["title"],
                    summary="", status="draft", tool=u["tool"], severity=u["severity"],
                    code=u["code"], symptoms=u["symptoms"], symptom_regex=u["symptom_regex"],
                    documented=u["documented"], source=u["source"], doc_source=u.get("doc_source", ""),
                    applies_to={"tool": [u["tool"]]}, license="Apache-2.0", mode="V")
        meta = {k: v for k, v in meta.items() if v not in ("", [], None)}
        fm = "\n".join(f"{k}: {json.dumps(v, ensure_ascii=False)}" for k, v in meta.items())
        (out / f"{u['id']}.md").write_text(f"---\n{fm}\n---\n\n" + "\n\n".join(body) + "\n", encoding="utf-8")


def main(repo, out):
    repo, out = Path(repo), Path(out)
    commit = subprocess.run(["git", "-C", str(repo), "rev-parse", "--short", "HEAD"],
                            capture_output=True, text=True).stdout.strip() or "unknown"
    pk = coded("packchk", repo / "tools/packchk/src/PackChk_Msgs.cpp", repo / "tools/packchk/README.md", repo, commit)
    sv = coded("svdconv", repo / "tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp", repo / "tools/svdconv/SVDConv/README.md", repo, commit)
    pm = projmgr(repo, commit)
    write(pk + sv + pm, out)
    for name, us in (("packchk", pk), ("svdconv", sv), ("csolution", pm)):
        e = sum(u["severity"] == "error" for u in us)
        d = sum(u["documented"] for u in us)
        print(f"{name:10s} {len(us):4d} Einheiten ({e} error, {len(us)-e} warning), mit Doku-Text: {d}")
    print(f"gesamt     {len(pk)+len(sv)+len(pm):4d}  devtools@{commit}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(*sys.argv[1:])
