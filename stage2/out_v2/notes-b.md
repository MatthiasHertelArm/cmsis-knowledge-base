# Remaining ambiguity in decompose_prompt v2 (runs: add-cmsis-target, evaluate-ethos-u-variants)
- verification: both a top-level "Validation" step and a "Validate the result" subsection exist; I used both, plus Validation Resources. Resources mixing real checks, tool self-tests (--help, negative tests) and bare command lists have no clear cut line.
- verification: "Run the script ... confirm four build directories" is a self-test of the runner or a success check? I counted it as a success check.
- generic delta: "only the parts beyond the core" is not clear for non-contiguous text; I used verbatim fragments, which can start mid-sentence.
- generic vs specific: user-choice (ask before copying/overwriting) vs rule-user-confirmation; I chose specific. rule-no-install says "without approval", but the Ethos-U rule forbids absolutely; I still mapped it generic.
- stop_conditions: "one entry per place" conflicts with the aggregate Critical blockers sentence, which also holds stops not named elsewhere; I kept it once. Fail-fast and "do not overwrite non-empty output dir" (Ethos-U) treated as duplicates or non-stops.
- triggers: add-cmsis-target yields only 2 fragments; fragments are not user-style phrasings.
- applies_to: tools that are only run for version checks (cbuild) still count as tool; non-entity items (Python 3, CMSIS-Toolbox) go to unmapped, no rule for skill dependencies like check-cmsis-environment.
- extracted: the "doubt means nothing" threshold is subjective; troubleshooting needs exact error strings, none exist in these inputs.
