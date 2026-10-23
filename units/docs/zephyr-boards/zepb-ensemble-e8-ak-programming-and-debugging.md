---
id: "zepb-ensemble-e8-ak-programming-and-debugging"
type: "concept"
domain: "bring-up"
title: "ensemble_e8_ak: Programming and Debugging"
summary: "Connect a USB cable from your PC to the PRG USB connector, and use the serial terminal of your choice (minicom, putty, etc.) with the following settings:"
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@76280bc:boards/alif/ensemble_e8_ak/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/alif/ensemble_e8_ak/doc/index.html#programming-and-debugging"
license: "Apache-2.0"
mode: "V"
---

### Configuring a Console


Connect a USB cable from your PC to the `PRG USB` connector, and use the
serial terminal of your choice (minicom, putty, etc.) with the following
settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

The target UART connected to `PRG USB` is selected with the 3-position
slide switch `SW4`:

+------------+-------------+-------------------------------------+
| `SW4`    | Target UART | Board target                        |
+============+=============+=====================================+
| Top        | SEUART      | Secure Enclave (not used by Zephyr) |
+------------+-------------+-------------------------------------+
| Center     | UART2       | `rtss_he`, `apss`               |
+------------+-------------+-------------------------------------+
| Bottom     | UART4       | `rtss_hp`                         |
+------------+-------------+-------------------------------------+


### Flashing


Alif Ensemble E8 AI/ML AppKit can be programmed using the Alif Security
Toolkit (SETOOLS). Refer to the Alif Software & Tools page for the SETOOLS
download and detailed instructions on using it to program the board.

Alternatively, the board can be flashed with `west flash` using the on-board
J-Link debugger. Connect a USB cable from your host computer to the
`PRG USB` connector. The sample application hello_world
is used for this example.

Building and flashing for the High Performance core (RTSS-HP):

On the serial terminal, you should see the following message:

```console

Hello World! ensemble_e8_ak/ae822fa0e5597bs0/rtss_hp
```
Building and flashing for the High Efficiency core (RTSS-HE):

On the serial terminal, you should see the following message:

```console

Hello World! ensemble_e8_ak/ae822fa0e5597bs0/rtss_he
```
Building for the Application Processor (APSS):


**Note:** On the APSS (Cortex-A32) cluster, Zephyr boots in the Non-Secure state, with Arm Trusted Firmware-A (TF-A) acting as the first-stage bootloader that initializes the system and hands off to the Zephyr image. The TF-A port for the Ensemble APSS cluster is not yet available upstream and is currently maintained in Alif's public repository: Alif Trusted Firmware-A. The resulting image is programmed and launched using the Alif Security Toolkit (SETOOLS); the `west flash` and `west debug` runners are not supported for the APSS target.


### Debugging


You can debug an application using `west debug`:

This will start a GDB server and connect to the target.
