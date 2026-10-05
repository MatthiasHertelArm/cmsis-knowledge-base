---
id: "intr-diving-into-jtag-security-part-6-debug-port-rdp-attack"
type: "concept"
domain: "debug"
title: "Diving into JTAG — Security (Part 6): Attack / Debug Port (RDP) Attack"
summary: "As we discussed when introducing RDP protection, any device released must have protection enabled."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-08-14-diving-into-jtag-part-6.md"
doc_source: "https://interrupt.memfault.com/blog/diving-into-jtag-part-6#debug-port-rdp-attack"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Attack_

As we discussed when introducing RDP protection, any device released must have
protection enabled. In such cases, to copy the firmware, for example, an
attacker has to use techniques such as chip decapping or glitching the hardware
logic by manipulating inputs such as power or clock sources and using the
resulting behavior to successfully bypass these protections. However, sometimes
, an attacker does not have to use such hardcore methods to achieve their goal,
especially if the level of protection enabled is not the highest. In this
section, I will give a high-level description of a few attack techniques. For a
deeper dive, see the full articles linked with each.

#### Firmware dumping technique for an ARM Cortex-M0 SoC

The first example describes a technique that allows you to read firmware from
the nRF51822 device even though memory read protection is enabled. However, the
protection level leaves access to the Debug Port and allows the reading and
writing of processor registers and even executing debug commands such as step.
Through this exposure, an attacker can read the firmware.

Debugger access allows us to write values to the `PC` (program counter) register
to jump to any instruction and enables us to perform step-by-step execution of
instructions. We can also read and write the contents of the processor's
general-purpose registers. To read from protected memory, we need to find a
`load word` instruction with an operand register, set the target address in the
operand register, and execute this single instruction. Since we can't read flash
memory, we don't know where the instructions are located. Therefore, it may
sound difficult to find the read word instruction. However, all we need is an
instruction that reads memory from an address in some register to a register,
which is a fairly common operation.

This method is described in detail in the article
[Firmware dumping technique for an ARM Cortex-M0 SoC](https://blog.includesecurity.com/2015/11/firmware-dumping-technique-for-an-arm-cortex-m0-soc/).
I highly recommend reading it.

#### nRF52 Debug Resurrection (APPROTECT Bypass)

Here, the situation is more complicated, and the security level prohibits access
to Debug Port. Therefore, the previous method will not work.

This is where **voltage glitching** comes in. Voltage glitching (also known as
fault injection or power glitching) is a technique used in hacker attacks on
microcontrollers and other embedded systems to disrupt their normal operation
and gain access to protected information or functions. This technique is based
on temporarily changing (glitching) the power supply voltage of a device,
causing it to malfunction. While the microcontroller is running, short bursts
(glitches) of low or high voltage are applied at certain points in time that
disrupt the normal operation of the device. These glitches can cause errors in
the execution of processor instructions, such as skipping or incorrect execution
of individual instructions. This can cause the microcontroller to miss important
safety checks. If a glitch is successfully synchronized, it can disable security
mechanisms or access protected memory, allowing an attacker to retrieve
sensitive data or gain control of the system.

The main goal of this method is to find the exact time interval to apply this
glitch.

The author of
[nRF52 Debug Resurrection (APPROTECT Bypass) Part 1](https://limitedresults.com/2020/06/nrf52-debug-resurrection-approtect-bypass/)
leverages this method by determining the exact time when the AHB-AP has to
initialize itself according to the value of the APPROTECT, which is stored in
UICR (a dedicated Flash memory partition) and applies the glitch at that exact
time, which allows him to bypass the protection and gain access to the
DebugPort. I highly suggest reading the original article for a deeper dive on
this method.
