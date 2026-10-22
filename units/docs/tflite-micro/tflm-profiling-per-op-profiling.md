---
id: "tflm-profiling-per-op-profiling"
type: "concept"
domain: "edge-ai"
title: "Profiling: Per-Op Profiling"
summary: "There is a feature in the MicroInterpreter to enable per-op profiling. To enable this, provide a MicroProfiler to the MicroInterpreter's constructor. When building with error strings enabled (i.e."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@bd621c2:tensorflow/lite/micro/docs/profiling.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/bd621c2/tensorflow/lite/micro/docs/profiling.md#per-op-profiling"
license: "Apache-2.0"
mode: "V"
---

There is a feature in the MicroInterpreter to enable per-op profiling. To enable
this, provide a MicroProfiler to the MicroInterpreter's constructor. When building
with error strings enabled (i.e. `TF_LITE_STRIP_ERROR_STRINGS` is not defined),
the interpreter automatically profiles each operator invocation using `ScopedMicroProfiler`.
