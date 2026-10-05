---
id: "cfrt-example-projects-build-and-run"
type: "concept"
domain: "rtos"
title: "Example Projects: Build and Run"
summary: "The Examples solution supports only \"Debug\" Build-Type which is optimized for debugging. It disables compiler optimization and retains all debug-related information. By default, Arm Compiler 6 is used to build the projects."
status: "draft"
collection: "cmsis-freertos"
source: "ARM-software/CMSIS-FreeRTOS@c3e5dc3:Documentation/Doxygen/src/example_projects.md"
doc_source: "https://github.com/ARM-software/CMSIS-FreeRTOS/blob/c3e5dc3/Documentation/Doxygen/src/example_projects.md#build-and-run"
license: "Apache-2.0"
mode: "V"
---

The **Examples** solution supports only "Debug" Build-Type which is optimized for debugging.
It disables compiler optimization and retains all debug-related information. By default,
Arm Compiler 6 is used to build the projects.

### Targets

Each example can be built for multiple target processors. The below table lists supported target
processors together with the corresponding context target-types and model executable that shall
be used for running the application image.

| Target processor | Target-Type | Model Executable       |
|:-----------------|:------------|:-----------------------|
| Cortex-M0        | CM0         | FVP_MPS2_Cortex-M0     |
| Cortex-M0+       | CM0plus     | FVP_MPS2_Cortex-M0plus |
| Cortex-M3        | CM3         | FVP_MPS2_Cortex-M3     |
| Cortex-M4        | CM4         | FVP_MPS2_Cortex-M4     |
| Cortex-M7        | CM7         | FVP_MPS2_Cortex-M7     |
| Cortex-M23       | CM23        | FVP_MPS2_Cortex-M23    |
| Cortex-M23       | CM23_noTZ   | FVP_MPS2_Cortex-M23    |
| Cortex-M33       | CM33        | FVP_MPS2_Cortex-M33    |
| Cortex-M33       | CM33_noTZ   | FVP_MPS2_Cortex-M33    |
| Cortex-M55       | CM55        | FVP_Corstone_SSE-300   |
| Cortex-M55       | CM55_noTZ   | FVP_Corstone_SSE-300   |
| Cortex-M85       | CM85        | FVP_Corstone_SSE-310   |
| Cortex-M85       | CM85_noTZ   | FVP_Corstone_SSE-310   |

### Build in VS Code using Arm Keil Studio Pack extensions

- See [Arm Keil Studio Visual Studio Code Extensions User Guide](https://developer.arm.com/documentation/108029/0000/?lang=en) for more information about using the Keil Studio extensions.
- Search for [Arm Keil Studio Pack](https://marketplace.visualstudio.com/items?itemName=Arm.keil-studio-pack) in the Visual Studio Marketplace to download the extensions.

To build a project using Keil Studio extensions open CMSIS view, open "Manage CMSIS Solution" view and select "Active Context" and "Active Projects". Build Type is automatically selected since there is only one option.

Once the context and projects are selected one can build them by selecting "Build" in CMSIS view.

### Build via command line

- See [CMSIS-Toolbox documentation](https://open-cmsis-pack.github.io/cmsis-toolbox/) to learn more about CMSIS Solution project build and management tools.

To build the project via command line one can use the following command syntax:

```shell
cbuild Examples.csolution.yml --context <project-name>.<build-type>+<target-type>
```

To list the available contexts execute the following command:

```shell
cbuild list contexts Examples.csolution.yml
```

### Execute on Virtual Hardware Target

[Arm Virtual Hardware Target](https://www.arm.com/products/development-tools/simulation/virtual-hardware) simulation models are used to execute the example application images.

To execute application image (axf or elf) on a simulation model use the following command syntax:

```shell
<model-executable> -f ./Board/<target_type>/fvp_config.txt ./out/<project>/<target_type>/Debug/<project>.axf
```
