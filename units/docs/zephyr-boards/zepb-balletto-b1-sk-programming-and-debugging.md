---
id: "zepb-balletto-b1-sk-programming-and-debugging"
type: "concept"
domain: "bring-up"
title: "balletto_b1_sk: Programming and Debugging"
summary: "The on-board USB-to-UART bridge is shared between the Secure Enclave UART and the UART2 user serial port, selected by the JP5 jumpers. Move JP5 to the UART2 position (JP5-3-5 and JP5-4-6) to reach the Zephyr console."
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@76280bc:boards/alif/balletto_b1_sk/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/alif/balletto_b1_sk/doc/index.html#programming-and-debugging"
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


The Alif Balletto B1 StartKit is programmed using the Alif Security Toolkit
(SETOOLS). Refer to the Balletto B1 StartKit Product Page for detailed
instructions on installing and using SETOOLS to program the board.

Building an application for the RTSS-HE core:

After building, use SETOOLS to flash the `build/zephyr/zephyr.bin` binary to
the board.

After flashing and resetting the board, you should see the following message
on the serial console:

```console

Hello World! balletto_b1_sk/ab1c1f4m51820ph0
```

### Debugging


The board supports debugging through the on-board J-Link debugger using standard
SEGGER J-Link tools.
