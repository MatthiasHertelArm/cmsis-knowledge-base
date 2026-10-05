---
id: "tflm-how-to-debug-invalid-output-python-layer-by-layer-debugging-tool"
type: "concept"
domain: "edge-ai"
title: "How to debug invalid output: Python Layer by Layer Debugging Tool"
summary: "The Python Tool/Script can first be used to compare TFLM vs Tflite outputs for random inputs by only providing a TfLite file."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@3f787dc:debugging_output.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/3f787dc/debugging_output.md#python-layer-by-layer-debugging-tool"
license: "Apache-2.0"
mode: "V"
---

The Python Tool/Script can first be used to compare TFLM vs Tflite outputs for
random inputs by only providing a TfLite file.

#### TfLite vs TFLM command:
``` 
 bazel run tensorflow/lite/micro/tools:layer_by_layer_debugger -- \
    --input_tflite_file=</path/to/my_model.tflite>
```

The Python Tool/Script can also be used to compare TFLM's python x86 output
vs expected output provided by the C++ Tool/binary.

#### TFLM vs Expected Command:
``` 
  bazel run tensorflow/lite/micro/tools:layer_by_layer_debugger -- \
    --input_tflite_file=</path/to/my_model.tflite> \
    --layer_by_layer_data_file=</path/to/my_debug_flatbuffer_file>
```

#### Optional Flags:
 ` --print_dump  `
When this flag is set, it will print the TFLM output for each layer that is
compared.

 ` --rng`
Integer random number seed for generating input data for comparisons against TFLite. (Default: 42)
