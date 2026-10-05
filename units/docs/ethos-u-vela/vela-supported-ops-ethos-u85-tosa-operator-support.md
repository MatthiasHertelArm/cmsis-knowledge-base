---
id: "vela-supported-ops-ethos-u85-tosa-operator-support"
type: "concept"
domain: "edge-ai"
title: "Supported Ops: Ethos-U85 TOSA Operator Support"
summary: "This section summarizes TOSA support for Ethos-U85 against the v1.0 PRO-INT 8k baseline."
status: "draft"
collection: "ethos-u-vela"
source: "artificial-intelligence/ethos-u/ethos-u-vela@eb9cf0d:SUPPORTED_OPS.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/eb9cf0d/SUPPORTED_OPS.md#ethos-u85-tosa-operator-support"
license: "Apache-2.0"
mode: "V"
---

This section summarizes TOSA support for Ethos-U85 against the v1.0 PRO-INT 8k baseline.

- Baseline:
  - TOSA Version: v1.0
  - TOSA Profile: PRO-INT
  - TOSA Level: 8k
- Supported extensions:
  - EXT-INT16
  - EXT-INT4
  - EXT-DOUBLEROUND
  - EXT-CONTROLFLOW (experimental)
- Unsupported operators:
  - TRANSPOSE_CONV2D with dynamic weights and/or bias
  - CONV3D with dynamic weights and/or bias
