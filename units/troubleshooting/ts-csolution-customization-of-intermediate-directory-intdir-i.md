---
id: "ts-csolution-customization-of-intermediate-directory-intdir-i"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: customization of intermediate directory 'intdir' is ignored by the cbuild2cmake backend"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["customization of intermediate directory 'intdir' is ignored by the cbuild2cmake backend"]
symptom_regex: "^customization of intermediate directory 'intdir' is ignored by the cbuild2cmake backend$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:204"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The csolution.yml sets `output-dirs: intdir:`, which only the legacy `--cbuildgen` flow uses; the default cbuild2cmake backend ignores it."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:193-209", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/schemas/common.schema.json:356-370"]
---

## Symptom

`customization of intermediate directory 'intdir' is ignored by the cbuild2cmake backend`

## Cause

The csolution.yml sets `output-dirs: intdir:`, which only the legacy `--cbuildgen` flow uses; the default cbuild2cmake backend ignores it.

## Fix

Remove `intdir:` from output-dirs:; to move intermediate files, set `output-dirs: tmpdir: <path>` instead.

## Trigger in the source

```cpp
if (m_cbuild2cmake) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:193-209`
- `tools/projmgr/schemas/common.schema.json:356-370`
