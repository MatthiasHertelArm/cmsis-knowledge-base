---
id: "etarm-arm-custom-operators-dispatch-shape"
type: "concept"
domain: "edge-ai"
title: "Arm Custom Operators: Dispatch Shape"
summary: "Arm Custom Operators: Dispatch Shape"
status: "draft"
collection: "executorch-arm"
source: "pytorch/executorch@658390c:examples/arm/custom_operators.md"
doc_source: "https://github.com/pytorch/executorch/blob/658390c/examples/arm/custom_operators.md#dispatch-shape"
license: "BSD-3-Clause"
mode: "V"
---

### Current Limitation
- The payload field named `workgroup_sizes` is currently consumed as the dispatch shape for `vkCmdDispatch(...)`.
- The shader's actual local workgroup size still comes from the GLSL/SPIR-V declaration.
- So today this field is effectively misnamed: it carries workgroup counts, not local workgroup size.

### What To Set
- Set `workgroup_sizes` to the dispatch grid you want the runtime to launch.
- Derive it from:
  - the total work your shader must cover, and
  - the shader-local workgroup size declared in the shader.
- For a 2D shader with local size `(lx, ly, lz)` covering an output of `(W, H)`, set:
  - `dispatch_x = ceil(W / lx)`
  - `dispatch_y = ceil(H / ly)`
  - `dispatch_z = 1` unless the shader maps work across `z`

### Practical Rule
- Treat shader local size and payload `workgroup_sizes` as two separate concepts.
- Local size is fixed by the shader.
- Payload `workgroup_sizes` must be computed from the work volume for that operator instance.
