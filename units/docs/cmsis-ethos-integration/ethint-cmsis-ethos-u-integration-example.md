---
id: "ethint-cmsis-ethos-u-integration-example"
type: "concept"
domain: "edge-ai"
title: "CMSIS Ethos-U integration example"
summary: "This repository demonstrates a CMSIS-Toolbox application using TensorFlow Lite Micro and the Arm Ethos-U NPU on the Alif AppKit-E8-AIML board. It provides Ethos-U55 and Ethos-U85 configurations for the board's M55 high-performance core."
status: "draft"
collection: "cmsis-ethos-integration"
source: "Arm-Examples/CMSIS-Ethos-Integration@529e966:README.md"
doc_source: "https://github.com/Arm-Examples/CMSIS-Ethos-Integration/blob/529e966/README.md"
license: "Apache-2.0"
mode: "V"
---

This repository demonstrates a CMSIS-Toolbox application using TensorFlow Lite
Micro and the Arm Ethos-U NPU on the Alif AppKit-E8-AIML board. It provides
Ethos-U55 and Ethos-U85 configurations for the board's M55 high-performance
core. The test runs two Vela-compiled LiteRT models, `hello_world` and
`tiny_cnn`, and compares their outputs with embedded reference values. A
successful run prints `TEST RESULT: PASS` over the board's virtual COM port.
