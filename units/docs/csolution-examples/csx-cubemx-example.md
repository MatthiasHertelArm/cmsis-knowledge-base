---
id: "csx-cubemx-example"
type: "concept"
domain: "project"
title: "CubeMX Example"
summary: "This csolution project shows the usage of STM32CubeMX which uses a generator import file to obtain the device configuration and HAL driver source files."
status: "draft"
collection: "csolution-examples"
source: "Open-CMSIS-Pack/csolution-examples@02f71b2:CubeMX/README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/csolution-examples/blob/02f71b2/CubeMX/README.md"
license: "Apache-2.0"
mode: "V"
---

This *csolution project* shows the usage of [STM32CubeMX](https://www.st.com/en/development-tools/stm32cubemx.html) which uses a [generator import file](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format#generator-import-file) to obtain the device configuration and HAL driver source files.

This project uses two different target-types to configure execution from Flash ROM or execution from RAM. It uses a [variable](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format#variables) to define the regions header file for each target in the file [`CubeMX.csolution.yml`](https://github.com/Open-CMSIS-Pack/csolution-examples/blob/02f71b2/CubeMX/./CubeMX.csolution.yml).
