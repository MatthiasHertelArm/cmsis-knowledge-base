---
id: "tbx-mcuxpresso-for-nxp-devices-overview"
type: "concept"
domain: "project"
title: "MCUXpresso for NXP Devices: Overview"
summary: "The MCUXpresso Config Tool is a graphical tool for configuring an NXP device or board. Based on user settings, MCUXpresso generates C code for project and peripheral initialization."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/MCUXpressoConfig.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/MCUXpressoConfig/#overview"
license: "Apache-2.0"
mode: "V"
---

The [MCUXpresso Config Tool](https://www.nxp.com/configtools) is a graphical tool for configuring an NXP device or board. Based on user settings, MCUXpresso generates C code for project and peripheral initialization. The CMSIS-Toolbox interacts with MCUXpresso Config Tools using the [generic interface for generators](https://open-cmsis-pack.github.io/cmsis-toolbox/MCUXpressoConfig/build-operation.md#generator-integration) and automatically adds generated source code to the project.

The `component: Device:Config Tools` connects a *csolution project* to MCUXpresso. This component imports the MCUXpresso generated files for a selected `device:` or `board:` using the [generator import file](https://open-cmsis-pack.github.io/cmsis-toolbox/MCUXpressoConfig/YML-CBuild-Format.md#generator-import-file) (`*.cgen.yml`). This `*.cgen.yml` file is similar to a [software layer](https://open-cmsis-pack.github.io/cmsis-toolbox/MCUXpressoConfig/build-overview.md#software-layers) but managed by MCUXpresso and should not be modified directly.

An example project created with MCUXpresso can be found in [**csolution-examples/DualCore**](https://github.com/Open-CMSIS-Pack/csolution-examples/tree/main/DualCore).

!!! Note
    - When a board is specified in the *csolution project*, MCUXpresso pre-configures the device peripherals with sensible settings for the evaluation board. The user may change these settings using the MCUXpresso dialogues.
    - When only a device is specified, the user needs to configure the peripherals manually using MCUXpresso dialogs.
