---
id: "zepb-stm32n6570-dk-programming-and-debugging"
type: "concept"
domain: "bring-up"
title: "stm32n6570_dk: Programming and Debugging"
summary: "STM32N6570_DK board includes an ST-LINK/V3 embedded debug tool interface. This probe allows to flash and debug the board using various tools."
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@8f62a4a:boards/st/stm32n6570_dk/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/st/stm32n6570_dk/doc/index.html#programming-and-debugging"
license: "Apache-2.0"
mode: "V"
---

STM32N6570_DK board includes an ST-LINK/V3 embedded debug tool interface.
This probe allows to flash and debug the board using various tools.



### Flashing or loading


The board is configured to be programmed using west STM32CubeProgrammer runner,
so its installation is needed.
Version 2.18.0 or later of STM32CubeProgrammer is required.


**Note:** Firmware is run in secure mode of execution, which requires a signature. After build, the build system  will automatically generate a signed version of the binary using STM32CubeProgrammer utility `STM32_SigningTool_CLI`. This utility is installed along with STM32CubeProgrammer, but make sure it is available in your `PATH` variable.

To program the board, there are two options:

- Program the firmware in external flash. At boot, it will then be loaded on RAM
  and executed from there.
- Optionally, it can also be taken advantage from the serial boot interface provided
  by the boot ROM. In that case, firmware is directly loaded in RAM and executed from
  there. It is not retained in persistent memory.


#### Programming an application to STM32N6570_DK


Here is an example to build and run hello_world application.

First, connect the STM32N6570_DK to your host computer using the ST-Link USB port.

Run a serial host program to connect with your Disco board:

```console

$ minicom -D /dev/ttyACM0
```
You should see the following message on the console:

```console

Hello World! stm32n6570_dk/stm32n657xx
```

### Debugging


You can debug an application in the usual way using west and the ST-LINK GDB Server.


**Note:** To enable debugging, before powering on the board, set the boot pins in the following configuration: * BOOT0: 0 (switch SW2 in position L) * BOOT1: 1 (switch SW1 in position H) .. tabs:: .. group-tab:: Application image To debug a multi-stage application (application loaded by a bootloader such as MCUboot), follow these steps: First, flash your application, it is required so that MCUboot can find it in external memory (see indications above). Then, launch debug session using the bootloader domain: .. code-block:: console west debug --domain mcuboot At this step, you're able to debug the bootloader. To debug the chainloaded application, now run the following gdb commands: .. code-block:: console (gdb) b do_boot (gdb) c # Once stopped in do_boot, add chainloaded application symbols (gdb) add-symbol-file ./build/hello_world/zephyr/zephyr.elf # Place breakpoint on 'main' in chainloaded application (gdb) b main (gdb) c Don't forget to systematically power reset the board before each debug session. This can be done using `the following script:<boards/st/common/scripts/board_power_reset.sh>` .. code-block:: console ./boards/st/common/scripts/board_power_reset.sh .. group-tab:: FSBL - ST-Link Here is an example for the hello_world application. .. zephyr-app-commands:: .. group-tab:: FSBL - Serial Boot Loader (USB) Here is an example for the hello_world application. .. zephyr-app-commands::

Another solution for debugging is to use STM32CubeIDE:

* Go to `File --> Import` and select `C/C++ --> STM32 Cortex-M Executable`.
* In the `Executable` field, browse to your `<ZEPHYR_PATH>/build/zephyr/zephyr.elf`.
* In `MCU` field, select `STM32N657X0HxQ`.
* Click on `Finish`.
* Finally, click on `Debug` to start the debugging session.


### Running tests with twister


Due to the BOOT switches manipulation required when flashing the board using `stm32n6570_dk`
board target, it is only possible to run twister tests campaign on `stm32n6570_dk/stm32n657xx/sb`
board target which doesn't require BOOT pins changes to load and execute binaries.
To do so, it is advised to use Twister's hardware map feature with the following settings:

```yaml

- platform: stm32n6570_dk/stm32n657xx/sb
  product: BOOT-SERIAL
  pre_script: <path_to_zephyr>/boards/st/common/scripts/board_power_reset.sh
  runner: stm32cubeprogrammer
```
.. _STM32N657X0 on www.st.com:
   https://www.st.com/en/microcontrollers-microprocessors/stm32n657x0.html
