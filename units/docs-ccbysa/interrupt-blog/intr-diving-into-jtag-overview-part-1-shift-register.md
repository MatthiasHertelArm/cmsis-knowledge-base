---
id: "intr-diving-into-jtag-overview-part-1-shift-register"
type: "concept"
domain: "debug"
title: "Diving into JTAG - Overview (Part 1): Shift register"
summary: "Data transfer (read/write) in the JTAG protocol is performed by the shift register principle. In a shift register, the data is transferred sequentially, bit by bit, one per clock cycle."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-11-29-diving-into-jtag-part1.md"
doc_source: "https://interrupt.memfault.com/blog/diving-into-jtag-part1#shift-register"
license: "CC-BY-SA-4.0"
mode: "V"
---

Data transfer (read/write) in the JTAG protocol is performed by the shift register principle. In a shift register, the data is transferred sequentially, bit by bit, one per clock cycle.



  


This register is located between the `TDI` and `TDO` pins and is used to receive information from the `TDI` pin and output information to the `TDO` pin. Every time you want to write something to the TAP via JTAG protocol - you set the necessary signals to the `TDI` pin - these signals are synchronously written to the shift register starting from the highest bit and gradually moving to the lowest bit of the register with each new clock, and the value of the lowest bit of the shift register with each clock is moved to the `TDO` pin, from which we can read it.

>**Note**: I have not found detailed information about this anywhere, but from
>a general understanding, I can assume that for each register accessible
>via JTAG protocol, there is a separate version of the shift register.
>I.e. assuming we have we have a TAP with `IR` register 4 bits length,
>`BYPASS` register 1 bit length, `IDCODE` register 32 bits length, then for
>each of these registers there will be a separate version of the shift
>register which will be integrated into the scan chain between `TDI` and
>`TDO` pins every time the corresponding `IR`, `BYPASS`, or `IDCODE`
>registers are selected. But this is just my assumption, which has not
>been documented yet.
