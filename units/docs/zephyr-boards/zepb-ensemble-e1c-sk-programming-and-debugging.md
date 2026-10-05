---
id: "zepb-ensemble-e1c-sk-programming-and-debugging"
type: "concept"
domain: "bring-up"
title: "ensemble_e1c_sk: Programming and Debugging"
summary: "The on-board USB-to-UART bridge is shared between the Secure Enclave UART and the UART2 user serial port, selected by the JP5 jumpers. Move JP5 to the UART2 position (JP5-3-5 and JP5-4-6) to reach the Zephyr console."
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@8f62a4a:boards/alif/ensemble_e1c_sk/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/alif/ensemble_e1c_sk/doc/index.html#programming-and-debugging"
license: "Apache-2.0"
mode: "V"
---

### Configuring a Console


The on-board USB-to-UART bridge is shared between the Secure Enclave UART and
the UART2 user serial port, selected by the JP5 jumpers. Move JP5 to the UART2
position (JP5-3-5 and JP5-4-6) to reach the Zephyr console.

Connect a USB cable from your PC to the PRG USB connector, and use the serial
terminal of your choice (minicom, putty, etc.) with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

To use SETOOLS without moving JP5 back, keep JP5 in the UART2 position and
connect a 1.8 V USB-to-serial cable to the SEUART header J10: pin 1 is GND,
pin 2 is the SEUART transmit line (to the cable RXD) and pin 3 is the SEUART
receive line (to the cable TXD). The Zephyr console and the Secure Enclave UART
are then available at the same time.


### Flashing


The Alif Ensemble E1C StartKit is programmed using the Alif Security Toolkit
(SETOOLS). Refer to the Ensemble E1C StartKit Product Page for detailed
instructions on installing and using SETOOLS to program the board.

Building an application for the RTSS-HE core:

After building, use SETOOLS to flash the `build/zephyr/zephyr.bin` binary to
the board.

After flashing and resetting the board, you should see the following message
on the serial console:

```console

Hello World! ensemble_e1c_sk/ae1c1f4051920ph0/rtss_he
```

### Debugging


The board supports debugging through the on-board J-Link debugger using standard
SEGGER J-Link tools.
