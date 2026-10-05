1. "Use for ... after" triggers: unclear whether a long enumerated "Use for" list (reset, bootloader, flash in proc-generate-debug-sequences) should be split per item or kept; I picked 5 distinctive ones, dropping generic words like reset, flash.
2. Triggers are not "short user phrasings" when the description is a clause ("without installing, configuring, or modifying it"); the prompt does not say whether such negative constraints count as triggers.
3. applies_to.tool: unclear whether skills/helpers ($validate-pdsc-sequence-xml) or non-entity tools (code CLI) count. I left them out and used unmapped only for pack concepts; the prompt does not define what belongs in unmapped.
4. generic delta "wörtlich nur die Teile über den Kern": the boundary is subjective (e.g. no-mutation: core "install" vs. PATH/activate/settings); I returned fragments, not full sentences. No guidance on fragment vs sentence.
5. Rule id: the shared rule file for rule-portability has id rule-portability-generate-debug-description (not canonical); prompt does not say whether `id` must echo the file id or the canonical one. I echoed the file id.
6. Rules like "Scope" (".dbgconf needs explicit confirmation") overlap rule-user-confirmation but also contain specific content; "im Zweifel specific" applied, but a partial match is not covered.
7. Stop conditions: "Critical blockers" rule text and the body step overlap with confirmation/validation stops; unclear if rule text counts as a stop place or only Execution Steps.
8. verification: unclear whether to split compound sentences into separate entries or keep each sentence; I split at clause level, quoting verbatim fragments.
9. extracted: nothing met the bar; no criterion for what counts as reusable beyond "im Zweifel nichts".
