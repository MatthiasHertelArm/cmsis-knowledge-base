---
id: "intr-diving-into-jtag-security-part-6-protection"
type: "concept"
domain: "debug"
title: "Diving into JTAG — Security (Part 6): Protection"
summary: "Let's start by considering simple protection methods that can be applied to make life more difficult for an attacker who wants to gain unauthorized access to a device using the JTAG interface."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-08-14-diving-into-jtag-part-6.md"
doc_source: "https://interrupt.memfault.com/blog/diving-into-jtag-part-6#protection"
license: "CC-BY-SA-4.0"
mode: "V"
---

Let's start by considering simple protection methods that can be applied to make
life more difficult for an attacker who wants to gain unauthorized access to a
device using the JTAG interface.

### Board-Level

The simplest, most obvious, but probably least effective method of protection is
to restrict access to the JTAG connector at the board level. This restriction is
achieved by physically removing the JTAG connector from the board at the end of
production, as shown in this picture, where you can see that the JTAG connector
was removed:



 


Another protection option is suitable when there is no JTAG connector on the
board at all and the JTAG pins are scattered across the board as test points.
For example, in the next picture, you can see that the board contains JTAG pins
as separate pads.



 


However, as you well understand, these methods provide only the most basic
protection, as soldering a JTAG connector is not a significant effort, nor is
finding the necessary JTAG pins on the microcontroller, especially when its part
number is written on the package, as shown in the photo. But even if the
microcontroller is unknown, there are ways to scan the pins of the
microcontroller to discover the necessary JTAG pins (I will discuss these
methods in more detail later).

### Chip-Level

Debug interfaces are convenient during device development and debugging, but it
is good practice to disable them in the release version of the device/firmware.
There are configurable bits in the microcontroller's non-volatile memory to
disable certain debug interface functions. The flexibility of configuring
protection features depends on the specific core and microcontroller model.

For instance, access to flash memory can be disabled. Some microcontroller
models support completely disabling the debug interface. The exact configuration
of possible protection features can be found in the microcontroller's
documentation. An example is the
[Flash Readout Protection (RDP) technology in STM32 microcontrollers](https://www.st.com/resource/en/application_note/an5156-introduction-to-security-for-stm32-mcus-stmicroelectronics.pdf).
This technology allows for the protection of the contents of the
microcontroller's embedded flash memory from being read through the debug
interface.



 


RDP has three levels of protection (0, 1, and 2):

- **Level 0** (default RDP level) The flash memory is fully open, and all memory
  operations are possible in all boot configurations (debug features, boot from
  RAM, boot from system memory bootloader, boot from flash memory). There is no
  protection in this configuration mode that is appropriate only for development
  and debug.
- **Level 1** Flash memory accesses (read, erase, program), or SRAM2 accesses
  via debug features (such as serial-wire or JTAG) are forbidden, even while
  booting from SRAM or system memory bootloader. In these cases, any read
  request to the protected region generates a bus error. However, when booting
  from flash memory, accesses to both flash memory and to SRAM2 (from user code)
  are allowed.
- **Level 2** All protections provided in Level 1 are active, and the MCU is
  fully protected. The RDP option byte and all other option bytes are frozen and
  can no longer be modified. The JTAG, SWV (single-wire viewer), ETM, and
  boundary scan are all disabled.

RDP can always be leveled up. Increasing the level is necessary in the following
cases:

- **Intellectual property protection**: Increasing the RDP level prevents
  reading the contents of the flash memory, which protects the firmware and
  other important data from being copied or analyzed by third parties.

- **Prevention of unauthorized firmware modification**: At higher protection
  levels (e.g., Level 2), it becomes impossible not only to read but also to
  write to flash memory without completely resetting the microcontroller. This
  helps prevent the introduction of malicious modifications to the software.

- **Debugging protection**: When the RDP level is raised, the microcontroller
  disables debugging interfaces (e.g., JTAG or SWD), preventing attackers from
  using them to debug and analyze the program's operation.

- **Compliance with safety standards**: In some applications (e.g., automotive
  or medical technology), compliance with certain safety standards is required,
  which necessitates hardware-level data protection.

A level regression is possible with the following consequences:

- Regression from RDP level 1 to RDP level 0 leads to a flash memory mass erase
  and the erase of SRAM2 and backup registers. You may need to perform a level
  regression to update software already in flash memory or when you need to
  repair a production device that has been returned.
- In RDP level 2, no regression is possible.

In consumer products, RDP should always be set to at least level 1. This setting
prevents basic attacks through the debug port or bootloader. RDP level 2 is
mandatory for implementing applications with a higher level of security.

The RDP technology for STM32 is an example; similar protection technologies
exist for other microcontrollers.
