---
id: "cet-executorch-pack-maintenance-and-ve-what-is-in-the-pack"
type: "concept"
domain: "pack"
title: "ExecuTorch pack maintenance and versioning: What is in the pack"
summary: "It is a source pack: nothing is prebuilt. Every operator is a selectable component, which is what lets create_ai_layer.py narrow the link to exactly the kernels a given .pte needs."
status: "draft"
collection: "cmsis-executorch"
source: "Arm-Examples/CMSIS-Executorch@0a243f1:documentation/executorch-pack-maintenance.md"
doc_source: "https://github.com/Arm-Examples/CMSIS-Executorch/blob/0a243f1/documentation/executorch-pack-maintenance.md#what-is-in-the-pack"
license: "Apache-2.0"
mode: "V"
---

| Path | Contents |
|---|---|
| `PyTorch.ExecuTorch.pdsc` | Component declarations — one component per operator, plus runtime and backend |
| `src/` | ExecuTorch runtime, kernel and Ethos-U backend sources |
| `include/` | Public headers, **including the bundled `include/flatbuffers/`** |
| `armclang_shims/` | Small compatibility shims for Arm Compiler 6 |
| `Documentation/` | Pack README |
| `LICENSE` | Upstream BSD-3-Clause (the template code around it is Apache-2.0) |

It is a **source** pack: nothing is prebuilt. Every operator is a selectable
component, which is what lets `create_ai_layer.py` narrow the link to
exactly the kernels a given `.pte` needs.
