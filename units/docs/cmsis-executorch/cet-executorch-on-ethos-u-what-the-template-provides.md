---
id: "cet-executorch-on-ethos-u-what-the-template-provides"
type: "concept"
domain: "edge-ai"
title: "ExecuTorch on Ethos-U: What the template provides"
summary: "ExecuTorch on Ethos-U: What the template provides"
status: "draft"
collection: "cmsis-executorch"
source: "Arm-Examples/CMSIS-Executorch@0a243f1:README.md"
doc_source: "https://github.com/Arm-Examples/CMSIS-Executorch/blob/0a243f1/README.md#what-the-template-provides"
license: "Apache-2.0"
mode: "V"
---

- Exporting an ExecuTorch ML model for Ethos-U from a Python virtual environment.
- The pack [`PyTorch::ExecuTorch`](https://www.keil.arm.com/packs/executorch-pytorch/) links only the required and operator components that the ML model needs.
- Managing the NPU and Vela configuration in the CMSIS solution project rather than duplicating it in the Python exporter.
- A three-step flow with a clean hand-over from the CMSIS-Toolbox to an MLOps system: the toolbox describes the target in a `*.cbuild-mlops.yml` file, a script turns that into the AI layer, and the toolbox builds the application.
- Running the finished application on a Corstone-320 FVP simulation model.
