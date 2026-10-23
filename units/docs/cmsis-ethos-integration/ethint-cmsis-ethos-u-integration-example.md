---
id: "ethint-cmsis-ethos-u-integration-example"
type: "concept"
domain: "edge-ai"
title: "CMSIS Ethos-U integration example"
summary: "This application tests Vela-compiled LiteRT models on the Alif AppKit-E8-AIML board, using its M55 high-performance core and Arm Ethos-U NPU. Separate solutions provide Ethos-U55 and Ethos-U85 configurations."
status: "draft"
collection: "cmsis-ethos-integration"
source: "Arm-Examples/CMSIS-Ethos-Integration@9b906f5:README.md"
doc_source: "https://github.com/Arm-Examples/CMSIS-Ethos-Integration/blob/9b906f5/README.md"
license: "Apache-2.0"
mode: "V"
---

This application tests Vela-compiled LiteRT models on the Alif AppKit-E8-AIML
board, using its M55 high-performance core and Arm Ethos-U NPU. Separate
solutions provide Ethos-U55 and Ethos-U85 configurations.

The application runs selected models through Ethos-U and compares its output
with embedded reference data. A successful run reports `TEST RESULT: PASS`.
