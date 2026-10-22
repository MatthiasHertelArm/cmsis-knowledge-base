---
id: "tbx-reference-applications-types-of-reference-applications"
type: "concept"
domain: "project"
title: "Reference Applications: Types of Reference Applications"
summary: "The MDK-Middleware provides software components for IPv4/IPv6 networking, USB Host/Device communication, and a variety of file systems for data storage."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/ReferenceApplications.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/ReferenceApplications/#types-of-reference-applications"
license: "Apache-2.0"
mode: "V"
---

*Reference Applications* may show the usage of middleware, software libraries, and custom code that can run on physical hardware or an FVP simulation model. Such software uses [application programming interfaces (APIs)](https://en.wikipedia.org/wiki/API) to interface with hardware interfaces or other software components.

### MDK-Middleware Reference Applications

The [MDK-Middleware](https://www.keil.arm.com/packs/mdk-middleware-keil) provides software components for IPv4/IPv6 networking, USB Host/Device communication, and a variety of file systems for data storage.

The MDK-Middleware software pack contains Reference Applications that show how to use these software components. These examples are target agnostic; adding a compatible layer that provides the required APIs allows running the example project on physical hardware or an FVP simulation model.

(figure: MDK-Middleware Example)

The picture above shows how a USB HID example connects to a board-specific software layer.
The *Reference Application* does not specify a target. For execution, a software layer is required that provides the target-specific APIs. These layers may support a physical board or an FVP simulation model and are typically provided in BSP packs.

The Reference example uses [`connections:`](https://open-cmsis-pack.github.io/cmsis-toolbox/ReferenceApplications/YML-Input-Format.md#connections) to list the consumed (required) APIs. The board layer in the BSP pack provides these [`connections:`](https://open-cmsis-pack.github.io/cmsis-toolbox/ReferenceApplications/YML-Input-Format.md#connections) and may offer several additional `connections:`, making the layer suitable for a wide range of Reference Applications.

As the *Reference Application* is not target-specific, it does not define a target type or add a target-specific software layer. It requires two steps to configure the `*.csolution.yml` file for an evaluation board or FVP simulation model. Refer to the [Usage](#usage) section for more information.

!!! Note
    Keep the Reference Application valid for `csolution`: do not add a placeholder target such as `${Name}`. Omit `target-types:` when the application provides no target, or retain only fully configured targets such as an FVP test target. A target for the selected hardware can be added when the application is configured.

### Targeting FVP Simulation Models

An [Arm Fixed Virtual Platform (FVP)](https://open-cmsis-pack.github.io/cmsis-toolbox/ReferenceApplications/YML-Input-Format.md#arm-fvp) can replace a physical board when the required interfaces are provided by an FVP-compatible software layer. Configure the Reference Application with the DFP or BSP that describes the simulated platform, select its virtual board or device, and add the compatible layer. A `target-set:` using the `Arm-FVP` debugger can then identify the model and its configuration file. The application sources remain unchanged when switching between compatible physical and simulated targets.

***Reference Application* `*.csolution.yml` file**

```yml
solution:
  cdefault:
  compiler: AC6
  :
  packs:
# Step 1: Specify DFP and BSP for the device and board, for example with:
#   - pack: Keil::STM32U5xx_DFP
#   - pack: Keil::B-U585I-IOT02A_BSP

# Step 1: Specify your board, for example with:
# target-types:
#   - type: STM32U585
#     board: B-U585I-IOT02A
# Step 2: Run `cbuild setup` and use cbuild-idx.yml to identify variables, for example:
#     variables:
#       - Board-Layer: $SolutionDir()$/Board/B-U585I-IOT02A/Board.clayer.yml
```

### Sensor Reference Applications

The overall concept of *Reference Applications* and the same board-specific software layers can be used for a wide range of software stacks. For example, a sensor SDK pack may provide *Reference Applications* that show the usage of a MEMS sensor. This MEMS sensor is additional hardware that could be provided by a widely supported Arduino UNO shield.

The sensor SDK with the related Arduino shield can be structured to work with a wide range of evaluation boards that offer a compatible board-specific software layer.

The overall structure of a sensor example project is shown in the picture below. It is composed of:

- The *Reference Application* with sensor-specific middleware that shows the usage of a MEMS sensor.
- `Layer type: Board` contains the hardware-specific setup of an evaluation board with a Cortex-M processor along with drivers, i.e. for SPI or I2C that connect to the pins of the Arduino shield.
- `Layer type: Shield` defines the pin routing of the Arduino UNO shield, which adds the MEMS sensor to the evaluation board.

(figure: Sensor Reference Application)

!!! Note
    As the `connections:` for the MEMS sensor are specific to the sensor itself, the same *Reference Application* also works with an evaluation board that integrates the MEMS sensor (and, therefore, requires no Shield layer). In this case, the board-specific software layer adds the sensor-specific `connections:`.

### Targeting Custom Hardware

A *Reference Application* may serve as a starting point for user applications that target custom hardware.

It is required to provide:

- A software layer with a compatible set of APIs (`connections:`) consumed by the *Reference Application*. This software layer can be added along with the target type (in the `*.csolution.yml` file) that defines the custom hardware.

!!! Note
    It is not required to define `connections:` as this information is only used to identify compatible layers.

- A header file that replaces the `CMSIS_target_header`. Refer to [Header File Structure](#header-file-structure) for more information.

**Example `*.csolution.yml` file for custom hardware**

```yml
solution:
  cdefault:
  compiler: AC6
  :
  target-types:
    - type: MyHardware
      device: STM32U585AIIx      # custom hardware uses only a device definition
      variables:
        - Board-Layer:  $SolutionDir()$/MyTarget/MyHardware.clayer.yml
```

**Example MyHardware.clayer.yml**

You may use a `*.clayer.yml` file for implementing the HAL drivers for the application and define the `CMSIS_target_header` as shown below:

```yml
layer:
  :
  define:
    - CMSIS_target_header: "\"MyHardware.h\""
```
