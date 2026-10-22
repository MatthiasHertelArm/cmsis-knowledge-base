---
id: "zepb-ensemble-e1c-dk-programming-and-debugging"
type: "concept"
domain: "bring-up"
title: "ensemble_e1c_dk: Programming and Debugging"
summary: "Connect a USB cable from your PC to the USB-to-UART bridge connector, and use the serial terminal of your choice (minicom, putty, etc.) with the following settings:"
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@76280bc:boards/alif/ensemble_e1c_dk/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/alif/ensemble_e1c_dk/doc/index.html#programming-and-debugging"
license: "Apache-2.0"
mode: "V"
---

### Configuring a Console


Connect a USB cable from your PC to the USB-to-UART bridge connector, and use
the serial terminal of your choice (minicom, putty, etc.) with the following
settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

The default UART console is:

- **RTSS-HE**: UART2


### Flashing


The Alif Ensemble E1C Development Kit is programmed using the Alif Security
Toolkit (SETOOLS). Refer to the Ensemble E1C DevKit Product Page for detailed
instructions on installing and using SETOOLS to program the board.

Building an application for the RTSS-HE core:

After building, use SETOOLS to flash the `build/zephyr/zephyr.bin` binary to
the board.

After flashing and resetting the board, you should see the following message
on the serial console:

```console

Hello World! ensemble_e1c_dk/ae1c1f4051920ph0/rtss_he
```

### Debugging


The board supports debugging via the JTAG debug connector using standard debugging tools
such as SEGGER J-Link.
