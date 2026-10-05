# Migration und Befunde

## Migrationspfad

1. **Inventur.** Alle Skills klassifizieren: reines Wissen, Workflow, Tool-Bindung, Router.
2. **Entity-Graph zuerst.** Aus dem Pack-Index generieren, Pack Docs als DocSection anhängen.
3. **Zerlegung per Skript.** Stufe 1 deterministisch (skill2ku.py), Stufe 2 per LLM (decompose_prompt.md). Danach menschliches Review, Status reviewed.
4. **Pilotdomäne.** Eine Domäne komplett, dazu das Golden Set. Vorschlag: Fehlerkatalog, weil am leichtesten zu befüllen und zu messen. Alternative: Optimierung.
5. **Parallelbetrieb.** Feature-Flag, Skills und Wissensbasis nebeneinander.
6. **Abschaltung.** Pro Skill erst Stub mit Verweis auf knowledge_search, dann löschen. Router bleiben.
7. **Betrieb.** CI-Lint, Owner pro Domäne, Index-Build bei jedem Pack-Release.

Schritt 2 und 3 lassen sich parallel starten.

## Analyse von Open-CMSIS-Pack/cmsis-skills (Stand 04.10.2026, main)

Alle 24 Skills folgen exakt dem Template mit sechs Abschnitten: Target & Persona, Prerequisites & Context, Execution Steps, Guardrails & Constraints, Expected Output, Validation Resources.

Ergebnis von skill2ku.py:

| | Anzahl |
|---|---|
| Procedures | 24 |
| Concepts (aus references/) | 7 |
| Artifacts (.agent-artifacts/) | 6 |
| DocSections (verlinkte URLs) | 17 |
| Guardrails roh | 147 |
| Rule-Knoten nach Text-Dedup | 117 |
| requires Kanten | 45 |
| produces / consumes Kanten | 3 / 10 |

Größe: 154 kB SKILL.md ergeben 145 kB Procedure-Bodies (Lauf 04.10.2026 mit korrigiertem skill2ku.py, der ganze Skill-Body bleibt erhalten; die früheren 112 kB fehlten Target & Persona und Validation Resources, siehe 05_arbeitsstand.md).

## Folgerungen

- Die Skills sind fast reine Workflows mit Stop-Bedingungen und Nutzerfreigaben. Sie werden als ganze Procedure-Knoten übernommen.
- Der Abhängigkeitsgraph ist der eigentliche Gewinn. Die 45 requires Kanten stehen heute als Fließtext in den Skills.
- Guardrails lassen sich per Textvergleich kaum deduplizieren. "No fabrication" steht in 23 Skills, jedes Mal mit eigener Aufzählung. Nur "Tone and style" fällt sauber zusammen. Die Trennung in kanonische Regel plus refines-Delta ist Aufgabe von Stufe 2.
- Die Token-Ersparnis kommt aus den Summaries als erster Retrieval-Stufe, nicht aus dem Volltext.
- Die Wissensbasis verlinkt die bestehenden Skills eher, als dass sie sie ersetzt. Der neue Inhalt sind die Domänen in 03_wissensdomaenen.md. Im Repo gibt es dazu bisher nur evaluate-ethos-u-variants und create-csolution-github-action.

## Kontext zum CDA

- Die Erweiterung vendort cmsis-skills unter skills/cmsis-skills/ und installiert sie als AI Skills Pack mit den Routern cmsis-project, cmsis-bring-up, cmsis-pack.
- Es gibt ein experimentelles Pack-Docs-System (Einstellung packDocs.enabled) mit dem Skill cmsis-pack-docs. Daran muss die Wissensbasis andocken.
- Eigene Guides des CDA: debug_instructions, cmsis-embedded-guide, troubleshooting. Kandidaten für die ersten Knoten.

## Offene Punkte

- Stufe 2 ist nicht ausgeführt, der Prompt ist ungetestet.
- Die Entity-Liste aus dem Pack-Index existiert noch nicht. applies_to hängt davon ab.
- Rechteklärung für Arm-Dokumente und die Keil Knowledge Base (intern, Export statt Crawl).
- Arm Learning Paths: Text unter CC BY-SA 4.0. Getrennt vom Apache-2.0 Pack halten, mit Rechtsabteilung klären.
- Schnittstelle zum bestehenden Pack-Docs-System des CDA festlegen.
- Pilotdomäne entscheiden.
