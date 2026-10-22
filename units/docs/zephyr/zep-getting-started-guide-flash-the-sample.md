---
id: "zep-getting-started-guide-flash-the-sample"
type: "concept"
domain: "project"
title: "Getting Started Guide: Flash the Sample"
summary: "Connect your board, usually via USB, and turn it on if there's a power switch. If in doubt about what to do, check your board's page in boards, as some boards require a specific setup or procedure to flash them."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/getting_started/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/getting_started/index.rst"
license: "Apache-2.0"
mode: "V"
---

Connect your board, usually via USB, and turn it on if there's a power switch.
If in doubt about what to do, check your board's page in boards, as some
boards require a specific setup or procedure to flash them.

Flash the sample with west flash. This programs the
application you just built onto the connected board:

```shell

west flash
```

**Note:** You may need to install additional host tools required by your board. The `west flash` command will print an error if any required dependencies are missing.


**Note:** On Linux, you may need to configure udev rules before flashing with a debug probe for the first time. See setting-udev-rules.

If you're using blinky, the LED will start to blink as shown in this figure:
