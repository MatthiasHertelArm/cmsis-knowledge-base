---
id: "tflm-error-handling-defensive-programmi-1-trust-boundaries-where-data-comes-from"
type: "concept"
domain: "edge-ai"
title: "Error Handling & Defensive Programming Guide: 1. Trust Boundaries: Where Data Comes From"
summary: "To achieve high performance without sacrificing critical stability, TFLM distinguishes between trusted and untrusted data sources."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@3f787dc:tensorflow/lite/micro/docs/error_handling_guide.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/3f787dc/tensorflow/lite/micro/docs/error_handling_guide.md#1-trust-boundaries-where-data-comes-from"
license: "Apache-2.0"
mode: "V"
---

To achieve high performance without sacrificing critical stability, TFLM
distinguishes between trusted and untrusted data sources.

### The C++ API (Trusted)

When a firmware developer uses the public TFLM C++ API (e.g., instantiating a
`MicroInterpreter` or calling `Invoke()`), we treat the developer as trusted.

*   **Recommendation:** The core API should not spend runtime cycles or binary
    space checking for invalid parameters (e.g., passing `nullptr`) or incorrect
    state-machine sequences.
*   **Mechanism:** Rely entirely on `TFLITE_DCHECK`. The firmware engineer gets
    an immediate assertion failure during local debugging if they misuse the
    API. In release builds, these compile out, leaving zero overhead.

### The FlatBuffer Model (Partially Trusted)

When dealing with the `.tflite` FlatBuffer model, we distinguish between two
types of malformation:

*   **Corrupted FlatBuffer Files (Structural Malformation):** The core
    `MicroInterpreter` assumes the FlatBuffer is structurally valid. We *do not*
    perform standard bounds checking on FlatBuffer schema offsets or operator
    tensor indices (e.g., if an operator requests tensor index `999` but the
    model only has `10` tensors, a production TFLM build will read out of
    bounds). To aid local debugging, structural checks are considered a
    "good-to-have" feature but **should exclusively use `TFLITE_DCHECK`**. If
    models are provided via an untrusted channel (e.g., OTA), the application
    layer is entirely responsible for validating the integrity of the model
    before passing it to TFLM.
*   **Invalid Model Topologies (Semantic Malformation):** The runtime *should*
    defend against TFLite Converter bugs or unsupported configurations (e.g.,
    wrong tensor shapes, unsupported types). This validation happens entirely in
    the Setup phase. Because developers can use `TF_LITE_STRIP_ERROR_STRINGS` to
    remove the string bloat in production, checking topologies in `Prepare`
    provides safe fallback (e.g., rejecting a bad OTA update) without the severe
    ROM penalty of embedded strings.

--------------------------------------------------------------------------------
