#!/usr/bin/env python3
"""stage2_merge: schreibt Stufe-2-Ergebnisse (JSON je Procedure) in die Einheiten aus Stufe 1.

- summary, triggers, applies_to, unmapped, verification, stop_conditions -> Frontmatter der Procedure.
  Der Body bleibt unveraendert. Die Beschreibung aus Stufe 1 bleibt als description erhalten.
- rules generic ohne delta: Procedure wandert von der spezifischen Rule zur kanonischen Rule.
  Bleibt die spezifische Rule ohne constrains, wird sie geloescht.
- rules generic mit delta: Rule bleibt, Body wird zum delta, refines -> canonical_id.
- Kanonische Rules werden als Stub angelegt (units/canonical/), Text schreibt ein Mensch.
- extracted -> units/extracted/<typ>/x-<proc>-<n>.md, status draft.

Aufruf: python stage2_merge.py <units-dir> <json-dir>
"""
import json, re, sys
from pathlib import Path
import yaml

LICENSE = "Apache-2.0"   # the canonical rules are distilled from cmsis-skills; an extracted unit keeps its procedure's licence
CANON = {
    "rule-no-fabrication": "No fabrication",
    "rule-tone-and-style": "Tone and style",
    "rule-portability": "Portability",
    "rule-no-install": "No installation or environment changes",
    "rule-user-confirmation": "Explicit user confirmation before file changes",
}


def load(p):
    m = re.match(r"---\n(.*?)\n---\n?(.*)", p.read_text(encoding="utf-8"), re.S)
    return yaml.safe_load(m.group(1)), m.group(2).strip()


def save(p, meta, body):
    fm = "\n".join(f"{k}: {json.dumps(v, ensure_ascii=False)}" for k, v in meta.items() if v not in ("", [], {}, None))
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(f"---\n{fm}\n---\n\n{body}\n", encoding="utf-8")


def main(units, jdir):
    units, jdir = Path(units), Path(jdir)
    rule_files = {load(p)[0]["id"]: p for p in (units / "rule").glob("*.md")}
    stats = dict(procs=0, moved=0, refined=0, deleted=0, extracted=0)
    for jf in sorted(jdir.glob("proc-*.json")):
        d = json.loads(jf.read_text(encoding="utf-8"))
        pid = d["id"]
        pp = units / "procedure" / f"{pid}.md"
        meta, body = load(pp)
        # Die Skill-Beschreibung aus Stufe 1 bleibt durchsuchbar: Stufe 2 kuerzt summary und triggers,
        # die Beschreibung nennt aber Symptome und Begriffe (HardFault, Hang), nach denen gesucht wird.
        if not meta.get("description"):
            meta["description"] = " ".join(meta.get("triggers") or []) or meta.get("summary", "")
        for k in ("summary", "triggers", "verification", "stop_conditions", "unmapped"):
            if d.get(k):
                meta[k] = d[k]
        meta["applies_to"] = {k: v for k, v in (d.get("applies_to") or {}).items() if v}
        meta["stage2"] = jf.name
        save(pp, meta, body)
        stats["procs"] += 1

        for r in d.get("rules", []):
            cid = r.get("canonical_id")
            if r.get("class") != "generic" or cid not in CANON or r["id"] not in rule_files:
                continue
            cp = units.parent / "canonical" / f"{cid}.md"
            if cp.exists():
                cm, cb = load(cp)
            else:
                cm, cb = dict(id=cid, type="rule", domain="general", title=CANON[cid], severity="must",
                              status="draft", license=LICENSE, canonical=True, constrains=[]), "_Kanonischer Text: wird von Hand geschrieben._"
            cm["constrains"] = sorted(set(cm.get("constrains", [])) | {pid})
            save(cp, cm, cb)
            rp = rule_files[r["id"]]
            if r["id"] == cid:
                continue                    # Rule ist schon die kanonische (z. B. geteilte Tone and style)
            rm, rb = load(rp)
            if (r.get("delta") or "").strip():
                rm["refines"] = sorted(set(rm.get("refines", [])) | {cid})
                rm["delta_of"] = cid
                save(rp, rm, rb + "\n\n## Delta zu " + cid + "\n\n" + r["delta"].strip())
                stats["refined"] += 1
            else:
                rm["constrains"] = [c for c in rm.get("constrains", []) if c != pid]
                stats["moved"] += 1
                if rm["constrains"]:
                    save(rp, rm, rb)
                else:
                    rp.unlink()
                    rule_files.pop(r["id"])
                    stats["deleted"] += 1

        for n, x in enumerate(d.get("extracted", []), 1):
            xm = dict(id=f"x-{pid[5:]}-{n}", type=x["type"], domain=meta.get("domain"), title=x["title"],
                      status="draft", symptoms=x.get("symptoms"), extracted_from=pid, source=meta.get("source"),
                      license=meta.get("license", LICENSE))
            save(units.parent / "extracted" / x["type"] / f"{xm['id']}.md", xm, x["body"])
            stats["extracted"] += 1

    # Tone and style ist in Stufe 1 bereits geteilt und heisst dort rule-tone-and-style: Doppel vermeiden
    dup = units.parent / "canonical" / "rule-tone-and-style.md"
    if dup.exists() and "rule-tone-and-style" in rule_files:
        cm, _ = load(dup)
        rm, rb = load(rule_files["rule-tone-and-style"])
        rm["constrains"] = sorted(set(rm.get("constrains", [])) | set(cm["constrains"]))
        rm["canonical"] = True
        save(rule_files["rule-tone-and-style"], rm, rb)
        dup.unlink()
    print(" | ".join(f"{k} {v}" for k, v in stats.items()))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(*sys.argv[1:])
