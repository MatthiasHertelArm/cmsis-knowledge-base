---
id: "intr-diving-into-jtag-security-part-6-attack-on-jtag"
type: "concept"
domain: "debug"
title: "Diving into JTAG — Security (Part 6): Attack / Attack on JTAG"
summary: "The next thing an attacker will determine is the number of devices in the JTAG chain, because even if we have only one microcontroller connected to JTAG - the number of TAPs in the chain may be more than one."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-08-14-diving-into-jtag-part-6.md"
doc_source: "https://interrupt.memfault.com/blog/diving-into-jtag-part-6#attack-on-jtag"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Attack_

The next thing an attacker will determine is the number of devices in the JTAG
chain, because even if we have only one microcontroller connected to JTAG - the
number of TAPs in the chain may be more than one. Next, we need to determine the
lengths of the `IR` and `DR` registers, as well as the number of `DR` registers
theoretically available.

#### Determining the number of TAPs in a JTAG chain

The following algorithm can be used to determine the number of TAPs in a JTAG
chain:

- Send the sequence `0b01100` on the `TMS` pin, thus switching to the `Shift-IR`
  state.
- Push a bunch of ones (as many as you can spare, e.g., 1000) through `TDI` to
  all `IR` registers in the chain. After this, all TAPs will be in `BYPASS`.
- Send the sequence `0b11000` to the selected `TMS` pin, thus switching to the
  `Shift-DR` state.
- Push a bunch of zeros (as many as you can spare, e.g., 1000) through `TDI`
  into all `DR` pins in the chain to reset them to zero
- Start pushing ones through `TDI` into `DR`. As soon as you get a one from
  `TDO`, stop. The number of TAPs in the chain is equal to the number of ones
  pushed in.

#### Determining the size of `IR` and `DR`

The next step is to determine the length of the `IR` and `DR` registers:

- Send on the `TMS` pin the sequence `0b01100` thus moving to the `Shift-IR`
  state.
- Push many ones through `TDI` and then send 0.
- After that, keep pushing ones to `TDI`, counting the number of cycles before 0
  appears on `TDO`. The number of cycles (plus one) will equal the length of the
  `IR` register.
- To find the length of `DR`, perform the same steps, but in the `Shift-DR`
  state

#### Defining undocumented JTAG instructions

Defining undocumented instructions is useful to an attacker because in many
cases, these instructions hide test and debug functions, such as BIT modes for
memory and I/O; scan modes; or debug modes and functions.

In the last section, we determined the length of the `IR` register, and thus we
found out the theoretical number of available JTAG commands (`DR` registers).
However, the number of actually implemented commands can be much smaller than
the theoretical number. To determine the implemented commands, an attacker must
scan and check the whole range. Fortunately, the `IR` register is very often
relatively small and unrealized commands usually behave like `BYPASS` or
generate some fixed value on the `TDO` pin. However, even with these facts,
identifying undocumented commands is a very difficult task, because the
implementation of commands other than standard commands is not specified in JTAG
and each manufacturer is free to do what it wants, so there is no universal
algorithm, so it is almost always solved by searching all available commands and
trying to determine how the behavior of the microcontroller has changed to
understand what a particular command does.

You can find more details
[here](https://deadhacker.com/wp-content/uploads/2010/02/blackbox-jtag-reverse-engineering-tmbinc.pdf)
