---
id: "alp-visualizing-ethos-u-performance-3-executorch-workflow-a-visual-overview"
type: "concept"
domain: "edge-ai"
title: "Visualize Ethos-U NPU performance with ExecuTorch on Arm FVPs: Understand the ExecuTorch workflow: A visual overview"
summary: "The diagram below summarizes the ExecuTorch workflow from model export to deployment. It shows how a trained PyTorch model is transformed into an optimized, quantized format and deployed to a target system such as an Arm Fixed Virtual Platform (FVP)."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/visualizing-ethos-u-performance/3-executorch-workflow.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/visualizing-ethos-u-performance/3-executorch-workflow/#a-visual-overview"
license: "CC-BY-SA-4.0"
mode: "V"
---

The diagram below summarizes the ExecuTorch workflow from model export to deployment. It shows how a trained PyTorch model is transformed into an optimized, quantized format and deployed to a target system such as an Arm Fixed Virtual Platform (FVP).

- On the left, the model is exported into a graph of operators, with eligible layers flagged for NPU acceleration.
- In the center, the AOT compiler optimizes and delegates operations, producing a `.pte` file ready for deployment.
- On the right, the model is executed on embedded Arm hardware, where delegated operators run on the Ethos-U NPU, and the rest are handled by the Cortex-M CPU.

This three-step workflow ensures your TinyML models are performance-tuned and hardware-aware before deployment—even without access to physical silicon.

(figure: Diagram showing the three-step ExecuTorch workflow from model export to deployment#center)
