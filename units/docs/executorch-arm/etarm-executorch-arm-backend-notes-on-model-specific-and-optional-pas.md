---
id: "etarm-executorch-arm-backend-notes-on-model-specific-and-optional-pas"
type: "concept"
domain: "edge-ai"
title: "ExecuTorch Arm® Backend: Notes on model specific and optional passes"
summary: "The current TOSA version does not support int64. However, int64 is commonly used in many models. In order to lower the operators with int64 inputs and/or outputs to TOSA, a few passes have been developed to handle the int64-related issues."
status: "draft"
collection: "executorch-arm"
source: "pytorch/executorch@6368414:backends/arm/README.md"
doc_source: "https://github.com/pytorch/executorch/blob/6368414/backends/arm/README.md#notes-on-model-specific-and-optional-passes"
license: "BSD-3-Clause"
mode: "V"
---

The current TOSA version does not support int64. However, int64 is commonly used in many models. In order to lower the operators with int64 inputs and/or outputs to TOSA, a few passes have been developed to handle the int64-related issues. The main idea behind these passes is to replace the uses of int64 with int32 where feasible.

- For floating-point models, these passes need to run very early in the lowering process and can be passed in to the to_edge_transform_and_lower() function call as an optional parameter.
- For quantized models, these transformations will be automatically handled during annotation before the export stage.

List of model specific and optional passes:

- ConvertInt64ConstOpsToInt32Pass
  - Functionalities:
    - Rewrites constant-producing ops that output int64 to instead output int32, when values are within int32 bounds.
  - Supported Ops:
    - `torch.full`, `torch.arange`, `torch.eye`, `torch.linspace`, `torch.tensor`
  - Example usage:
    - backends/arm/test/models/stable_diffusion/test_CLIPTextModelWithProjection.py
    - backends/arm/test/models/stable_diffusion/test_T5EncoderModel.py

- ConvertInt64OutputOpsToInt32Pass
  - Overview:
    - Rewrites or removes operations that produce int64 outputs, converting them to int32 where possible.
    - Overflow checks are applied selectively; for ops without such checks, users need to ensure values fit within the int32 range.
  - Functionalities:
    1. Handling casting to int64:
       - (1) int32 -> int64:
         - Removes the cast and redirect uses of int64 to int32
       - (2) other types -> int64:
         - Rewrites the cast to other types -> int32
       - Supported Ops:
         - torch.ops.aten.to.\[dtype|dtype_layout\]
         - exir_ops.edge.dim_order_ops.\_to_dim_order_copy.default
    2. Post-process argmax and argmin outputs:
       - Converts only downstream paths whose statically inferred values remain
         within the int32 range.
       - Leaves unsafe direct consumers on int64 and inserts int64 boundary
         casts where converted paths reach unsafe consumers or model outputs.
       - Supported Ops:
         - torch.ops.aten.argmax.default
         - exir_ops.edge.aten.argmax.default
         - torch.ops.aten.argmin.default
         - exir_ops.edge.aten.argmin.default
    3. Post-process TopK indices:
       - Applies the same range-safe path conversion to `getitem(topk, 1)`.
       - Leaves `getitem(topk, 0)` values and unsafe direct consumers unchanged.
       - Inserts int64 boundary casts where converted paths reach unsafe
         consumers or model outputs.
       - Keeps gather indices int64 so an undelegated gather remains valid.
       - Prepares supported static TopK for delegation with int32 indices,
         preserving int64 model outputs and consumers that require int64.
       - For TopK configurations that cannot be delegated, downstream index
         operations can still use int32 where range analysis proves it safe.
       - Supported Ops:
         - torch.ops.aten.topk.default
         - exir_ops.edge.aten.topk.default
  - Example usage:
    - (Functionality 1) backends/arm/test/models/stable_diffusion/test_T5EncoderModel.py
    - (Functionality 2) backends/arm/test/models/stable_diffusion/test_CLIPTextModelWithProjection.py

- InsertInt32CastsAfterInt64PlaceholdersPass
  - Functionalities:
    - Inserts an int64 -> int32 cast immediately after each int64 placeholder (graph input).
    - Redirects all uses of each int64 placeholder to its int32 cast output.
    - Inserts local int32 -> int64 casts at call sites where an operator requires int64 inputs, e.g. `torch.nn.functional.one_hot`
  - Pass ordering:
    - When used with `ConvertInt64ConstOpsToInt32Pass` and `ConvertInt64OutputOpsToInt32Pass`, run this pass last.
    - Rationale: Those passes may cause retracing to re-infer some int64 placeholders as int32. Running this pass last casts only inputs that remain int64, minimizing inserted casts.
  - Example usage:
    - backends/arm/test/models/test_llama.py
    - backends/arm/test/models/stable_diffusion/test_CLIPTextModelWithProjection.py
    - backends/arm/test/models/stable_diffusion/test_T5EncoderModel.py

- ToDevicePass
  - This is a utility for moving an already-quantized or already-decomposed GraphModule to another device.
  - it is intended to be used immediately before rerunning / retracing / torch.export.export(...)
  - Functionalities:
    - Calls `.to(device)` on the GraphModule and rewrites explicit `device=` kwargs on `call_function` nodes to a user-specified device.
    - Useful when manually moving an already-quantized or already-decomposed graph module to another device for validation, since some constant-producing nodes may still carry an export-time device kwarg.
  - Example usage:
    - `from executorch.exir.passes import ToDevicePass`
    - `graph_module = ToDevicePass("cpu")(graph_module).graph_module`
    - backends/arm/test/misc/test_post_quant_device_switch.py
