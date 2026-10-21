# Projektanweisung: CDA Wissensbasis



## Ziel

Die Skill-basierte RAG-Story des CMSIS Developer Assistant (CDA) wird zu einer Wissensbasis mit Knowledge Graph ausgebaut. Sie ergänzt die CMSIS Pack Docs um domänenspezifisches Wissen: Optimierung, Test, Projektverwaltung, RTOS-Kernel, Fehlerkatalog und weitere Domänen.


## Feste Entscheidungen

- Pack Docs liefern das Was, die Wissensbasis das Wie, Wann und Warum.
- Join-Key zwischen beiden sind CMSIS-Entitäten aus PDSC und csolution.
- Wissenseinheiten sind Markdown mit Frontmatter in Git. Typen: Concept, Procedure, Rule, Pattern, Troubleshooting.
- Index: eine SQLite-Datei mit FTS5, sqlite-vec und Kantentabelle. Keine Graph-DB.
- Zugriff über wenige MCP-Tools: knowledge_search, knowledge_get, knowledge_expand.
- Bestehende Skills werden als ganze Procedure-Knoten übernommen und beim Retrieval nie gekürzt.
- Auslieferung als CMSIS Pack mit knowledge/ Ordner, damit Vendoren eigenes Wissen mitliefern können.
- Muss mit kleinen lokalen Modellen funktionieren: erst Summaries, Volltext nur auf Nachfrage.

## Arbeitsregeln

- Keine Fakten erfinden. Jede Wissenseinheit muss auf eine Quelle aus 04_quellenliste.md oder auf Matthias zurückführbar sein.
- Lizenzmodus der Quelle beachten: V Volltext, S eigene Summary plus Link, R nur Referenz.
- Neue Einheiten immer mit status: draft anlegen.
- Zahlen und Befunde aus 02_migration_und_befunde.md nicht fortschreiben, ohne das Skript neu laufen zu lassen.
- URLs und Dokumentnummern vor Verwendung prüfen. Mit * markierte Quellen sind ungeprüft.

## Stil

Deutsch, kurz, keine Gedankenstriche als Satzzeichen. Fachbegriffe und Bezeichner bleiben englisch.

## Dateien im Projektwissen

| Datei | Inhalt |
|---|---|
| 01_konzept_und_schema.md | Architektur, Knoten- und Kantentypen, Auflösungsregeln, SQL |
| 02_migration_und_befunde.md | Migrationspfad, Analyse der 24 Skills, offene Punkte |
| 03_wissensdomaenen.md | Themenlandkarte mit Priorität |
| 04_quellenliste.md | Quellen je Domäne mit Lizenz und Modus |
| skill2ku.py | Stufe 1 der Zerlegung, deterministisch |
| decompose_prompt.md | Stufe 2 der Zerlegung, LLM-Prompt, ungetestet |
