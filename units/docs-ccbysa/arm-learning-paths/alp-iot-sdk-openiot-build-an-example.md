---
id: "alp-iot-sdk-openiot-build-an-example"
type: "concept"
domain: "project"
title: "Build and run Arm Total Solutions for IoT: Build and run Open-IoT-SDK examples: Build an example"
summary: "The projects are located in the examples folder. Review the list of available projects:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/iot-sdk/openiot.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/iot-sdk/openiot/#build-an-example"
license: "CC-BY-SA-4.0"
mode: "V"
---

The projects are located in the `examples` folder. Review the list of available projects:

```console
ls examples
```

The output is:

```output
blinky  keyword  speech
```

Use the `ats.sh` script to build the examples. 

The `blinky` example demonstrates how to use Trusted Firmware-M to create secure and non-secure partitions, and blink the LED from the non-secure code.

Build `blinky` example by running:

```console
./ats.sh build blinky
```

Ignore any warnings from the build. The build takes a few minutes to complete.
