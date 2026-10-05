---
id: "tflm-how-to-debug-invalid-output-c-expected-layer-by-layer-output-tool-on"
type: "concept"
domain: "edge-ai"
title: "How to debug invalid output: C++ Expected Layer by Layer Output Tool on TFLite Micro"
summary: "This C++ binary allows you to pass in a TfLite model and returns a flatbuffer file with input and the corresponding output values appended into it that can be passed into a python debugging tool which can compare …"
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@3f787dc:debugging_output.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/3f787dc/debugging_output.md#c-expected-layer-by-layer-output-tool-on-tflite-micro"
license: "Apache-2.0"
mode: "V"
---

This C++ binary allows you to pass in a TfLite model and returns a flatbuffer
file with input and the corresponding output values appended into it that can be
passed into a python debugging tool which can compare those golden values vs
the x86 TFLM reference kernel implementation.

The C++ Tool/binary will write a debugging file to the path provide in
2nd arg using the tflite_model provided in the 1st arg.

##### Command bazel/blaze:

```
 bazel run tensorflow/lite/micro/tools:layer_cc -- \
    </path/to/input_model.tflite>
   </path/to/output.file_name>
```

##### How to Build using Makefile :

```
make -f tensorflow/lite/micro/tools/make/Makefile layer_by_layer_output_tool -j24
```
