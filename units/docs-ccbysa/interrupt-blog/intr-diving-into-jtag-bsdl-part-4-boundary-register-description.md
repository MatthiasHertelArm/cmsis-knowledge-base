---
id: "intr-diving-into-jtag-bsdl-part-4-boundary-register-description"
type: "concept"
domain: "debug"
title: "Diving into JTAG — BSDL (Part 4): Boundary Register Description"
summary: "The Boundary Register description contains a list of boundary-scan cells, along with information regarding the cell type and associated control. For example:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-03-29-diving-into-jtag-part-4.md"
doc_source: "https://interrupt.memfault.com/blog/diving-into-jtag-part-4#boundary-register-description"
license: "CC-BY-SA-4.0"
mode: "V"
---

The Boundary Register description contains a list of boundary-scan cells, along
with information regarding the cell type and associated control. For example:

```plaintext
attribute BOUNDARY_LENGTH of XYZ : entity is 7;

attribute BOUNDARY_REGISTER of XYZ : entity is
    "0 (BC_1, Y(1), output3, X, 6, 0, Z), "&
    "1 (BC_1, Y(2), output3, X, 6, 0, Z), "&
    "2 (BC_1, Y(3), output3, X, 6, 0, Z), "&
    "3 (BC_1, A(1), input, X), "&
    "4 (BC_1, A(2), input, X), "&
    "5 (BC_1, A(3), input, X), "&
    "6 (BC_1, OE, input, X), "&
    "6 (BC_1, *, control, 0)";
```

The `BOUNDARY_LENGTH` attribute specifies the total number of boundary scan
cells.

The `BOUNDARY_REGISTER` attribute specifies the configuration of each boundary
scan cell. Each entry in the attribute represents one cell and includes
information about the cell type, associated signal, mode of operation, and
optional parameters. The format of these entries starting with the first item
is:

- **Cell Number:** The number of the scanning cell and correspondingly the bit
  number in the `BSR` register.
- **Cell Type (BC_1, BC_2, etc.):** Indicates the cell class defined by IEEE
  1149.1. This may sound familiar because we discussed scan cell types in
  [the last article](https://interrupt.memfault.com/blog/diving-into-jtag-part-3#the-boundary-scan-cells).
- **Bound Signal:** For example, `Y(1)`, `A(1)` specifies the logical name of
  the signal bound to this cell.
- **Mode of Operation:** Indicates the cell's function: `input`, `output2`,
  `output3`, `bidir`, `control` or `controlr`. We also touched these functions
  in
  [the previous article](https://interrupt.memfault.com/blog/diving-into-jtag-part-3#the-boundary-scan-register-bsr).
- **Additional Parameters:** These include initial values or conditions for
  specific modes of cell operation. For example, for the STM32F407VG
  microcontroller, these additional parameters are as follows:
  - `Safe` - the value with which the BSR cell should be loaded for safe
    operation when the program can select a random value.
  - `ccel` - the control cell number. Specifies the control cell that drives the
    output enable for this port. As discussed in last week's article, there can
    be multiple scan cells per controller pin and in such cases usually one of
    the scan cells is a control cell, which controls the functionality of one or
    more other cells, for example, by switching them between input and output
    modes. And this parameter indicates the number of the cell which is the
    control cell for this cell
  - `disval` - the value to be written to the control cell for it to switch this
    port from the "output" state to the "input" state.
  - `rslt` - the resulting state. Shows the state of the driver when it is
    disabled.
