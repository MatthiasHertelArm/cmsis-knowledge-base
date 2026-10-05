---
id: "vela-supported-ops-ethos-u55-and-ethos-u65-tosa-generic-con"
type: "concept"
domain: "edge-ai"
title: "Supported Ops: Ethos-U55 and Ethos-U65 TOSA Generic Constraints"
summary: "This is a list of constraints that most TOSA operators must satisfy in order to be scheduled on the NPU."
status: "draft"
collection: "ethos-u-vela"
source: "artificial-intelligence/ethos-u/ethos-u-vela@eb9cf0d:SUPPORTED_OPS.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/eb9cf0d/SUPPORTED_OPS.md#ethos-u55-and-ethos-u65-tosa-generic-constraints"
license: "Apache-2.0"
mode: "V"
---

This is a list of constraints that most TOSA operators must satisfy in order to be scheduled on the NPU.

- Baseline:
  - TOSA Version: v1.0
  - TOSA Profile: PRO-INT
  - TOSA Level: 8k
- PRO-INT extensions:
  - EXT-INT16: 16-bit integer operations
  - EXT-INT4: 4-bit integer weights
  - EXT-DOUBLEROUND: double rounding support for RESCALE
- Operators and configurations not listed as supported below are not supported.
- For TOSA operators, CPU fallback is not supported.
