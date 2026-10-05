---
id: "alp-observing-ethos-u-on-alif-6-alif-cmsis-project-configure-the-project-file"
type: "concept"
domain: "edge-ai"
title: "Run MNIST on an Alif E8 Ensemble DevKit using ExecuTorch and Ethos-U85: Create the Alif E8 CMSIS project: Configure the project file"
summary: "The mnist_executorch/mnist_executorch.cproject.yml file describes the MNIST application: its source files, components, include paths, and build options."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/6-alif-cmsis-project.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/6-alif-cmsis-project/#configure-the-project-file"
license: "CC-BY-SA-4.0"
mode: "V"
---

The `mnist_executorch/mnist_executorch.cproject.yml` file describes the MNIST application: its source files, components, include paths, and build options.

Locate this file and replace the contents with the following configuration:

```yaml
# yaml-language-server: $schema=https://raw.githubusercontent.com/Open-CMSIS-Pack/devtools/tools/projmgr/2.6.0/tools/projmgr/schemas/cproject.schema.json
project:
  groups:
    - group: App
      files:
        - file: main.cpp
        - file: executorch_runner.cpp
        - file: executorch_runner.h
        - file: SEGGER_RTT_Conf.h
        - file: assets/mnist_model_data.h

    - group: SEGGER_RTT
      files:
        - file: ../libs/SEGGER_RTT_V796h/RTT/SEGGER_RTT.c
        - file: ../libs/SEGGER_RTT_V796h/RTT/SEGGER_RTT_printf.c
        - file: ../libs/SEGGER_RTT_V796h/Syscalls/SEGGER_RTT_Syscalls_GCC.c

  output:
    base-name: $Project$
    type:
      - elf
      - bin

  layers:
    - layer: ../device/ensemble/alif-ensemble.clayer.yml

  packs:
    - pack: AlifSemiconductor::Ensemble
    - pack: ARM::ethos-u-core-driver

  components:
    - component: ARM::Machine Learning:NPU Support:Ethos-U Driver&Generic U85

  define:
    - C10_USING_CUSTOM_GENERATED_MACROS
    - ETHOSU
    - ETHOSU85

  add-path:
    - .
    - assets
    - ../libs/SEGGER_RTT_V796h/RTT
    - ../third_party/executorch/et_bundle/include
    - ../third_party/executorch/et_bundle/include/executorch/runtime/core/portable_type/c10

  misc:
    - for-compiler: GCC
      C-CPP:
        - -std=c++17
        - -fno-rtti
        - -fno-exceptions
        - -DETHOSU_ARCH=u85
        - -DETHOSU_MACS=256
        - -DETHOSU_MODEL=1
      Link:
        - -L/absolute/path/to/third_party/executorch/et_bundle/lib
        - -Wl,--whole-archive
        - -lexecutorch
        - -lexecutorch_core
        - -lexecutorch_delegate_ethos_u
        - -lcortex_m_ops_lib
        - -Wl,--no-whole-archive
        - -Wl,--start-group
        - -lextension_runner_util
        - -lcortex_m_kernels
        - -lportable_ops_lib
        - -lportable_kernels
        - -lquantized_ops_lib
        - -lquantized_kernels
        - -lkernels_util_all_deps
        - -lcmsis-nn
        - -lflatccrt
        - -Wl,--end-group
```

**Warning:**
Update the `-L` path to match the absolute path to your `third_party/executorch/et_bundle/lib` directory. For example: `-L/Users/username/mnist_alif/alif_vscode-template/third_party/executorch/et_bundle/lib`.


There are several important details in this configuration:

- `--whole-archive` is required for `libexecutorch`, `libexecutorch_core`, `libexecutorch_delegate_ethos_u`, and `libcortex_m_ops_lib`. These libraries contain static registration constructors — for operator registration and PAL symbols — that the linker would otherwise discard as unused.
- Don't add `portable_ops_lib` or `quantized_ops_lib` to `--whole-archive`. They are large and will overflow the microcontroller's ITCM or MRAM.
- `--start-group` and `--end-group` resolve circular dependencies among the remaining libraries.
- `C10_USING_CUSTOM_GENERATED_MACROS` tells ExecuTorch to skip looking for a `cmake_macros.h` header that doesn't exist in the bare-metal build.
- The c10 include path provides the tensor type definitions that ExecuTorch's headers depend on.
