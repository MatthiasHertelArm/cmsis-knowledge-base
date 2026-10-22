---
id: "cda-embedded-debugging-troubleshooting-fault-analysis-quick-reference"
type: "concept"
domain: "debug"
title: "Embedded Debugging Troubleshooting: Fault Analysis Quick Reference"
summary: "Embedded Debugging Troubleshooting: Fault Analysis Quick Reference"
status: "draft"
collection: "cda-guides"
source: "Open-CMSIS-Pack/CMSIS-Developer-Assistant@29d444c:docs/agent-resources/troubleshooting/embedded.md"
doc_source: "https://github.com/Open-CMSIS-Pack/CMSIS-Developer-Assistant/blob/29d444c/docs/agent-resources/troubleshooting/embedded.md#fault-analysis-quick-reference"
license: "Apache-2.0"
mode: "V"
---

| Fault Bit | Register | Meaning |
|---|---|---|
| FORCED | HFSR | Fault escalated to HardFault — check CFSR |
| DACCVIOL | MMFSR | Data access violation (null ptr, MPU) |
| IACCVIOL | MMFSR | Instruction access violation |
| PRECISERR | BFSR | Precise bus error — check BFAR for address |
| IMPRECISERR | BFSR | Imprecise bus error (buffered write) |
| UNDEFINSTR | UFSR | Undefined instruction |
| INVSTATE | UFSR | Invalid EPSR.T bit (tried ARM mode) |
| NOCP | UFSR | Coprocessor not enabled (FPU?) |
| DIVBYZERO | UFSR | Division by zero |
| UNALIGNED | UFSR | Unaligned access |
