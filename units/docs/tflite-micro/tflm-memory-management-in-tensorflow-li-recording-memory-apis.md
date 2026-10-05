---
id: "tflm-memory-management-in-tensorflow-li-recording-memory-apis"
type: "concept"
domain: "edge-ai"
title: "Memory Management in TensorFlow Lite Micro: Recording Memory APIs"
summary: "TFLM provides simple APIs for auditing memory usage in the shared tensor arena. These APIs are opt-in and require some additional memory overhead and a working debug logging implementation (reference implementation)."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@3f787dc:tensorflow/lite/micro/docs/memory_management.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/3f787dc/tensorflow/lite/micro/docs/memory_management.md#recording-memory-apis"
license: "Apache-2.0"
mode: "V"
---

TFLM provides simple APIs for auditing memory usage in the shared tensor arena.
These APIs are opt-in and require some additional memory overhead and a working
debug logging implementation
[(reference implementation)](https://github.com/tensorflow/tflite-micro/blob/main/tensorflow/lite/micro/debug_log.cc).

A typical bare-bones TFLM interpreter setup looks as such:

```c++
// Buffer for the tensor arena:
size_t tensor_arena_size = 2048;
uint8_t tensor_arena[tensor_arena_size];

// Interpreter using the shared tensor arena above:
tflite::MicroInterpreter interpreter(
  tflite::GetModel(my_model_data), ops_resolver,
  tensor_arena, tensor_arena_size);

// Invoke one time which will allocate internals:
if (interpreter.Invoke() != kTfLiteOk) {
  MicroPrintf("Exception during invoke()!");
}
```

Recording API can simply be used by including the `RecordingMicroInterpreter`
class (`recording_micro_interpreter.h`) and replace `tflite::MicroInterpreter`
with `tflite::RecordingMicroInterpreter`. The same call to `invoke()` is
performed, but another call is made to `PrintAllocations()` which will output
detailed allocation logging:

```c++
// Add an include to the recording API:
#include "recording_micro_interpreter.h"

// Simply change the class name from 'MicroInterpreter' to 'RecordingMicroInterpreter':
tflite::RecordingMicroInterpreter interpreter(
  tflite::GetModel(my_model_data), ops_resolver,
  tensor_arena, tensor_arena_size);

// Invoke one time which will allocate internals:
if (interpreter.Invoke() != kTfLiteOk) {
  MicroPrintf("Exception during invoke()!");
}

// Print out detailed allocation information:
interpreter.GetMicroAllocator().PrintAllocations();
```

The output of this call will look something similar to this (output from the
[memory_arena_threshold_test](https://github.com/tensorflow/tflite-micro/blob/main/tensorflow/lite/micro/memory_arena_threshold_test.cc#L205)):

```bash
[RecordingMicroAllocator] Arena allocation total 9568 bytes
[RecordingMicroAllocator] Arena allocation head 7744 bytes
[RecordingMicroAllocator] Arena allocation tail 1824 bytes
[RecordingMicroAllocator] 'TfLiteEvalTensor data' used 360 bytes with alignment overhead (requested 360 bytes for 15 allocations)
[RecordingMicroAllocator] 'Persistent TfLiteTensor data' used 0 bytes with alignment overhead (requested 0 bytes for 0 tensors)
[RecordingMicroAllocator] 'Persistent TfLiteTensor quantization data' used 0 bytes with alignment overhead (requested 0 bytes for 0 allocations)
[RecordingMicroAllocator] 'TfLiteTensor variable buffer data' used 0 bytes with alignment overhead (requested 0 bytes for 0 allocations)
[RecordingMicroAllocator] 'NodeAndRegistration struct' used 392 bytes with alignment overhead (requested 392 bytes for 7 NodeAndRegistration structs)
[RecordingMicroAllocator] 'Operator runtime data' used 136 bytes with alignment overhead (requested 136 bytes for 5 OpData structs)
```

### Allocation Section Details

More information about each recorded allocation section:

*   'TfLiteEvalTensor data'
    *   C struct that holds the data type, dimension, and a pointer to the
        buffer representing the Tensor.
*   'Persistent TfLiteTensor data'
    *   C struct that holds more information than a `TfLiteEvalTensor` struct in
        the graph.
    *   Allocations in this bucket will only show up when accessing tensors from
        the accessors on `tflite::MicroInterpreter`.
*   'Persistent TfLiteTensor quantization data'
    *   Length of persistent quantization data assigned to persistent
        `TfLiteTensor` structs.
    *   Allocations in this bucket will only show up when accessing tensors from
        the accessors on `tflite::MicroInterpreter`.
*   'TfLiteTensor variable buffer data'
    *   Length of buffer data from a variable tensor (retains data throughout
        calls to `invoke()`).
*   'NodeAndRegistration struct'
    *   C struct that holds a `TfLiteRegistration` and `TfLiteNode` struct
        instance.
    *   Each operator in a model will contain one `NodeAndRegistration` struct.
*   'Operator runtime data'
    *   Persistent allocations of data cached by TFLM kernels (e.g. quantization
        params, multipliers, etc).
