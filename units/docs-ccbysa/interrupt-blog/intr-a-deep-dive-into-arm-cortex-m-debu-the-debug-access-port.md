---
id: "intr-a-deep-dive-into-arm-cortex-m-debu-the-debug-access-port"
type: "concept"
domain: "debug"
title: "A Deep Dive into ARM Cortex-M Debug Interfaces: The ARM Debugger Stack / The Debug Access Port"
summary: "The DAP is an implementation of the ARM Debug Interface Architecture Specification[^2]."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-08-06-a-deep-dive-into-arm-cortex-m-debug-interfaces.md"
doc_source: "https://interrupt.memfault.com/blog/a-deep-dive-into-arm-cortex-m-debug-interfaces#the-debug-access-port"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: The ARM Debugger Stack_

The **DAP** is an implementation of the **ARM Debug Interface Architecture Specification**[^2]. The specification defines a set of **Debug Port** Registers that can be accessed to perform operations on the chip as well as the pinout a MCU needs to expose so external debuggers can attach to it. This is quite nice because it means reading state ( memory, registers, etc) over the DAP is pretty much the same operation regardless of the ARM MCU being used.

#### Access Port

The **Debug Port** can be used to configure transactions and read or write to one or more **Access Port**s (**AP**). An **Access Port** exposes an interface to different parts of the MCU. The only requirements for an **AP** are that they must:

- expose an Identification Register so a debugger can skip over it if it doesn't understand the type
- Must be selectable via the Debug Port

The most common type of Access Port is known as the `MEM-AP` which exposes an interface to different Memory buses available on a given ARM chip. On `ARM Cortex-M`, the `MEM-AP` which is typically accessed is known as the `AHB-AP`. The default APs that are selected can be found in the `APSEL` part of the **DP** `AP Select Register`[^1]:



#### AHB-AP

The **Advanced High-performance Bus** (**AHB**) is a bus present on `ARM` devices that interconnects the memory and peripherals present on the MCU. The **AHB-AP** exposes access to this bus via several registers. The most common registers used in the **AHB-AP** are:

- **Control/Status Word register** (`CSW`) Used to configure the rules to be used when performing a memory access on the AHB.
- **Transfer Address Register** (`TAR`) Used to control the address that will be accessed
- **Data Read/Write register** (`DRW`) Depending on the access, contains the data to write to or read from the `TAR`

Extensive details about how to access the register set can be found in the ARM Debug Interface Specification[^2]

#### Debug Port External Connection Options

The DAP spec defines three different protocols which can be used to expose an interface from the **Debug Port** to the outside world. They are:

- **JTAG Debug Port (JTAG-DP)** - Based on the IEEE 1149.1 Standard for **Test Access Port** (`TAP`). A `JTAG` interface is exposed in pretty much any piece of silicon and was standardized in 1990 with several revisions added over the years. This debug interface requires the MCU expose at least 4 pins and one optional pin (`DBGTRSTn`). At its core, the protocol operates on a sequence of shift registers and a fairly complex state machine to push data in / get data out
- **Serial Wire Debug (SWD) Port (SW-DP)** - `SWD` was designed to reduce the number of physical pins that need to be exposed. MCUs have a small number of pins available and reducing the pin count needed for debugging means there are more GPIOs free for external sensors or that a smaller footprint package can be used. One pin, `SWDIO`, is used for input/output and the other `SWCLK` is used for clocking data in and out. Sampling of `SWDIO` is performed on the rising edge of the clock
- **Serial Wire/JTAG Debug Port (SWJ-DP)** `SWJ-DP` is the best of both worlds and exposes an interface where `JTAG` or `SWD` can be used. The pins are carefully assigned between the two protocols so a negotiation can take place to select the protocol that is in use. This is the configuration you will see exposed on most MCUs because the user can then chose to use either protocol depending on their needs
