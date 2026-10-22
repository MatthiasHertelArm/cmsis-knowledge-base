---
id: "tbx-build-information-files-cbuild-mlops-yml"
type: "concept"
domain: "project"
title: "Build Information Files: File Format / `*.cbuild-mlops.yml`"
summary: "The <solution-name>.cbuild-mlops.yml file contains parameters for MLOps integration. This file is generated when the mlops: node is present in the .csolution.yml file."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/YML-CBuild-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/#cbuild-mlops-yml"
license: "Apache-2.0"
mode: "V"
---

_Part of: File Format_

The `<solution-name>.cbuild-mlops.yml` file contains parameters for [MLOps integration](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/build-overview.md#mlops-integration). This file is generated when the [`mlops:`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#mlops) node is present in the `*.csolution.yml` file. The intent is to provide ML model and NPU parameters (including Vela configuration for Ethos-U) and information for build and test environments.

Refer to [MLOps Integration](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/build-overview.md#mlops-integration) for more information.

`cbuild-mlops:`                                             | Content
:-----------------------------------------------------------|:------------------------------------
    `description:`                           | Descriptive text of the ML model under development.
    `processor:`                             | Processor information for the ML model.
    `npu:`                                   | NPU type and MAC configuration (only present for devices with NPU).
    `vela:`                                  | Vela INI file and option string (only present for Ethos-U NPUs).
    `model:`                                 | Layer location and custom properties for ML model generation. Custom properties may contain scalar values, lists, and nested maps.
       `clayer:`                | Path to the ML model layer, relative to the generated `*.cbuild-mlops.yml` file.
       `<key>:`                 | Custom property preserved from the input `model:` node after recursive variable expansion.
    `hardware:`                              | Hardware test configuration (active target, `cbuild-run` file, and output image list).
    `simulator:`                             | Simulator test configuration (active target, output image list, and FVP invocation details).

**Example:**

```yml
cbuild-mlops:
  description: ML model for detecting Rock/Paper/Scissors images
  processor:
    type: Cortex-M55
  npu:
    type: Ethos-U85
    macs: 256
  vela:
    ini: .cmsis/ensemble_vela.ini
    options: --accelerator-config ethos-u85-256 --system-config RTSS_HE_SRAM_MRAM --memory-mode Shared_Sram
  model:
    clayer: ai_layer/ai_layer.clayer.yml
    framework: ExecuTorch
    source:
      - models/rps_detector.pte
    settings:
      delegate: Ethos-U
      quantize: true
  hardware:
    active: AppKit-E8-U85@HIL
    cbuild-run: out/MyApp+AppKit-E8-U85.cbuild-run.yml
  simulator:
    active: SSE-320-U85@FVP-Test
    model: FVP_Corstone_SSE-320
    config-file: Board/Corstone-320/fvp_config.txt
```
