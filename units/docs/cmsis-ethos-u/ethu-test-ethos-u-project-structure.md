---
id: "ethu-test-ethos-u-project-structure"
type: "concept"
domain: "edge-ai"
title: "Test-Ethos-U: Project structure"
summary: "Each solution contains one target and share project assembled from:"
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@b2b641e:examples/Test-Ethos-U/README.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/b2b641e/examples/Test-Ethos-U/README.md#project-structure"
license: "Apache-2.0"
mode: "V"
---

Project consists of three solutions:

- `Test-Ethos-U55.csolution.yml`: uses Cortex-M55 and Ethos-U55
- `Test-Ethos-U65.csolution.yml`: uses Cortex-M55 and Ethos-U65
- `Test-Ethos-U85.csolution.yml`: uses Cortex-M85 and Ethos-U85

Each solution contains one target and share project assembled from:

- `Test-Ethos-U.cproject.yml`: connects the layers and test application.
- `Board/Corstone-300/` and `Board/Corstone-320/`: board layers for SSE-300 and SSE-320 FVPs.
- `Model/`: contains TFLM components, tensor arena, original and Vela-compiled models, Vela configuration.
- `script/`: model converter and its documentation.
- `Source/test_main.cpp`: invokes both models and checks their output against the golden vectors.
