---
id: "avh-use-with-keil-vision-project-configuration"
type: "concept"
domain: "test"
title: "Use with Keil µVision: Project Configuration"
summary: "Two important configuration areas need special attention in µVision projects for Arm FVPs:"
status: "draft"
collection: "avh"
source: "ARM-software/AVH@bb8431b:DoxyGen/infrastructure/src/avh_mdk_uv4.md"
doc_source: "https://github.com/ARM-software/AVH/blob/bb8431b/DoxyGen/infrastructure/src/avh_mdk_uv4.md#project-configuration"
license: "Apache-2.0"
mode: "V"
---

Two important configuration areas need special attention in µVision projects for Arm FVPs:

- mdk_uv4_fvp_targets in the project. This is required for new projects or when changing the target device in an
  existing project.
- mdk_uv4_fvp_debug in the project. This step is typically needed for setting up any project, but with reference
  examples brief verification of the default settings can be sufficient.

### Target selection

Device support for Arm FVP targets is implemented with the same CMSIS principles as used for real hardware devices.
[CMSIS-based projects for Arm FVPs](https://github.com/ARM-software/AVH/blob/bb8431b/DoxyGen/infrastructure/src/../../simulation/html/avh_fvp_cmsis.html) lists the device family packs and BSP
packs required for use with Arm FVPs.

When opening an existing project, you will be asked if any missing packs required by the project shall be installed. If
you agree to that, also the necessary pack with device definition for the target device used in the project will be
automatically installed.

When creating a new project or when changing the target in an existing project you need to select an FVP target as follows:

- Install the CMSIS-Pack with target device definition, if not present yet:
    - Start [*Pack Installer*](https://developer.arm.com/documentation/101407/latest/Creating-Applications/Software-Components/Pack-Installer)
      utility.
    - In *Devices* tab expand *ARM* section and select the target Cortex-M core.
    - In the [*Packs*](https://developer.arm.com/documentation/101407/latest/Creating-Applications/Software-Components/Pack-Installer/Packs-Dialog)
      tab under *Device Specific* category select the target CMSIS-Pack that implements the required device according
      to the table in [CMSIS-based projects for Arm FVPs](https://github.com/ARM-software/AVH/blob/bb8431b/DoxyGen/infrastructure/src/../../simulation/html/avh_fvp_cmsis.html).
    - Press *Install* or *Update* button in the Action field to get the latest version installed. For example for Arm
      Cortex-M4:

      (figure: Install device pack for Arm FVP)
    - Observe the button status changed to *Up to date* and return to the project in µVision.
- Select AVH device as the target in your project:
    - In the project open *Options for target...* dialog and select *Device* tab.
    - In the list of device vendors expand *ARM* group.
    - Expand the group of your target Cortex-M core.
    - In the list select the target device according to the table in
      [CMSIS-based projects for Arm FVPs](https://github.com/ARM-software/AVH/blob/bb8431b/DoxyGen/infrastructure/src/../../simulation/html/avh_fvp_cmsis.html) and press *OK*. For example for Arm
      Cortex-M4:

      (figure: Select Arm FVP device as the target)

### Run and debug configuration

Configure execution and debug of an µVision project on an Arm FVP model using the steps explained in the
[Debug Driver Coviguration](https://developer.arm.com/documentation/101407/latest/Simulation/AVH-FVP-Targets/Debug-Driver-Configuration)
for Arm FVP targets.

- In the **Debug** tab, in the **Initilization File** field, use the ... button to provide a path to a file that
  assigns `CORE_CLK` to the same value as specified for the `core_clk.mul` parameter in the model configuration file.
  This ensures that the timing for µVision displays is correctly calculated in synch with the simulation. **Edit**
  button can be used to view and modify the file in the µVision editor. Figure below shows the example configuration
  and content of the files used, *mdk_fvp_config.txt* and *mdk_fvp_init.ini*:

  (figure: MDK Core Clock configuration)
