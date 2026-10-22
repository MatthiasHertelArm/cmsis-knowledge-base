---
id: "tflm-memory-management-in-tensorflow-li"
type: "concept"
domain: "edge-ai"
title: "Memory Management in TensorFlow Lite Micro"
summary: "This document outlines how memory is managed internally by TensorFlow Lite Micro (TFLM) today. It outlines the \"online\" allocation strategy used by the default TFLM APIs for loading a model into a shared tensor arena."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@bd621c2:tensorflow/lite/micro/docs/memory_management.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/bd621c2/tensorflow/lite/micro/docs/memory_management.md"
license: "Apache-2.0"
mode: "V"
---

This document outlines how memory is managed internally by TensorFlow Lite Micro
(TFLM) today. It outlines the "online" allocation strategy used by the default
TFLM APIs for loading a model into a shared tensor arena.
