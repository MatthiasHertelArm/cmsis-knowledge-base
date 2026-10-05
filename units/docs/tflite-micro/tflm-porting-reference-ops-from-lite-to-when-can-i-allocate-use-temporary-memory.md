---
id: "tflm-porting-reference-ops-from-lite-to-when-can-i-allocate-use-temporary-memory"
type: "concept"
domain: "edge-ai"
title: "Porting Reference Ops from Lite to Micro: When can I allocate/use temporary memory?"
summary: "The TfLiteContext::RequestScratchBufferInArena method is available only within the scope of your operator's Prepare method. The TfLiteContext::GetScratchBuffer method is available only within the scope of your operator's Invoke method."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@3f787dc:tensorflow/lite/micro/docs/porting_reference_ops.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/3f787dc/tensorflow/lite/micro/docs/porting_reference_ops.md#when-can-i-allocate-use-temporary-memory"
license: "Apache-2.0"
mode: "V"
---

The `TfLiteContext::RequestScratchBufferInArena` method is available only within
the scope of your operator's `Prepare` method.
The `TfLiteContext::GetScratchBuffer` method is available only within
the scope of your operator's `Invoke` method.

The `MicroContext::AllocateTempBuffer` and `MicroContext::DeallocateTempBuffer`
methods are only available within the scope of your operator's `Prepare` method.
