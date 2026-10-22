---
id: "ethint-cmsis-ethos-u-integration-example-project-layout"
type: "concept"
domain: "edge-ai"
title: "CMSIS Ethos-U integration example: Project layout"
summary: "CMSIS Ethos-U integration example: Project layout"
status: "draft"
collection: "cmsis-ethos-integration"
source: "Arm-Examples/CMSIS-Ethos-Integration@9b906f5:README.md"
doc_source: "https://github.com/Arm-Examples/CMSIS-Ethos-Integration/blob/9b906f5/README.md#project-layout"
license: "Apache-2.0"
mode: "V"
---

| Path | Purpose |
| --- | --- |
| [`Test-Ethos-U55.csolution.yml`](https://github.com/Arm-Examples/CMSIS-Ethos-Integration/blob/9b906f5/Test-Ethos-U55.csolution.yml), [`Test-Ethos-U85.csolution.yml`](https://github.com/Arm-Examples/CMSIS-Ethos-Integration/blob/9b906f5/Test-Ethos-U85.csolution.yml) | Defines targets, build and MLOps settings |
| [`Test-Ethos-U.cproject.yml`](https://github.com/Arm-Examples/CMSIS-Ethos-Integration/blob/9b906f5/Test-Ethos-U.cproject.yml) | Project file that selects application, ML layer, and board layer |
| [`Source/app_main.cpp`](https://github.com/Arm-Examples/CMSIS-Ethos-Integration/blob/9b906f5/Source/app_main.cpp) | Start the application and runs test |
| [`Model/`](https://github.com/Arm-Examples/CMSIS-Ethos-Integration/blob/9b906f5/Model/) | Model layer containing multiple ML models |
| [`Board/AppKit-E8_M55_HP/`](https://github.com/Arm-Examples/CMSIS-Ethos-Integration/blob/9b906f5/Board/AppKit-E8_M55_HP/) | Contains AppKit-E8 board layer |
| [`script/`](https://github.com/Arm-Examples/CMSIS-Ethos-Integration/blob/9b906f5/script/) | Model converter and its [usage guide](https://github.com/Arm-Examples/CMSIS-Ethos-Integration/blob/9b906f5/script/README.md) |
