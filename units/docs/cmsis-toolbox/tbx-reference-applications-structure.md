---
id: "tbx-reference-applications-structure"
type: "concept"
domain: "project"
title: "Reference Applications: Structure"
summary: "The following section describes the overall file structure of Reference Applications."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/ReferenceApplications.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/ReferenceApplications/#structure"
license: "Apache-2.0"
mode: "V"
---

The following section describes the overall file structure of *Reference Applications*.

### Project Files

A `*.csolution.yml` project file containing software layers for two different evaluation boards should look like the one shown below. This project contains three examples that show the different features of USB device middleware.

The actual example project (HID, MSC, or CDC1) is selected using a [target-set](https://open-cmsis-pack.github.io/cmsis-toolbox/ReferenceApplications/build-overview.md#working-with-target-set); the compiler is selected using the `--toolchain` option. To translate the HID *Reference Application* for the B-U585I-IOT02A board, use:

```bash
cbuild USB_Device.csolution.yml --active B-U585I-IOT02A@HID --toolchain AC6
```

**Example `USB_Device.csolution.yml` file for two boards with three projects**

```yml
solution:
  created-for: CMSIS-Toolbox@2.4.0
  cdefault:

  target-types:
    - type: B-U585I-IOT02A
      board: B-U585I-IOT02A
      variables:
        - Board-Layer: $SolutionDir()$\Board\B-U585I-IOT02A\Board.clayer.yml
      target-set:
        - set: HID
          images:
            - project-context: HID.Debug
        - set: MSC
          images:
            - project-context: MassStorage.Debug
        - set: CDC1
          images:
            - project-context: VirtualCOM.Debug

    - type: LPC55S69-EVK            # type name identical with board name?
      board: LPC55S69-EVK
      variables:
        - Board-Layer: $SolutionDir()$\Board\LPC55S69-EVK\Board.clayer.yml
      target-set:
        - set: HID
          images:
            - project-context: HID.Debug
        - set: MSC
          images:
            - project-context: MassStorage.Debug
        - set: CDC1
          images:
            - project-context: VirtualCOM.Debug

  build-types:
    - type: Debug
      debug: on
      optimize: debug
    - type: Release
      debug: off
      optimize: balanced

  projects:
    - project: HID/HID.cproject.yml
    - project: MSC/MassStorage.cproject.yml
    - project: CDC1/VirtualCOM.cproject.yml
```

### Typical Directory Structure

The table below shows the typical directory structure of the above example from the programmer's point of view. The software layer in the directory `./Board` is copied from the BSP of the related board.

Directory Content                   | Content
:-----------------------------------|:---------------
`USB_Device.csolution.yml`          | Overall CMSIS solution project file.
`./HID/`                            | HID example project from MDK-Middleware pack.
`./MSC/`                            | MSC example project from MDK-Middleware pack.
`./CDC1/`                           | CDC1 example project from MDK-Middleware pack.
`./Board/B-U585I-IOT02A`            | Board software layer from B-U585I-IOT02A BSP.
`./Board/LPC55S69-EVK`              | Board software layer from LPC55S69-EVK BSP.

### Header File Structure

The interfaces between the software layers are defined in header files. Thus, is it possible to reuse the various software blocks with other build systems that are not CMSIS aware. The following diagram shows the overall header file structure.

(figure: Header File Structure)

The *Reference Application* has no direct access to hardware. Therefore, it does not use the [`CMSIS_device_header`](https://arm-software.github.io/CMSIS_6/latest/Core/using_pg.html#using_packs) provided by the CMSIS-Core that defines the registers and interrupt mapping.

To access target hardware, these header files are used by the *Reference Application*:

- Standardized `Driver API header files` are used for communication with device peripherals. Header files of CMSIS-Drivers are provided by the [CMSIS base software pack](https://arm-software.github.io/CMSIS_6/latest/General/index.html).
- The configuration of the driver interfaces is defined by the `CMSIS_target_header`. This header therefore specifies the available resources of the target hardware that can be used by the *Reference Application*. The [Header File Example](#header-file-example) shows a typical structure of the `CMSIS_target_header`.
- When a shield is applied to an evaluation board, the `CMSIS_shield_header` extends the resource configuration of the `CMSIS_target_header`.

!!! Note
    The driver implementation of the hardware abstraction might use *shim layer* as shown on the right side of above diagram. For example, the [driver implementation for STM32 devices](https://github.com/Open-CMSIS-Pack/CMSIS-Driver_STM32) uses the STM32 HAL.

### Application Program Start

A *Reference Application* starts with the C function `app_main` as shown below.

```c
#include CMSIS_target_header    // board resource definitions

// reference application of a middleware component
int app_main (void)  {

};
```

The application may use an RTOS kernel or run a simple `while` loop. Additional software components such as [CMSIS-View](https://www.keil.arm.com/packs/cmsis-view-arm), [CMSIS-DSP](https://www.keil.arm.com/packs/cmsis-dsp-arm), or [MbedTLS](https://www.keil.arm.com/packs/mbedtls-arm/) are added directly to the *Reference Application*. In general, the `connections:` that are consumed should be minimized, allowing the example to be run on many different target boards.

### Board Layer

The board layer provides system startup, board/device hardware initialization, and transfers control to the application. It also exposes various drivers and interfaces.

**Typical Features:**

- System startup, including clock and memory configuration.
- Device/Board hardware initialization.
- Calls the application startup function.
- Drivers for board peripherals \[optional].
- Interfaces to LEDs and switches \[optional].
- STDIO re-targeting to debug interfaces \[optional].
- Shield setup and drivers for Arduino interfaces \[optional].
- Heap and Stack configuration \[optional].

**Files:**

- CMSIS startup and system file for device initialization.
- `main.c` source module that implements the function `main`.
- Optional drivers and interfaces (CMSIS-Drivers, GPIO, STDIO).
- Files that relate to the device and/or board configuration (i.e. generated by MCUXpresso or STM32CubeMX)
- Linker script definition for boards that require specific memory configurations.

The configuration parameters of the available APIs are defined in `CMSIS_target_header`.

**Generator Usage:**

The board-specific software layer is used in many different projects. When a board configuration is generated by tools, such as MCUXpresso or STM32CubeMX, for example, [configure the generator output directory](https://open-cmsis-pack.github.io/cmsis-toolbox/ReferenceApplications/build-overview.md#configure-generator-output) and import file using the [`generators:`](https://open-cmsis-pack.github.io/cmsis-toolbox/ReferenceApplications/YML-Input-Format.md#generators) node in the `*.clayer.yml` file as shown below:

```yml
layer:

  generators:
    options:
      - generator: CubeMX
        path: ./CubeMX
        name: Board
```

### Shield Layer

A shield layer adds support for additional hardware via plugin shields (i.e. Arduino Uno).  Arduino shields [*consume connections*](https://open-cmsis-pack.github.io/cmsis-toolbox/ReferenceApplications/YML-Input-Format.md#example-sensor-shield) with the prefix `ARDUINO_UNO_`. In the future, other shields may be supported as well.

Shields may feature various hardware modules such as WiFi chips or MEMS sensors. Frequently, the shield's software layer only defines a header file that redirects the Arduino-specific `connect:` to a chip-specific `connect:`, which is then used by application software.

The shield's software layer is configured from the board software layer, which calls the following function:

``` c
extern int32_t shield_setup (void);
```
