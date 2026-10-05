---
id: "intr-diving-into-jtag-bsdl-part-4-register-access-description"
type: "concept"
domain: "debug"
title: "Diving into JTAG — BSDL (Part 4): Register Access Description"
summary: "The register access defines which register is placed between TDI and TDO for each instruction."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-03-29-diving-into-jtag-part-4.md"
doc_source: "https://interrupt.memfault.com/blog/diving-into-jtag-part-4#register-access-description"
license: "CC-BY-SA-4.0"
mode: "V"
---

The register access defines which register is placed between `TDI` and `TDO` for
each instruction.

As discussed in
[Part 1](https://interrupt.memfault.com/blog/diving-into-jtag-part1), various
codes placed in the instruction register can select various internal registers
as a data register: `BYPASS`, `IDCODE`, `BSR`. The `REGISTER_ACCESS` attribute
determines which instruction will connect which register as a data register. For
example:

```plaintext
attribute REGISTER_ACCESS of XYZ : entity is
    "BOUNDARY (EXTEST, SAMPLE), "&
    "BYPASS (BYPASS) ";
```

Similar to instructions that may be standard, or may be unique to a particular
chip manufacturer (or a particular model), the JTAG module's plug-in registers
may not be limited to a list of `DEVICE_ID`, `BYPASS`, and `BOUNDARY`. By
entering the `MY_INSTRUCTION_OPCODE` instruction in the `INSTRUCTION_OPCODE`
attribute, it is possible to tell the control software in the `REGISTER_ACCESS`
attribute that it wishes to connect a non-standard register if the corresponding
instruction has been loaded into the instruction register:

```plaintext
attribute REGISTER_ACCESS of SIMPLE_IC : entity is
    <...>
    "MY_REG[8] (MY_INSTRUCTION)," &
    <...>
```

Here [8] defines the length of the register.

In addition, you can specify in this attribute what value the register to be
connected should be initialized with when the JTAG module enters the
`Capture-DR` state:

```plaintext
"MY_REG[8] (MY_INSTRUCTION CAPTURES 01010101)," &
```
