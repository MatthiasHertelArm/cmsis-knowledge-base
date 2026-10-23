---
id: "ethu-test-ethos-u-ml-models"
type: "concept"
domain: "edge-ai"
title: "Test-Ethos-U: ML models"
summary: "hello_world is the classic TinyML \"hello world\" — the sine-approximation model from the TensorFlow Lite Micro examples, popularized by Pete Warden and Daniel Situnayake's book TinyML. It is the smallest thing that proves the NPU path works end to end."
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@cf13d8d:examples/Test-Ethos-U/README.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/cf13d8d/examples/Test-Ethos-U/README.md#ml-models"
license: "Apache-2.0"
mode: "V"
---

| ML model      | Purpose                                                     |
| ------------- | ----------------------------------------------------------- |
| `hello_world` | Approximates `sin(x)` with the classic TinyML dense network |
| `tiny_cnn`    | Classifies four types of synthetic 16 x 16 stripe patterns  |

`hello_world` is the classic TinyML "hello world" — the sine-approximation
model from the TensorFlow Lite Micro examples, popularized by Pete Warden and
Daniel Situnayake's book *TinyML*. It is the smallest thing that proves the
NPU path works end to end.

`tiny_cnn` was written for this example: a dense-only graph never touches
the convolution, depthwise convolution, and pooling paths that real
workloads depend on. It classifies synthetic 16x16 stripe patterns generated
in-process, so the test needs no external dataset.

Both supplied quantized models compile to **zero CPU operators** — the whole
graph runs on the NPU:

| ML model      | Operators exercised                                                         | Vela result  |
| ------------- | --------------------------------------------------------------------------- | ------------ |
| `hello_world` | `FULLY_CONNECTED`                                                           | 3 NPU, 0 CPU |
| `tiny_cnn`    | `CONV_2D`, `DEPTHWISE_CONV_2D`, `MAX_POOL_2D`, `RESHAPE`, `FULLY_CONNECTED` | 6 NPU, 0 CPU |

The original `.tflite` files are provided so the models can be recompiled for a
different NPU configuration or memory mode.
