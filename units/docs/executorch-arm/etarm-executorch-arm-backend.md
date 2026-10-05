---
id: "etarm-executorch-arm-backend"
type: "concept"
domain: "edge-ai"
title: "ExecuTorch Arm® Backend"
summary: "This subtree contains the Arm® Backend implementation for ExecuTorch. It supports multiple targets using a common infrastructure, that lowers PyTorch models to a TOSA representation. This representation is used to deploy to the following targets:"
status: "draft"
collection: "executorch-arm"
source: "pytorch/executorch@658390c:backends/arm/README.md"
doc_source: "https://github.com/pytorch/executorch/blob/658390c/backends/arm/README.md"
license: "BSD-3-Clause"
mode: "V"
---

This subtree contains the Arm® Backend implementation for ExecuTorch.
It supports multiple targets using a common infrastructure, that lowers
PyTorch models to a TOSA representation. This representation is used to
deploy to the following targets:

- **Arm® Ethos™-U55/65/85** - Compiled using the Ethos-U Vela compiler.
- **VKML using VGF Format, for ML extensions for Vulkan®** – a format containing SPIR-V™ ML operators for Vulkan Machine Learning (VKML) devices.

The backend provides an ahead-of-time (AOT) flow, that produces a PTE file for your
chosen target. The AOT flow supports the following development operating systems:

- Linux aarch64
- Linux x86_64
- macOS™ with Apple® Silicon

In addition, the following deployment paths are supported by this backend:

- Bare metal build of a reference runtime for Arm® Cortex®-M with Ethos-U acceleration:
  - Full testing is available in tree using Corstone™ Fixed Virtual Platforms (FVP).
- Linux target support for VGF capable targets, using the executor_runner.

More information on TOSA can be found here: https://github.com/arm/tosa-specification.
