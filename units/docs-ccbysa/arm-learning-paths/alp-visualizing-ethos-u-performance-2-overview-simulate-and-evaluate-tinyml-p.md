---
id: "alp-visualizing-ethos-u-performance-2-overview-simulate-and-evaluate-tinyml-p"
type: "concept"
domain: "edge-ai"
title: "Visualize Ethos-U NPU performance with ExecuTorch on Arm FVPs: Overview: Simulate and evaluate TinyML performance on Arm virtual hardware"
summary: "In this section, you’ll learn how TinyML, ExecuTorch, and Arm Fixed Virtual Platforms work together to simulate embedded AI workloads before hardware is available."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/visualizing-ethos-u-performance/2-overview.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/visualizing-ethos-u-performance/2-overview/#simulate-and-evaluate-tinyml-performance-on-arm-virtual-hardware"
license: "CC-BY-SA-4.0"
mode: "V"
---

In this section, you’ll learn how TinyML, ExecuTorch, and Arm Fixed Virtual Platforms work together to simulate embedded AI workloads before hardware is available.

Choosing the right hardware for your machine learning (ML) model starts with having the right tools. In many cases, you need to test and iterate before your target hardware is even available, especially when working with cutting-edge accelerators like the Ethos-U NPU.

Arm [Fixed Virtual Platforms](https://developer.arm.com/Tools%20and%20Software/Fixed%20Virtual%20Platforms) (FVPs) let you visualize and test model performance before any physical hardware is available.

 By simulating hardware behavior at the system level, FVPs allow you to:

- Benchmark inference speed and measure operator-level performance
- Identify which operations are delegated to the NPU and which execute on the CPU
- Validate end-to-end integration between components like ExecuTorch and Arm NN
- Iterate faster by debugging and optimizing your workload without relying on hardware

This makes FVPs a crucial tool for embedded ML workflows where precision, portability, and early validation matter.
