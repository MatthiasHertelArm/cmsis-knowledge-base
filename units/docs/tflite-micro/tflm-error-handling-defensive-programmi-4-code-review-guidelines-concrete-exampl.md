---
id: "tflm-error-handling-defensive-programmi-4-code-review-guidelines-concrete-exampl"
type: "concept"
domain: "edge-ai"
title: "Error Handling & Defensive Programming Guide: 4. Code Review Guidelines & Concrete Examples"
summary: "Fuzzer fixes should align with the core philosophy. We evaluate them based on the type of crash:"
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@3f787dc:tensorflow/lite/micro/docs/error_handling_guide.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/3f787dc/tensorflow/lite/micro/docs/error_handling_guide.md#4-code-review-guidelines-concrete-examples"
license: "Apache-2.0"
mode: "V"
---

How to address common scenarios in PRs:

### Validating Framework Pointers

**Discouraged.** Please avoid wasting ROM checking the validity of the TFLM
framework itself. The `context` and `node` pointers passed by the runtime are
typically guaranteed to be valid. Notably, `TF_LITE_ENSURE(context, context !=
nullptr)` is logically flawed: if `context` is actually `nullptr`, the macro
will dereference it to log the error, causing an immediate hardware fault.

### Validating Public API Parameters

**Discouraged.** This penalizes production deployments for bugs that the
firmware developer should have caught during local testing. We recommend asking
the contributor to use `TFLITE_DCHECK(op_resolver != nullptr);` instead of
adding `if (op_resolver == nullptr) return kTfLiteError;` to the
`MicroInterpreter` API.

### Preventing Null Pointer Dereferences

*   **If in `Prepare` (Recommended):** It is standard practice to check for
    nulls when pulling tensors from the context.

```cpp
TfLiteTensor* operand = micro_context->AllocateTempInputTensor(node, kOperandTensor);
TF_LITE_ENSURE(context, operand != nullptr);
```

*   **If in `Eval` (Discouraged):** Production builds shouldn't pay the cycle
    cost for checks that can't fail at runtime if `Prepare` succeeded. Ask the
    author to change it to `TFLITE_DCHECK`.

```cpp
const TfLiteEvalTensor* input_id = tflite::micro::GetEvalInput(context, node, 0);
TFLITE_DCHECK(input_id != nullptr);
```

### Preventing Buffer Overflows

*   **If in `Prepare` (Recommended):** Use `TF_LITE_ENSURE` to validate that
    tensor sizes are compatible.
*   **If in `Eval`:** If the overflow comes from invalid *control data* (like an
    input tensor providing indices), it *should* be validated in `Eval` to
    prevent memory corruption. Use raw returns:

```cpp
// e.g., third_party/tflite_micro/tensorflow/lite/micro/kernels/gather_nd.cc
// Note: use subtraction to prevent integer overflow!
if (from_pos < 0 || from_pos > params_flat_size - slice_size) {
  return kTfLiteError; // Halts execution to prevent out-of-bounds memory read
}
```

```
If it's just an invariant guaranteed by `Prepare`, ask to discard the check or
use `TFLITE_DCHECK`.
```

### Fixing Fuzzer Crashes

Fuzzer fixes should align with the core philosophy. We evaluate them based on
the type of crash:

1.  **Corrupted FlatBuffer Files (Working As Intended):** If the fuzzer mutates
    the FlatBuffer byte array so a `Tensor` offset points beyond the end of the
    file (causing a segfault), **request changes if the PR uses `TF_LITE_ENSURE`
    or raw `if` statements**. To keep the binary size as small as possible, we
    prefer to omit the FlatBuffer verifier. However, **it is recommended to
    accept the PR if it exclusively uses `TFLITE_DCHECK`** to catch the
    out-of-bounds index. This treats the structural check purely as a zero-cost
    developer aid during debugging.
2.  **Invalid Model Topologies (Fix in Prepare):** If the fuzzer generates a
    valid FlatBuffer but modifies a `CONV_2D` operator to have 0 inputs instead
    of the expected 3, **this is a good fix in `Prepare`** using
    `TF_LITE_ENSURE_EQ(context, NumInputs(node), 3);`.
3.  **Static Math Crashes (Fix in Prepare):** If the fuzzer sets a quantization
    `scale` parameter to `0.0` (causing a hardware trap during inference),
    **this is a good fix in `Prepare`** using `TF_LITE_ENSURE(context, scale !=
    0.0);`.
4.  **Dynamic Math/Data Crashes (Fix in Eval):** If the fuzzer provides input
    data to a `GATHER` op with an index of `999` (causing out-of-bounds
    corruption), or a divisor tensor evaluates to `0` (causing a divide-by-zero
    trap), **this is a good fix in `Eval`**. Prefer a raw `if (index >= 10)
    return kTfLiteError;` to save ROM (avoid using `TF_LITE_ENSURE` here just to
    log the error; save the ROM).
