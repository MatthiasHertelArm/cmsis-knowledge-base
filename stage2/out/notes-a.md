# Ambiguities in decompose_prompt.md (runs: generate-debug-sequences, check-pyocd-availability)
- Task 4 refers to a "Validation" section; neither input has one (sections are "Validation Resources" plus a "Validation" step inside Execution Steps). I used Validation Resources (and for pyocd also step 4). Neither contains explicit commands/expected output for proc 1, so verification is prose, not commands.
- Task 5: "generic" vs "specific" has no criteria. No-fabrication/no-mutation/etc. texts differ per procedure, so unclear whether they are generic with a delta or specific. I treated procedure-named content as specific.
- Task 5: canonical_id naming undefined. Only example is rule-no-fabrication; I invented rule-portability for the shared rule whose id is rule-portability-generate-debug-description. rule-tone-and-style is already shared and reused as its own canonical id.
- Task 5: unclear whether delta for the proc-1 no-fabrication rule is the enumerated behavior list or empty (generic rule text unknown to the model); I put the list in delta.
- Portability rule wording ("each") differs from the procedure body ("every"); Task 5 does not say which wins.
- Task 3: "portability says vendor-neutral" is not a literal field value; proc 1 "any existing DFP, do not assume family/probe/toolchain" was read as neutral (empty applies_to); proc 2 portability is OS-neutral only, so tool:pyocd was kept. VS Code/arm.vscode-cmsis-debugger has no entity ID.
- Task 2: proc 1 has "Use for", not "Use when"; triggers are paraphrased, which is mild improvisation.
- Task 5: for specific rules the output schema shows only generic fields; I omitted canonical_id/delta. Task 7 stop_conditions lacks a granularity rule (quote vs paraphrase); I quoted.
