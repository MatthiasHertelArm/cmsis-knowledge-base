---
id: "intr-diving-into-jtag-bsdl-part-4-instruction-register-description"
type: "concept"
domain: "debug"
title: "Diving into JTAG — BSDL (Part 4): Instruction Register Description"
summary: "The Instruction Register description identifies the device-dependent characteristics of the Instruction Register. For example:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-03-29-diving-into-jtag-part-4.md"
doc_source: "https://interrupt.memfault.com/blog/diving-into-jtag-part-4#instruction-register-description"
license: "CC-BY-SA-4.0"
mode: "V"
---

The Instruction Register description identifies the device-dependent
characteristics of the Instruction Register. For example:

```plaintext
attribute INSTRUCTION_LENGTH of XYZ : entity is 2;

attribute INSTRUCTION_OPCODE of XYZ : entity is
    "BYPASS (11), "&
    "EXTEST (00), "&
    "SAMPLE (10) ";

attribute INSTRUCTION_CAPTURE of XYZ : entity is "01";
```

The `INSTRUCTION_LENGTH` attribute defines the length of the `IR` register in
bits.

The `INSTRUCTION_OPCODE` attribute defines the command codes.

The `INSTRUCTION_CAPTURE` attribute defines the value that will be loaded into
the shift register when TAP enters the `Capture-IR` state, in other words, this
attribute specifies what the instruction register is initialized with.
