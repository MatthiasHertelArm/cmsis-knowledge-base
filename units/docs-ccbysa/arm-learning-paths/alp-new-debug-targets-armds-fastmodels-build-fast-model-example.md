---
id: "alp-new-debug-targets-armds-fastmodels-build-fast-model-example"
type: "concept"
domain: "debug"
title: "Add new debug targets to Arm Development Studio: Debug connection to Arm Fast Models: Build Fast Model example"
summary: "A number of ready made example systems are provided with Arm Fast Models, including all of the Fixed Virtual Platform (FVP) examples."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/new_debug_targets_armds/fastmodels.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/new_debug_targets_armds/fastmodels/#build-fast-model-example"
license: "CC-BY-SA-4.0"
mode: "V"
---

A number of ready made example systems are provided with Arm Fast Models, including all of the Fixed Virtual Platform (FVP) examples.

Use the supplied `FVP_MPS2_Cortex-M3` Fast Models example, which is installed in the
```console
FastModelsPortfolio_<version>\examples\LISA\FVP_MPS2\Build_Cortex-M3
```
directory of your Fast Models installation.

Open `System Canvas`, and select `File` > `Load project` from the menu.

Navigate to the `FVP_MPS2_Cortex-M3.sgproj` project as above. Click `Open` to load.

Click `Build` to create the FVP. The FVP executable will be in the appropriate subfolder depending on platform and compiler version, for example:
```text
Win64-Release-VC2019\isim_system_Win64-Release-VC2019.exe
```
