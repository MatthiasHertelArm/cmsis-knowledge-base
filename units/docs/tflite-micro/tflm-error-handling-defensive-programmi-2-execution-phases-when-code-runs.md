---
id: "tflm-error-handling-defensive-programmi-2-execution-phases-when-code-runs"
type: "concept"
domain: "edge-ai"
title: "Error Handling & Defensive Programming Guide: 2. Execution Phases: When Code Runs"
summary: "TFLM distinguishes between setup (which runs once) and execution (which runs continuously)."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@3f787dc:tensorflow/lite/micro/docs/error_handling_guide.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/3f787dc/tensorflow/lite/micro/docs/error_handling_guide.md#2-execution-phases-when-code-runs"
license: "Apache-2.0"
mode: "V"
---

TFLM distinguishes between setup (which runs once) and execution (which runs
continuously).

### Phase 1: Setup & Initialization (`Prepare`)

During the `Prepare` phase, kernels should validate their inputs and parameters
to ensure `Eval` can run blindly and safely. We prioritize clear error messages
here (relying on `TF_LITE_STRIP_ERROR_STRINGS` to mitigate the ROM cost in
production) and we can afford to spend CPU cycles on validation.

**What to Validate (Use `TF_LITE_ENSURE`):**

*   **Model-provided parameters:** Check the number of inputs/outputs, tensor
    types, and tensor shapes.
*   **Quantization parameters:** Explicitly check for invalid quantization
    parameters (e.g., a `scale` of `0.0` or a `zero_point` out of bounds) that
    could cause a divide-by-zero or overflow later in `Eval`.
*   **Resource allocations:** Check if memory allocations (like
    `AllocateTempInputTensor`) return `nullptr`.

### Phase 2: Execution (`Eval`)

During the `Eval` phase, the runtime is vulnerable to data that causes hardware
traps or memory corruption. We should avoid spending cycles or ROM on redundant
checks.

**What to Defend Against (Recommended Validation):**

Kernels should actively defend against three specific runtime threats during
`Eval`:

1.  **Out-of-bounds Memory Access:** If an input tensor contains indices or
    offsets generated at runtime (e.g., in `GATHER`, `STRIDED_SLICE`), these
    **should** be bounds-checked at runtime using a raw `if (!valid) return
    kTfLiteError;`.
2.  **Hardware Faults (Divide by Zero):** Kernels should mathematically protect
    against divide-by-zero (e.g., if a divisor comes from an input tensor) or
    explicitly check and return an error.
3.  **Infinite Loops:** All loops inside `Eval` *should* have a guaranteed
    maximum bound to prevent data-dependent infinite hangs.

**What to Ignore (GIGO for Signal Data):**

*   TFLM kernels are **strongly discouraged** from explicitly scanning general
    input signal data (like images or audio) for `NaN`/`Inf`. For standard math
    operations, garbage data simply results in garbage output (GIGO).

--------------------------------------------------------------------------------
