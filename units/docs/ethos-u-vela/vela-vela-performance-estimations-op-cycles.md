---
id: "vela-vela-performance-estimations-op-cycles"
type: "concept"
domain: "edge-ai"
title: "Vela Performance Estimations: Op Cycles"
summary: "Shows the total cycle estimation for the operator in terms of cycles and as a fraction (%) of the estimated total cycles of the entire network."
status: "draft"
collection: "ethos-u-vela"
source: "artificial-intelligence/ethos-u/ethos-u-vela@4bd6685:PERFORMANCE.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/4bd6685/PERFORMANCE.md#op-cycles"
license: "Apache-2.0"
mode: "V"
---

Shows the total cycle estimation for the operator in terms of cycles and as a
fraction (%) of the estimated total cycles of the entire network.

The cycle counts are then broken down into NPU, SRAM AC, DRAM AC, OnFlash AC
and OffFlashAC:

### NPU

The estimated number of total cycles for the entire NPU.

### SRAM AC, DRAM AC, OnFlash AC, OffFlash AC

Estimated number of Access cycles for respective memory
