---
id: "tflm-porting-reference-ops-from-lite-to-how-do-i-allocate-use-temporary-memory"
type: "concept"
domain: "edge-ai"
title: "Porting Reference Ops from Lite to Micro: How do I allocate/use temporary memory?"
summary: "Use the TfLiteContext::RequestScratchBufferInArena and TfLiteContext::GetScratchBuffer methods. The temporary memory is shared between all operators, and is only valid for your operator within the scope of your operator's Invoke method."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@3f787dc:tensorflow/lite/micro/docs/porting_reference_ops.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/3f787dc/tensorflow/lite/micro/docs/porting_reference_ops.md#how-do-i-allocate-use-temporary-memory"
license: "Apache-2.0"
mode: "V"
---

Use the `TfLiteContext::RequestScratchBufferInArena` and
`TfLiteContext::GetScratchBuffer` methods.  The temporary memory is shared
between all operators, and is only valid for your operator within the scope
of your operator's `Invoke` method.  Do not attempt to use temporary memory
to share data between operator invocations.  Scratch buffer temporary memory is
to be used only as pre-allocated storage during the execution scope of your
operator's `Invoke` method.

An example code snippet looks like ([add_n.cc](https://github.com/tensorflow/tflite-micro/blob/3f787dc/tensorflow/lite/micro/docs/../kernels/add_n.cc)):
```C++
if (output->type == kTfLiteFloat32) {
    // Allocate scratch buffer space for pointer to each tensor's data
    // and store the scratch buffer index in the node's user_data
    int scratch_index;
    size_t scratch_size = sizeof(float*) * num_inputs;
    TF_LITE_ENSURE_OK(context, context->RequestScratchBufferInArena(
                                   context, scratch_size, &scratch_index));
    node->user_data =
        reinterpret_cast<decltype(node->user_data)>(scratch_index);
}
```
And to use the buffer:
```C++
int scratch_index =
    static_cast<int>(reinterpret_cast<intptr_t>(node->user_data));
void* scratch_buffer = context->GetScratchBuffer(context, scratch_index);
```

If temporary memory is needed for a calculation during the operator's `Prepare`
method, use `MicroContext::AllocateTempBuffer`.  A matching call to
`MicroContext::DeallocateTempBuffer` must be made prior to returning from your
operator's `Prepare` method.

An example code snippet ([depthwise_conv_vision.cc](https://github.com/tensorflow/tflite-micro/blob/3f787dc/tensorflow/lite/micro/docs/../kernels/xtensa/depthwise_conv_vision.cc)):
```C++
TfLiteTensor filter_int8;

if (filter->type == kTfLiteInt4) {
    const size_t bytes_unpacked = filter->bytes * 2;
    filter_int8.data.data = micro_context->AllocateTempBuffer(
        bytes_unpacked, tflite::MicroArenaBufferAlignment());
    filter_int8.dims = filter->dims;
    filter_int8.type = kTfLiteInt8;
    tflite::tensor_utils::UnpackDenseInt4IntoInt8(
        GetTensorData<int8_t>(filter), GetTensorShape(filter).FlatSize(),
        GetTensorData<int8_t>(&filter_int8));
}

...

if (filter->type == kTfLiteInt4) {
    micro_context->DeallocateTempBuffer(GetTensorData<uint8_t>(&filter_int8));
}
```
