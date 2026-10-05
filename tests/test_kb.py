#!/usr/bin/env python3
"""Tests fuer build_index, kb_lib und kb_server. Aufruf: python tests/test_kb.py (aus kb/)."""
import asyncio, json, sqlite3, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from kb_lib import KB  # noqa: E402

FAIL = 0


def check(name, cond, info=""):
    global FAIL
    print(("ok   " if cond else "FAIL ") + name + (f"  [{info}]" if info and not cond else ""))
    FAIL += not cond


def build(db, extra=()):
    return subprocess.run([sys.executable, str(ROOT / "tools/build_index.py"), "--units",
                           str(ROOT / "tests/fixtures/units"), *extra, "--entities", str(ROOT / "build/entities"),
                           "--out", str(db), "--no-vec", "--strict"], capture_output=True, text=True)


with tempfile.TemporaryDirectory() as td:
    db = Path(td) / "t.db"
    r = build(db)
    check("strict build faellt bei stale applies_to mit Exit 2", r.returncode == 2, r.stdout[-300:])
    kb = KB(db, use_vec=False)
    unres = kb.db.execute("SELECT src,key,value FROM unresolved").fetchall()
    check("stale component erkannt", [tuple(u) for u in unres] == [("fx-stale", "component", "Nonexistent::Foo:Bar")], unres)
    q = "stack sizing pattern"
    ids = [x["id"] for x in kb.search(q)["results"]]
    check("ohne Kontext: spezifisch verdraengt generisch (refines)", "fx-m55" in ids and "fx-generic" not in ids, ids)
    m55 = kb.context_entities(device="AE722F80F55D5LS:M55_HE", compiler="AC6")
    check("Device-Kontext loest Core auf", "core:Cortex-M55" in m55, sorted(m55)[:8])
    ids = [x["id"] for x in kb.search(q, ctx=m55)["results"]]
    check("M55-Kontext: fx-m55 sichtbar", ids[:1] == ["fx-m55"], ids)
    m33 = kb.context_entities(device="STM32U585AIIx", compiler="GCC")
    ids = [x["id"] for x in kb.search(q, ctx=m33)["results"]]
    check("M33-Kontext: nur generische Einheit", "fx-m55" not in ids and "fx-generic" in ids, ids)
    m33ac6 = kb.context_entities(device="STM32U585AIIx", compiler="AC6")
    ids = [x["id"] for x in kb.search(q, ctx=m33ac6)["results"]]
    check("M33 + AC6: M55-Einheit bleibt draussen (UND ueber Dimensionen)", "fx-m55" not in ids and "fx-generic" in ids, ids)
    new = kb.context_entities(device="MYNEWCHIP_M55", compiler="AC6")
    r = kb.search(q, ctx=new)
    hit = [x for x in r["results"] if x["id"] == "fx-m55"]
    check("unbekanntes Device: Einheit bleibt, als unverified markiert", hit and hit[0].get("applies") == "unverified", r["results"])
    check("unbekanntes Device: generische Einheit bleibt daneben", "fx-generic" in [x["id"] for x in r["results"]], r["results"])
    check("unbekanntes Device wird gemeldet", r.get("context_unresolved") == ["device:MYNEWCHIP_M55"], r.get("context_unresolved"))
    # Lokales Overlay: DFP im Workspace und kb-entities.yml
    ws = ROOT / "tests/fixtures/workspace"
    cb200 = ws / "out/app/app.MYCHIP200.cbuild.yml"
    c = KB.parse_cbuild(cb200)
    before = kb.context_entities(c["device"], c["components"], c["compiler"])
    check("ohne Overlay: lokales Device unbekannt", "core:Cortex-M55" not in before)
    ov = kb.use_workspace(cb200)
    check("Overlay findet DFP und kb-entities.yml", ov["devices"] == 3 and len(ov["log"]) == 2, ov)
    after = kb.context_entities(c["device"], c["components"], c["compiler"])
    check("mit Overlay: Core und Familie aus lokalem PDSC", {"core:Cortex-M55", "family:MyVendor::MYCHIP Series"} <= after, sorted(after))
    r = kb.search(q, ctx=after)
    hit = [x for x in r["results"] if x["id"] == "fx-m55"]
    check("mit Overlay: M55-Einheit gilt sicher", hit and "applies" not in hit[0] and "context_unresolved" not in r, r)
    c300 = KB.parse_cbuild(ws / "out/app/app.MYCHIP300.cbuild.yml")
    ctx300 = kb.context_entities(c300["device"], c300["components"], c300["compiler"])
    check("Device nur mit Doku: Core aus kb-entities.yml", "core:Cortex-M55" in ctx300, sorted(ctx300))
    docs = [n for n in kb.expand("device:MYCHIP300", "documents")["neighbors"]]
    check("Device nur mit Doku: Referenzhandbuch verlinkt", docs and docs[0]["title"] == "MYCHIP300 Reference Manual (draft)", docs)
    check("manueller Core vorhanden", kb.get("core:Cortex-M99").get("type") == "core")
    check("Index-Datei unveraendert", sqlite3.connect(db).execute("SELECT count(*) FROM nodes WHERE id='device:MYCHIP200'").fetchone()[0] == 0)
    edge = kb.db.execute("SELECT qual FROM edges WHERE src='fx-m55' AND dst='toolchain:AC6'").fetchone()
    check("Versionsbereich als qual gespeichert", edge and json.loads(edge[0]) == {"range": ">=6.20"}, edge)
    check("knowledge_get liefert Body ungekuerzt", kb.get("fx-m55")["body"] == "stack sizing fixture body m55")

# Volle Datenbank, falls gebaut
full = ROOT / "build/knowledge.db"
if full.exists():
    kb = KB(full, use_vec=False)
    r = kb.search("board mounted device 'XYZ123' not found")["results"]
    check("exakter Fehlerstring trifft Troubleshooting zuerst", r and r[0]["id"] == "ts-csolution-board-mounted-device" and r[0]["exact_symptom"], r[:1])
    r = kb.search("error csolution: board mounted device STM32U585AIIx not found\nerror csolution: processing context 'app+U5' failed")["results"]
    check("echte Tool-Ausgabe mit Praefix und zwei Zeilen trifft exakt", r and r[0]["id"] == "ts-csolution-board-mounted-device" and r[0]["exact_symptom"], r[:1])
    r = [x["id"] for x in kb.search("M302")["results"]]
    check("M302 ist mehrdeutig (packchk und svdconv)", {"ts-packchk-m302", "ts-svdconv-m302"} <= set(r[:2]), r[:3])
    r = kb.search("M302", ctx=kb.context_entities(tools=["packchk"]))["results"]
    check("Tool-Kontext loest M302 auf", r and r[0]["id"] == "ts-packchk-m302", r[:1])
    proc = kb.get("proc-generate-debug-sequences")
    src = (ROOT / proc["meta"]["path"]).read_text()
    check("Procedure-Body vollstaendig", proc["body"].strip() == src.split("---\n", 2)[2].strip())
    r = kb.search("debug sequences", budget=300)
    check("Token-Budget eingehalten", r["budget_used"] <= 300 or len(r["results"]) == 1, r["budget_used"])

    async def mcp_roundtrip():
        from mcp.client.stdio import stdio_client, StdioServerParameters
        from mcp.client.session import ClientSession
        p = StdioServerParameters(command=sys.executable, args=[str(ROOT / "tools/kb_server.py"), str(full)],
                                  env={"KB_NO_VEC": "1"})
        async with stdio_client(p) as (rd, wr):
            async with ClientSession(rd, wr) as s:
                await s.initialize()
                tools = sorted(t.name for t in (await s.list_tools()).tools)
                res = await s.call_tool("knowledge_search", {"query": "No vendor tag found in the PDSC file"})
                return tools, json.loads(res.content[0].text)
    try:
        tools, res = asyncio.run(mcp_roundtrip())
        check("MCP: drei Tools", tools == ["knowledge_expand", "knowledge_get", "knowledge_search"], tools)
        check("MCP: Suche liefert Treffer", res["results"][0]["id"] == "ts-packchk-m302", res["results"][:1])
    except Exception as e:
        check("MCP-Roundtrip", False, repr(e))

print("\n" + ("ALLE TESTS OK" if not FAIL else f"{FAIL} FEHLER"))
sys.exit(1 if FAIL else 0)
