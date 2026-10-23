---
id: "tflm-porting-reference-ops-from-lite-to-when-can-i-inspect-tensor-data"
type: "concept"
domain: "edge-ai"
title: "Porting Reference Ops from Lite to Micro: When can I inspect tensor data?"
summary: "Tensor data can always be inspected within the scope of your operator's Invoke method."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@f7ed40d:tensorflow/lite/micro/docs/porting_reference_ops.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/f7ed40d/tensorflow/lite/micro/docs/porting_reference_ops.md#when-can-i-inspect-tensor-data"
license: "Apache-2.0"
mode: "V"
---

Tensor data can always be inspected within the scope of your operator's `Invoke`
method.

Within the scope of your operator's `Prepare` method, use
`tflite::IsConstantTensor` before inspecting the tensor data.
Only when `tflite::IsConstantTensor` returns `true`, does the tensor have valid
data.
