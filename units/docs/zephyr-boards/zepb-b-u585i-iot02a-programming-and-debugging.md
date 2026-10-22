---
id: "zepb-b-u585i-iot02a-programming-and-debugging"
type: "concept"
domain: "bring-up"
title: "b_u585i_iot02a: Programming and Debugging"
summary: "B_U585I_IOT02A Discovery kit includes an ST-LINK/V3 embedded debug tool interface. This probe allows to flash the board using various tools."
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@76280bc:boards/st/b_u585i_iot02a/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/st/b_u585i_iot02a/doc/index.html#programming-and-debugging"
license: "Apache-2.0"
mode: "V"
---

B_U585I_IOT02A Discovery kit includes an ST-LINK/V3 embedded debug tool interface.
This probe allows to flash the board using various tools.



### Flashing


The board is configured to be flashed using west STM32CubeProgrammer runner,
so its installation is required.

Alternatively, OpenOCD or JLink can also be used to flash the board using
the `--runner` (or `-r`) option:

```console

$ west flash --runner openocd
$ west flash --runner jlink
```
Connect the B_U585I_IOT02A Discovery kit to your host computer using the USB
port, then run a serial host program to connect with your Discovery
board. For example:

```console

$ minicom -D /dev/ttyACM0
```
Then, build and flash in the usual way. Here is an example for the
hello_world application.

You should see the following message on the console:

```console

Hello World! arm
```

### Debugging


Default flasher for this board is OpenOCD. It could be used in the usual way.
Here is an example for the blinky application.


### Disabling TrustZone® on the board


If you have flashed a sample to the board that enables TrustZone, you will need
to disable it before you can flash and run a new non-TrustZone sample on the
board.

To disable TrustZone, it's necessary to change AT THE SAME TIME the `TZEN`
and `RDP` bits. `TZEN` needs to get set from 1 to 0 and `RDP`,
needs to be set from `DC` to `AA` (step 3 below).

This is documented in the AN5347, in section 9, "TrustZone deactivation".

However, it's possible that the `RDP` bit is not yet set to `DC`, so you
first need to set it to `DC` (step 2).

Finally you need to set the "Write Protection 1 & 2" bytes properly, otherwise
some memory regions won't be erasable and mass erase will fail (step 4).

The following command sequence will fully deactivate TZ:

Step 1:

Ensure U23 BOOT0 switch is set to 1 (switch is on the left, assuming you read
"BOOT0" silkscreen label from left to right). You need to press "Reset" (B2 RST
switch) after changing the switch to make the change effective.

Step 2:

```console

$ STM32_Programmer_CLI -c port=/dev/ttyACM0 -ob rdp=0xDC
```
Step 3:

```console

$ STM32_Programmer_CLI -c port=/dev/ttyACM0 -tzenreg
```
Step 4:

```console

$ STM32_Programmer_CLI -c port=/dev/ttyACM0 -ob wrp1a_pstrt=0x7f
$ STM32_Programmer_CLI -c port=/dev/ttyACM0 -ob wrp1a_pend=0x0
$ STM32_Programmer_CLI -c port=/dev/ttyACM0 -ob wrp1b_pstrt=0x7f
$ STM32_Programmer_CLI -c port=/dev/ttyACM0 -ob wrp1b_pend=0x0
$ STM32_Programmer_CLI -c port=/dev/ttyACM0 -ob wrp2a_pstrt=0x7f
$ STM32_Programmer_CLI -c port=/dev/ttyACM0 -ob wrp2a_pend=0x0
$ STM32_Programmer_CLI -c port=/dev/ttyACM0 -ob wrp2b_pstrt=0x7f
$ STM32_Programmer_CLI -c port=/dev/ttyACM0 -ob wrp2b_pend=0x0
```
.. _STM32U585 on www.st.com:
   https://www.st.com/en/microcontrollers-microprocessors/stm32u575-585.html

.. _AN5347, in section 9:
   https://www.st.com/resource/en/application_note/dm00625692-stm32l5-series-trustzone-features-stmicroelectronics.pdf
