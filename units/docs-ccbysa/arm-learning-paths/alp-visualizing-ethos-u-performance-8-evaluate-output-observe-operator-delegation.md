---
id: "alp-visualizing-ethos-u-performance-8-evaluate-output-observe-operator-delegation"
type: "concept"
domain: "edge-ai"
title: "Visualize Ethos-U NPU performance with ExecuTorch on Arm FVPs: Evaluate Ethos-U Performance: Observe Operator Delegation"
summary: "This output indicates which operators go to processors: - Ethos-U85 NPU: occurrences_in_delegated_graphs - Cortex-M85 CPU: occurrences_in_non_delegated_graph"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/visualizing-ethos-u-performance/8-evaluate-output.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/visualizing-ethos-u-performance/8-evaluate-output/#observe-operator-delegation"
license: "CC-BY-SA-4.0"
mode: "V"
---

This output indicates which operators go to processors:
- **Ethos-U85 NPU:** `occurrences_in_delegated_graphs`
- **Cortex-M85 CPU:** `occurrences_in_non_delegated_graph`

```bash { output_lines = "1-34" }
Total delegated subgraphs: 1
Number of delegated nodes: 419
Number of non-delegated nodes: 3

Delegation table:
╒════╤════════════════════════════════════════════════════╤═══════════════════════════════════╤═══════════════════════════════════════╕
│    │ op_type                                            │   occurrences_in_delegated_graphs │   occurrences_in_non_delegated_graphs │
╞════╪════════════════════════════════════════════════════╪═══════════════════════════════════╪═══════════════════════════════════════╡
│  0 │ aten_add_tensor                                    │                                10 │                                     0 │
├────┼────────────────────────────────────────────────────┼───────────────────────────────────┼───────────────────────────────────────┤
│  1 │ aten_clone_default                                 │                                 1 │                                     0 │
├────┼────────────────────────────────────────────────────┼───────────────────────────────────┼───────────────────────────────────────┤
│  2 │ aten_convolution_default                           │                                52 │                                     0 │
├────┼────────────────────────────────────────────────────┼───────────────────────────────────┼───────────────────────────────────────┤
│  3 │ aten_hardtanh_default                              │                                35 │                                     0 │
├────┼────────────────────────────────────────────────────┼───────────────────────────────────┼───────────────────────────────────────┤
│  4 │ aten_linear_default                                │                                 1 │                                     0 │
├────┼────────────────────────────────────────────────────┼───────────────────────────────────┼───────────────────────────────────────┤
│  5 │ aten_mean_dim                                      │                                 1 │                                     0 │
├────┼────────────────────────────────────────────────────┼───────────────────────────────────┼───────────────────────────────────────┤
│  6 │ aten_view_copy_default                             │                                 1 │                                     0 │
├────┼────────────────────────────────────────────────────┼───────────────────────────────────┼───────────────────────────────────────┤
│  7 │ cortex_m_dequantize_per_tensor_default             │                                 0 │                                     1 │
├────┼────────────────────────────────────────────────────┼───────────────────────────────────┼───────────────────────────────────────┤
│  8 │ cortex_m_quantize_per_tensor_default               │                                 0 │                                     1 │
├────┼────────────────────────────────────────────────────┼───────────────────────────────────┼───────────────────────────────────────┤
│  9 │ getitem                                            │                                 0 │                                     1 │
├────┼────────────────────────────────────────────────────┼───────────────────────────────────┼───────────────────────────────────────┤
│ 10 │ quantized_decomposed_dequantize_per_tensor_default │                               217 │                                     0 │
├────┼────────────────────────────────────────────────────┼───────────────────────────────────┼───────────────────────────────────────┤
│ 11 │ quantized_decomposed_quantize_per_tensor_default   │                               101 │                                     0 │
├────┼────────────────────────────────────────────────────┼───────────────────────────────────┼───────────────────────────────────────┤
│ 12 │ Total                                              │                               419 │                                     3 │
╘════╧════════════════════════════════════════════════════╧═══════════════════════════════════╧═══════════════════════════════════════╛
```
