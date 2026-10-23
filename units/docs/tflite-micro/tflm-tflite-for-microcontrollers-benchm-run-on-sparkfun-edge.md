---
id: "tflm-tflite-for-microcontrollers-benchm-run-on-sparkfun-edge"
type: "concept"
domain: "edge-ai"
title: "TFLite for Microcontrollers Benchmarks: Run on Sparkfun Edge"
summary: "The following instructions will help you build and deploy this benchmark on the SparkFun Edge development board."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@f7ed40d:tensorflow/lite/micro/benchmarks/README.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/f7ed40d/tensorflow/lite/micro/benchmarks/README.md#run-on-sparkfun-edge"
license: "Apache-2.0"
mode: "V"
---

The following instructions will help you build and deploy this benchmark on the
[SparkFun Edge development board](https://sparkfun.com/products/15170).


If you're new to using this board, we recommend walking through the
[AI on a microcontroller with TensorFlow Lite and SparkFun Edge](https://codelabs.developers.google.com/codelabs/sparkfun-tensorflow)
codelab to get an understanding of the workflow.

Build binary using

```
make -f tensorflow/lite/micro/tools/make/Makefile TARGET=sparkfun_edge person_detection_benchmark_bin
```

Refer to flashing instructions in the [Person Detection Example](https://github.com/tensorflow/tflite-micro/blob/main/tensorflow/lite/micro/examples/person_detection/README.md#running-on-sparkfun-edge).
