---
id: "sds-overview-sds-recording-performance"
type: "concept"
domain: "test"
title: "Overview: SDS Recording Performance"
summary: "The following section lists the communication speeds that can be achieved on different targets with various interfaces."
status: "draft"
collection: "sds-framework"
source: "ARM-software/SDS-Framework@4459441:documentation/overview.md"
doc_source: "https://github.com/ARM-software/SDS-Framework/blob/4459441/documentation/overview.md#sds-recording-performance"
license: "Apache-2.0"
mode: "V"
---

The following section lists the communication speeds that can be achieved on different targets with various interfaces.

!!! Note
    - Performance measurements were obtained using the [DataTest](https://arm-software.github.io/SDS-Framework/main/template.html#using-datatest) project, which validates captured data streams on the available interfaces.
    - SDS data files were verified using the [SDS-Check](https://arm-software.github.io/SDS-Framework/main/utilities.html#sds-check) utility.
    - In addition to transfer performance, CPU idle time was measured to estimate the processing capacity available while communication was active.
    - When using playback, the transfer performance is not critical, as the algorithm will only be executed when data is available.

[Using the USB](https://github.com/ARM-software/SDS-Framework/blob/4459441/documentation/sdsio.md#layer-sdsio_usb) or [Network](https://github.com/ARM-software/SDS-Framework/blob/4459441/documentation/sdsio.md#layer-sdsio_network) interface on different target hardware:

| Interface                                     | USB                    | Network                |
|-----------------------------------------------|------------------------|------------------------|
| Alif Semiconductor DevKit-E8      (@ 400 MHz) | 20 MB/s (55% idle)     | 8 MB/s (66% idle)      |
| STMicroelectronics STM32N6570-DK  (@ 600 MHz) | 13 MB/s (55% idle)     |                        |
| STMicroelectronics B-U585I-IOT02A (@ 160 MHz) | 1.1 MB/s (86% idle)    |                        |

[Using the RTT](https://github.com/ARM-software/SDS-Framework/blob/4459441/documentation/sdsio.md#layer-sdsio_rtt) interface on the STM32F769I-EVAL board (with maximum SWD clock 12 MHz that is imposed by hardware) with different debug adapters:

- ST-Link (SWD clock: 10 MHz): 130 kB/s
- ULINKplus (SWD clock: 10 MHz): 250 kB/s
- J-Link Pro (SWD clock: auto): 800 kB/s

[Using the FileSystem](https://github.com/ARM-software/SDS-Framework/blob/4459441/documentation/sdsio.md#layer-sdsio_fs) on the STM32H7B3_DK board with CPU running at 280 MHz, SDMMC with 4-bit bus: 5 MB/s
