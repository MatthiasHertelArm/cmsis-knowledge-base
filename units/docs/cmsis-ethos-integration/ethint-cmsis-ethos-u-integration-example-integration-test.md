---
id: "ethint-cmsis-ethos-u-integration-example-integration-test"
type: "concept"
domain: "edge-ai"
title: "CMSIS Ethos-U integration example: Integration Test"
summary: "The test runner is simple. It supports ML model with one int8 input, one int8 output, and full Ethos-U offload."
status: "draft"
collection: "cmsis-ethos-integration"
source: "Arm-Examples/CMSIS-Ethos-Integration@9b906f5:README.md"
doc_source: "https://github.com/Arm-Examples/CMSIS-Ethos-Integration/blob/9b906f5/README.md#integration-test"
license: "Apache-2.0"
mode: "V"
---

The test runner is simple. It supports ML model with
**one int8 input, one int8 output, and full Ethos-U offload**.

- `TestModel_Int8()` runs the model, checks every output value against its
  tolerance, optionally checks the winning class, and records a PASS/FAIL result.

A model's `PASS` result confirms that inference executed successfully through
Ethos-U and matched its reference within the configured tolerance on the target
being tested.

Tests run sequentially and reuse a 64 KiB, 16-byte-aligned tensor arena in
`Source/model_test.cpp`. Board linker files place the model and arena in
NPU-accessible memory.
