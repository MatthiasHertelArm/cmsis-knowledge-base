---
id: "avh-use-with-keil-studio-target-selection"
type: "concept"
domain: "test"
title: "Use with Keil Studio: Target selection"
summary: "Keil Studio natively supports the Open-CMSIS-Pack format for device support and management of software components. See CMSIS-based projects for AVH FVPs for the list of the device family packs and BSP packs required for use with Arm FVPs."
status: "draft"
collection: "avh"
source: "ARM-software/AVH@bb8431b:DoxyGen/infrastructure/src/avh_mdk_vscode.md"
doc_source: "https://github.com/ARM-software/AVH/blob/bb8431b/DoxyGen/infrastructure/src/avh_mdk_vscode.md#target-selection"
license: "Apache-2.0"
mode: "V"
---

Keil Studio natively supports the [Open-CMSIS-Pack format](https://www.open-cmsis-pack.org/) for device support and
management of software components. See [CMSIS-based projects for AVH FVPs](https://github.com/ARM-software/AVH/blob/bb8431b/DoxyGen/infrastructure/src/../../simulation/html/avh_fvp_cmsis.html)
for the list of the device family packs and BSP packs required for use with Arm FVPs.

- When opening an existing
  [csolution project](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/blob/main/docs/YML-Input-Format.md) in Keil
  Studio, all necessary packs for the target will be automatically installed.
- When creating a new solution, you need to select a target device that corresponds to the Arm FVP model according to
  the table in [CMSIS-based projects for AVH FVPs](https://github.com/ARM-software/AVH/blob/bb8431b/DoxyGen/infrastructure/src/../../simulation/html/avh_fvp_cmsis.html).

You can view the device name defined for the target in the project `csolution.yml` file, or by clicking the
*Manage solution settings* button in the **CMSIS** view, as shown on the image below.
[Manage solutions](https://mdk-packs.github.io/vscode-cmsis-solution-docs/manage_settings.html) explains the concept in
details.

(figure: CMSIS Manage solution settings)
