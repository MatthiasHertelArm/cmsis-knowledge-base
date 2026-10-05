---
id: "tflm-error-handling-defensive-programmi-3-macro-selection-guide"
type: "concept"
domain: "edge-ai"
title: "Error Handling & Defensive Programming Guide: 3. Macro Selection Guide"
summary: "To strike the right balance between debuggability, code size (ROM), and performance, follow this decision tree."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@3f787dc:tensorflow/lite/micro/docs/error_handling_guide.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/3f787dc/tensorflow/lite/micro/docs/error_handling_guide.md#3-macro-selection-guide"
license: "Apache-2.0"
mode: "V"
---

To strike the right balance between debuggability, code size (ROM), and
performance, follow this decision tree.

### The Decision Tree

1.  **Are you writing a Unit Test?**
    *   Use GoogleTest-style macros like `EXPECT_EQ`, `EXPECT_NEAR`, etc. for
        verifying test conditions.
2.  **Are you in `Init` or `Prepare`?**
    *   Use `TF_LITE_ENSURE`. We want to fail early with a clear log message if
        the model is incompatible.
3.  **Are you in `Eval` (or a helper called by `Eval`)?**
    *   *Is it an invariant guaranteed by `Prepare`?* (e.g., "this pointer
        cannot be null"). Use `TFLITE_DCHECK`. It costs nothing in production.
    *   *Is it validating control data from an input tensor?* (e.g., a dynamic
        index). Use a raw `if (!condition) return kTfLiteError;`. This safely
        prevents memory corruption without paying the ROM cost of a string
        literal.
    *   *Are you propagating an error from a helper function?* Use
        `TF_LITE_ENSURE_STATUS` or `TF_LITE_ENSURE_OK`.

### Macro Cheat Sheet

Macro                                          | Cost in Release                                          | When to Use
:--------------------------------------------- | :------------------------------------------------------- | :----------
`TFLITE_DCHECK`
`TFLITE_DCHECK_EQ`          | **Zero** (Optimized out)                                 | **Default for `Eval` invariants and FlatBuffer structural bounds checking.**
`if (!cond) return kTfLiteError;`              | **Low** (Branch only)                                    | **Default for validating control data in `Eval`.**
`TF_LITE_ENSURE_OK`
`TF_LITE_ENSURE_STATUS` | **Low** (Branch only)                                    | **Default for propagating errors from helper functions.**
`TF_LITE_ENSURE`
`TF_LITE_ENSURE_EQ`        | **High** (Branch + logs `__FILE__`, `__LINE__`, `#cond`) | **Default for `Prepare` / Setup.** Can be used in `Eval` *only* if the failure indicates an unrecoverable state-machine corruption; avoid for normal signal data out-of-bounds.
`TF_LITE_ENSURE_MSG`                           | **Highest** (Branch + custom string)                     | **Use Sparingly.** Only when the default `TF_LITE_ENSURE` error is too cryptic.
`TFLITE_CHECK`                                 | **Fatal** (Calls `Abort()`)                              | **Avoid in core TFLM.** Halts the microcontroller.

> **The Hidden Cost of `TF_LITE_ENSURE`:** This macro expands to an `if` branch
> that calls `TF_LITE_KERNEL_LOG`. By default, this embeds `__FILE__`,
> `__LINE__`, and the stringified condition directly into the `.rodata` section
> of the binary. Every single invocation permanently consumes precious ROM. If
> you have multiple preconditions, combine them into a single
> `TF_LITE_ENSURE(context, a != nullptr && b != nullptr)`. **Note:** For
> production builds where ROM is severely constrained, firmware developers
> should define the `TF_LITE_STRIP_ERROR_STRINGS` macro to compile out these
> strings, reducing `TF_LITE_ENSURE` to a simple low-cost branch.

--------------------------------------------------------------------------------
