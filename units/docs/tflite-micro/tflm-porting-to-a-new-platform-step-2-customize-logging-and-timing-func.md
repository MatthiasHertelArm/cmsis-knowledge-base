---
id: "tflm-porting-to-a-new-platform-step-2-customize-logging-and-timing-func"
type: "concept"
domain: "edge-ai"
title: "Porting to a new platform: Step 2: Customize Logging and Timing Function for your Platform"
summary: "Replace the following files with a version that is specific to your target platform:"
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@f7ed40d:tensorflow/lite/micro/docs/new_platform_support.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/f7ed40d/tensorflow/lite/micro/docs/new_platform_support.md#step-2-customize-logging-and-timing-function-for-your-platform"
license: "Apache-2.0"
mode: "V"
---

Replace the following files with a version that is specific to your target
platform:

 * [debug\_log.cc](https://github.com/tensorflow/tflite-micro/blob/main/tensorflow/lite/micro/debug_log.cc)
 * [micro\_time.cc](https://github.com/tensorflow/tflite-micro/blob/main/tensorflow/lite/micro/micro_time.cc)
 * [system\_setup.cc](https://github.com/tensorflow/tflite-micro/blob/main/tensorflow/lite/micro/system_setup.cc)

These can be placed anywhere in your directory tree. The only requirement is
that when linking TFLM into a binary, the implementations of the functions in
[debug\_log.h](https://github.com/tensorflow/tflite-micro/blob/main/tensorflow/lite/micro/debug_log.h),
[micro\_time.h](https://github.com/tensorflow/tflite-micro/blob/main/tensorflow/lite/micro/micro_time.h)
and [system\_setup.h](https://github.com/tensorflow/tflite-micro/blob/main/tensorflow/lite/micro/system_setup.h)
can be found.

For example, the implementations of these functions for:
  * [Sparkfun Edge](https://github.com/advaitjain/tflite-micro-sparkfun-edge-examples/tree/120f68ace95ae3d66963977ac7754acd0c86540d/tensorflow/lite/micro/sparkfun_edge)
is the implementation of these functions for the Sparkfun Edge.
