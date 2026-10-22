---
id: "ts-packchk-m384"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M384: Condition '…': Direct or indirect recursion detected. Skipping condition while searching for '…'."
status: "draft"
tool: "packchk"
severity: "error"
code: "M384"
symptoms: ["M384", "Condition '%NAME%': Direct or indirect recursion detected. Skipping condition while searching for '%NAME2%'."]
symptom_regex: "^Condition '.+?': Direct or indirect recursion detected\\. Skipping condition while searching for '.+?'\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Resolve recursion in condition _'NAME'_."
summary: "packchk resolves conditions by following the condition references in the PDSC, and it found a condition that refers back to itself, either directly or through a chain of other conditions. %NAME% is the condition where the cycle was detected …"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp (trigger not available in the clone; message text and README cause only)"]
---

## Symptom

`M384`
`Condition '%NAME%': Direct or indirect recursion detected. Skipping condition while searching for '%NAME2%'.`

## Cause

packchk resolves conditions by following the condition references in the PDSC, and it found a condition that refers back to itself, either directly or through a chain of other conditions. %NAME% is the condition where the cycle was detected and %NAME2% is the condition being searched for when the loop was hit; the tool skips that condition instead of evaluating it again.

## Fix

Open the PDSC and find the condition named in the message. Follow its <accept>/<require>/<deny> references and remove or break the reference that leads back to a condition already on the chain, so that the conditions form a tree rather than a loop. Then rerun packchk.

## Note

Derived from the message text and README cause only, because the source clone was not available; the exact recursion check and the reference elements it follows are not confirmed from the source.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp (trigger not available in the clone; message text and README cause only)`
