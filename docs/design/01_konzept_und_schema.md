# Konzept und Schema

## Kernidee

Pack Docs liefern das Was (API, Parameter, Device-Fakten). Die Wissensbasis liefert das Wie, Wann und Warum. Verbunden werden beide über gemeinsame CMSIS-Entitäten als Join-Key.

## Zwei Knotenklassen

**Entity-Knoten** werden generiert, nie von Hand gepflegt. Quelle: Pack-Index, PDSC, csolution.
Typen: Pack, Device, Board, Core, Component, API, Toolchain, DocSection, Artifact.

**Knowledge-Knoten** sind redaktionell.
Gemeinsame Felder: id, type, domain, title, summary (max. 40 Wörter, erste Retrieval-Stufe), body, status (draft/reviewed), owner, updated.

| Typ | Zusatzfelder |
|---|---|
| Concept | definition |
| Procedure | preconditions, steps, verification, tools, stop_conditions, output |
| Rule | severity (must/should), rationale, optional check |
| Pattern | problem, solution, tradeoffs |
| Troubleshooting | symptoms (Fehlerstrings/Regex), cause, fix |

verification lässt den Agenten seinen Erfolg selbst prüfen. symptoms trifft Fehlermeldungen exakt über BM25.

## Beispiel Frontmatter

```yaml
id: opt-lto-armclang
type: procedure
domain: optimization
applies_to:
  compiler: [AC6]
  component: ["CMSIS:CORE"]
  core: [Cortex-M55, Cortex-M85]
requires: [concept-link-time-opt]
refs: ["pack://ARM.CMSIS/docs/Core/..."]
```

## Kanten

| Kante | Von nach | Quelle |
|---|---|---|
| part_of | Device nach Pack, API nach Component usw. | generiert |
| documents | DocSection nach Entity | generiert |
| applies_to | Knowledge nach Entity, mit Versionsbereich | Frontmatter |
| references | Knowledge nach DocSection | Frontmatter |
| requires | Knowledge nach Knowledge | Frontmatter |
| refines | Knowledge nach Knowledge, spezifisch vor allgemein | Frontmatter |
| conflicts_with | Rule/Pattern zu Rule/Pattern | Frontmatter |
| supersedes | Knowledge nach Knowledge | Frontmatter |
| constrains | Rule nach Procedure | aus Skill-Guardrails |
| produces | Procedure nach Artifact | aus Skills (Owned artifact) |
| consumes | Procedure nach Artifact | aus Skills |

produces und consumes kamen erst aus der Analyse der echten Skills dazu: Bring-up- und Pack-Skills übergeben Ergebnisse über Dateien in .agent-artifacts/.

## Auflösungsregeln

- Leeres applies_to heißt universell gültig.
- Geltung vererbt sich entlang part_of: eine Einheit für eine Device-Familie gilt für alle Devices darunter.
- Treffen mehrere Einheiten, gewinnt die spezifischere über refines.
- Lässt sich ein applies_to nach einem Pack-Update nicht mehr auflösen, schlägt die CI fehl. Das ist die Stale-Erkennung.

## Speicher

```sql
CREATE TABLE nodes(id TEXT PRIMARY KEY, kind TEXT, type TEXT,
  domain TEXT, title TEXT, summary TEXT, body TEXT, meta JSON);
CREATE TABLE edges(src TEXT, rel TEXT, dst TEXT, qual JSON,
  PRIMARY KEY(src, rel, dst));
CREATE VIRTUAL TABLE nodes_fts USING fts5(title, summary, body, symptoms);
CREATE VIRTUAL TABLE nodes_vec USING vec0(embedding FLOAT[384]);
```

Hybrid und lokal lauffähig: BM25 plus Embeddings plus Kantentabelle. Kleines Embedding-Modell (bge-small oder nomic-embed).

## Retrieval über MCP

- knowledge_search(query, domain?): filtert zuerst nach Projektkontext aus cbuild.yml (Device, Komponenten, Compiler), dann Hybrid-Suche und Rerank.
- knowledge_get(id): volle Einheit.
- knowledge_expand(id, relation): ein Hop zu Voraussetzungen und zugehörigen Pack-Doc-Abschnitten.

Antworten mit Token-Budget: erst Summaries, Volltext nur auf Nachfrage. Procedures werden nie gekürzt.

## Was von Skills bleibt

Zwei bis drei dünne Router-Skills, die nur sagen, wann welches Tool zu rufen ist.

## Pipeline und Auslieferung

CI prüft das Frontmatter, löst Entity-Referenzen gegen den Pack-Index auf, baut Embeddings und das Index-Artefakt. Auslieferung als CMSIS Pack mit knowledge/ Ordner. Der CDA indiziert beim Pack-Install mit.

## Governance

Ein Maintainer je Domäne nach Vorbild des Linux-Kernels, dazu ein MAINTAINERS File, das die CI für Reviews auswertet.

## Evaluation

Golden Set mit 50 bis 100 realen Fragen je Domäne. Recall@k und Tokenverbrauch gegen die heutige Skill-Baseline messen.
