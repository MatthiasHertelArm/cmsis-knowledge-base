#!/usr/bin/env python3
"""skill2ku: zerlegt cmsis-skills (SKILL.md nach SKILL_TEMPLATE) in Wissenseinheiten.

Stufe 1 (dieses Skript, deterministisch): Template-Abschnitte -> Procedure-, Rule-,
Concept- und Artifact-Knoten plus Kanten. Guardrails werden skill-uebergreifend
dedupliziert. Stufe 2 (LLM, siehe decompose_prompt.md): applies_to, Feinzerlegung.

Aufruf: python skill2ku.py <cmsis-skills/generic-mcu-skills/skills> <out-dir>
        python skill2ku.py <CMSIS-Developer-Assistant/skills> <out-dir> --known <units-dir> [--known ...]

Second form (added 5 Oct 2026): the skills the CMSIS Developer Assistant writes itself. A source
folder with a catalog.json is read through it: only the entries with source "bundled" or
"extension" are taken (not the vendored cmsis-skills, the generated routers and cmsis-help), and the
domain is the catalog category. --known names unit folders of an earlier run, so that a reference to
one of their procedures becomes a requires edge.

In both forms the text files a skill ships next to SKILL.md (assets/, templates/, references/
other than *.md) become entity nodes of type "asset" with the file as body, linked from the
procedure with a references edge: the procedure text names them by path, and knowledge_get
returns the file.
"""
import json, re, sys
from difflib import SequenceMatcher
from pathlib import Path

TOOLS = ["csolution", "cbuild", "cpackget", "pyocd", "west", "vcpkg", "packchk", "vela"]
SIM = 0.85  # Aehnlichkeit, ab der zwei Guardrails als dieselbe Regel gelten
ASSET_MAX = 64_000        # bytes; a larger file is not a template an agent should read whole
SUMMARY_WORDS = 40        # the lint limit of build_index
MARKER_BLOCK = re.compile(r"<!-- cmsis-developer-assistant:([a-z-]+):begin -->.*?<!-- cmsis-developer-assistant:\1:end -->\n?", re.S)


def unquote(v):
    """A frontmatter value written as a JSON string ("...") without its quotes."""
    if len(v) > 1 and v[0] == '"' and v[-1] == '"':
        try:
            return json.loads(v)
        except ValueError:
            pass
    return v


def short_description(skill_dir):
    """interface.short_description of agents/openai.yaml, or ''."""
    f = skill_dir / "agents" / "openai.yaml"
    if not f.exists():
        return ""
    m = re.search(r"^\s*short_description:\s*(.*)$", f.read_text(encoding="utf-8"), re.M)
    return unquote(m.group(1).strip()) if m else ""


def asset_files(skill_dir):
    """The text files of a skill other than SKILL.md, agents/ and references/*.md, with their content."""
    out = []
    for f in sorted(skill_dir.rglob("*")):
        rel = f.relative_to(skill_dir)
        if not f.is_file() or rel.name in ("SKILL.md", "README.md") or rel.parts[0] == "agents" \
                or (rel.parts[0] == "references" and f.suffix == ".md") or any(p.startswith(".") for p in rel.parts):
            continue
        raw = f.read_bytes()
        if len(raw) > ASSET_MAX:
            continue
        try:
            out.append((rel.as_posix(), raw.decode("utf-8")))
        except UnicodeDecodeError:
            continue
    return out


def split_sections(md):
    fm, body = {}, md
    m = re.match(r"---\n(.*?)\n---\n(.*)", md, re.S)
    if m:
        for line in m.group(1).splitlines():
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip()
        body = m.group(2)
    sec, cur = {}, None
    for line in body.splitlines():
        h = re.match(r"## (.+)", line)
        if h:
            cur = re.sub(r"\s*\(.*\)$", "", h.group(1)).strip()
            sec[cur] = []
        elif cur:
            sec[cur].append(line)
    return fm, {k: "\n".join(v).strip() for k, v in sec.items()}


def split_body(md):
    m = re.match(r"---\n.*?\n---\n(.*)", md, re.S)
    return (m.group(1) if m else md).strip()


def bullets(text):
    """'- **Label:** Text' -> [(label, text)], Folgezeilen werden angehaengt."""
    out = []
    for line in text.splitlines():
        m = re.match(r"- \*\*(.+?):\*\*\s*(.*)", line)
        if m:
            out.append([m.group(1), m.group(2)])
        elif line.startswith("- "):
            out.append(["", line[2:]])
        elif out and line.strip():
            out[-1][1] += " " + line.strip()
    return out


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def norm(s):
    return re.sub(r"\W+", " ", s.lower()).strip()


def main(src, out, known=()):
    src, out = Path(src), Path(out)
    files = sorted(src.rglob("SKILL.md"))
    category = {}
    catalog = src / "catalog.json"
    if catalog.exists():
        # The CMSIS Developer Assistant's own skills: chosen and placed by its catalog.
        for e in json.loads(catalog.read_text(encoding="utf-8"))["skills"]:
            if e["source"] in ("bundled", "extension") and e["name"] != "cmsis-help":
                category[e["name"]] = e["category"]
        files = [f for f in files if f.parent.parent == src and f.parent.name in category]
    names = {f.parent.name for f in files}
    known_names = set()
    for d in known:
        known_names |= {p.stem[5:] for p in Path(d).rglob("proc-*.md")}
    nodes, edges, rules = {}, [], []

    for f in files:
        name = f.parent.name
        rel = f.parent.relative_to(src).parts
        domain = category.get(name) or (rel[0] if len(rel) > 1 else name)
        text = MARKER_BLOCK.sub("", f.read_text(encoding="utf-8"))
        fm, sec = split_sections(text)
        pid = f"proc-{name}"
        pre = dict((k, v) for k, v in bullets(sec.get("Prerequisites & Context", "")))
        description = unquote(fm.get("description", ""))
        summary, triggers = description, []
        if catalog.exists() and len(description.split()) > SUMMARY_WORDS and short_description(f.parent):
            # Too long for a search result: the short description is the summary, the long one stays searchable.
            summary, triggers = short_description(f.parent), [description]
        nodes[pid] = dict(
            kind="knowledge", type="procedure", domain=domain, title=name,
            summary=summary, triggers=triggers, status="draft", source=str(f.relative_to(src)),
            preconditions=pre.get("Expected input", pre.get("Required input", "")),
            portability=pre.get("Portability", ""),
            tools=[t for t in TOOLS if re.search(rf"\b{t}\b", text)],
            output=sec.get("Expected Output", ""),
            # Ganzer Skill-Body, unveraendert: Procedures werden nie gekuerzt. Die Felder oben sind
            # zusaetzliche Extrakte fuer Index und Filter, kein Ersatz fuer den Text.
            body=split_body(text), sections=sorted(sec))
        for dep in sorted(set(re.findall(r"[$`]([a-z][a-z0-9-]+)`?", text)) & (names | known_names) - {name}):
            edges.append((pid, "requires", f"proc-{dep}"))
        for path, content in asset_files(f.parent):
            aid = f"asset-{name}-{slug(path)}"
            nodes[aid] = dict(kind="entity", type="asset", title=path, body=content,
                              source=str((f.parent / path).relative_to(src)), of=pid)
            edges.append((pid, "references", aid))
        for art in sorted(set(re.findall(r"\.agent-artifacts/[\w<>.\-]+", text))):
            aid = "artifact-" + slug(art.split("/", 1)[1])
            nodes.setdefault(aid, dict(kind="entity", type="artifact", title=art))
            owned = art in pre.get("Owned artifact", "")
            edges.append((pid, "produces" if owned else "consumes", aid))
        for url in sorted(set(re.findall(r"https?://[^\s)>\]]+", text))):
            did = "doc-" + slug(re.sub(r"https?://", "", url))[:60]
            nodes.setdefault(did, dict(kind="entity", type="docsection", title=url))
            edges.append((pid, "references", did))
        for ref in sorted(f.parent.glob("references/*.md")):
            cid = f"concept-{ref.stem}"
            nodes[cid] = dict(kind="knowledge", type="concept", domain=domain, title=ref.stem,
                              status="draft", source=str(ref.relative_to(src)),
                              body=ref.read_text(encoding="utf-8"))
            edges.append((pid, "requires", cid))
        for label, body in bullets(sec.get("Guardrails & Constraints", "")):
            rules.append((label, body, pid))

    # Guardrails clustern: gleiche Regel in vielen Skills -> ein Rule-Knoten
    clusters = []
    for label, body, pid in rules:
        for c in clusters:
            if c["label"] == label and SequenceMatcher(None, norm(c["body"]), norm(body)).ratio() >= SIM:
                c["procs"].append(pid)
                break
        else:
            clusters.append(dict(label=label, body=body, procs=[pid]))
    seen = {}
    for c in clusters:
        base = "rule-" + (slug(c["label"]) or "unnamed")
        seen[base] = seen.get(base, 0) + 1
        shared = len(c["procs"]) > 1
        rid = base if seen[base] == 1 and shared else f"{base}-{c['procs'][0][5:]}"
        n, base_rid = 1, rid
        while rid in nodes:
            n += 1
            rid = f"{base_rid}-{n}"
        title = c["label"] or " ".join(re.sub(r"[`*]", "", c["body"]).split()[:8])
        nodes[rid] = dict(kind="knowledge", type="rule", title=title, severity="must",
                          status="draft", shared=shared, body=c["body"])
        edges += [(rid, "constrains", p) for p in c["procs"]]

    # Ausgabe: eine Markdown-Datei je Wissensknoten, dazu graph.json
    for nid, n in nodes.items():
        if n["kind"] != "knowledge":
            continue
        meta = {k: v for k, v in n.items() if k not in ("body", "kind") and v not in ("", [])}
        meta["id"] = nid
        for rel in ("requires", "produces", "consumes", "references", "constrains"):
            dst = [d for s, r, d in edges if s == nid and r == rel]
            if dst:
                meta[rel] = dst
        p = out / n["type"] / f"{nid}.md"
        p.parent.mkdir(parents=True, exist_ok=True)
        fmtxt = "\n".join(f"{k}: {json.dumps(v, ensure_ascii=False)}" for k, v in meta.items())
        p.write_text(f"---\n{fmtxt}\n---\n\n{n.get('body', '')}\n", encoding="utf-8")
    (out / "graph.json").write_text(json.dumps(
        dict(nodes={k: {a: b for a, b in v.items() if a != "body" or v.get("type") == "asset"} for k, v in nodes.items()},
             edges=[dict(src=s, rel=r, dst=d) for s, r, d in edges]), indent=1, ensure_ascii=False))

    by = lambda t: sum(1 for n in nodes.values() if n["type"] == t)
    sh = [c for c in clusters if len(c["procs"]) > 1]
    print(f"Skills: {len(files)} | Procedures: {by('procedure')} | Concepts: {by('concept')} | "
          f"Artifacts: {by('artifact')} | DocSections: {by('docsection')} | Assets: {by('asset')}")
    pb = sum(len(n.get("body", "").encode()) for n in nodes.values() if n["type"] == "procedure")
    sb = sum(len(f.read_bytes()) for f in files)
    print(f"Groesse: SKILL.md {sb/1e3:.0f} kB, Procedure-Bodies {pb/1e3:.0f} kB")
    print(f"Guardrails roh: {len(rules)} -> Rule-Knoten: {len(clusters)} "
          f"(davon geteilt: {len(sh)}, decken {sum(len(c['procs']) for c in sh)} Vorkommen ab)")
    for c in sorted(sh, key=lambda c: -len(c["procs"])):
        print(f"  {len(c['procs']):3d}x {c['label']}")
    for r in ("requires", "produces", "consumes", "references", "constrains"):
        print(f"Kanten {r}: {sum(1 for e in edges if e[1] == r)}")


if __name__ == "__main__":
    args, known = [], []
    rest = sys.argv[1:]
    while rest:
        a = rest.pop(0)
        if a == "--known" and rest:
            known.append(rest.pop(0))
        else:
            args.append(a)
    if len(args) != 2:
        sys.exit(__doc__)
    main(*args, known=known)
