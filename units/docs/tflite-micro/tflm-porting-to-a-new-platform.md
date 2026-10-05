---
id: "tflm-porting-to-a-new-platform"
type: "concept"
domain: "edge-ai"
title: "Porting to a new platform"
summary: "At its core, TFLM is a portable library that can be used on a variety of target hardware to run inference on TfLite models."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@3f787dc:tensorflow/lite/micro/docs/new_platform_support.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/3f787dc/tensorflow/lite/micro/docs/new_platform_support.md"
license: "Apache-2.0"
mode: "V"
---

At its core, TFLM is a portable library that can be used on a variety of target
hardware to run inference on TfLite models.

Prior to integrating TFLM with a specific hardware involves tasks that are
outside the scope of the TFLM project, including:

 * Toolchain setup - TFLM requires support for C++17
 * Set up and installation of board-specific SDKs and IDEs
 * Compiler flags and Linker setup
 * Integrating peripherals such as cameras, microphones and accelerometers to
   provide the sensor inputs for the ML models.

In this guide we outline our recommended approach for integrating TFLM with a
new target hardware assuming that you have already set up a development and
debugging environment for your board independent of TFLM.
