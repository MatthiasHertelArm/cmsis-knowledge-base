#!/usr/bin/env python3
"""entities: erzeugt den Entity-Graphen aus Pack-Index und PDSC-Dateien.

Entity-Knoten werden generiert, nie von Hand gepflegt. IDs folgen der csolution-Notation,
damit applies_to im Frontmatter direkt dieselben Bezeichner nutzt:

  pack:ARM::CMSIS                         Pack (ohne Version)
  family:Keil::STM32U5 Series             Device-Familie, Unterfamilie: subfamily:...
  device:STM32U585AIIx                    Device (Dname ist im Index eindeutig genug, Vendor in meta)
  board:STMicroelectronics::B-U585I-IOT02A
  core:Cortex-M33
  component:ARM::CMSIS:CORE               Cvendor::Cclass:Cgroup[:Csub]
  api:CMSIS:RTOS2                         Cclass:Capiversion-unabhaengig
  toolchain:AC6 | GCC | CLANG | IAR
  doc:<sha1-12>                           book-Eintrag aus PDSC (DocSection)

Kanten: part_of, mounted_on, has_core, implements, documents.

Aufruf: python entities.py <index.pidx> <pdsc-dir> <out-dir>
"""
import hashlib, json, re, sys
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path

TOOLCHAINS = {"AC6": "Arm Compiler for Embedded 6", "GCC": "GNU Arm Embedded", "CLANG": "LLVM/Clang", "IAR": "IAR"}


def vend(v):
    """Dvendor 'STMicroelectronics:13' -> 'STMicroelectronics' (Enum-Suffix aus dem Schema)."""
    return re.sub(r":\d+$", "", v or "")


def strip_ns(root):
    for el in root.iter():
        if isinstance(el.tag, str) and "}" in el.tag:
            el.tag = el.tag.split("}", 1)[1]
    return root


class Graph:
    """Sammelt Entity-Knoten und Kanten. Von entities.py (Index) und overlay.py (lokal) genutzt."""

    def __init__(self):
        self.nodes, self.edges = {}, set()

    def node(self, nid, typ, title, **meta):
        n = self.nodes.setdefault(nid, dict(id=nid, kind="entity", type=typ, title=title, meta={}))
        n["meta"].update({k: v for k, v in meta.items() if v not in (None, "", [])})
        return nid

    def edge(self, s, r, d, **q):
        self.edges.add((s, r, d, json.dumps(q, sort_keys=True) if q else ""))

    def mark_unresolved(self):
        """Unaufgeloeste Ziele (z. B. mountedDevice ohne DFP) als Platzhalter markieren."""
        for s, r, d, q in list(self.edges):
            if d not in self.nodes:
                self.node(d, d.split(":", 1)[0], d.split(":", 1)[1].split("::")[-1], unresolved=True)

    def write(self, out):
        out = Path(out)
        out.mkdir(parents=True, exist_ok=True)
        with open(out / "entities.jsonl", "w", encoding="utf-8") as fh:
            for n in self.nodes.values():
                fh.write(json.dumps(n, ensure_ascii=False) + "\n")
        with open(out / "entity_edges.jsonl", "w", encoding="utf-8") as fh:
            for s, r, d, q in sorted(self.edges):
                fh.write(json.dumps(dict(src=s, rel=r, dst=d, qual=json.loads(q) if q else None)) + "\n")


def ingest_pdsc(g, root, pid, **extra):
    """Ein geparstes PDSC in den Graphen uebernehmen. extra landet im meta aller erzeugten Knoten."""
    node, edge = g.node, g.edge
    pvendor = (root.findtext("vendor") or "").strip()
    g.nodes[pid]["meta"]["description"] = re.sub(r"\s+", " ", (root.findtext("description") or "")).strip()[:300]

    def books(el, target):
        for b in el.findall("book") + el.findall("documentation"):
            name = b.get("name") or b.get("title") or ""
            if not name:
                continue
            did = "doc:" + hashlib.sha1(f"{pid}|{name}".encode()).hexdigest()[:12]
            node(did, "docsection", b.get("title") or name, path=name, category=b.get("category"), pack=pid, **extra)
            edge(did, "documents", target)

    # Devices: family > subFamily > device > variant, Attribute vererben sich nach unten
    def walk(el, inherited, parent):
        attrs = dict(inherited)
        proc = el.find("processor")
        if proc is not None:
            attrs.update({k: v for k, v in proc.attrib.items()})
        for c in el.findall("processor"):
            if c.get("Dcore"):
                attrs.setdefault("cores", set()).add(c.get("Dcore"))
        if el.tag == "family":
            nid = node(f"family:{vend(el.get('Dvendor'))}::{el.get('Dfamily')}", "family", el.get("Dfamily"),
                       vendor=vend(el.get("Dvendor")), **extra)
        elif el.tag == "subFamily":
            nid = node(f"subfamily:{el.get('DsubFamily')}", "subfamily", el.get("DsubFamily"), **extra)
        elif el.tag in ("device", "variant"):
            name = el.get("Dname") or el.get("Dvariant")
            nid = node(f"device:{name}", "device", name, vendor=vend(inherited.get("Dvendor")), pack=pid, **extra)
            cores = attrs.get("cores") or ({attrs["Dcore"]} if attrs.get("Dcore") else set())
            for core in sorted(cores):
                node(f"core:{core}", "core", core)
                edge(nid, "has_core", f"core:{core}")
            for k in ("Dfpu", "Dmpu", "Dtz", "Ddsp", "Dmve", "Dclock"):
                if attrs.get(k):
                    g.nodes[nid]["meta"][k] = attrs[k]
        else:
            nid = parent
        if nid != parent:
            edge(nid, "part_of", parent)
            books(el, nid)
        inh = dict(attrs, Dvendor=el.get("Dvendor", inherited.get("Dvendor")))
        for child in el:
            if child.tag in ("subFamily", "device", "variant"):
                walk(child, inh, nid)

    for fam in root.findall("devices/family"):
        walk(fam, {"Dvendor": fam.get("Dvendor")}, pid)

    for b in root.findall("boards/board"):
        bv = b.get("vendor") or pvendor
        bid = node(f"board:{bv}::{b.get('name')}", "board", b.get("name"), vendor=bv,
                   revision=b.get("revision"), pack=pid, **extra)
        edge(bid, "part_of", pid)
        books(b, bid)
        for md in b.findall("mountedDevice"):
            if md.get("Dname"):
                edge(bid, "mounted_on", f"device:{md.get('Dname')}")

    for api in root.findall("apis/api"):
        aid = node(f"api:{api.get('Cclass')}:{api.get('Cgroup')}", "api",
                   f"{api.get('Cclass')}:{api.get('Cgroup')}", version=api.get("Capiversion"), **extra)
        edge(aid, "part_of", pid)

    for bundle in root.findall("components/bundle"):
        for c in bundle.findall("component"):
            c.attrib.setdefault("Cbundle", bundle.get("Cbundle"))
            c.attrib.setdefault("Cclass", bundle.get("Cclass"))
    for c in root.findall("components/component") + root.findall("components/bundle/component"):
        cv = c.get("Cvendor") or pvendor
        parts = [c.get("Cclass"), c.get("Cgroup")] + ([c.get("Csub")] if c.get("Csub") else [])
        if not all(parts):
            continue
        cid = node(f"component:{cv}::{':'.join(parts)}", "component", ":".join(parts),
                   vendor=cv, bundle=c.get("Cbundle"), pack=pid, **extra)
        edge(cid, "part_of", pid)
        if c.get("Capiversion"):
            edge(cid, "implements", f"api:{c.get('Cclass')}:{c.get('Cgroup')}")


def main(pidx, pdsc_dir, out):
    pdsc_dir = Path(pdsc_dir)
    g = Graph()
    for t, desc in TOOLCHAINS.items():
        g.node(f"toolchain:{t}", "toolchain", t, description=desc)

    idx = ET.parse(pidx).getroot()
    active = {}
    for p in idx.iter("pdsc"):
        a = p.attrib
        pid = g.node(f"pack:{a['vendor']}::{a['name']}", "pack", f"{a['vendor']}::{a['name']}",
                     version=a.get("version"), url=a.get("url"), deprecated=a.get("deprecated"),
                     replacement=a.get("replacement"))
        if "deprecated" not in a:
            active[f"{a['vendor']}.{a['name']}.pdsc"] = pid
        if a.get("replacement"):
            g.edge(pid, "superseded_by", "pack:" + a["replacement"].replace(".", "::", 1))

    parsed, failed = 0, []
    for fname, pid in sorted(active.items()):
        f = pdsc_dir / fname
        if not f.exists():
            continue
        try:
            root = strip_ns(ET.parse(f).getroot())
        except ET.ParseError as e:
            failed.append((fname, str(e)))
            continue
        parsed += 1
        ingest_pdsc(g, root, pid)

    g.mark_unresolved()
    g.write(out)
    nodes, edges = g.nodes, g.edges
    c = Counter(n["type"] for n in nodes.values())
    print(f"PDSC gelesen: {parsed}, Parse-Fehler: {len(failed)}")
    print("Knoten: " + ", ".join(f"{k} {v}" for k, v in c.most_common()))
    print("Kanten: " + ", ".join(f"{k} {v}" for k, v in Counter(e[1] for e in edges).most_common()))
    print(f"Unaufgeloest: {sum(1 for n in nodes.values() if n['meta'].get('unresolved'))}")
    for f, e in failed[:5]:
        print("  Parse-Fehler", f, e)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    main(*sys.argv[1:])
