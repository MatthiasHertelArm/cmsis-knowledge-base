---
id: "ethu-vela"
type: "concept"
domain: "edge-ai"
title: "Vela"
summary: "Arm Vela is an ahead-of-time (AOT) neural network model compiler for the Ethos-U55, Ethos-U65, and Ethos-U85 NPUs."
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@b2b641e:documentation/doxygen/vela/src/main.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/b2b641e/documentation/doxygen/vela/src/main.md"
license: "Apache-2.0"
mode: "V"
---

Arm Vela is an ahead-of-time (AOT) neural network model compiler for the
[Ethos-U55](https://www.arm.com/products/silicon-ip-cpu/ethos/ethos-u55),
[Ethos-U65](https://www.arm.com/products/silicon-ip-cpu/ethos/ethos-u65), and
[Ethos-U85](https://www.arm.com/products/silicon-ip-cpu/ethos/ethos-u85) NPUs.
It converts a quantized TensorFlow Lite
(`.tflite`) or TOSA (`.tosa`) ML model into command streams and encoded constant
data for a selected Ethos-U configuration.

This chapter covers Vela 5.1 and later. Use `vela --version` to identify the
installed version and consult its release notes for version-specific changes.
