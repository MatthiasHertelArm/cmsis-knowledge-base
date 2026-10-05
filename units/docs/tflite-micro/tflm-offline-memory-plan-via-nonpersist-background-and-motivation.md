---
id: "tflm-offline-memory-plan-via-nonpersist-background-and-motivation"
type: "concept"
domain: "edge-ai"
title: "Offline Memory Plan Via NonpersistentMemoryPlannerShim: Background and Motivation"
summary: "The (memory management page) describes a way to specify the offset of each non persistent buffer in a flatbuffer model file."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@3f787dc:tensorflow/lite/micro/docs/offline_memory_plan.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/3f787dc/tensorflow/lite/micro/docs/offline_memory_plan.md#background-and-motivation"
license: "Apache-2.0"
mode: "V"
---

The
[(memory management page)](https://github.com/tensorflow/tflite-micro/blob/3f787dc/tensorflow/lite/micro/docs/memory_management.md#offline-planned-tensor-allocations)
describes a way to specify the offset of each non persistent buffer in a
flatbuffer model file. This document describes an alternative that allows the
offset of each non persistent buffer for the Model within the TFLM arena to be
specified by a C++ struct. The approach in this document is an early stage
exploration of what the next version of offline memory planning in TFLM might
look like.

If the NonPersistentMemoryPlannerShim is used, then the final binary does not
have any of the symbols associated with the GreedyMemoryPlanner which results in
a reduced memory footprint.

Additionally, the offline planning of the non-persistent buffers can be used to
have a more efficient utilization compared to the GreedyMemoryPlanner.
