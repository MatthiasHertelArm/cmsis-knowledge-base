---
id: "etarm-introduction-functioning-of-a-system-with-an-ethos-u"
type: "concept"
domain: "edge-ai"
title: "Introduction: Functioning of a system with an Ethos-U"
summary: "A system with an Ethos-U and Cortex-M or Arm® Cortex®-A functions in the following way: - The CPU(Cortex-M or Cortex-A) dispatches an inference job to the Ethos-U NPU."
status: "draft"
collection: "executorch-arm"
source: "pytorch/executorch@24a6116:examples/arm/ethos-u-porting-guide.md"
doc_source: "https://github.com/pytorch/executorch/blob/24a6116/examples/arm/ethos-u-porting-guide.md#functioning-of-a-system-with-an-ethos-u"
license: "BSD-3-Clause"
mode: "V"
---

A system with an Ethos-U and Cortex-M or Arm® Cortex®-A functions in the following way:
- The CPU(Cortex-M or Cortex-A) dispatches an inference job to the Ethos-U NPU. The inference job is in the form of command stream - a sequence of instructions that the NPU
executes. The command stream is generated as part of the `to_edge_transform_and_lower` AoT compile stage. The command stream is embedded within the pte file and at runtime,
the pte file is stored in the memory of the SoC.
- The Ethos-U NPU autonomously reads the command stream from memory. When the NPU finishes processing the command stream, it raises an interrupt to the CPU to signal
that the inference job is complete. The CPU executes the interrupt handler and resumes its normal execution.

### Ethos-U memory regions
In order to allow this functioning, the Ethos-U driver defines the following regions that the NPU hardware will access:
- Ethos-U scratch buffer - a contiguous block of memory used by the NPU to store the intermediate tensors produced and consumed during inference. Applicable for any Ethos-U NPU.
- Neural Network - a contiguous block of memory holding constant data such as weights, biases, quantization parameters required to run an inference. Applicable for
any Ethos-U NPU.
- Ethos-U fast scratch buffer -  a contiguous block of memory for the case when the Ethos-U scratch buffer and Neural Network are both in the external memory.
Applicable only for Ethos-U65 and Ethos-U85 in Dedicated_Sram memory mode.

### Ethos-U driver
The key function of the Ethos-U driver enabling the interaction with the NPU is
(ethosu_invoke_v3)[https://github.com/pytorch/executorch/blob/main/backends/arm/runtime/EthosUBackend.cpp#L324]. The `ethosu_invoke_v3` function takes as input a driver handle,
a pointer towards  the command stream and the size of the command stream, base address as well as the size of the base addresses. For a system with Cortex-M, there is a 1:1
mapping between base pointer and region, so we will pass three base pointers and each base pointer will correspond to one region. Then, as part of the compilation stage
in `to_edge_transform_and_lower`, the Ethos-U compiler will generate command stream taking into account the three regions. In other words, at runtime, the ethos-U driver
knows the address of the command stream, its size, as well as the address for the locations in memory needed to store the intermediate tensors.
The Ethos-U driver will pass these address to the NPU and the NPU will issue memory requests to the on-chip or external memories in order to access the necessary data
(e.g. read weights, store an intermediate result into the scratch buffer, etc). The `backends/arm/runtime/EthosUBackend.cpp` already integrates the Ethos-U driver and it
already supports the three memory modes of the Ethos-U. Therefore, you should reuse `backends/arm/runtime/EthosUBackend.cpp` as is, without modifications.
The key question for any porting is how to initialize the NPU and
make sure it works. Let's analyse these questions in the following section.

**Note:** Interrupts work differently between Cortex-M and Cortex-A and a system with Cortex-A will use more base pointers and won't have a 1:1 mapping between Ethos-U
driver base pointer and Ethos-U region. The `backends/arm/runtime/EthosUBackend.cpp` is for a system with Cortex-M. Going forward, we assume we have a system with Cortex-M, similar to the Corstone platforms.
