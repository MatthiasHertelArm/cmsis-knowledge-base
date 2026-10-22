---
id: "vela-vela-cli-options-supported-operator-report"
type: "concept"
domain: "edge-ai"
title: "Vela CLI Options: Command Line Interface / Supported Operator Report"
summary: "Generate the SUPPORTED_OPS.md file in the current working directory."
status: "draft"
collection: "ethos-u-vela"
source: "artificial-intelligence/ethos-u/ethos-u-vela@4bd6685:OPTIONS.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/4bd6685/OPTIONS.md#supported-operator-report"
license: "Apache-2.0"
mode: "V"
---

_Part of: Command Line Interface_

Generate the SUPPORTED_OPS.md file in the current working directory. Contains
a summary for TFLite operators which shows all the operators that can be placed
on the NPU, and what the constraints are for that operator to be scheduled on
the NPU. If the constraints are not met, then it will be scheduled on the CPU
instead. For TOSA operators fallback to the CPU is not allowed.  
This option can be used without the required Network argument.  
**Type: N/A**  
**Default: N/A**  

```bash
vela --supported-ops-report
```
