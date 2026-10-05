---
id: "spec-recommended-terminology-general"
type: "concept"
domain: "pack"
title: "Recommended terminology: General"
summary: "Recommended terminology: General"
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doc/Glossary.md"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/Glossary.html"
license: "Apache-2.0"
mode: "V"
---

- **API**
  An application programming interface defines the interactions between multiple software
  intermediaries. They are what Open-CMSIS-Pack components publicly expose for the other components to use.
- **API extension**
  A set of methods and types exposed by a Open-CMSIS-Pack Component expanding the capabilities of another
  Open-CMSIS-Pack component.
- [**Baremetal application**](https://en.wikipedia.org/wiki/Bare_metal)
  **Bare metal** refers to a computer executing instructions directly on logic hardware without an
  intervening operating system. On Cortex-M target this is generally understood as an application
  running in a single thread without task-scheduling. A bare-metal application may still use interrupts.
- **Bootstrap**
  Bootstrapping is a self-starting process that is supposed to proceed without external input.
  - **Application bootstrap**
    Covers the operation related to the application specific operations such as setup of the
    connectivity stacks as well as the various middleware constituting the application.
  - **Device bootstrap**
    Covers the operation related to the board/product startup. E.g. clock initialisation, external
    peripheral reset and initialisation.
- **BSP** / **Board Support Package**
  A component providing board-specific support.
  This component typically provides through direct implementation or through dependencies, the device
  bootstrap and exposes the device specific features such as functions to get peripherals and/or bus
  instances,  pin multiplexing etc.
- **Components**
    The use of *component* on its own is deprecated because ambiguous. Please use one of those more
    specific forms instead:
  - **API component**
    A specialization of a software component that describes an interface. It must also document all
    expected behaviour of the API implementation as well as correct usage of the API.
  - **Implementation Component**
    A component that implements an interface. Such component may export an API extension.)
  - **Software component**
    A software component is a basic building block for the construction of applications. It is a set
    of files, include paths, configurations and dependencies. It can optionally implement one or
    more API.
- **Connectivity**
  Any technology used to interact with entities beyond the device's boundary.
  For example, a UART interface may be considered connectivity when used as a Modbus server endpoint.
- **Dependency**
  In context of software components is a relationship where one software component requires anything
  from the other software component or API component or configuration or tool chain or hardware.
- **External peripheral**
  A piece of hardware external to the chip running the code.
  It may be controlled through a hardware-accelerated bus interface or a bit-banged bus interface.
- **Host** / **Host platform**
  A machine running a desktop/server grade OS.
- **Hardware (HW) Platform**
  A piece of hardware running an embedded application. This can be anything from development kits to
  standalone System on Chips or for example an IoT device.
- **IoT OS**
  A set software stacks typically used by IoT devices and provided by an OS vendor (Mbed, Zephyr,
  AWS FreeRTOS, Azure RTOS, ...). An IoT OS is typically made of a kernel (the RTOS), a connectivity
  stack (IP, BLE etc), a storage stack (block devices, file systems etc) and other middleware.
- **Internal** / **On-chip peripheral**
  A piece of hardware internal to the chip running the code.
  It is controlled through the chip memory space.
- **Pack** / **Software Pack**
  A collection of files including a [Pack Description](#pack-desc) file forming
  one or more [Software Component](#component)(s) to be distributed, e.g. as an
  archive or through a [Software Repository](#software-repository).
- **Pack Description** (PDSC)
  A machine readable file containing meta data for one or more [Software Component](#component)(s)
  maintained and shipped alongside.
- **Pack Index**
  A machine readable index file of available [Pack](#software-pack)s and their according
  origin. The origin can be the location a [Pack](#software-pack) archive can be fetched from
  or a [Software Repository](#software-repository) to refer to.
- **(Local) Packs Folder**
  A location within an [Application Developer](https://github.com/ARMmbed/Open-CMSIS-Pack-architecture/wiki/Requirements#application-developer)'s
  development environment where [Pack](#software-pack)s are stored to (unarchived).
- **Peripheral driver** / **Hardware Abstraction Layer (HAL)**
  A piece of software interacting with some piece of hardware either as an *internal peripheral* through the memory bus or as an *external peripheral* through an ADC input, a SPI bus, or an I²C bus.
  In the context of Open-CMSIS-Pack, Peripheral driver and HAL driver are synonyms.
  Examples include:
  - The software driving a CRC hardware acceleration
  - The software driving a sensor, for example an accelerometer
  - The software driving a stepper motor controller
- **Real-Time Operating System (RTOS)**
  Part of the OS that implements threading, real-time scheduling and related operations.
  Some well known RTOS for microcontrollers include FreeRTOS (used in AWS-FreeRTOS), RTX (used in Mbed-OS), and ThreadX (used in Azure RTOS).
- **Software Repository**
  Arbitrary directory structure containing files typically version controlled
  by a [VCS](https://en.wikipedia.org/wiki/Version_control).
