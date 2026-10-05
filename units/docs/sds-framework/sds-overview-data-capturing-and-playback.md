---
id: "sds-overview-data-capturing-and-playback"
type: "concept"
domain: "test"
title: "Overview: Data Capturing and Playback"
summary: "The following diagram shows the workflow for recording (physical data capture) and playback (regression testing). SDS supports recording and playback on target hardware, and playback on the FVP simulation model."
status: "draft"
collection: "sds-framework"
source: "ARM-software/SDS-Framework@4459441:documentation/overview.md"
doc_source: "https://github.com/ARM-software/SDS-Framework/blob/4459441/documentation/overview.md#data-capturing-and-playback"
license: "Apache-2.0"
mode: "V"
---

The following diagram shows the workflow for recording (physical data capture) and playback (regression testing). SDS supports recording and playback on target hardware, and playback on the [FVP simulation model](https://github.com/Arm-software/avh).

(figure: Workflow)

The [**SDSIO Interface**](https://github.com/ARM-software/SDS-Framework/blob/4459441/documentation/sdsio.md) is integrated into the target application and runs on the microcontroller.
It enables data streaming into SDS data files via various interfaces such as USB, Ethernet, RTT, UART or File System.
The I/O implementation included in SDS utilizes the [MDK-Middleware](https://www.keil.arm.com/packs/mdk-middleware-keil/overview/),
however custom interfaces to other middleware or different communication channels can also be used.

The [**SDSIO-Server**](https://github.com/ARM-software/SDS-Framework/blob/4459441/documentation/utilities.md#sdsio-server) running on a host computer captures the recorded data stream and stores it in SDS data files.
Each recording creates one set of SDS data files that are identified by a sequential number.
The SDS data files are in binary format and may be described using a [YAML metadata file](https://github.com/ARM-software/SDS-Framework/tree/main/schema).
With this information, other tools can utilize the content of the SDS data files as shown in the picture below.

(figure: Analysis of SDS data files)

On target hardware or in a FVP simulation environment, the [**SDSIO Interface**](https://github.com/ARM-software/SDS-Framework/blob/4459441/documentation/sdsio.md#layer-sdsio_fvp) streams the SDS data files back to the algorithm under test. With this interface, the algorithm receives
the same data stream as captured on physical hardware. The setup can therefore be used for validation, performance optimization, and can run in CI environments for test automation.
