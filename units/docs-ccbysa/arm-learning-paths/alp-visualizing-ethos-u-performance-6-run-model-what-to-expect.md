---
id: "alp-visualizing-ethos-u-performance-6-run-model-what-to-expect"
type: "concept"
domain: "edge-ai"
title: "Visualize Ethos-U NPU performance with ExecuTorch on Arm FVPs: Deploy and run Mobilenet V2 on the Corstone-320 FVP: What to expect"
summary: "A high number of delegated nodes means the majority of model execution was successfully offloaded to the Ethos-U NPU for acceleration. This confirms that the model was successfully compiled, deployed, and run with NPU acceleration."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/visualizing-ethos-u-performance/6-run-model.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/visualizing-ethos-u-performance/6-run-model/#what-to-expect"
license: "CC-BY-SA-4.0"
mode: "V"
---

ExecuTorch will:

- Compile the PyTorch model to .pte format
- Generate intermediate files (YAMLs, graphs, etc.)
- Run the compiled model on the FVP
- Output execution timing, operator delegation, and performance stats

You should see output like:

```bash
Batch Inference time     4.94 ms,  202.34 inferences/s
Total delegated subgraphs: 1
Number of delegated nodes: 419
```

A high number of delegated nodes means the majority of model execution was successfully offloaded to the Ethos-U NPU for acceleration. This confirms that the model was successfully compiled, deployed, and run with NPU acceleration.
