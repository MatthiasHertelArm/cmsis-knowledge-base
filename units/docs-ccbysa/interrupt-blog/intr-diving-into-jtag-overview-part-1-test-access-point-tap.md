---
id: "intr-diving-into-jtag-overview-part-1-test-access-point-tap"
type: "concept"
domain: "debug"
title: "Diving into JTAG - Overview (Part 1): Test Access Point (TAP)"
summary: "The Test Access Port (TAP) is one of the key elements of the JTAG protocol designed to control and configure chips connected to the JTAG chain."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-11-29-diving-into-jtag-part1.md"
doc_source: "https://interrupt.memfault.com/blog/diving-into-jtag-part1#test-access-point-tap"
license: "CC-BY-SA-4.0"
mode: "V"
---

The Test Access Port (TAP) is one of the key elements of the JTAG protocol designed to control and configure chips connected to the JTAG chain.

The TAP operates as a simple finite-state machine that is controlled by the `TMS` (Test Mode Select) signal. It allows access to the internal registers of microcontrollers and other devices through JTAG commands.

Each device connected to the JTAG chain has its own TAP, which consists of the `IR` (Instruction Register) and DR (Data Register) registers. The `IR` the register is used to select the instruction to be executed on the device and the DR the register is used to transfer data.
