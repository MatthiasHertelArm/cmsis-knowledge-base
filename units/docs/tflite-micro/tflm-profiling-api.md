---
id: "tflm-profiling-api"
type: "concept"
domain: "edge-ai"
title: "Profiling: API"
summary: "The MicroInterpreter class constructor contains an optional profiler argument. This profiler must be an instance of the tflite::MicroProfilerInterface class, and should implement the BeginEvent and EndEvent methods."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@f7ed40d:tensorflow/lite/micro/docs/profiling.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/f7ed40d/tensorflow/lite/micro/docs/profiling.md#api"
license: "Apache-2.0"
mode: "V"
---

The MicroInterpreter class constructor contains an optional profiler argument.
This profiler must be an instance of the `tflite::MicroProfilerInterface` class, and should
implement the `BeginEvent` and `EndEvent` methods. There is a default implementation
in `tensorflow/lite/micro/micro_profiler.cc` which can be used for most purposes.

The best practice for profiling across multiple invocations is to reset or call
`ClearEvents()` in between invocations.
