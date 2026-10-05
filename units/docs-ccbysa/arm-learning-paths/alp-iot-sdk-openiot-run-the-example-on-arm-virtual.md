---
id: "alp-iot-sdk-openiot-run-the-example-on-arm-virtual"
type: "concept"
domain: "project"
title: "Build and run Arm Total Solutions for IoT: Build and run Open-IoT-SDK examples: Run the example on Arm Virtual Hardware"
summary: "To run the blinky example on Arm Virtual Hardware for Corstone-300:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/iot-sdk/openiot.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/iot-sdk/openiot/#run-the-example-on-arm-virtual-hardware"
license: "CC-BY-SA-4.0"
mode: "V"
---

To run the `blinky` example on `Arm Virtual Hardware for Corstone-300`:

```console
./ats.sh run blinky
```
Observe in the output that the system boots through Arm Trusted Firmware (default build uses dummy keys), before the main application.

The output will be similar to:

```output
[INF] Starting bootloader
[INF] Beginning BL2 provisioning
[WRN] TFM_DUMMY_PROVISIONING is not suitable for production! This device is NOT SECURE
[INF] Swap type: none
[INF] Swap type: none
[INF] Bootloader chainload address offset: 0x0
[INF] Jumping to the first image slot
[INF] Beginning TF-M provisioning
<NUL>[WRN] <NUL>TFM_DUMMY_PROVISIONING is not suitable for production! <NUL>This device is NOT SECURE<NUL>
<NUL>[Sec Thread] Secure image initializing!
<NUL>Booting TF-M v1.7.0+3ae2ac302
<NUL>Creating an empty ITS flash layout.
Creating an empty PS flash layout.
[INF][Crypto] Provisioning entropy seed... complete.
[DBG][Crypto] Initialising mbed TLS 3.2.1 as PSA Crypto backend library... complete.
Initialising kernel
Starting kernel and threads
The LED started blinking...
LED on
LED off
LED on
LED off
...
```

Use `Ctrl+C` to stop the simulation.
