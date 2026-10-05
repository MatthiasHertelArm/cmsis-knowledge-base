---
id: "alp-visualizing-ethos-u-performance-3-executorch-workflow-executorch-in-three-steps"
type: "concept"
domain: "edge-ai"
title: "Visualize Ethos-U NPU performance with ExecuTorch on Arm FVPs: Understand the ExecuTorch workflow: ExecuTorch in three steps"
summary: "For more detail, see the ExecuTorch documentation."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/visualizing-ethos-u-performance/3-executorch-workflow.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/visualizing-ethos-u-performance/3-executorch-workflow/#executorch-in-three-steps"
license: "CC-BY-SA-4.0"
mode: "V"
---

ExecuTorch works in three main steps:

**Step 1: Export the model**

   - Convert a trained PyTorch model into an operator graph
   - Identify operators that can be offloaded to the Ethos-U NPU (for example, ReLU, conv, and quantize)

**Step 2: Compile with the AOT compiler**

   - Translate the operator graph into an optimized, quantized format
   - Use `--delegate` to move eligible operations to the Ethos-U accelerator
   - Save the compiled output as a `.pte` file

**Step 3: Deploy and run**

   - Execute the compiled model on an FVP or physical target
   - The Ethos-U NPU runs delegated operators - all others run on the Cortex-M CPU

For more detail, see the [ExecuTorch documentation](https://docs.pytorch.org/executorch/stable/intro-how-it-works.html).
