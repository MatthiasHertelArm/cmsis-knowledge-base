---
id: "intr-a-deep-dive-into-arm-cortex-m-debu-debug-probes"
type: "concept"
domain: "debug"
title: "A Deep Dive into ARM Cortex-M Debug Interfaces: The ARM Debugger Stack / Debug Probes"
summary: "The next step is getting a computer to talk to the MCU."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-08-06-a-deep-dive-into-arm-cortex-m-debug-interfaces.md"
doc_source: "https://interrupt.memfault.com/blog/a-deep-dive-into-arm-cortex-m-debug-interfaces#debug-probes"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: The ARM Debugger Stack_

The next step is getting a computer to talk to the MCU. Typically another piece of hardware (often referred to as an "interfacing MCU") will be used to map from the `SWD` or `JTAG` connection to a USB protocol that can talk to the computer. Sometimes the interface will be provided via an external dongle and other times via an integrated IC on the development board being used. If you are designing your own development board, it's always a good idea to expose these debug pins to an external header to keep your options open.

#### Debug Probe Options

There are _quite_ a few interfacing options you will see depending on the ARM MCU, IDE, and development kit you are using. Some of the most popular are:

- **Future Technology Devices International** (**FTDI**)'s FT Series chips which expose a bridge between USB and the raw signal lines they are connected to. The same chip is also very popular for exposing a UART connection. They are fairly cheap and expose a USB interface, know as **The Multi Protocol Synchronous Serial Engine** (`MPSSE`), which can be used for issuing `JTAG` or `SWD` transactions (and other serial protocols)
- **CMSIS-DAP**[^3] [^4] A standardized protocol for interfacing with the ARM **Debug Access Port**. ARM maintains an open source implementation of the specification know as **DAPLink**[^5]. This image is flashed on an interfacing MCU where one side is connected to the pins of the MCU being debugged and the other side exposes a USB connection which communicates using USB HID commands. The nice part about this standard is that it can talk JTAG & SWD but the protocol does not need to be implemented on the computer. Additionally since almost any modern computer has support for HID, no additional USB drivers are needed. Many development kits come with a CMSIS-DAP pin compatible MCU available that can easily be re-flashed. For example, the **LPC-Link2**[^6] found on a lot of NXP dev boards does this.
- **SEGGER J-Link Debug Probe**[^7] A proprietary cross-platform debug probe that bridges USB to `JTAG` or `SWD`. There are many different form factors available and **SEGGER** also has firmwares available to convert a lot of other debug probes to be J-Link compatible
- **ST-Link**[^8] - A proprietary debug probe maintained by **STMicroelectronics**. There has been three iterations of the hardware, the latest of which is known as **STLINK-V3**

#### Desktop Software to Interface with Debug Probe

Once you have selected a debug probe, the next step is choosing what software on the computer to use to communicate with the probe.

There are numerous options available but an overwhelming majority of the software stacks available will expose a `gdbserver` interface which exposes the "GDB Remote Serial Protocol"[^9] on one side and talks the necessary debug probe protocol to the interfacing MCU on the other. Even if you are using an Eclipse based IDE (i.e NXP's **MCUXpresso**, **STM32CubeIDE**, **TrueSTUDIO**, **WICED-Studio IDE**, etc), the debug interface is usually leveraging a `gdbserver` behind the scenes.

When selecting the software to use, the other item you want to look at is its board support. If the MCU in use has an internal micro flash, many of these probes also come with support for programming that flash so you can easily load new programs on the MCU.

##### GDB Server Options

The actual GDB server used is usually based on the debug probe selected. Some of the common choices are:

- **pyOCD**[^10] A Python-based open source implementation compatible with **CMSIS-DAP** and **ST-Link** debug probes. The project is maintained by ARM. This is my favorite gdbserver at the moment. If you want to understand more about the ARM Coresight internals, reading through the code itself is actually a great reference and being open source the framework can be easily extended to support a variety of use cases.
- **openOCD**[^11] A C-based open source `gdbserver` implementation for a wide array of debug probes. The project probably supports the widest array of debug probes out of any project available (you can run `openocd -c interface_list` to see) including **FTDI**, **CMSIS-DAP**, **J-Link** and about 17 other adapters. The project dates back to 2005 and while it has support for a wide array of parts I have found it to be a bit flaky to use for projects over the years.
- **SEGGER JLinkGDBServer**[^12] A proprietary `gdbserver` distributed as a binary. Has support for an impressive amount of devices. (You can find the list at `<SEGGER JLink install path>/JLinkDevices.xml`). I've found it to be quite reliable for debugging but when there are issues, things can be quite painful to fix without being able to see the source
- **texane/stlink**[^13] An open source implementation of the ST-Link Debug Probe protocol. This project is independently maintained and not affiliated with ST.
- Proprietary GDB Servers used with different IDEs such as **PEMicro GDB Server**[^14], NXP **LinkServer/Redlink** and **ST-LINK_gdbserver**[^15].

#### Extending Debug Probe Software

##### RTOS Awareness

Features like **RTOS Awareness** -- the ability to see all the tasks currently active on an MCU when you run `info threads` or view a task list in Eclipse -- needs to be implemented on the `gdbserver` side. When a GDB client connects to a server, it will ask the server for the thread list. If the server can't resolve the thread list, it will only show the stack trace for the active task.

The RTOS awareness implementations all wind up looking pretty similar. The **GDB Remote Serial Protocol** has a message, `qSymbol`, which can be used to ask the client to look up the address for a given symbol (i.e `pxCurrentTCB` would be a symbol you'd need to look up the address of in order to implement a FreeRTOS plugin). The server will look up the symbols it needs to uncover the **Thread Control Block** (`TCB`) for all the tasks in the system. Once it has the list, the `gdbserver` will recover the state of each thread by issuing reads to the memory of the MCU. Sometimes to aid in the recovery of this information an RTOS will export special symbols to expose offsets of `TCB` info. (i.e Zephyr[^23])

Conveniently, many of the GDB Server options expose APIs for implementing thread awareness. The ones I am aware of and have implemented RTOS plugins with include:

- **OpenOCDs RTOS plugin**[^20] A C-based RTOS-plugin API
- **SEGGER GDB Server RTOS plugin SDK**[^21] You have to request access but the API is also in C. If you look at the way the OpenOCD plugin works the SEGGER based API is extremely similar.
- **pyOCD RTOS plugin**[^22] The API is in Python but similarly structured to the other two C based APIs

##### SEGGER Open Flashloader / Custom flash loaders

A ton of MCUs these days allow one to execute code from external flash parts. Very rarely will the debug probe software have a pre-existing flash loader for a custom configuration like this. **SEGGER** conveniently has an API to implement a Custom Flash Loader.

The way it works is you provide micro-code that is flashed into RAM to initialize, read, erase, and write to the flash part of interest. The `SEGGER JLinkGDBServer` will just jump to these functions to perform the operations on the external flash. I've implemented a few of these and while it can be a convenient tool to have, developing these plugins can be quite challenging as this code runs before the debugger starts. So a failure will not drop out to a breakpoint you can look at. The "best" way to debug these plugins is to sprinkle messages in RAM which can be read post-mortem.

#### The Desktop Debugger

All of the pieces we've mentioned stack together and make up "the debugger".

There a few common interfaces to the stack:

- a GDB Cli Client that you would launch by running a command like:

```
arm-none-eabi-gdb-py --eval-command="target remote localhost:<remote port>" --symbols=<ELF>
```

- An Eclipse based GUI that has different views you can use to inspect variables or see memory
- VSCode Plugins[^17][^25] that interfaces with GDB and let's you hover over and view variables
