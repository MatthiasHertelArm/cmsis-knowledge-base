---
id: "ethu-zephyr-verification-checklist"
type: "concept"
domain: "edge-ai"
title: "Zephyr: Verification checklist"
summary: "Zephyr: Verification checklist"
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@cf13d8d:documentation/doxygen/zephyr/src/main.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/cf13d8d/documentation/doxygen/zephyr/src/main.md#verification-checklist"
license: "Apache-2.0"
mode: "V"
---

- Confirm the build uses the intended board and devicetree node has
  `status = "okay"`.
- Confirm `CONFIG_TENSORFLOW_LITE_MICRO=y` and `CONFIG_ETHOS_U=y` in the final
  Zephyr configuration.
- Confirm the Vela target, system configuration, and memory mode match the
  physical NPU and devicetree memory mapping.
- Confirm the NPU interrupt is delivered and the driver completes an inference.
- Compare inference output against a known-good input before measuring
  performance.
- Measure stack, heap, tensor-arena, model, and optional spill-cache use on the
  final target.
