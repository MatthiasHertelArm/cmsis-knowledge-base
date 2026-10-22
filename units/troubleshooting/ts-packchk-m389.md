---
id: "ts-packchk-m389"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M389: The component '…' (Line …) has dependency '…' : '…' that is resolved by the component itself."
status: "draft"
tool: "packchk"
severity: "warning"
code: "M389"
symptoms: ["M389", "The component '%NAME%' (Line %LINE%) has dependency '%EXPR%' : '%NAME2%' that is resolved by the component itself."]
symptom_regex: "^The component '.+?' \\(Line .+?\\) has dependency '.+?' : '.+?' that is resolved by the component itself\\.$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "packchk prints this warning when a component in the PDSC declares a dependency expression whose referenced component is provided by the component itself, so the dependency can never be resolved from outside the component."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"]
---

## Symptom

`M389`
`The component '%NAME%' (Line %LINE%) has dependency '%EXPR%' : '%NAME2%' that is resolved by the component itself.`

## Cause

packchk prints this warning when a component in the PDSC declares a dependency expression whose referenced component is provided by the component itself, so the dependency can never be resolved from outside the component. The %NAME% and %LINE% placeholders identify the component and its line in the PDSC, and %EXPR% and %NAME2% show the dependency expression and the component name it refers to. The exact trigger condition could not be checked because the source lines were not available, so this reading comes from the message text alone.

## Fix

Open the PDSC at the reported line and review the <require> or <deny> entry of the named component. Remove the self-referencing dependency, or change it so it refers to a component that other packs or the same pack actually provide, then rerun packchk.

## Note

The source trigger was not available, so the cause is inferred from the message wording. The README does not document this message. Verify the self-reference condition against the source before relying on the fix wording.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp`
