---
id: "alp-visualizing-ethos-u-performance-3-executorch-workflow-overview"
type: "concept"
domain: "edge-ai"
title: "Visualize Ethos-U NPU performance with ExecuTorch on Arm FVPs: Understand the ExecuTorch workflow: Overview"
summary: "Before setting up your environment, it helps to understand how ExecuTorch processes a model and runs it on Arm-based hardware. ExecuTorch uses ahead-of-time (AOT) compilation to transform PyTorch models into optimized operator graphs that run efficiently on resource-constrained systems."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/visualizing-ethos-u-performance/3-executorch-workflow.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/visualizing-ethos-u-performance/3-executorch-workflow/#overview"
license: "CC-BY-SA-4.0"
mode: "V"
---

Before setting up your environment, it helps to understand how ExecuTorch processes a model and runs it on Arm-based hardware. ExecuTorch uses ahead-of-time (AOT) compilation to transform PyTorch models into optimized operator graphs that run efficiently on resource-constrained systems. The workflow supports hybrid execution across CPU and NPU cores, allowing you to profile, debug, and deploy TinyML workloads with low runtime overhead and high portability across Arm microcontrollers.
