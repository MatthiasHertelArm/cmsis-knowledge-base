---
id: "ethint-cmsis-ethos-u-integration-example-project-layout"
type: "concept"
domain: "edge-ai"
title: "CMSIS Ethos-U integration example: Project layout"
summary: "The checked-in Vela outputs are ready to build. After changing an NPU or memory configuration, generate the solution's .cbuild-mlops.yml by opening or building that solution, then recompile the models as described below and in the model converter guide."
status: "draft"
collection: "cmsis-ethos-integration"
source: "Arm-Examples/CMSIS-Ethos-Integration@529e966:README.md"
doc_source: "https://github.com/Arm-Examples/CMSIS-Ethos-Integration/blob/529e966/README.md#project-layout"
license: "Apache-2.0"
mode: "V"
---

| Path | Purpose |
| ---- | ------- |
| [`Test-Ethos-U55.csolution.yml`](https://github.com/Arm-Examples/CMSIS-Ethos-Integration/blob/529e966/Test-Ethos-U55.csolution.yml), [`Test-Ethos-U85.csolution.yml`](https://github.com/Arm-Examples/CMSIS-Ethos-Integration/blob/529e966/Test-Ethos-U85.csolution.yml) | Target, build, and MLOps settings for each NPU |
| [`Test-Ethos-U.cproject.yml`](https://github.com/Arm-Examples/CMSIS-Ethos-Integration/blob/529e966/Test-Ethos-U.cproject.yml) | Shared test application and layer selection |
| [`Board/AppKit-E8_M55_HP/`](https://github.com/Arm-Examples/CMSIS-Ethos-Integration/blob/529e966/Board/AppKit-E8_M55_HP/) | AppKit-E8 board layers, linker configuration, and board setup guide |
| [`Model/`](https://github.com/Arm-Examples/CMSIS-Ethos-Integration/blob/529e966/Model/) | Quantized and Vela-compiled models, model sources, and the ML layer |
| [`Source/test_main.cpp`](https://github.com/Arm-Examples/CMSIS-Ethos-Integration/blob/529e966/Source/test_main.cpp) | Runs both models and checks their outputs |
| [`script/`](https://github.com/Arm-Examples/CMSIS-Ethos-Integration/blob/529e966/script/) | Model converter and its [usage guide](https://github.com/Arm-Examples/CMSIS-Ethos-Integration/blob/529e966/script/README.md) |

The checked-in Vela outputs are ready to build. After changing an NPU or memory
configuration, generate the solution's `*.cbuild-mlops.yml` by opening or
building that solution, then recompile the models as described below and in the
[model converter guide](https://github.com/Arm-Examples/CMSIS-Ethos-Integration/blob/529e966/script/README.md).
