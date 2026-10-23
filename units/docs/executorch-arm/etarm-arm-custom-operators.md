---
id: "etarm-arm-custom-operators"
type: "concept"
domain: "edge-ai"
title: "Arm Custom Operators"
summary: "As a practical extension of torch.library, the Arm backends provide a way to keep selected custom operators inside delegated partitions and lower them to backend-specific implementations such as shaders or other target-side code."
status: "draft"
collection: "executorch-arm"
source: "pytorch/executorch@24a6116:examples/arm/custom_operators.md"
doc_source: "https://github.com/pytorch/executorch/blob/24a6116/examples/arm/custom_operators.md"
license: "BSD-3-Clause"
mode: "V"
---

As a practical extension of `torch.library`, the Arm backends provide a way to
keep selected custom operators inside delegated partitions and lower them to
backend-specific implementations such as shaders or other target-side code.

Arm custom operators are lowered through the Arm TOSA dialect as `tosa.CUSTOM`
nodes. In practice this means a user-visible library op is first captured in the
graph, then rewritten to `tosa.CUSTOM` with a stable `operator_name`,
`domain_name`, and `implementation_attrs` payload that describes the shader or
other backend-specific implementation contract.

The main APIs involved are:
- register the operator with the Arm partitioner using `partitioner.register_custom_partition_op(...)` so it can stay inside the delegated graph
- add a pass that rewrites the `torch.library` op to `tosa.CUSTOM` in the Arm backend.
- provide the target-side implementation, for example a GLSL shader
- provide a function that builds the `tosa.CUSTOM` definition and payload

For a minimal end-to-end example showing the required pieces in Python, see
`examples/arm/custom_operators.py`.
