---
id: "ocp-mdk-middleware-reference-applicati-demo-mdk-middleware-reference-applicatio"
type: "concept"
domain: "project"
title: "MDK-Middleware Reference Applications Demo: Demo: MDK-Middleware Reference Application - USB Device"
summary: "MDK-Middleware software pack contains components for IPv4 and IPv6 networking, USB Host and Device communication, as well as file system for data storage."
status: "draft"
collection: "ocp-tools-readmes"
source: "Open-CMSIS-Pack/Create-Scalable-SW@8b5a61f:Demo/MDK-MW_RefApp.md"
doc_source: "https://github.com/Open-CMSIS-Pack/Create-Scalable-SW/blob/8b5a61f/Demo/MDK-MW_RefApp.md#demo-mdk-middleware-reference-application-usb-device"
license: "Apache-2.0"
mode: "V"
---

[MDK-Middleware](https://github.com/ARM-software/MDK-Middleware/tree/main/Documentation#readme) software pack contains components for IPv4 and IPv6 networking, USB Host and Device communication, as well as file system for data storage. 

[MDK-Middleware Examples](https://github.com/ARM-software/MDK-Middleware/tree/main/Examples) are reference applications that use defined interfaces (APIs) and are therefore hardware agnostic. These project examples show usage of middleware components and require a board layer with drivers for the specific target hardware.

[USB Device](https://github.com/ARM-software/MDK-Middleware/tree/main/Examples/USB/Device/)
- Open directory `USB Device` in Visual Studio Code (VS Code)
- Tools specified in `vcpkg-configuration.json` are automatically installed
  >Remove `cmsis-toolbox` from `vcpkg-configuration.json` to use the `2.5.0-devint1` version installed locally (when using STM32CubeMX)
- Use bash as command line interface
- Install local packs as described in [Demo Prerequisites](#demo-prerequisites)
- Target: STMicroelectronics B-U585I-IOT02A Board
  - Add target under `target-types:` to `USB_Device.csolution.yml`
    ```
        - type: B-U585I-IOT02A
          board: STMicroelectronics::B-U585I-IOT02A
    ```
  - Run `cbuild setup` to detect compatible board layers
    ```
    cbuild setup USB_Device.csolution.yml
    ```
  - Open `USB_Device.cbuild-idx.yml` and copy the `Board-Layer` variable to `USB_Device.csolution.yml`
    ```
          variables:
            - Board-Layer: <board_layer_path>.Board.clayer.yml
    ```
  - Copy layer to csolution project (use information from `USB_Device.cbuild-idx.yml`)
    ```
    mkdir -p <copy-to>
    cp -r <path> <copy-to>
    ```
  - Adjust `Board-Layer` variable in `USB_Device.csolution.yml` to reflect the copied layer path
  - Build the application: context `HID.Debug` (specify `--packs` to download missing packs)
    ```
    cbuild USB_Device.csolution.yml --context HID.Debug+B-U585I-IOT02A --update-rte --packs
    ```
  - [Optional]: Examine `*.cbuild.yml` which is the Software Bill-Of-Material (BOM) and lists build information, packs, components, licenses, ...
  - List generators
    ```
    csolution list generators USB_Device.csolution.yml
    ```
  - Run generator (CubeMX)
    ```
    csolution run -g CubeMX USB_Device.csolution.yml
    ```
  - Change configuration in STM32CubeMX
    - Tab `Pinout & Configuration`- Category `Security` - Component `AES`: enable `Activated`
    - Run `GENERATE CODE`
  - Updated `Board.cgen.yml` contains new files for AES (`stm32u5xx_hal_cryp.c` and `stm32u5xx_hal_cryp_ex.c`)
  - Build the modified application: context `HID.Debug`
      ```
    cbuild USB_Device.csolution.yml --context HID.Debug+B-U585I-IOT02A --update-rte
    ```
  - Use VS Code CMSIS extensions to build the application
    - Use `...` and `Clean Output Directories` (avoid conflict with previous CLI builds)
    - Use `Manage Solution Settings` - Project Name `HID` and Build Type `Debug`
    - Use `Build`
- Target: NXP EVKB-IMXRT1050 Board
  - Add target under `target-types:` to `USB_Device.csolution.yml`
    ```
        - type: EVKB-IMXRT1050
          board: NXP::EVKB-IMXRT1050
    ```
  - Run `cbuild setup` to detect compatible board layers
    ```
    cbuild setup USB_Device.csolution.yml
    ```
  - Open `USB_Device.cbuild-idx.yml` and copy the `Board-Layer` variable to `USB_Device.csolution.yml`
    ```
          variables:
            - Board-Layer: <board_layer_path>.Board.clayer.yml
    ```
  - Build the application: context `HID.Debug` (specify `--packs` to download missing packs)
    ```
    cbuild USB_Device.csolution.yml --context HID.Debug+EVKB-IMXRT1050 --update-rte --packs
    ```
  - Build the application: context `HID.Debug` with GCC
    ```
    cbuild USB_Device.csolution.yml --context HID.Debug+EVKB-IMXRT1050 --update-rte --toolchain GCC --rebuild
    ```
    >Remove startup for AC6 `<layer_local_path>/RTE/Device/MIMXRT1052DVL6B/startup_MIMXRT1052.S` to bypass current DFP limitation
