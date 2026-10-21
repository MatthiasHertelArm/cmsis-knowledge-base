"""kb_lib: Retrieval-Logik fuer knowledge.db. Vom MCP-Server und von den Tests genutzt.

Ablauf knowledge_search:
  1. Projektkontext (Device, Komponenten, Compiler) in eine Entity-Menge aufloesen,
     inklusive Vorfahren entlang part_of und Cores des Devices.
  2. Kandidaten: BM25 (FTS5) und Vektor-kNN (sqlite-vec), fusioniert per Reciprocal Rank Fusion.
     Trifft die Anfrage ein symptom_regex exakt, steht die Einheit vorne.
  3. Filter: Einheit ohne applies_to gilt universell, sonst muss ein Ziel im Kontext liegen.
     Spezifischere Einheiten (refines) verdraengen die allgemeinere.
  4. Ausgabe nur Summaries bis zum Token-Budget. Volltext liefert knowledge_get, ungekuerzt.
"""
import json, re, sqlite3
from functools import lru_cache
from pathlib import Path

import yaml

RRF_K = 60
FIRST_LINE_BONUS = 0.05     # exakter Treffer in der ersten Zeile vor einem in spaeteren Zeilen
OVERVIEW_ROLES = ("intro", "summary", "preface")
OVERVIEW_WEIGHT = 0.6



def tokens(text):
    return int(len(text or "") / 4) + 1       # grobe Schaetzung, reicht fuer Budgetierung


def fallback_summary(r):
    """Solange Stufe 2 keine summary geschrieben hat: Symptom bzw. erste 40 Woerter ohne Markdown."""
    meta = json.loads(r["meta"] or "{}")
    if r["type"] == "troubleshooting" and meta.get("symptoms"):
        return f"[{meta.get('tool', '')}] " + meta["symptoms"][-1]
    text = re.sub(r"^#+ .*$|[`*_]", "", r["body"] or "", flags=re.M)
    return " ".join(text.split()[:40])


class KB:
    def __init__(self, path, use_vec=True):
        self.db = sqlite3.connect(path, check_same_thread=False)
        self.db.row_factory = sqlite3.Row
        self.vec = None
        if use_vec:
            try:
                import sqlite_vec
                self.db.enable_load_extension(True)
                sqlite_vec.load(self.db)
                model = self.db.execute("SELECT value FROM info WHERE key='embed_model'").fetchone()
                if model:
                    from fastembed import TextEmbedding
                    self.vec = TextEmbedding(model[0])
            except Exception:
                self.vec = None
        self.symptoms = []
        for r in self.db.execute("SELECT id, json_extract(meta,'$.symptom_regex') rx FROM nodes "
                                 "WHERE type='troubleshooting' AND rx IS NOT NULL"):
            try:
                self.symptoms.append((r["id"], re.compile(r["rx"], re.I)))
            except re.error:
                pass

    # ---------- lokales Overlay ----------
    def add_overlay(self, g):
        """Entities aus dem Workspace (overlay.build) ueber den Index legen. Die Index-Datei bleibt
        unveraendert: TEMP-Views namens nodes/edges verdecken die Tabellen fuer diese Verbindung."""
        db = self.db
        db.executescript("""
        DROP VIEW IF EXISTS temp.nodes; DROP VIEW IF EXISTS temp.edges;
        CREATE TEMP TABLE IF NOT EXISTS ov_nodes(id TEXT PRIMARY KEY, kind TEXT, type TEXT, domain TEXT,
            title TEXT, summary TEXT, body TEXT, meta JSON);
        CREATE TEMP TABLE IF NOT EXISTS ov_edges(src TEXT, rel TEXT, dst TEXT, qual JSON);
        DELETE FROM temp.ov_nodes; DELETE FROM temp.ov_edges;
        """)
        for n in g.nodes.values():
            db.execute("INSERT OR REPLACE INTO temp.ov_nodes VALUES(?,?,?,?,?,?,?,?)",
                       (n["id"], "entity", n["type"], None, n["title"], None, None, json.dumps(n["meta"])))
        for s_, r, d, q in g.edges:
            db.execute("INSERT INTO temp.ov_edges VALUES(?,?,?,?)", (s_, r, d, q or None))
        db.executescript("""
        CREATE TEMP VIEW nodes AS
            SELECT * FROM temp.ov_nodes
            UNION ALL SELECT * FROM main.nodes WHERE id NOT IN (SELECT id FROM temp.ov_nodes);
        CREATE TEMP VIEW edges AS
            SELECT * FROM temp.ov_edges UNION ALL SELECT * FROM main.edges;
        """)
        self.overlay = {"nodes": len(g.nodes), "devices": sum(1 for n in g.nodes.values() if n["type"] == "device")}

    def use_workspace(self, path):
        """Overlay fuer den Workspace eines cbuild.yml laden, neu nur wenn sich PDSC oder
        kb-entities.yml geaendert haben."""
        import sys
        sys.path.insert(0, str(Path(__file__).parent))
        import overlay
        ws = overlay.workspace_of(path)
        stamp = (str(ws), tuple(sorted((str(f), f.stat().st_mtime) for f in overlay.scan_pdsc(ws))),
                 tuple((n, (ws / n).stat().st_mtime) for n in overlay.MANUAL_NAMES if (ws / n).exists()))
        if getattr(self, "_ws_stamp", None) != stamp:
            g, log = overlay.build(ws)
            self.add_overlay(g)
            self.overlay["workspace"] = str(ws)
            self.overlay["log"] = log
            self._ws_stamp = stamp
        return self.overlay

    # ---------- Kontext ----------
    def ancestors(self, nid, depth=6):
        seen, frontier = {nid}, {nid}
        for _ in range(depth):
            nxt = set()
            for n in frontier:
                for r in self.db.execute("SELECT dst FROM edges WHERE src=? AND rel IN ('part_of','has_core')", (n,)):
                    if r[0] not in seen:
                        nxt.add(r[0])
            seen |= nxt
            frontier = nxt
        return seen

    def context_entities(self, device=None, components=(), compiler=None, board=None, tools=()):
        ents = set()
        if device:
            d = "device:" + device.split("::")[-1].split(":")[0]
            ents |= self.ancestors(d)
        if board:
            b = board.split("@")[0]
            bid = b if b.startswith("board:") else "board:" + b
            ents |= self.ancestors(bid)
            for r in self.db.execute("SELECT dst FROM edges WHERE src=? AND rel='mounted_on'", (bid,)):
                ents |= self.ancestors(r[0])
        for c in components:
            c = re.sub(r"@.*$", "", c)
            cid = "component:" + c if "::" in c else None
            if cid:
                ents.add(cid)
            ents |= {r[0] for r in self.db.execute(
                "SELECT id FROM nodes WHERE type='component' AND (id=? OR id LIKE ?)",
                (f"component:{c}", f"component:%::{c.split('::')[-1]}"))}
        if compiler:
            ents.add("toolchain:" + re.sub(r"@.*$", "", compiler).upper())
        ents |= {f"tool:{t}" for t in tools}
        return ents

    @staticmethod
    def parse_cbuild(path):
        """*.cbuild.yml -> device, board, compiler, components."""
        y = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
        b = y.get("build", y)
        comps = [c.get("component", "") for c in b.get("components", []) if isinstance(c, dict)]
        return dict(device=b.get("device"), board=b.get("board"), compiler=b.get("compiler"),
                    components=[c for c in comps if c])

    # ---------- Suche ----------
    def _bm25(self, q, n):
        terms = re.findall(r"\w+", q)
        if not terms:
            return []
        fts = " OR ".join(f'"{t}"' for t in terms)
        return [r[0] for r in self.db.execute(
            "SELECT id FROM nodes_fts WHERE nodes_fts MATCH ? ORDER BY bm25(nodes_fts, 0, 8, 4, 1, 6, 6) LIMIT ?",
            (fts, n))]

    def _knn(self, q, n):
        if not self.vec:
            return []
        import sqlite_vec
        v = list(self.vec.query_embed(q))[0] if hasattr(self.vec, "query_embed") else list(self.vec.embed([q]))[0]
        return [r[0] for r in self.db.execute(
            "SELECT id FROM nodes_vec WHERE embedding MATCH ? AND k = ? ORDER BY distance",
            (sqlite_vec.serialize_float32(list(v)), n))]

    def applies(self, nid, ctx):
        """UND ueber Dimensionen (core, toolchain, family ...), ODER innerhalb einer Dimension.
        Rueckgabe (gilt, Anzahl Ziele, unverified). Kennt der Kontext eine Dimension gar nicht
        (z. B. neues Device ohne Core im Graph), wird die Einheit nicht verworfen, sondern als
        unverified markiert."""
        tg = [r[0] for r in self.db.execute("SELECT dst FROM edges WHERE src=? AND rel='applies_to'", (nid,))]
        if not tg:
            return True, 0, False                # universell
        if ctx is None:
            return True, len(tg), False
        dims = {}
        for t in tg:
            dims.setdefault(t.split(":", 1)[0], []).append(t)
        ctx_dims = {c.split(":", 1)[0] for c in ctx}
        unverified = False
        for dim, targets in dims.items():
            if any(t in ctx for t in targets):
                continue
            if dim not in ctx_dims:
                unverified = True                # Kontext sagt nichts ueber diese Dimension
                continue
            return False, len(tg), False         # Kontext widerspricht
        return True, len(tg), unverified

    def unresolved_context(self, ctx):
        """Kontext-IDs, die der Graph nicht kennt, z. B. ein Device aus einem lokalen DFP."""
        return sorted(c for c in ctx or () if not self.db.execute("SELECT 1 FROM nodes WHERE id=?", (c,)).fetchone())

    def search(self, query, domain=None, types=None, ctx=None, k=8, budget=800):
        # Tool-Ausgabe wie "error csolution: ..." oder "<datei> - error csolution: ...": Praefix weg, je Zeile pruefen
        lines = [re.sub(r"^.*?\b(?:error|warning|info)\s+[\w.-]+:\s*", "", l).strip() for l in query.splitlines()] or [query]
        # Erste passende Zeile je Einheit: in Tool-Ausgabe ist der erste Fehler die Ursache, spaetere folgen daraus
        first = {}
        for i, rx in self.symptoms:
            hit = next((n for n, l in enumerate(lines) if l and rx.search(l)), None)
            if hit is not None:
                first[i] = hit
        exact = sorted(first, key=first.get)
        lists = [self._bm25(query, 60), self._knn(query, 60)]
        score = {}
        for lst in lists:
            for rank, nid in enumerate(lst):
                score[nid] = score.get(nid, 0) + 1 / (RRF_K + rank + 1)
        for nid in exact:
            score[nid] = score.get(nid, 0) + 1.0 + FIRST_LINE_BONUS * (1 - first[nid] / len(lines))
        # Overview units (a chapter's intro or summary, role in the frontmatter) answer the broad question but
        # must not hide the section that answers the specific one: their score is scaled down, not removed.
        for nid in list(score):
            meta = self.db.execute("SELECT json_extract(meta,'$.role') FROM nodes WHERE id=?", (nid,)).fetchone()
            if meta and meta[0] in OVERVIEW_ROLES:
                score[nid] *= OVERVIEW_WEIGHT
        rows = []
        for nid in sorted(score, key=lambda x: -score[x]):
            r = self.db.execute("SELECT id,type,domain,title,summary,body,meta FROM nodes WHERE id=?", (nid,)).fetchone()
            if not r or (domain and r["domain"] != domain) or (types and r["type"] not in types):
                continue
            ok, spec, unv = self.applies(nid, ctx)
            if not ok:
                continue
            rows.append((r, score[nid], spec, unv))
        # refines: liegt eine spezifischere Einheit im Ergebnis, faellt die allgemeinere raus
        ids = {r[0]["id"] for r in rows if not r[3]}   # nur sicher geltende Einheiten verdraengen
        refined = {d for (s, d) in self.db.execute("SELECT src,dst FROM edges WHERE rel='refines'") if s in ids}
        out, used = [], 0
        for r, sc, spec, unv in rows:
            if r["id"] in refined:
                continue
            summ = r["summary"] or fallback_summary(r)
            item = dict(id=r["id"], type=r["type"], title=r["title"], summary=summ,
                        score=round(sc, 4), exact_symptom=r["id"] in exact,
                        full_tokens=tokens(r["body"]))
            if unv:
                item["applies"] = "unverified"
            t = tokens(json.dumps(item))
            if out and used + t > budget:
                break
            out.append(item)
            used += t
            if len(out) >= k:
                break
        res = dict(results=out, budget_used=used, context_filter=ctx is not None)
        unk = self.unresolved_context(ctx)
        if unk:
            res["context_unresolved"] = unk
        return res

    def get(self, nid):
        r = self.db.execute("SELECT * FROM nodes WHERE id=?", (nid,)).fetchone()
        if not r:
            return dict(error=f"unknown id {nid}")
        d = dict(r)
        d["meta"] = json.loads(d["meta"] or "{}")
        return d                                   # Procedures und alle anderen: nie gekuerzt

    def expand(self, nid, relation=None):
        q = "SELECT src,rel,dst FROM edges WHERE (src=? OR dst=?)" + (" AND rel=?" if relation else "")
        args = (nid, nid, relation) if relation else (nid, nid)
        out = []
        for s, rel, d in self.db.execute(q + " LIMIT 200", args):
            other, direction = (d, "out") if s == nid else (s, "in")
            r = self.db.execute("SELECT kind,type,title,summary FROM nodes WHERE id=?", (other,)).fetchone()
            out.append(dict(rel=rel, direction=direction, id=other,
                            type=r["type"] if r else None, title=r["title"] if r else None,
                            summary=(r["summary"] if r else None)))
        return dict(id=nid, neighbors=out)
