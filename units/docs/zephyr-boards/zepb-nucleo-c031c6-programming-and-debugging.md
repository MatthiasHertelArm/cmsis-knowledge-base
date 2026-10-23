---
id: "zepb-nucleo-c031c6-programming-and-debugging"
type: "concept"
domain: "bring-up"
title: "nucleo_c031c6: Programming and Debugging"
summary: "Nucleo C031C6 board includes an ST-LINK/V2-1 embedded debug tool interface."
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@76280bc:boards/st/nucleo_c031c6/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/st/nucleo_c031c6/doc/index.html#programming-and-debugging"
license: "Apache-2.0"
mode: "V"
---

Nucleo C031C6 board includes an ST-LINK/V2-1 embedded debug tool interface.

Applications for the `nucleo_c031c6` board configuration can be built and
flashed in the usual way (see build_an_application and
application_run for more details).


### Flashing


The board is configured to be flashed using west STM32CubeProgrammer runner,
so its installation is required.


#### Flashing an application to Nucleo C031C6


Here is an example for the blinky application.

You will see the LED blinking every second.
