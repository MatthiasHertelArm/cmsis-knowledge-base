---
id: "intr-diving-into-jtag-boundary-scan-par-the-boundary-scan-register-bsr"
type: "concept"
domain: "debug"
title: "Diving into JTAG — Boundary Scan (Part 3): The Boundary Scan Register (`BSR`)"
summary: "Boundary Scan Register (BSR) is one of the data registers (DR) consisting of a sequence of scan cells (Boundary-Scan Cells). Figure 5 shows how the scan cells are linked together to form the boundary-scan register."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-03-22-diving-into-jtag-part-3.md"
doc_source: "https://interrupt.memfault.com/blog/diving-into-jtag-part-3#the-boundary-scan-register-bsr"
license: "CC-BY-SA-4.0"
mode: "V"
---

Boundary Scan Register (`BSR`) is one of the data registers (`DR`) consisting of
a sequence of scan cells (Boundary-Scan Cells). Figure 5 shows how the scan
cells are linked together to form the boundary-scan register. The order of
linking within the device is determined by the physical adjacency of the pins
and/or by other layout constraints. The boundary-scan register is selected by
the `EXTEST`, `SAMPLE`, `PRELOAD`, and `INTEST` instructions.



  


During scan operations, data is shifted BSR in the direction from `TDI` to
`TDO`. The values in the scan cells can be changed or read, allowing testing to
be performed.

The size and format of this register determine the number and sequence of scan
cells in a particular chip - i.e., before testing, it is necessary to find out
the length and format of the `BSR` register. This information is supplied by the
manufacturer in the BSDL file format for a particular chip. Here is an example
of a truncated BSDL file for the STM32F407 microcontroller:

```plaintext
num       cell        port     function
405       BC_1,        *,      CONTROL,
404       BC_1,        PE2,    OUTPUT3,
403       BC_4,        PE2,    INPUT,
```

where,

- `num`: Is the cell number.
- `cell`: Is the cell type as defined by the standard.
- `port`: Is the design port name. Control cells do not have a port name.
- `function`: Is the function of the cell as defined by the standard. Is one of
  `input`, `output2`, `output3`, `bidir`, `control`, or `controlr`.

We can see from this file that:

- The number of scan cells, and consequently the length of the `BSR` register is
  405 pieces/bit.
- One I/O pin can have 3 scan cells which are divided according to the
  functionality to be performed: `CONTROL`, `OUTPUT3`, `INPUT`.

This information must be considered when forming the contents of the register
`BSR`.
