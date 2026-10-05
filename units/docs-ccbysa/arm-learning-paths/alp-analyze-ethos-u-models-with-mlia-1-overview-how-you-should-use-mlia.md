---
id: "alp-analyze-ethos-u-models-with-mlia-1-overview-how-you-should-use-mlia"
type: "concept"
domain: "edge-ai"
title: "Analyze machine learning models for Arm Ethos-U with Arm ML Inference Advisor: Understand where MLIA fits in model preparation: How you should use MLIA"
summary: "MLIA isn't a replacement for graph visualization or runtime profiling. It's an advisory layer that helps earlier in the model preparation workflow. The following table shows which questions MLIA and related tools can answer:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/analyze-ethos-u-models-with-mlia/1-overview.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/analyze-ethos-u-models-with-mlia/1-overview/#how-you-should-use-mlia"
license: "CC-BY-SA-4.0"
mode: "V"
---

MLIA isn't a replacement for graph visualization or runtime profiling. It's an advisory layer that helps earlier in the model preparation workflow. The following table shows which questions MLIA and related tools can answer:

| Tool or backend | Use it to answer |
| --- | --- |
| MLIA | Is this model suitable for my target, and what should I change? |
| Vela | Which operators are supported, and which layers dominate compiler-estimated cycles? |
| Corstone FVP | What NPU performance counters does a packaged `.pte` artifact produce for the whole model run on a virtual platform? |
| Model Explorer | What does the generated model artifact graph look like? |
| Runtime-specific profiling tools | What happened when the model ran? For example, use ETRecord, ETDump, and ExecuTorch Inspector for ExecuTorch deployments. Use LiteRT benchmark and profiling tools for LiteRT deployments. |

Vela-backed MLIA checks use compiler estimates. The checks can include operator-level breakdowns, such as which layers dominate estimated cycles or have low MAC utilization.

Corstone-backed MLIA checks run a packaged `.pte` file on an FVP and report NPU performance counters for the whole model run. The checks don't provide per-layer estimates or operator breakdowns.

Model Explorer can show how an ExecuTorch `.pte` artifact is partitioned into delegate regions. Runtime-specific profiling tools can show behavior after you have a runnable deployment.

Use the following tools together:

- Use MLIA before or during model preparation.
- Use Model Explorer to inspect generated artifacts and delegation structure.
- Use runtime profiling tools after you can execute the model.
