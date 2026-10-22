---
id: "tbx-csolution-project-format-mlops-management"
type: "concept"
domain: "project"
title: "CSolution Project Format: MLOps Management"
summary: "The mlops: node can be specified in the .csolution.yml file to provide parameters for MLOps integration."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/YML-Input-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/#mlops-management"
license: "Apache-2.0"
mode: "V"
---

The `mlops:` node can be specified in the `*.csolution.yml` file to provide parameters for [MLOps integration](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/build-overview.md#mlops-integration).

When `mlops:` is present, the CMSIS-Toolbox generates an additional information file `*.cbuild-mlops.yml` (in the same folder as the `*.csolution.yml` file) that contains parameters such as processor/NPU configuration, Vela options (for Ethos-U), and information required for building and running tests.

!!! Note
    Custom properties under `model:` may contain simple values, lists, and grouped settings with additional levels. This allows one conversion workflow to process multiple models or related artifacts.

### `mlops:`

`mlops:`                                                 |              | Content
:--------------------------------------------------------|:-------------|:------------------------------------
    `description:`                        |   Optional   | Descriptive text of the ML model under development.
    [`npu:`](#npu)                        |   Optional   | Select the NPU type and MAC configuration.
    [`vela:`](#vela)                      |   Optional   | Vela configuration (only applicable for Ethos-U NPUs).
    [`model:`](#model)                    |   Optional   | Location and custom properties for ML model generation.
    [`hardware:`](#hardware)              |   Optional   | Select the hardware target-set used for tests.
    [`simulator:`](#simulator)            |   Optional   | Select the simulator target-set used for tests.

### `npu:`

`npu:`                                                   |              | Content
:--------------------------------------------------------|:-------------|:------------------------------------
    `type:`                               |   Optional   | NPU type name (default: first NPU from the selected device features).
    `macs:`                               |   Optional   | MAC configuration (default: first MAC configuration from the selected device features).

### `vela:`

The `vela:` node is only relevant for Ethos-U NPUs.

`vela:`                                                  |              | Content
:--------------------------------------------------------|:-------------|:------------------------------------
    `ini:`                                |   Optional   | Explicit Vela INI file (default: use INI file provided by the device/DFP).
    `system:`                             |   Optional   | System configuration selector from the Vela INI file.
    `memory:`                             |   Optional   | Memory configuration selector from the Vela INI file.
    `misc:`                               |   Optional   | Additional Vela command-line options (literal string).

### `model:`

`model:`                                                 |              | Content
:--------------------------------------------------------|:-------------|:------------------------------------
    `clayer:`                             |   Optional   | Path to the layer that contains the ML model under development. The path is resolved and emitted relative to the generated `*.cbuild-mlops.yml` file.
    `<key>:`                              |   Optional   | Custom information (value, list, or sub-groups) for ML model generation. Information is exported in the `model:` node of the generated `*.cbuild-mlops.yml` file.

!!! Note
    [`Variables`](#variables) may be used as values for `clayer:` and custom information in `<key>`, including values in lists and grouped settings. Variables are expanded at every level. An undefined variable expands to an empty string.

### `hardware:`

`hardware:`                                              |              | Content
:--------------------------------------------------------|:-------------|:------------------------------------
    `target:`                             |   Optional   | Explicit target selection in the format `<target-type>[@<target-set>]` (default: first `target-types:` entry and its first target-set).

### `simulator:`

`simulator:`                                             |              | Content
:--------------------------------------------------------|:-------------|:------------------------------------
    `target:`                             |   Optional   | Explicit target selection in the format `<target-type>[@<target-set>]` (default: last `target-types:` entry and its first target-set; typically a target using an Arm FVP debugger).

**Example:**

```yml
solution:
  mlops:
    description: ML model for detecting Rock/Paper/Scissors images
    npu:
      type: Ethos-U85
      macs: 256
    vela:
      ini: .cmsis/ensemble_vela.ini
      system: RTSS_HE_SRAM_MRAM
      memory: Shared_Sram
      misc: --verbose
    model:
      clayer: $AI-Layer$
      framework: ExecuTorch
      source:
        - models/rps_detector.pte
        - $Model-Source$
      settings:
        delegate: Ethos-U
        quantize: true
    hardware:
      target: AppKit-E8-U85@HIL
    simulator:
      target: SSE-320-U85@FVP-Test
```
