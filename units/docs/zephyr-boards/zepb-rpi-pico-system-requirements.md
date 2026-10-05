---
id: "zepb-rpi-pico-system-requirements"
type: "concept"
domain: "bring-up"
title: "rpi_pico: System requirements"
summary: "Building for the Raspberry Pi Pico W requires the AIROC binary blobs provided by Infineon. Run the command below to retrieve those files:"
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@8f62a4a:boards/raspberrypi/rpi_pico/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/raspberrypi/rpi_pico/doc/index.html#system-requirements"
license: "Apache-2.0"
mode: "V"
---

### Prerequisites for the Pico W


Building for the Raspberry Pi Pico W requires the AIROC binary blobs
provided by Infineon. Run the command below to retrieve those files:

```console

west blobs fetch hal_infineon
```

**Note:** It is recommended running the command above after `west update`.
