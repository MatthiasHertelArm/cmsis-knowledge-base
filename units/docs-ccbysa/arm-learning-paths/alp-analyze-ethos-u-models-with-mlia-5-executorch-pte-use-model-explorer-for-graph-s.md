---
id: "alp-analyze-ethos-u-models-with-mlia-5-executorch-pte-use-model-explorer-for-graph-s"
type: "concept"
domain: "edge-ai"
title: "Analyze machine learning models for Arm Ethos-U with Arm ML Inference Advisor: Analyze ExecuTorch artifacts with MLIA and Corstone: Use Model Explorer for graph"
summary: "You've used MLIA with LiteRT, TOSA, and ExecuTorch .pte artifacts. MLIA answers target-aware questions about compatibility, estimated performance, runtime counters, and advice."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/analyze-ethos-u-models-with-mlia/5-executorch-pte.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/analyze-ethos-u-models-with-mlia/5-executorch-pte/#use-model-explorer-for-graph-structure"
license: "CC-BY-SA-4.0"
mode: "V"
---

You've used MLIA with LiteRT, TOSA, and ExecuTorch `.pte` artifacts. MLIA answers target-aware questions about compatibility, estimated performance, runtime counters, and advice. To see how these artifacts can be visualized as graphs in Model Explorer, continue with the [Explore model artifacts with Model Explorer](https://learn.arm.com/learning-paths/cross-platform/explore-model-artifacts-with-model-explorer/) Learning Path. You'll use many of the same files from the model artifacts repository.

Model Explorer can open some formats directly, while other formats use adapters. Use Model Explorer alongside MLIA when you want to connect target advice with the graph structure that produced it.

In the earlier example, Ethos-U85 is expected to perform better due to its platform differences. The model also delegates differently for Ethos-U85 compared to Ethos-U55.

The model pattern is:

```output
convolution / activation
conditional select
convolution / activation / convolution
```

On Ethos-U55, the conditional select part isn't kept inside the Ethos-U delegate path. The partitioning is as follows:

```output
EthosUBackend region
aten::gt / aten::where outside delegate
EthosUBackend region
```

On Ethos-U85, this backend flow handles the model pattern more cleanly, so the packaged artifact has one `EthosUBackend` region. This provides a further performance benefit because it reduces fragmentation between CPU and NPU. Use Model Explorer with Arm adapters to visualize how models delegate to different backends.

**Note:**
An ExecuTorch `.pte` file can contain work outside an accelerator delegate. However, there's no guarantee that every non-delegated operator can run on the CPU runtime that you deploy. CPU execution depends on the kernel libraries linked into that runtime and the operators, dtypes, layouts, and shapes that they support.

Cortex-M bare-metal runtimes are usually built with a smaller, more selective kernel set than Cortex-A runtimes. The difference in kernel set is because Cortex-M systems have tighter memory and storage constraints. In both cases, CPU fallback support depends on which kernels are included in the runtime build.
