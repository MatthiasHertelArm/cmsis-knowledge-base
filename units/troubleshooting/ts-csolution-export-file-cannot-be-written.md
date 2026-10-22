---
id: "ts-csolution-export-file-cannot-be-written"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: export file cannot be written"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["export file cannot be written"]
symptom_regex: "^export file cannot be written$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgr.cpp:811"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "During convert, after the regular cprj for a context has been written, the tool also writes a non-locked export copy named <context name><export suffix>.cprj into that context's cprj directory."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:805-813", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:807-811"]
---

## Symptom

`export file cannot be written`

## Cause

During convert, after the regular cprj for a context has been written, the tool also writes a non-locked export copy named <context name><export suffix>.cprj into that context's cprj directory. This message is printed when GenerateCprj fails for that export path, so the file or its directory could not be written. The source does not show the underlying I/O error, so the exact reason (permissions, invalid path, full disk) is not visible from these lines.

## Fix

Check that the cprj output directory of the context is writable and that the export suffix yields a valid file name, then re-run the convert command. The source gives no other workaround; if the error persists, check the directory permissions and the path for the export file directly.

## Trigger in the source

```cpp
if (m_generator.GenerateCprj(*contextItem, exportfilename, true)) {
```

## Note

The regular cprj write failure at ProjMgr.cpp:802 prints a different message ("file cannot be written"). This export path is only reached when m_export is non-empty and m_cbuildgen is set. The README does not document this message.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgr.cpp:805-813`
- `tools/projmgr/src/ProjMgr.cpp:807-811`
