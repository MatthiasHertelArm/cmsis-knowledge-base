---
id: "ocp-sensor-sdk-example"
type: "concept"
domain: "project"
title: "Sensor-SDK-Example"
summary: "This software pack demonstrates the usage of CMSIS-Toolbox » Reference Applications for the distribution of Sensor interfaces along with example projects. It contains sensor interface middleware that utilizes I2C or SPI CMSIS-Driver for usage in production code."
status: "draft"
collection: "ocp-tools-readmes"
source: "Open-CMSIS-Pack/Sensor-SDK-Example@3cee161:README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/Sensor-SDK-Example/blob/3cee161/README.md"
license: "Apache-2.0"
mode: "V"
---

This software pack demonstrates the usage of [CMSIS-Toolbox » Reference Applications](https://open-cmsis-pack.github.io/cmsis-toolbox/ReferenceApplications) for the distribution of Sensor interfaces along with example projects. It contains sensor interface middleware that utilizes I2C or SPI [CMSIS-Driver](https://arm-software.github.io/CMSIS_5/Driver/html/index.html) for usage in production code.

The pack is based on the [NXP IoT Sensing Software Development Kit (ISSDK)](https://www.nxp.com/design/design-center/software/sensor-toolbox/iot-sensing-software-development-kit-issdk-embedded-software-framework:IOT-SENSING-SDK) and demonstrates how the CMSIS-Toolbox simplifies the distribution of software frameworks. The example projects that are part of the SDK use interfaces of a board layer that is distributed as part of a Board Support Pack (BSP).  Many board layers are already provided in the BSP packs available on [github.com/Open-CMSIS-Pack](https://github.com/Open-CMSIS-Pack) making it easy to evaluate the NXP sensor Arduino shields with range of different microcontroller boards.

(figure: Select Context Set)

The relevant content of this software pack is in the following directories:

Directory                  | Description
:--------------------------|:------------------------------------
[`sensors`](https://github.com/Open-CMSIS-Pack/Sensor-SDK-Example/blob/3cee161/sensors)       | Interface middleware that connects a sensor to I2C or SPI driver.
[`shields`](https://github.com/Open-CMSIS-Pack/Sensor-SDK-Example/blob/3cee161/shields)       | Contains the mapping of the interface middleware to physical I/O (of an Arduino shield).
[`examples`](https://github.com/Open-CMSIS-Pack/Sensor-SDK-Example/blob/3cee161/examples)     | Demonstrate the usage of the middleware.
[`drivers`](https://github.com/Open-CMSIS-Pack/Sensor-SDK-Example/blob/3cee161/drivers)       | Contains helper functions for the examples.

The Pack Description file [`NXP.ISSDK.pdsc`](https://github.com/Open-CMSIS-Pack/Sensor-SDK-Example/blob/3cee161/NXP.ISSDK.pdsc) defines the software components for [`sensor`](https://github.com/Open-CMSIS-Pack/Sensor-SDK-Example/blob/3cee161/sensors) interface middleware and the [`driver`](https://github.com/Open-CMSIS-Pack/Sensor-SDK-Example/blob/3cee161/drivers) utilities. These software components are used by the [`examples`](https://github.com/Open-CMSIS-Pack/Sensor-SDK-Example/blob/3cee161/examples) but can be also used in the production software.
