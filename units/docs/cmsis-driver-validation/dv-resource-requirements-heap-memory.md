---
id: "dv-resource-requirements-heap-memory"
type: "concept"
domain: "drivers"
title: "Resource Requirements: Heap Memory"
summary: "Heap memory is used by the memory allocation functions."
status: "draft"
collection: "cmsis-driver-validation"
source: "ARM-software/CMSIS-Driver_Validation@81a7e18:Documentation/Doxygen/src/DriverValidation.txt"
doc_source: "https://arm-software.github.io/CMSIS-Driver_Validation/latest/resource_requirements.html"
license: "Apache-2.0"
mode: "V"
---

Heap memory is used by the memory allocation functions.

It is usually configured in the **startup_`<device>`.s** or **startup_`<device>`.c** 
file located under the **Device** component class but it can also, in some cases, be configured by a **linker script** instead.

Some interface test functions allocate additional buffers from the heap memory.

The CMSIS-Driver Validation framework does not impose heap requirements because it does not use heap memory.

Each interface test module has specific requirements for the heap memory, default requirements are listed below:

| Interface test module   | Heap memory requirement (in bytes) |
| :---------------------: | :--------------------------------: |
| CAN                     | 128                                |
| Ethernet                | 3028                               |
| SPI                     | 12288                              |
| USART                   | 8192                               |

Interface test modules that are not listed in the previous table do not use heap memory.

The system heap memory size must support the largest heap requirement of any used interface test module.

For example, if SPI driver testing is selected heap memory size should be set to at least 12 kB.

Suggested value for heap memory size is **16 kB**.

**Note:** Each module contains additional settings in related configuration file which are not exposed through
      Configuration Wizard and impact the heap memory requirement.

      If these values are changed please adjust heap memory size accordingly.
