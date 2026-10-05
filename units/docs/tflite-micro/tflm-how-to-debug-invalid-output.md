---
id: "tflm-how-to-debug-invalid-output"
type: "concept"
domain: "edge-ai"
title: "How to debug invalid output"
summary: "The TFLM debugging output tools allow TFLM users to easily debug their models by providing a tool that will compare the intermediate values(output of each OP/Kernel) from a model post invoke between the TFLM and TfLite."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@3f787dc:debugging_output.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/3f787dc/debugging_output.md"
license: "Apache-2.0"
mode: "V"
---

The TFLM debugging output tools allow TFLM users to easily debug their models
by providing a tool that will compare the intermediate  values(output of each OP/Kernel)
from a model post invoke between the TFLM and TfLite. As well as a way to
compare intermediate values between TFLM x86 implementations and Optimized 
Implementations.
