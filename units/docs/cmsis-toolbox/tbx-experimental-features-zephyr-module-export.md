---
id: "tbx-experimental-features-zephyr-module-export"
type: "concept"
domain: "project"
title: "Experimental Features: Zephyr Module Export"
summary: "This is work in progress and the intended usage is initially for ML models generated for ExecuTorch. However the concept is flexible enough so that it can extend to other software components."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/Experimental-Features.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/Experimental-Features/#zephyr-module-export"
license: "Apache-2.0"
mode: "V"
---

This is work in progress and the intended usage is initially for ML models generated for ExecuTorch. However the concept is flexible enough so that it can extend to other software components. 

The CMSIS-Toolbox 2.14 allows to export a software layer (defined in `*.clayer.yml`) into a Zephyr module so that software delivered as CMSIS-Packs can be integrated in Zephyr builds.

A layer is converted to a Zephyr module with the standard Zephyr entry points:

- `zephyr/module.yml` to declare the module and connect it to CMake/Kconfig integration.
- `Kconfig` options that expose the available CMSIS-Pack components and allow enabling/disabling them via `CONFIG_...` defines.
- `CMakeLists.txt` / `sources.cmake` that map the selected CMSIS-Pack sources and include paths into the Zephyr build.
- Generated compatibility headers (for example `RTE_Components.h` / `Pre_Include_Global.h`) to bridge CMSIS component configuration into the consuming build.

The exported module can then be consumed by a Zephyr application by adding the module path to `ZEPHYR_EXTRA_MODULES` (or through a west manifest) and enabling the desired `CONFIG_...` symbols in `prj.conf`.

Example: the [cmsis-to-zephyr-concept `ml_inference` example](https://github.com/brondani/cmsis-to-zephyr-concept/tree/main/ml_inference) shows a minimal end-to-end flow: exporting a layer as a Zephyr module and consuming it from a Zephyr application.
