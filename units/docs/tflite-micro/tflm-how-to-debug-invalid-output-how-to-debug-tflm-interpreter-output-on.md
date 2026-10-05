---
id: "tflm-how-to-debug-invalid-output-how-to-debug-tflm-interpreter-output-on"
type: "concept"
domain: "edge-ai"
title: "How to debug invalid output: How to debug TFLM Interpreter output on embedded targets"
summary: "First you call a C++ binary that takes a TfLite model and returns a file that has random inputs and their corresponding output values for each layer of the model it was provided."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@3f787dc:debugging_output.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/3f787dc/debugging_output.md#how-to-debug-tflm-interpreter-output-on-embedded-targets"
license: "Apache-2.0"
mode: "V"
---

First you call a C++ binary that takes a TfLite model and returns a file that has
random inputs and their corresponding output values for each layer of the model
it was provided.

The second is you provide a TfLite model and file outputted by C++ binary above
to a  python script. The script runs TFLM x86 inference comparison to the 
expected output.
