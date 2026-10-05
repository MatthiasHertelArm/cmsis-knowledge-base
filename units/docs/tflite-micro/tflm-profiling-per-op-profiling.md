---
id: "tflm-profiling-per-op-profiling"
type: "concept"
domain: "edge-ai"
title: "Profiling: Per-Op Profiling"
summary: "There is a feature in the MicroInterpreter to enable per-op profiling. To enable this, provide a MicroProfiler to the MicroInterpreter's constructor then build with a non-release build to disable the NDEBUG define surrounding the ScopedOperatorProfile within the MicroInterpreter."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@3f787dc:tensorflow/lite/micro/docs/profiling.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/3f787dc/tensorflow/lite/micro/docs/profiling.md#per-op-profiling"
license: "Apache-2.0"
mode: "V"
---

There is a feature in the MicroInterpreter to enable per-op profiling. To enable
this, provide a MicroProfiler to the MicroInterpreter's constructor then build
with a non-release build to disable the NDEBUG define surrounding the
ScopedOperatorProfile within the MicroInterpreter.
