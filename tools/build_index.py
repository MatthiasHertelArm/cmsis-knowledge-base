#!/usr/bin/env python3
"""build_index: baut knowledge.db aus Wissenseinheiten (Markdown + Frontmatter) und Entity-Graph.

Schema nach 01_konzept_und_schema.md, ergaenzt um:
  - nodes_fts mit triggers-Spalte (Stufe 2, dazu die Skill-Beschreibung aus Stufe 1) neben symptoms
  - Tabelle unresolved: applies_to-Ziele, die sich nicht aufloesen lassen (Stale-Erkennung)
  - Embeddings optional (--no-vec), Modell BAAI/bge-small-en-v1.5, 384 Dimensionen

Aufruf: python build_index.py --units <dir> [--units <dir> ...] --entities <dir> --out knowledge.db [--strict] [--no-vec]
Exit-Code 2 bei --strict und unaufgeloesten applies_to-Zielen (CI-Gate).
"""
import argparse, json, re, sqlite3, sys
from pathlib import Path
import yaml

KNOWLEDGE_TYPES = {"concept", "procedure", "rule", "pattern", "troubleshooting"}
RELATIONS = ("requires", "refines", "conflicts_with", "supersedes", "constrains",
             "produces", "consumes", "references")
TOOLS = ["csolution", "cbuild", "cpackget", "packchk", "svdconv", "pyocd", "west", "vcpkg", "vela", "gdb", "cmsis-debugger", "cmsis-solution"]
APPLIES_KEYS = {"device", "family", "board", "core", "component", "api", "pack", "toolchain", "compiler", "tool"}
EMBED_MODEL = "BAAI/bge-small-en-v1.5"


def read_unit(p):
    text = p.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n?(.*)", text, re.S)
    if not m:
        raise ValueError(f"{p}: kein Frontmatter")
    meta = yaml.safe_load(m.group(1)) or {}
    return meta, m.group(2).strip()


def lint(meta, p):
    errs = []
    for k in ("id", "type", "title", "status"):
        if not meta.get(k):
            errs.append(f"{p}: Feld '{k}' fehlt")
    if meta.get("type") not in KNOWLEDGE_TYPES:
        errs.append(f"{p}: unbekannter type '{meta.get('type')}'")
    if meta.get("status") not in ("draft", "reviewed"):
        errs.append(f"{p}: status muss draft oder reviewed sein")
    s = meta.get("summary") or ""
    if len(s.split()) > 40:
        errs.append(f"{p}: summary hat {len(s.split())} Woerter (max. 40)")
    for k in (meta.get("applies_to") or {}):
        if k not in APPLIES_KEYS:
            errs.append(f"{p}: applies_to-Schluessel '{k}' unbekannt")
    return errs


class Resolver:
    """Loest applies_to-Werte gegen Entity-IDs auf. Akzeptiert csolution-Schreibweisen."""

    def __init__(self, db):
        self.ids = {r[0] for r in db.execute("SELECT id FROM nodes WHERE kind='entity'")}
        self.by_suffix = {}
        for i in self.ids:
            if i.startswith("component:"):
                # component:ARM::CMSIS:CORE -> auch ueber CMSIS:CORE findbar
                self.by_suffix.setdefault("component:" + i.split("::", 1)[-1], set()).add(i)

    def resolve(self, key, value):
        key = {"compiler": "toolchain"}.get(key, key)
        v = re.sub(r"@.*$", "", str(value))           # Versionsbereich abschneiden
        if key == "toolchain":
            v = v.upper()
        if key == "device":
            v = v.split("::")[-1].split(":")[0]       # Vendor:: und :Pname entfernen
        cand = f"{key}:{v}"
        if cand in self.ids:
            return [cand]
        if key == "component" and cand in self.by_suffix:
            return sorted(self.by_suffix[cand])
        if key == "family":
            return sorted(i for i in self.ids if i.startswith("family:") and i.endswith("::" + v))
        return []


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--units", action="append", required=True)
    ap.add_argument("--entities", action="append", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--strict", action="store_true")
    ap.add_argument("--no-vec", action="store_true")
    a = ap.parse_args()

    out = Path(a.out)
    out.unlink(missing_ok=True)
    db = sqlite3.connect(out)
    db.executescript("""
    CREATE TABLE nodes(id TEXT PRIMARY KEY, kind TEXT, type TEXT, domain TEXT, title TEXT,
                       summary TEXT, body TEXT, meta JSON);
    CREATE TABLE edges(src TEXT, rel TEXT, dst TEXT, qual JSON, PRIMARY KEY(src, rel, dst));
    CREATE TABLE unresolved(src TEXT, key TEXT, value TEXT);
    CREATE VIRTUAL TABLE nodes_fts USING fts5(id UNINDEXED, title, summary, body, symptoms, triggers,
                                              tokenize='porter unicode61');
    CREATE INDEX edges_dst ON edges(dst, rel);
    """)

    # Entities: Index plus optionale weitere Verzeichnisse (z. B. overlay.py eines Hersteller-Packs)
    with db:
        for ed in map(Path, a.entities):
            for line in open(ed / "entities.jsonl", encoding="utf-8"):
                n = json.loads(line)
                db.execute("INSERT OR REPLACE INTO nodes VALUES(?,?,?,?,?,?,?,?)",
                           (n["id"], "entity", n["type"], None, n["title"], None, None, json.dumps(n["meta"])))
            for line in open(ed / "entity_edges.jsonl", encoding="utf-8"):
                e = json.loads(line)
                db.execute("INSERT OR IGNORE INTO edges VALUES(?,?,?,?)",
                           (e["src"], e["rel"], e["dst"], json.dumps(e["qual"]) if e["qual"] else None))
        for t in TOOLS:
            db.execute("INSERT OR IGNORE INTO nodes VALUES(?,?,?,?,?,?,?,?)",
                       (f"tool:{t}", "entity", "tool", None, t, None, None, "{}"))
    res = Resolver(db)

    # Wissenseinheiten
    errors, units = [], []
    for d in a.units:
        for p in sorted(Path(d).rglob("*.md")):
            try:
                meta, body = read_unit(p)
            except Exception as ex:
                errors.append(str(ex))
                continue
            e = lint(meta, p)
            errors += e
            if not any("fehlt" in x for x in e):
                units.append((p, meta, body))
    seen = set()
    with db:
        for p, meta, body in units:
            nid = meta["id"]
            if nid in seen:
                errors.append(f"{p}: id '{nid}' doppelt")
                continue
            seen.add(nid)
            m = {k: v for k, v in meta.items() if k not in ("id", "type", "domain", "title", "summary")}
            m["path"] = str(p)
            db.execute("INSERT INTO nodes VALUES(?,?,?,?,?,?,?,?)",
                       (nid, "knowledge", meta["type"], meta.get("domain"), meta["title"],
                        meta.get("summary", ""), body, json.dumps(m, ensure_ascii=False)))
            db.execute("INSERT INTO nodes_fts VALUES(?,?,?,?,?,?)",
                       (nid, meta["title"], meta.get("summary", ""), body,
                        " ".join(meta.get("symptoms") or []),
                        " ".join((meta.get("triggers") or []) + ([meta["description"]] if meta.get("description") else []))))
            for rel in RELATIONS:
                for dst in meta.get(rel) or []:
                    db.execute("INSERT OR IGNORE INTO edges VALUES(?,?,?,NULL)", (nid, rel, dst))
            for key, vals in (meta.get("applies_to") or {}).items():
                for v in vals if isinstance(vals, list) else [vals]:
                    hits = [f"tool:{v}"] if key == "tool" and f"tool:{v}" in res.ids | {f"tool:{t}" for t in TOOLS} \
                        else res.resolve(key, v)
                    if not hits:
                        db.execute("INSERT INTO unresolved VALUES(?,?,?)", (nid, key, str(v)))
                    for h in hits:
                        q = json.dumps({"range": str(v).split("@", 1)[1]}) if "@" in str(v) else None
                        db.execute("INSERT OR IGNORE INTO edges VALUES(?,?,?,?)", (nid, "applies_to", h, q))

    # Kanten auf unbekannte Wissensknoten
    dangling = db.execute("""SELECT e.src, e.rel, e.dst FROM edges e LEFT JOIN nodes n ON n.id=e.dst
                             WHERE n.id IS NULL AND e.rel IN (%s)""" % ",".join("?" * len(RELATIONS)),
                          RELATIONS).fetchall()
    for s, r, d in dangling:
        if not d.startswith(("doc-", "artifact-", "asset-")):     # skill2ku-Entities kommen aus graph.json
            errors.append(f"{s}: {r} -> {d} existiert nicht")

    # skill2ku-Entities (artifact, docsection aus URLs) nachziehen
    for d in a.units:
        g = Path(d) / "graph.json"
        if g.exists():
            gj = json.loads(g.read_text(encoding="utf-8"))
            with db:
                for nid, n in gj["nodes"].items():
                    if n.get("kind") == "entity":
                        # An asset is a file a skill ships: its content is the body, so knowledge_get
                        # returns it. It is not in nodes_fts: search finds procedures, not templates.
                        m = {k: n[k] for k in ("source", "of") if k in n}
                        db.execute("INSERT OR IGNORE INTO nodes VALUES(?,?,?,?,?,?,?,?)",
                                   (nid, "entity", n["type"], None, n["title"], None, n.get("body"), json.dumps(m)))

    if not a.no_vec:
        import sqlite_vec
        from fastembed import TextEmbedding
        db.enable_load_extension(True)
        sqlite_vec.load(db)
        db.execute("CREATE VIRTUAL TABLE nodes_vec USING vec0(id TEXT PRIMARY KEY, embedding FLOAT[384])")
        rows = db.execute("SELECT id, title, summary, body, json_extract(meta,'$.symptoms') "
                          "FROM nodes WHERE kind='knowledge'").fetchall()
        texts = [f"{t}. {s or ''} {' '.join(json.loads(sy) if sy else [])} {(b or '')[:600]}" for _, t, s, b, sy in rows]
        model = TextEmbedding(EMBED_MODEL)
        with db:
            for (nid, *_), vec in zip(rows, model.embed(texts, batch_size=64)):
                db.execute("INSERT INTO nodes_vec VALUES(?,?)", (nid, sqlite_vec.serialize_float32(list(vec))))
        db.execute("CREATE TABLE info(key TEXT PRIMARY KEY, value TEXT)")
        db.execute("INSERT INTO info VALUES('embed_model', ?)", (EMBED_MODEL,))
        db.commit()

    st = dict(db.execute("SELECT kind||'/'||type, count(*) FROM nodes GROUP BY 1").fetchall())
    kn = {k.split("/")[1]: v for k, v in st.items() if k.startswith("knowledge/")}
    print("Wissensknoten:", kn)
    print("Entities:", sum(v for k, v in st.items() if k.startswith("entity/")))
    print("Kanten:", dict(db.execute("SELECT rel, count(*) FROM edges GROUP BY rel").fetchall()))
    unres = db.execute("SELECT count(*) FROM unresolved").fetchone()[0]
    print(f"Unaufgeloeste applies_to: {unres}, Lint-Fehler: {len(errors)}")
    for e in errors[:15]:
        print("  ", e)
    db.execute("VACUUM")
    db.close()
    print(f"{out}: {out.stat().st_size/1e6:.1f} MB")
    if errors and a.strict:
        sys.exit(1)
    if unres and a.strict:
        sys.exit(2)


if __name__ == "__main__":
    main()
