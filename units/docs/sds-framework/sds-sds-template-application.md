---
id: "sds-sds-template-application"
type: "concept"
domain: "test"
title: "SDS Template Application"
summary: "The SDS template application is a test framework for DSP and ML algorithms. It supports recording and playback of real-world data streams on physical hardware or simulation models using Arm Virtual Hardware (FVP), feeding a user algorithm under test."
status: "draft"
collection: "sds-framework"
source: "ARM-software/SDS-Framework@c18efee:documentation/template.md"
doc_source: "https://github.com/ARM-software/SDS-Framework/blob/c18efee/documentation/template.md"
license: "Apache-2.0"
mode: "V"
---

<!-- markdownlint-disable MD013 -->
<!-- markdownlint-disable MD036 -->
<!-- markdownlint-disable MD060 -->

The [SDS template application](https://github.com/ARM-software/SDS-Framework/tree/main/template) is a test framework for DSP and ML algorithms. It supports recording and playback of real-world data streams on physical hardware or simulation models using [Arm Virtual Hardware (FVP)](https://github.com/ARM-software/AVH), feeding a user algorithm under test. The real-world data streams are captured in SDS data files. This enables multiple use cases:

- Validate and optimize algorithms using playback. This makes it possible to repeat test cases with the same data stream.
- The captured data streams can be labeled and used as a training dataset for AI models in MLOps systems.

The SDS template application is implemented as a [CMSIS-Toolbox Reference Application](https://open-cmsis-pack.github.io/cmsis-toolbox/ReferenceApplications/). It is hardware-agnostic and requires an `SDSIO-Layer` and a `Board-Layer` with drivers for the target hardware.

An `SDSIO-Layer` connects the SDS template application to a communication interface for SDS file I/O operations.
For hardware targets, the following [SDSIO interfaces](https://github.com/ARM-software/SDS-Framework/blob/c18efee/documentation/sdsio.md) are available as pre-configured software layers:

- [Ethernet Interface](https://github.com/ARM-software/SDS-Framework/blob/c18efee/documentation/sdsio.md#layer-sdsio_network) using the MDK-Middleware Network component.
- [USB Bulk Interface](https://github.com/ARM-software/SDS-Framework/blob/c18efee/documentation/sdsio.md#layer-sdsio_usb) using the MDK-Middleware USB component.
- [RTT (Real-Time Transfer)](https://github.com/ARM-software/SDS-Framework/blob/c18efee/documentation/sdsio.md#layer-sdsio_rtt) using the SEGGER RTT component for I/O via the debug adapter.
- [Memory Card Interface](https://github.com/ARM-software/SDS-Framework/blob/c18efee/documentation/sdsio.md#layer-sdsio_fs) using the MDK-Middleware File System component.

With a custom SDSIO interface, alternative I/O configurations are possible.
