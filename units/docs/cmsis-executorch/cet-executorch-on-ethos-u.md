---
id: "cet-executorch-on-ethos-u"
type: "concept"
domain: "edge-ai"
title: "ExecuTorch on Ethos-U"
summary: "(figure: Build and test Ethos-U85-256) (figure: Build and test Ethos-U55-128) (figure: Test Python environment) (figure: License: Apache-2.0) (figure: CMSIS-Toolbox: 2.15) (figure: ExecuTorch: 1.5.1)"
status: "draft"
collection: "cmsis-executorch"
source: "Arm-Examples/CMSIS-Executorch@0a243f1:README.md"
doc_source: "https://github.com/Arm-Examples/CMSIS-Executorch/blob/0a243f1/README.md"
license: "Apache-2.0"
mode: "V"
---

[(figure: Build and test Ethos-U85-256)](https://github.com/Arm-Examples/CMSIS-Executorch/actions/workflows/test-cmsis-executorch.yml)
[(figure: Build and test Ethos-U55-128)](https://github.com/Arm-Examples/CMSIS-Executorch/actions/workflows/test-cmsis-executorch-u55.yml)
[(figure: Test Python environment)](https://github.com/Arm-Examples/CMSIS-Executorch/actions/workflows/test-python-environment.yml)
[(figure: License: Apache-2.0)](https://github.com/Arm-Examples/CMSIS-Executorch/blob/0a243f1/LICENSE)
[(figure: CMSIS-Toolbox: 2.15)](https://open-cmsis-pack.github.io/cmsis-toolbox/)
[(figure: ExecuTorch: 1.5.1)](https://www.keil.arm.com/packs/executorch-pytorch/)

This repository is a template for creating embedded applications that deploy
and run an [ExecuTorch](https://github.com/pytorch/executorch) ML model on an Arm
Ethos-U NPU.

- The [`PyTorch::ExecuTorch`](https://www.keil.arm.com/packs/executorch-pytorch/)
  pack provides the ExecuTorch runtime, required operators, and Ethos-U backend.
- The [`ARM::CMSIS-Ethos-U`](https://www.keil.arm.com/packs/cmsis-ethos-u-arm/overview/)
  pack provides Ethos-U drivers, configuration support, Corstone reference
  integrations and examples, and documentation for deploying ML models on
  Ethos-U.
- The build process uses [CMSIS-Toolbox 2.15.0](https://open-cmsis-pack.github.io/cmsis-toolbox/)
  or higher.

The template can be used for applications targeting any Ethos-U configuration;
the default solution targets the Arm Corstone-320 reference platform with an
Ethos-U85 NPU. The same workflow applies to other ML models, targets, and
applications: export and quantize an ML model developed in PyTorch, delegate it
to Ethos-U, select only the required runtime components, and build it into an
embedded application.
