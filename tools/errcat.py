#!/usr/bin/env python3
"""errcat: extrahiert Meldungstexte aus Open-CMSIS-Pack/devtools als Troubleshooting-Drafts.

Quellen (alle Apache-2.0, Modus V):
  packchk  tools/packchk/src/PackChk_Msgs.cpp   + Tabelle in tools/packchk/README.md
  svdconv  tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp + Tabelle in SVDConv/README.md
  csolution tools/projmgr/src/*.cpp (ProjMgrLogger::Get().Error/Warn, m_toolchainErrors[...].insert)
            and the schema checker's message (SCHEMA_MESSAGES), which csolution logs through a variable

cause/fix werden nur aus den README-Tabellen uebernommen. Fuer csolution gibt es keine
Doku-Tabelle: dort steht nur die ausloesende Bedingung aus dem Quelltext (trigger_code),
cause und fix bleiben leer und sind Aufgabe des Reviews.

A symptom pattern matches one line of tool output, as the search tests it: a message is cut at its
first newline (the rest is printed on the next lines), a variable at the end of the line may be
empty, and a part printed only on a condition (`cond ? "text" : ""`) is optional. Messages that only
sum up the errors printed before them get `role: summary` (SUMMARY).

Aufruf: python errcat.py <devtools> <out-dir>
"""
import json, re, subprocess, sys
from pathlib import Path

REPO = "Open-CMSIS-Pack/devtools"
LEVELS = {"ERROR": "error", "WARNING": "warning"}
OPT = "%VAR?%"          # a part of a csolution message printed only on a condition: may be empty

# Messages csolution prints that the scan of tools/projmgr/src cannot see, because ProjMgrYamlSchemaChecker
# logs each schema error through a variable (err.m_msg): the text, and the files of devtools that hold it.
# The schema checker library throws it for a YAML file that does not parse, and devtools' patch of
# json-schema-validator puts it in place of the validator's own messages for a value the schema rejects.
SCHEMA_MESSAGES = {
    "schema check failed, verify syntax": ["libs/ymlschemachecker/src/YmlSchemaValidator.cpp",
                                           "external/json-schema-validator.patch"],
}

# Messages that only sum up the errors printed before them: the unit gets `role: summary`, and a search
# that finds a unit for an earlier line names that one. Each was read in the source (devtools@6cb5a3c):
SUMMARY = {
    # ProjMgr.cpp ProcessContexts: printed when ProjMgrWorker::ProcessContext returns false; its steps
    # (packs, device and board, linker, components, files, debuggers, images) log their own errors first,
    # only the toolchain errors (m_toolchainErrors) are printed after all contexts.
    "ts-csolution-processing-context",
    # ProjMgr.cpp RunListTargetSets: ListTargetSets returns false only after it logged
    # "no target-set was found with filter '…'".
    "ts-csolution-processing-target-sets-list-failed",
    # ProjMgrWorker.cpp AddContexts: a project is missing from the parsed cprojects only when PopulateContexts
    # logged "cproject file was not found" for it or ParseCproject failed with its schema or YAML errors.
    "ts-csolution-cproject-not-parsed-adding-context-failed",
}


def one_line(template):
    """The first line of a message: up to its first newline, a real one or an escaped `\\n` of the C++ literal."""
    return re.split(r"\n|\\n", template.lstrip(), maxsplit=1)[0].rstrip()


def to_regex(template, var=r"%[A-Z0-9_]+%"):
    """The pattern of the message's first line. A variable at its end may be empty (`.*`): a message can end
    where the variable would start."""
    parts = [p for p in re.split(f"({var}|{re.escape(OPT)})", one_line(template)) if p]

    def piece(i, p):
        if p != OPT and not re.fullmatch(var, p):
            return re.escape(p).replace("\\ ", " ")
        return ".*" if i == len(parts) - 1 else ".*?" if p == OPT else ".+?"
    rx = "".join(piece(i, p) for i, p in enumerate(parts))
    return "^" + rx + "$" if rx else ""


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
        out[m.group(1)] = (m.group(2), text.encode().decode("unicode_escape"))   # newlines kept for to_regex
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
    for code, (lvl, raw) in tab.items():
        text = raw.replace("\n", " ").strip()      # the whole message as one text; the pattern takes its first line
        if lvl not in LEVELS or not text:
            continue
        d = doc.get(code, {})
        units.append(dict(
            id=f"ts-{tool}-{code.lower()}", tool=tool, code=code, severity=LEVELS[lvl],
            title=f"{tool} {code}: {title_text(text)}",
            symptoms=[code, text], symptom_regex=to_regex(raw),
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
    """'"foo '" + x + "' bar"' -> "foo '<x>' bar". Reine Variablen -> None.
    A piece that is nothing but a conditional part marked by optional_parts() becomes OPT."""
    pieces = re.split(r'("(?:[^"\\]|\\.)*")', expr)
    out, has_lit = [], False
    for p in pieces:
        if p.startswith('"'):
            out.append(p[1:-1].encode().decode("unicode_escape"))
            has_lit = True
        elif p.strip(" +\n\t"):
            out.append(OPT if not re.sub(r"\w*\(__OPT__\)", "", p).strip(" +\n\t") else "%VAR%")
    t = "".join(out)
    # a run of variables is one variable; it may be empty only when every one of them may be
    t = re.sub(r"(?:%VAR%|%VAR\?%)*%VAR%(?:%VAR%|%VAR\?%)*", "%VAR%", t)
    t = re.sub(r"(?:%VAR\?%)+", OPT, t).strip()
    return t if has_lit and re.sub(r"%VAR\??%|\W", "", t) else None


def optional_parts(expr):
    """The expression with each parenthesised condition that prints a text or nothing,
    `(cond ? "text" + x : "")`, replaced by `(__OPT__)`: that part of the message may be missing.
    A condition between two texts stays as it is."""
    out, stack, i, instr = list(expr), [], 0, False
    spans = []
    while i < len(expr):
        c = expr[i]
        if instr:
            if c == "\\":
                i += 1
            elif c == '"':
                instr = False
        elif c == '"':
            instr = True
        elif c == "'":
            i += 4 if expr[i + 1:i + 2] == "\\" else 3       # a char literal such as '@' or '\n'
            continue
        elif c == "(":
            stack.append(i)
        elif c == ")" and stack:
            start = stack.pop()
            if not any(a <= start and i <= b for a, b in spans) and conditional_with_empty_branch(expr[start + 1:i]):
                spans = [(a, b) for a, b in spans if not (start <= a and b <= i)] + [(start, i)]
        i += 1
    for a, b in sorted(spans, reverse=True):
        out[a:b + 1] = "(__OPT__)"
    return "".join(out)


def conditional_with_empty_branch(inner):
    """`cond ? a : b` at the top level of `inner`, one of a and b the empty string literal."""
    depth, instr, q, i = 0, False, -1, 0
    while i < len(inner):
        c = inner[i]
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
        elif depth == 0 and c == "?" and q < 0:
            q = i
        elif depth == 0 and c == ":" and q >= 0 and inner[i + 1:i + 2] != ":" and inner[i - 1:i] != ":":
            a, b = inner[q + 1:i].strip(), inner[i + 1:].strip()
            return '""' in (a, b)
        i += 1
    return False


def projmgr(repo, commit):
    seen, units = {}, []
    for f in sorted((repo / "tools/projmgr/src").glob("*.cpp")):
        text = f.read_text(encoding="utf-8", errors="replace")
        # the logger's calls, and the toolchain messages it prints later (ProjMgrWorker::HasToolchainErrors)
        for m in re.finditer(r"ProjMgrLogger::Get\(\)\.(Error|Warn)\s*\(|"
                             r"m_toolchainErrors\[MessageType::(Error|Warning)\]\.insert\s*\(", text):
            level = m.group(1) or ("Warn" if m.group(2) == "Warning" else "Error")
            expr = first_arg(call_args(text, m.end() - 1))
            t = template_of(expr)
            if not t:
                continue
            line = text.count("\n", 0, m.start()) + 1
            # ausloesende Bedingung: letzte if-Zeile in den 6 Zeilen davor
            ctx = text[:m.start()].splitlines()[-6:]
            cond = next((c.strip() for c in reversed(ctx) if re.match(r"\s*(\}\s*else\s*)?if\s*\(", c)), "")
            key = (level, t)
            if key in seen:
                seen[key]["locations"].append(f"{f.name}:{line}")
                continue
            u = dict(
                id="", tool="csolution", code="", severity="error" if level == "Error" else "warning",
                title=f"csolution: {title_text(t, r'%VAR%')}", template=t,
                symptoms=[one_line(t).replace("%VAR%", "<…>")],
                symptom_regex=to_regex(template_of(optional_parts(expr)), r"%VAR%"),
                cause="", fix="", trigger_code=cond, documented=False,
                source=f"{REPO}@{commit}:tools/projmgr/src/{f.name}:{line}", locations=[f"{f.name}:{line}"])
            seen[key] = u
            units.append(u)
    units += schema_checker(repo, commit)
    used = {}
    for u in units:
        # the id from the whole message, as before the cut at the first newline: the analyses are keyed by it
        base = "ts-csolution-" + (re.sub(r"[^a-z0-9]+", "-", literal_core(u["template"], r"%VAR%").lower()).strip("-")[:48] or "msg")
        used[base] = used.get(base, 0) + 1
        u["id"] = base if used[base] == 1 else f"{base}-{used[base]}"
    return units


def schema_checker(repo, commit):
    """The SCHEMA_MESSAGES as csolution units, from the first place that holds each (a patch: its added lines)."""
    units = []
    for text, files in SCHEMA_MESSAGES.items():
        locations, cond = [], ""
        for rel in files:
            lines = (repo / rel).read_text(encoding="utf-8", errors="replace").splitlines()
            for n, l in enumerate(lines, 1):
                if f'"{text}"' in l and (l.startswith("+") or not rel.endswith(".patch")):
                    locations.append(f"{rel}:{n}")
                    cond = cond or next((c.strip() for c in reversed(lines[max(0, n - 7):n - 1])
                                         if re.match(r"\s*(\}\s*)?(else\s*)?(if|catch)\s*\(", c)), "")
        if not locations:
            print(f"  not in devtools any more: {text}")
            continue
        units.append(dict(
            id="", tool="csolution", code="", severity="error", title=f"csolution: {title_text(text)}",
            template=text, symptoms=[text], symptom_regex=to_regex(text), cause="", fix="", trigger_code=cond,
            documented=False, source=f"{REPO}@{commit}:{locations[0]}", locations=locations))
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
                    role="summary" if u["id"] in SUMMARY else "",
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
    for missing in sorted(SUMMARY - {u["id"] for u in pm}):
        print(f"  SUMMARY names {missing}, which is no unit any more")
    for name, us in (("packchk", pk), ("svdconv", sv), ("csolution", pm)):
        e = sum(u["severity"] == "error" for u in us)
        d = sum(u["documented"] for u in us)
        print(f"{name:10s} {len(us):4d} Einheiten ({e} error, {len(us)-e} warning), mit Doku-Text: {d}")
    print(f"gesamt     {len(pk)+len(sv)+len(pm):4d}  devtools@{commit}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(*sys.argv[1:])
