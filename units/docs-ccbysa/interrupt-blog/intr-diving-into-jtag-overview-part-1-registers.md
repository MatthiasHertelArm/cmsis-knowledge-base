---
id: "intr-diving-into-jtag-overview-part-1-registers"
type: "concept"
domain: "debug"
title: "Diving into JTAG - Overview (Part 1): Registers"
summary: "The TAP state machine allows access to two special registers, the IR, and a symbolic register called DR."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-11-29-diving-into-jtag-part1.md"
doc_source: "https://interrupt.memfault.com/blog/diving-into-jtag-part1#registers"
license: "CC-BY-SA-4.0"
mode: "V"
---

The TAP state machine allows access to two special registers, the `IR`, and a symbolic register called DR.

The instruction registers store the current instruction to be executed. The value of this register is used by the TAP controller to decide what to do with incoming signals. The most commonly used instruction specifies which data register the incoming data should go into.

The Data Register is a placeholder for the register that is currently selected with the current content of the `IR`. Thus, `IR` is an index into a number of registers, and DR is the currently selected register. There are three main types of data registers:

- BSR (Boundary Scan Register) — The main register for testing. It is used to transfer data to and from the pins of the chip.
- `BYPASS` is a single-bit register that transfers data from `TDI` to `TDO`. It allows testing other chips connected in series with minimum delays.
- `IDCODE`S — stores the ID code and revision number of the chip.



  



In the picture above you can see an approximate illustration of the principle of operation of the DR register: the switchers SW3 and SW4 choose the current register depending on the instruction in `IR`.

The size of the `IR` is implementation specific and usually varies between 4 and 32 bits. Since the selected register is directly accessed when scanning DR, the size DR depends on the current instruction.

JTAG registers are an important part of the microcontroller debugging process because they allow you to control and monitor the state of the microcontroller during program execution. Each microcontroller manufacturer may use its own JTAG registers, so you should consult the documentation of your particular microcontroller for details on the JTAG registers it supports.
