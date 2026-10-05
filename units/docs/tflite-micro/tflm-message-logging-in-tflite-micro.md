---
id: "tflm-message-logging-in-tflite-micro"
type: "concept"
domain: "edge-ai"
title: "Message Logging in TFLite Micro"
summary: "TFLM currently support MicroPrintf to log errors or messages to the terminal. This is a light-weight printf-lite utility available to log messages to the terminal."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@3f787dc:tensorflow/lite/micro/docs/logging.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/3f787dc/tensorflow/lite/micro/docs/logging.md"
license: "Apache-2.0"
mode: "V"
---

TFLM currently support `MicroPrintf` to log errors or messages to the terminal. This is a light-weight printf-lite utility available to log messages to the terminal. The `MicroPrintf` calls are designed to be ignored or optimized-out by the compiler, during deployment, if `TF_LITE_STRIP_ERROR_STRINGS` environment flag is set. This is useful to reduce the binary size of the TFLM application.
