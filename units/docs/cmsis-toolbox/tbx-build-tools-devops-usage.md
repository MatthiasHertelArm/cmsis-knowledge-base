---
id: "tbx-build-tools-devops-usage"
type: "concept"
domain: "project"
title: "Build Tools: DevOps Usage"
summary: "The CMSIS-Toolbox supports Continuous Integration (CI) tests in DevOps systems. The ./out directory contains all build artifacts of an application for execution on physical hardware or simulation models."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/build-tools.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/build-tools/#devops-usage"
license: "Apache-2.0"
mode: "V"
---

The CMSIS-Toolbox supports Continuous Integration (CI) tests in DevOps systems. The `./out` directory contains all build artifacts of an application for execution on physical hardware or simulation models. [Arm Fixed Virtual Platforms (FVPs)](https://open-cmsis-pack.github.io/cmsis-toolbox/build-tools/YML-Input-Format.md#arm-fvp) enable unit and integration testing with simulation models and virtual interfaces. Using [software layers](https://open-cmsis-pack.github.io/cmsis-toolbox/build-tools/build-overview.md#software-layers) allows the same application to be tested on physical hardware or an FVP simulation model. The following commands show typical usage of the CMSIS-Toolbox build system in CI environments.

The commands below show typical builds in a CI system. Using `--packs` installs all public packs with implicit acceptance of licenses. This command builds all projects, target-types, and build-types. Using [`--context`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-tools/build-overview.md#context) reduces the scope of the build. Using [`--frozen-packs`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-tools/build-overview.md#reproducible-builds) uses exactly the packs that are specified in the file `*.cbuild-pack.yml`.

```shell
cbuild Hello.csolution.yml --packs                          # install packs and build all targets
cbuild Hello.csolution.yml --packs --active FVP-SSE-300     # build FVP target
cbuild Hello.csolution.yml --packs --frozen-packs           # use exact pack versions of *.cbuild-pack.yml
```

Packs that are not public are installed using `cpackget`.  The following commands use the MDK-Middleware development repository to install a pre-release pack in a GitHub Actions CI workflow.

```yml
    - name: Checkout MDK-Middleware
      uses: actions/checkout@v4
      with:
        repository: ARM-software/MDK-Middleware
        path: ./MDK-Middleware

    - name: Initialize CMSIS pack system and use MDK-Middleware pack from development repo
      run: |
        cpackget init https://www.keil.com/pack/index.pidx
        cpackget update-index
        cpackget add ./MDK-Middleware/Keil.MDK-Middleware.pdsc
```

### Examples

Several [Arm examples](https://github.com/Arm-Examples) show CI workflows using the CMSIS-Toolbox.

Example            | Description
:------------------|:------------------
[AVH-Hello](https://github.com/Arm-Examples/AVH-Hello) | Build and execution test for a "Hello World" example using a GitHub Actions matrix with Cortex-M FVP simulation models and Arm Compiler or GCC.
[AVH_CI_Template](https://github.com/Arm-Examples/AVH_CI_Template)     | CI Template for unit test automation that uses GitHub Actions.
[CMSIS Version 6](https://github.com/ARM-software/CMSIS_6/actions) | Runs a CMSIS-Core validation test across the supported processors using multiple compilers.
[RTOS2 Validation](https://github.com/ARM-software/CMSIS-RTX/actions) | Runs the CMSIS-RTOS2 validation across Keil RTX using source and library variants.
[STM32H743I-EVAL_BSP](https://github.com/Open-CMSIS-Pack/STM32H743I-EVAL_BSP) | Build test of a Board Support Pack (BSP) with MDK-Middleware [Reference Applications](https://open-cmsis-pack.github.io/cmsis-toolbox/build-tools/ReferenceApplications.md) using Arm Compiler or GCC. The artifacts store the various example projects for testing on the hardware board.
