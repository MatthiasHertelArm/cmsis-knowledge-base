# Arbeitsstand 04.10.2026

Prototyp der Wissensbasis, gebaut gegen cmsis-skills@25c2085, devtools@30f5e81 und den Keil Pack-Index vom 04.10.2026. Alle Einheiten status: draft.

## Was läuft

| Baustein | Datei | Stand |
|---|---|---|
| Entity-Graph | tools/entities.py | 26.903 Entities aus 1.485 von 1.493 aktiven PDSC |
| Stufe 1 | tools/skill2ku.py | korrigiert, siehe Befunde |
| Stufe 2 | stage2/decompose_prompt.md (v2), tools/stage2_merge.py | an 4 Procedures getestet |
| Fehlerkatalog | tools/errcat.py | 397 Troubleshooting-Einheiten |
| Index | tools/build_index.py | knowledge.db, 26 MB, FTS5 + sqlite-vec + Kanten, --strict als CI-Gate |
| MCP-Server | tools/kb_server.py, tools/kb_lib.py | knowledge_search, knowledge_get, knowledge_expand |
| Tests | tests/test_kb.py | 15 von 15 grün, inkl. MCP-Roundtrip |

## Zahlen (Skriptläufe vom 04.10.2026)

| | Anzahl |
|---|---|
| Entities: Device / Component / DocSection / Pack / Subfamily / Family / Board / API / Core | 12.618 / 6.390 / 2.991 / 1.827 / 1.536 / 884 / 534 / 58 / 29 |
| Entity-Kanten part_of / has_core / documents / mounted_on / implements | 69.592 / 13.069 / 5.827 / 545 / 213 |
| Wissensknoten | 24 Procedures, 120 Rules, 8 Concepts, 1 Pattern, 397 Troubleshooting |
| Troubleshooting packchk / svdconv / csolution | 121 / 142 / 134 |
| davon mit Ursache und Fix aus README | 85 / 129 / 0 |
| Suche: Antwortgröße, Latenz | ca. 525 Token bei k = 5, 57 ms im Mittel, CPU |
| Alle 24 Procedure-Bodies zusammen | ca. 36.300 Token (Zeichen / 4) |
| Lint | 13 Procedures mit summary über 40 Wörtern (kommt aus description, Aufgabe von Stufe 2) |

## Befunde

1. **Stufe 1 hat Text verloren.** skill2ku.py hat Target & Persona und Validation Resources verworfen. Die 112 kB in 02 waren deshalb zu klein. Jetzt bleibt der ganze Skill-Body erhalten: 145 kB aus 154 kB SKILL.md (Rest ist Frontmatter). Die übrigen Zahlen in 02 sind bestätigt.
2. **Unbenannte Guardrails** bekamen leere Titel und IDs wie rule-unnamed-x-x-x. Titel jetzt aus den ersten Wörtern, IDs nummeriert.
3. **requires ist eigentlich "erwähnt".** check-pyocd-availability und pyocd-detect-debug-topology zeigen gegenseitig aufeinander. Stufe 2 sollte jede Erwähnung typisieren: requires, hands_off_to, see_also.
4. **Meldungsnummern kollidieren** zwischen Tools (M302 in packchk und svdconv). Der Tool-Kontext in knowledge_search löst das.
5. **csolution hat keine Meldungsdoku.** 134 Meldungen, nur Symptom und auslösende Bedingung aus dem Quelltext. Das ist die eigentliche Autorenarbeit im Pilot.
6. **Keine Entity für NPUs.** Ethos-U55/U85 stehen nicht als Core im PDSC. Edge-AI-Einheiten brauchen einen Entity-Typ accelerator.
7. **Gleiche Component-ID in vielen DFPs.** 6.390 IDs, 52k part_of Kanten zu Packs. applies_to auf Component ist deshalb grob, Device oder Family ist meist besser.
8. **PDSC-Download:** github raw ist aus der Sandbox gesperrt, keil.com/pack/<Vendor.Name>.pdsc spiegelt alle PDSC. 3 Geehy-PDSC sind kein gültiges XML.
9. **Dvendor trägt Enum-Suffix** ("STMicroelectronics:13"), wird beim Generieren entfernt.

## Stufe 2: Test

Zwei Durchläufe an add-cmsis-target, check-pyocd-availability, evaluate-ethos-u-variants, generate-debug-sequences.

| Befund v1 | Änderung v2 |
|---|---|
| Abschnitt "Validation" gibt es nicht | Quellen benannt: Validation-Schritt, dann Validation Resources |
| canonical_id frei erfunden | feste Liste kanonischer Regeln |
| applies_to leer trotz csolution, weil herstellerneutral | tool unabhängig von Neutralität |
| applies_to als Liste, Index erwartet Objekt | Objekt je Schlüssel, dazu unmapped |
| Felder bei specific unklar | leer vorgegeben |

Offen nach v2: Granularität von delta (Satz oder Fragment), Trigger bei langen "Use for"-Listen, Abgrenzung tool gegenüber aufgerufenen Skills.

**Vorschlag, nicht entschieden:** die fünf kanonischen Regeln rule-no-fabrication, rule-tone-and-style, rule-portability, rule-no-install, rule-user-confirmation. Die letzten beiden habe ich aus den Testläufen abgeleitet, sie brauchen deine Freigabe und einen von Hand geschriebenen Text.

## Nächste Schritte

1. Pilotdomäne entscheiden. Empfehlung bleibt Fehlerkatalog.
2. Stufe 2 v2 auf die übrigen 20 Procedures, danach Review.
3. csolution-Meldungen mit realen Fällen aus den Issue-Trackern verknüpfen. Braucht ein GitHub-Token (Search API).
4. Entity-Typ accelerator ergänzen.
5. Golden Set für den Pilot, Messung gegen die Skill-Baseline.
6. Schnittstelle zum Pack-Docs-System des CDA festlegen (DocSection-IDs teilen).

## Nachbauen

```bash
python tools/entities.py index.pidx pdsc/ build/entities
python tools/skill2ku.py cmsis-skills/generic-mcu-skills/skills units/skills
python tools/stage2_merge.py units/skills stage2/out_v2      # legt units/canonical und units/extracted an
python tools/errcat.py devtools units/troubleshooting
python tools/build_index.py --units units/skills --units units/canonical --units units/extracted \
  --units units/troubleshooting --entities build/entities --out build/knowledge.db
python tests/test_kb.py
python tools/kb_server.py build/knowledge.db                 # MCP über stdio, KB_NO_VEC=1 für nur BM25
```

## Nachtrag 04.10.2026

- **Fix Kontextfilter:** applies_to war ODER über alle Ziele. Eine Einheit für Cortex-M55 + AC6 erschien auch in M33-Projekten mit AC6. Jetzt UND über Dimensionen (core, toolchain, family ...), ODER innerhalb einer Dimension. 18 von 18 Tests grün.
- **Unbekanntes Device** (z. B. aus einem lokalen DFP): Einheiten mit Core- oder Familienbezug bleiben sichtbar, markiert als `applies: unverified`. Die Antwort meldet `context_unresolved`. Generische Einheiten werden daneben nicht verdrängt.
- **Entscheidung Matthias:** Neue Cores werden manuell als Entity gepflegt. Kein Architektur- oder declared-Mechanismus nötig.
- **Lokales Overlay gebaut (tools/overlay.py).** Für Devices, die nur Doku haben oder deren Pack erst im lokalen Repo entsteht. Quellen: `path:` unter packs in csolution.yml und cbuild.yml, alle *.pdsc im Workspace, `$CMSIS_PACK_ROOT/.Local/local_repository.pidx`, `kb-entities.yml` (im Workspace oder in .cmsis/). Der MCP-Server lädt das Overlay, sobald knowledge_search ein cbuild bekommt, und lädt neu, wenn sich PDSC oder kb-entities.yml ändern. Die Index-Datei bleibt unverändert (TEMP-Views). Laden 21 ms, Suche danach 11 bis 13 ms ohne Embeddings. Als CLI erzeugt overlay.py Entities für die CI eines Hersteller-Packs, build_index.py nimmt dafür mehrere `--entities` an. 27 von 27 Tests grün.
- **kb-entities.yml** ist auch der Ort für manuell gepflegte Cores (Entscheidung oben). Format siehe tests/fixtures/workspace/.cmsis/kb-entities.yml.
- Offen: Doku-Inhalte nur-Doku-Devices werden verlinkt, nicht indiziert. Volltext gehört ins Pack-Docs-System.
