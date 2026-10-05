#!/usr/bin/env python3
"""overlay: Entities aus dem lokalen Arbeitsstand, ergaenzend zum Pack-Index.

Fuer Devices, die es offiziell noch nicht gibt. Quellen, in dieser Reihenfolge:

  1. Packs mit path: in *.csolution.yml und *.cbuild.yml (lokal zusammengebaute Packs)
  2. Alle *.pdsc im Workspace (Pack-Repo in Arbeit, noch nicht installiert)
  3. $CMSIS_PACK_ROOT/.Local/local_repository.pidx (per cpackget add registrierte lokale Packs)
  4. kb-entities.yml im Workspace oder in .cmsis/: Devices, die nur Doku haben, und manuell
     gepflegte Cores

Alle erzeugten Knoten tragen meta.origin = "local" und meta.source = Datei.

Aufruf als CLI (z. B. fuer die CI eines Hersteller-Packs):
  python overlay.py <workspace> <out-dir>      schreibt entities.jsonl und entity_edges.jsonl
"""
import os, re, sys
import xml.etree.ElementTree as ET
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent))
from entities import Graph, ingest_pdsc, strip_ns, vend  # noqa: E402

SKIP_DIRS = {".git", "node_modules", "out", "tmp", "build", ".venv", "__pycache__"}
MANUAL_NAMES = ("kb-entities.yml", ".cmsis/kb-entities.yml")


def expand(path, base):
    """${CMSIS_PACK_ROOT}, $SolutionDir()$ und relative Pfade aufloesen."""
    p = str(path)
    p = p.replace("$SolutionDir()$", str(base)).replace("${CMSIS_PACK_ROOT}", os.environ.get("CMSIS_PACK_ROOT", ""))
    p = os.path.expandvars(os.path.expanduser(p))
    q = Path(p)
    return q if q.is_absolute() else (Path(base) / q).resolve()


def find_pdsc(folder):
    folder = Path(folder)
    return sorted(folder.glob("*.pdsc")) if folder.is_dir() else ([folder] if folder.suffix == ".pdsc" else [])


def pack_paths(ws):
    """path:-Eintraege unter packs: aus csolution.yml und cbuild.yml."""
    out = []
    for f in list(ws.rglob("*.csolution.yml"))[:20] + list(ws.rglob("*.cbuild.yml"))[:50]:
        if SKIP_DIRS & set(f.relative_to(ws).parts[:-1]):
            continue
        try:
            y = yaml.safe_load(f.read_text(encoding="utf-8")) or {}
        except Exception:
            continue
        root = y.get("solution") or y.get("build") or {}
        for p in root.get("packs") or []:
            if isinstance(p, dict) and p.get("path"):
                out.append((expand(p["path"], f.parent), f))
    return out


def scan_pdsc(ws, max_depth=6):
    hits = []
    for dirpath, dirnames, filenames in os.walk(ws):
        rel = Path(dirpath).relative_to(ws)
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS and not d.startswith(".")]
        if len(rel.parts) >= max_depth:
            dirnames[:] = []
        hits += [Path(dirpath) / f for f in filenames if f.endswith(".pdsc")]
    return hits


def local_repo_pdsc():
    root = os.environ.get("CMSIS_PACK_ROOT")
    idx = Path(root, ".Local", "local_repository.pidx") if root else None
    if not idx or not idx.exists():
        return []
    out = []
    for p in ET.parse(idx).getroot().iter("pdsc"):
        url = p.get("url", "")
        base = Path(re.sub(r"^file://", "", url))
        out.append(base / f"{p.get('vendor')}.{p.get('name')}.pdsc")
    return out


def add_pdsc(g, f, seen, log):
    f = Path(f)
    if not f.exists() or f.resolve() in seen:
        return
    seen.add(f.resolve())
    try:
        root = strip_ns(ET.parse(f).getroot())
    except ET.ParseError as e:
        log.append(f"PDSC nicht lesbar: {f}: {e}")
        return
    vendor, name = (root.findtext("vendor") or "").strip(), (root.findtext("name") or "").strip()
    if not vendor or not name:
        log.append(f"PDSC ohne vendor oder name: {f}")
        return
    rel = root.find("releases/release")
    pid = g.node(f"pack:{vendor}::{name}", "pack", f"{vendor}::{name}", origin="local", source=str(f),
                 version=rel.get("version") if rel is not None else None)
    ingest_pdsc(g, root, pid, origin="local", source=str(f))
    log.append(f"PDSC: {f}")


def add_manual(g, f, ws, log):
    """kb-entities.yml: Devices nur mit Doku, manuell gepflegte Cores."""
    y = yaml.safe_load(Path(f).read_text(encoding="utf-8")) or {}
    src = dict(origin="local", source=str(f), manual=True)
    for c in y.get("cores") or []:
        g.node(f"core:{c['name']}", "core", c["name"], **src)
    for d in y.get("devices") or []:
        v = vend(d.get("vendor", ""))
        nid = g.node(f"device:{d['name']}", "device", d["name"], vendor=v, **src, **(d.get("features") or {}))
        if d.get("family"):
            fid = g.node(f"family:{v}::{d['family']}", "family", d["family"], vendor=v, **src)
            g.edge(nid, "part_of", fid)
        for core in ([d["core"]] if isinstance(d.get("core"), str) else d.get("core") or []):
            g.node(f"core:{core}", "core", core)
            g.edge(nid, "has_core", f"core:{core}")
        for doc in d.get("docs") or []:
            path = str(expand(doc["path"], Path(f).parent)) if doc.get("path") else doc.get("url")
            did = "doc:local:" + re.sub(r"[^A-Za-z0-9]+", "-", f"{d['name']}-{doc.get('title', path)}")[:60]
            g.node(did, "docsection", doc.get("title") or path, path=path, category=doc.get("category", "manual"), **src)
            g.edge(did, "documents", nid)
    log.append(f"manuell: {f} ({len(y.get('devices') or [])} Devices, {len(y.get('cores') or [])} Cores)")


def build(ws):
    """Graph aus dem Workspace. Rueckgabe (Graph, Log)."""
    ws = Path(ws).resolve()
    g, seen, log = Graph(), set(), []
    for folder, origin in pack_paths(ws):
        for f in find_pdsc(folder):
            add_pdsc(g, f, seen, log)
    for f in scan_pdsc(ws):
        add_pdsc(g, f, seen, log)
    for f in local_repo_pdsc():
        add_pdsc(g, f, seen, log)
    for name in MANUAL_NAMES:
        if (ws / name).exists():
            add_manual(g, ws / name, ws, log)
    return g, log


def workspace_of(path):
    """Vom cbuild.yml aufwaerts bis zum Ordner mit *.csolution.yml oder .git."""
    p = Path(path).resolve()
    p = p if p.is_dir() else p.parent
    for d in [p, *p.parents]:
        if list(d.glob("*.csolution.yml")) or (d / ".git").exists():
            return d
    return p


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    g, log = build(sys.argv[1])
    g.write(sys.argv[2])
    print("\n".join(log))
    print(f"{len(g.nodes)} Knoten, {len(g.edges)} Kanten")
