---
id: "vela-vela"
type: "concept"
domain: "edge-ai"
title: "Vela"
summary: "Vela is a compiler for Arm Ethos-U NPU edge AI devices. It is used to convert neural networks defined in TOSA or TensorFlow Lite/LiteRT format into Ethos-U command streams."
status: "draft"
collection: "ethos-u-vela"
source: "artificial-intelligence/ethos-u/ethos-u-vela@4bd6685:README.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/4bd6685/README.md"
license: "Apache-2.0"
mode: "V"
---

Vela is a compiler for [Arm Ethos-U NPU](https://www.arm.com/products/silicon-ip-cpu)
edge AI devices.  It is used to convert neural networks defined in [TOSA](https://www.mlplatform.org/tosa/)
or [TensorFlow Lite/LiteRT](https://ai.google.dev/edge/litert) format into
Ethos-U command streams.

The input network must have quantised activations and quantised weights in order
to be accelerated by the Ethos-U.

More details about Ethos-U devices:
* Ethos-U55, [product](https://www.arm.com/products/silicon-ip-cpu/ethos/ethos-u55) and [developer](https://developer.arm.com/Processors/Ethos-U55) information
* Ethos-U65, [product](https://www.arm.com/products/silicon-ip-cpu/ethos/ethos-u65) and [developer](https://developer.arm.com/Processors/Ethos-U65) information
* Ethos-U85, [product](https://www.arm.com/products/silicon-ip-cpu/ethos/ethos-u85) and [developer](https://developer.arm.com/Processors/Ethos-U85) information
