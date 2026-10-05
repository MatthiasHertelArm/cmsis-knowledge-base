---
id: "ethu-general-deployment-lifecycle"
type: "concept"
domain: "edge-ai"
title: "General: Deployment lifecycle"
summary: "The detailed procedure and required evidence are in Integration. The Vela compiler's estimates are useful for comparison but do not replace measurements on the target."
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@b2b641e:documentation/doxygen/general/src/main.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/b2b641e/documentation/doxygen/general/src/main.md#deployment-lifecycle"
license: "Apache-2.0"
mode: "V"
---

1. Select the device and CMSIS-Toolbox build context. Use its DFP when the pack
   provides the required Ethos-U resources.
2. Select a quantized ML model and ML inference runtime, and supply
   the matching `vela.ini`, linker, and driver configuration.
3. Compile for size to establish the model-controlled memory floor.
4. Reserve memory for the ML inference runtime and application, then use the
   remaining budget to compile performance candidates.
5. Place model artifacts and buffers with the linker and configure the driver
   to match the same memory mapping.
6. Implement target hooks for interrupts, cache maintenance, address remapping,
   and RTOS synchronization as needed.
7. Validate correctness with a small known-good ML model. Then measure the
   production ML model on hardware and tune the system based on those results.

The detailed procedure and required evidence are in
Integration. The Vela compiler's estimates are
useful for comparison but do not replace measurements on the target.
