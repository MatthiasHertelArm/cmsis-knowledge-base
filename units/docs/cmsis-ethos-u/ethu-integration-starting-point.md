---
id: "ethu-integration-starting-point"
type: "concept"
domain: "edge-ai"
title: "Integration: Starting point"
summary: "The starting point is a pretrained, quantized ML model that meets the application's functional requirements. Before selecting a specific Edge AI MCU, compile the model with Vela for one or more Ethos-U reference systems as described in Compare Ethos-U configurations."
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@b2b641e:documentation/doxygen/integration/src/main.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/b2b641e/documentation/doxygen/integration/src/main.md#starting-point"
license: "Apache-2.0"
mode: "V"
---

The starting point is a pretrained, quantized ML model that meets the
application's functional requirements. Before selecting a specific Edge AI MCU,
compile the model with Vela for one or more Ethos-U reference systems as
described in
Compare Ethos-U configurations.

Vela reports operator placement and estimates memory use, bandwidth, and NPU
cycles. See Read the Vela reports.
Use these results for device selection, then validate with a device-specific
compile and measurements on the target hardware.

Some model zoos may provide corresponding performance and memory data for
Ethos-U-based systems. Confirm that the published configuration is relevant to
the candidate device before using those results.

### Determine the memory budget

Estimate the application's memory needs before selecting a device:

- Compile the ML model with the optimization strategy that matches the
  application requirements, and record the reported memory areas. Use
  `--optimise Size` to minimize memory use or `--optimise Performance` when
  performance is the priority and sufficient memory is available. See
  Vela memory mode parameters.
- Add runtime and application data, stacks, heaps,
  alignment, padding, and a safety margin.

After the application runs on the target, the remaining memory can be used to
tune performance. See Understand arena cache and spilling.
