---
id: "zepb-ensemble-e8-dk-programming-and-debugging"
type: "concept"
domain: "bring-up"
title: "ensemble_e8_dk: Programming and Debugging"
summary: "Connect a USB cable from your PC to the USB-to-UART bridge connector, and use the serial terminal of your choice (minicom, putty, etc.) with the following settings:"
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@76280bc:boards/alif/ensemble_e8_dk/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/alif/ensemble_e8_dk/doc/index.html#programming-and-debugging"
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

The default UART consoles are:

- **RTSS-HP**: UART4
- **RTSS-HE**: UART2
- **APSS**: UART2


### Flashing


Alif Ensemble E8 Development Kit can be programmed using the Alif Security
Toolkit (SETOOLS). Refer to the Ensemble E8 DevKit Product Page for detailed
instructions on using SETOOLS to program the board.

Alternatively, the board can be flashed using a SEGGER J-Link debug probe with
`west flash`. Connect the board to your host computer using the J-Link debug
interface. The sample application hello_world is used for
this example.

Building and flashing for the High Performance core (RTSS-HP):

On the serial terminal, you should see the following message:

```console

Hello World! ensemble_e8_dk/ae822fa0e5597ls0/rtss_hp
```
Building and flashing for the High Efficiency core (RTSS-HE):

On the serial terminal, you should see the following message:

```console

Hello World! ensemble_e8_dk/ae822fa0e5597ls0/rtss_he
```
Building for the Application Processor (APSS):


**Note:** On the APSS (Cortex-A32) cluster, Zephyr boots in the Non-Secure state, with Arm Trusted Firmware-A (TF-A) acting as the first-stage bootloader that initializes the system and hands off to the Zephyr image. The TF-A port for the Ensemble APSS cluster is not yet available upstream and is currently maintained in Alif's public repository: Alif Trusted Firmware-A. The resulting image is programmed and launched using the Alif Security Toolkit (SETOOLS); the `west flash` and `west debug` runners are not supported for the APSS target.


### Debugging


You can debug an application using `west debug`:

This will start a GDB server and connect to the target.
