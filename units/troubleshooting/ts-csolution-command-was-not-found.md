---
id: "ts-csolution-command-was-not-found"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: <command> was not found"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["<command> was not found"]
symptom_regex: "^<command> was not found$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgr.cpp:407"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`<command> was not found`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (!m_rpcServer.Run()) {
```
