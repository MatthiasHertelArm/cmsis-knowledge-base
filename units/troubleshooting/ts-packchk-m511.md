---
id: "ts-packchk-m511"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M511: Xerxes reports: …"
status: "draft"
tool: "packchk"
severity: "error"
code: "M511"
symptoms: ["M511", "Xerxes reports: %MSG%"]
symptom_regex: "^Xerxes reports: .+?$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "The message is a generic wrapper: packchk prints M511 with %MSG% filled in by the text of an error reported by the Xerxes checker, so the text after the bar is the real reason."
cause_origin: "source-analysis"
confidence: "low"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"]
---

## Symptom

`M511`
`Xerxes reports: %MSG%`

## Cause

The message is a generic wrapper: packchk prints M511 with %MSG% filled in by the text of an error reported by the Xerxes checker, so the text after the bar is the real reason. Without the source lines the exact trigger cannot be confirmed, so the cause is only what the message format suggests: a pack-content check failed and Xerxes reported the specific problem in %MSG%.

## Fix

Read the Xerxes text that follows 'Xerxes reports:' in the build log and correct the pack file or content it names, then rerun packchk on the pack. Since the trigger is not available here, no further fix can be stated with confidence.

## Note

Clone not available; the trigger line was not inspected, so the cause is inferred from the message text only and is not confirmed from source. Confidence capped at medium by the task, set to low because the trigger was not seen. The README does not document M511.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence low, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp`
