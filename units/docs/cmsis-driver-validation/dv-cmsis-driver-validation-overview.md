---
id: "dv-cmsis-driver-validation-overview"
type: "concept"
domain: "drivers"
title: "CMSIS-Driver Validation: Overview"
summary: "The branch main of this repository contains the code of CMSIS-Driver Validation Suite. User documentation explains the scope and the usage of the framework."
status: "draft"
collection: "cmsis-driver-validation"
source: "ARM-software/CMSIS-Driver_Validation@81a7e18:README.md"
doc_source: "https://arm-software.github.io/CMSIS-Driver_Validation/latest/README.html"
license: "Apache-2.0"
mode: "V"
---

The branch **main** of this repository contains the code of CMSIS-Driver Validation Suite. [User documentation](http://arm-software.github.io/CMSIS-Driver_Validation/main/index.html) explains the scope and the usage of the framework.

[See verified releases](https://github.com/ARM-software/CMSIS-Driver_Validation/releases) of CMSIS-Driver Validation suite in source code archives and in [CMSIS-Pack (.pack)](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/index.html) format as download assets.

Feel free to raise an [issue on GitHub](https://github.com/ARM-software/CMSIS-Driver_Validation/issues) to report a misbehavior (i.e. bugs), start discussions about enhancements or create a pull request with suggested modifications.

### Supported Driver Interfaces

The CMSIS-Driver Validation provides tests for the following CMSIS-Driver interfaces:

Extensive tests with available test servers:
  - **SPI** - Serial Peripheral Interface driver.
  - **USART** - Universal Synchronous and Asynchronous Receiver/Transmitter interface driver.
  - **WiFi** - Wireless Fidelity Interface module/shield driver.

Basic tests:
  - **CAN** - Controller Area Network interface driver.
  - **Ethernet** - Ethernet MAC and PHY peripheral interface driver.
  - **I2C** - Inter-Integrated Circuit multi-master serial single-ended bus interface - driver.
  - **MCI** - Memory Card Interface driver for SD/MMC memory.
  - **USB Device** - Universal Serial Bus Device interface driver.
  - **USB Host** - Universal Serial Bus Host interface driver.
