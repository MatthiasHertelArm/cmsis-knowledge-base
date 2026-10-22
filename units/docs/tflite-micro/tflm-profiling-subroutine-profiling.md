---
id: "tflm-profiling-subroutine-profiling"
type: "concept"
domain: "edge-ai"
title: "Profiling: Subroutine Profiling"
summary: "In order to further dig into performance of specific routines, the MicroProfiler can be used directly from the TFLiteContext or a new MicroProfiler can be created if the TFLiteContext is not available where the profiling needs to happen."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@bd621c2:tensorflow/lite/micro/docs/profiling.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/bd621c2/tensorflow/lite/micro/docs/profiling.md#subroutine-profiling"
license: "Apache-2.0"
mode: "V"
---

In order to further dig into performance of specific routines, the MicroProfiler
can be used directly from the TFLiteContext or a new MicroProfiler can be
created if the TFLiteContext is not available where the profiling needs to
happen. The MicroProfiler's `BeginEvent` and `EndEvent` can be called directly, or
wrapped using a [ScopedMicroProfiler](https://github.com/tensorflow/tflite-micro/blob/bd621c2/tensorflow/lite/micro/docs/../micro_profiler.h).
