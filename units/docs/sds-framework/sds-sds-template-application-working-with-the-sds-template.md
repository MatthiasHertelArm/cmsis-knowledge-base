---
id: "sds-sds-template-application-working-with-the-sds-template"
type: "concept"
domain: "test"
title: "SDS Template Application: Working with the SDS Template"
summary: "The SDS template application and SDSIO interface layers are part of the SDS pack."
status: "draft"
collection: "sds-framework"
source: "ARM-software/SDS-Framework@4459441:documentation/template.md"
doc_source: "https://github.com/ARM-software/SDS-Framework/blob/4459441/documentation/template.md#working-with-the-sds-template"
license: "Apache-2.0"
mode: "V"
---

The SDS template application and [SDSIO interface layers](https://github.com/ARM-software/SDS-Framework/blob/4459441/documentation/sdsio.md) are part of the [SDS pack](https://www.keil.arm.com/packs/sds-arm).

Several [Board Support Packs (BSP)](https://www.keil.arm.com/packs/) contain board layers that support the required API interfaces. Refer to the *Overview* page of the pack to check the *Provided connection API Interface* of the layers. The table below lists the required API interfaces that should be provided by the `Board-Layer`.  

Required API Interface      | Description     |
:---------------------------|:----------------|
[**SDSIO File System**](https://github.com/ARM-software/SDS-Framework/blob/4459441/documentation/sdsio.md#layer-sdsio_fs)  |  |
CMSIS_MCI                   | [CMSIS-Driver MCI](https://arm-software.github.io/CMSIS_6/latest/Driver/group__mci__interface__gr.html) interface to memory card. |
CMSIS_VIO, STDOUT, STDERR   | For user button and printf output. |
[**SDSIO Network**](https://github.com/ARM-software/SDS-Framework/blob/4459441/documentation/sdsio.md#layer-sdsio_network)  |  |
CMSIS_ETH                   | [CMSIS-Driver Ethernet](https://arm-software.github.io/CMSIS_6/latest/Driver/group__eth__interface__gr.html) MAC/PHY interface. |
CMSIS_VIO, STDOUT, STDERR   | For user button and printf output. |
[**SDSIO USB Device**](https://github.com/ARM-software/SDS-Framework/blob/4459441/documentation/sdsio.md#layer-sdsio_usb)   |  |
CMSIS_USB_Device            | [CMSIS-Driver USB Device](https://arm-software.github.io/CMSIS_6/latest/Driver/group__usbd__interface__gr.html) interface. |
CMSIS_VIO, STDOUT, STDERR   | For user button and printf output. |

!!! Note
    - RTT has no API interface requirements to a board layer and may be used when no compatible board layer is available.
    - When no board layer is available, it is possible to [create a compatible board layer](https://open-cmsis-pack.github.io/cmsis-toolbox/ReferenceApplications/#structure).

### Using VS Code

This section explains how to use SDS template application with the [Arm CMSIS Solution](https://marketplace.visualstudio.com/items?itemName=Arm.cmsis-csolution) for VS Code. This extension is for example part of the [Keil Studio](https://www.keil.arm.com/).

The example below uses the [STM32F746G-DISCO](https://www.keil.arm.com/packs/stm32f746g-disco_bsp-keil) board, which provides interfaces for all SDSIO communication interfaces.

#### Install Required Packs

To make the software components available, install the SDS pack and the pack for the selected evaluation board, for example with:

```shell
>cpackget add ARM::SDS
>cpackget add Keil::STM32F746G-DISCO_BSP
```

#### Create New Solution

In the [**Create a new solution**](https://mdk-packs.github.io/vscode-cmsis-solution-docs/create_app.html) dialog, select the target board and the SDS reference application.

(figure: Select Reference Application)

After the *csolution project* loads, VS Code displays a dialog where you can select a compatible software layer and an installed compiler toolchain.

!!! Note
    - If no compatible software layer is available for SDS, use the `V2M-MPS3-SSE-300-FVP` board. Then adapt `SDS.csolution.yml` and create a software layer for your target hardware as outlined in [Compile for Custom Hardware](#compile-for-custom-hardware). The [layer: sdsio_rtt](https://github.com/ARM-software/SDS-Framework/blob/4459441/documentation/sdsio.md#layer-sdsio_rtt) has minimal requirements because it uses the debug adapter as the communication interface to the SDSIO-Server.

(figure: Configure Solution)

!!! Note
    - The **Add Software Layer** dialog only appears when the BSP contains a board layer with compatible API Interfaces (see next section).
    - ST board layers are configured for the Arm Compiler (AC6) using STM32CubeMX.  However, it is easy to reconfigure for different compilers. The steps are provided in the BSP overview.

#### Build the Template Application

The SDS template application contains three targets (an evaluation board and two AVH FVP simulation models) and two projects:

- **DataTest** is a data communication test between target and SDSIO-Server or file system.
- **AlgorithmTest** allows you to add the DSP or ML algorithm that should be tested.

Use the `CMSIS:Manage Solution Settings` command to select the project you want to explore. Start with **DataTest**, which should work out of the box on target hardware.

(figure: Select Project)

Once the project is selected and the debug adapter is configured, save the solution and use the build command to generate the template application. Then download the application to the selected target.

### Compile for Custom Hardware

The steps to add a custom hardware configuration are:

- Open the `*.csolution.yml` file and add a new `target-type`.

```yml
  packs:
    - pack: <DFP for your hardware> # use keil.arm.com/packs to search for packs

  target-types:
    - type: MyHardware
      device: STM32U535CBTx
      variables:
        - Board-Layer: $SolutionDir()$/Board/MyHardware/Board.clayer.yml
        - SDSIO-Layer: $SolutionDir()$/sdsio/rtt/sdsio_rtt.clayer.yml
```

- Add a board layer that implements the API interfaces described above.

!!! Note
    - You may copy an existing board layer as starting point. But typically these board layers support a range of reference applications and contain driver API interfaces that may be removed.
    - The step above allows also manual configuration without using the VS Code IDE.
