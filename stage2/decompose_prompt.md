# Stufe 2: Verfeinerung der Wissenseinheiten (LLM)

Version 2, 04.10.2026. Getestet an 4 Procedures (add-cmsis-target, check-pyocd-availability,
evaluate-ethos-u-variants, generate-debug-sequences). Änderungen gegenüber v1 am Ende.

Eingabe je Lauf: eine Procedure-Datei aus Stufe 1 (Frontmatter plus vollständiger Skill-Body),
alle Rule-Dateien, die sie per `constrains` betreffen, die Liste gültiger Entity-IDs und die
Liste kanonischer Regeln (unten). Ausgabe: ein JSON-Objekt, sonst nichts.

## System

You refine knowledge units for the CMSIS Developer Assistant knowledge base.
You never add facts. Every field you write must be traceable to the input text.
If the input does not state something, leave the field empty.

## Kanonische Regeln

Nur diese IDs sind als `canonical_id` erlaubt. Neue kanonische Regeln legt ein Mensch an.

| canonical_id | Kern |
|---|---|
| rule-no-fabrication | Keine erfundenen Werte, Pfade, Versionen, Adressen oder Ergebnisse |
| rule-tone-and-style | Ton und Stil der Ausgabe |
| rule-portability | Herstellerneutral, keine Annahmen über Familie, Probe, Toolchain |
| rule-no-install | Nichts installieren oder Umgebung verändern ohne Freigabe |
| rule-user-confirmation | Änderungen an Dateien erst nach ausdrücklicher Nutzerfreigabe |

## Aufgaben

1. **summary**: höchstens 40 Wörter, was die Procedure erreicht. Kein "Use when".
2. **triggers**: 2 bis 5 kurze Nutzerformulierungen aus dem Teil der `description`, der
   beschreibt, wann die Procedure gilt ("Use when", "Use for", "Use after"). Gleiche Wörter
   wie im Text verwenden, nicht frei umschreiben. Sie gehen in den BM25-Index.
3. **applies_to**: Objekt mit Schlüsseln `tool`, `toolchain`, `core`, `component`, `api`.
   Werte nur aus der Entity-Liste, ohne Präfix (`tool:pyocd` wird zu `"tool": ["pyocd"]`).
   - `tool`: jedes Werkzeug, das die Procedure ausführt (z. B. csolution, cpackget, pyocd, vela).
     Herstellerneutralität ändert daran nichts.
   - `toolchain`, `core`, `component`, `api`: nur wenn der Text sie ausdrücklich als
     Voraussetzung nennt. Steht in `portability`, dass die Procedure herstellerneutral ist,
     bleiben `core` und `component` leer.
   - Nennt der Text etwas, für das es keine Entity gibt, kommt es in `unmapped` (Freitext).
4. **verification**: wie der Agent den Erfolg prüft. Quellen in dieser Reihenfolge: der Schritt
   in "Execution Steps", der "Validation" oder "Validate" heißt, dann der Abschnitt
   "Validation Resources". Befehle und erwartete Ergebnisse wörtlich. Selbsttests des Tools
   oder Doku-Links gehören nicht dazu.
5. **rules**: für jede Rule-Datei genau ein Eintrag.
   - `generic`: der Kern entspricht einer kanonischen Regel aus der Tabelle. Dann
     `canonical_id` setzen und in `delta` wörtlich nur die Teile, die über den Kern hinausgehen
     (z. B. die Aufzählung, was nicht erfunden werden darf). Ist nichts darüber hinaus, bleibt
     `delta` leer.
   - `specific`: kein kanonischer Kern. Dann `canonical_id` und `delta` leer lassen.
   Im Zweifel `specific`.
6. **extracted**: Wissen im Body, das außerhalb dieser Procedure wiederverwendbar ist.
   Je Fund: `type` (concept | pattern | troubleshooting), `title`, `body` (wörtlich, nur
   Platzhalter dürfen bleiben), bei troubleshooting zusätzlich `symptoms` (exakte
   Fehlerstrings des Tools, keine Statuswerte anderer Skills). Höchstens 5 je Procedure.
   Im Zweifel nichts extrahieren.
7. **stop_conditions**: jede Stelle, an der die Procedure anhält oder den Nutzer fragt.
   Ein Eintrag je Stelle, wörtlich, ohne Zusammenfassungen derselben Stellen.

## Ausgabeformat

```json
{
  "id": "proc-...",
  "summary": "",
  "triggers": [],
  "applies_to": {"tool": [], "toolchain": [], "core": [], "component": [], "api": []},
  "unmapped": [],
  "verification": [],
  "stop_conditions": [],
  "rules": [
    {"id": "rule-...", "class": "generic", "canonical_id": "rule-no-fabrication", "delta": ""},
    {"id": "rule-...", "class": "specific", "canonical_id": "", "delta": ""}
  ],
  "extracted": [
    {"type": "troubleshooting", "title": "", "symptoms": [], "body": ""}
  ]
}
```

## Nach dem Lauf (Skript stage2_merge.py, kein LLM)

- summary, triggers, applies_to, verification, stop_conditions ins Frontmatter der Procedure.
  Der Body bleibt unverändert.
- `generic` mit leerem `delta`: die procedure-spezifische Rule entfällt, die Kante
  `constrains` geht an die kanonische Regel.
- `generic` mit `delta`: Rule bleibt, bekommt `refines: [canonical_id]`.
- Den Text der kanonischen Regeln schreibt ein Mensch einmal, nicht das Modell.
- `extracted` landet als Draft unter `units/extracted/`, Dedup per Embedding folgt.
- Jede Einheit bleibt `status: draft` bis zum Review durch den Domain-Owner.

## Änderungen gegenüber v1

| Befund im Test | Änderung |
|---|---|
| Abschnitt "Validation" existiert nicht | Quellen für verification benannt |
| canonical_id frei erfunden (rule-portability) | feste Liste kanonischer Regeln |
| applies_to leer trotz csolution, cpackget, weil herstellerneutral | tool unabhängig von Neutralität |
| applies_to als Liste, Index erwartet Objekt | Objekt je Schlüssel, dazu unmapped |
| Felder für specific unklar | leere Felder vorgegeben |
| "Use for" statt "Use when" | alle Varianten genannt |
| stop_conditions doppelt (einzeln und zusammengefasst) | ein Eintrag je Stelle |
