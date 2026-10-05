---
id: "intr-diving-into-jtag-boundary-scan-par-the-boundary-scan-cells"
type: "concept"
domain: "debug"
title: "Diving into JTAG — Boundary Scan (Part 3): The Boundary Scan Cells"
summary: "As mentioned above, scan cells are the core element that makes Boundary Scan possible."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-03-22-diving-into-jtag-part-3.md"
doc_source: "https://interrupt.memfault.com/blog/diving-into-jtag-part-3#the-boundary-scan-cells"
license: "CC-BY-SA-4.0"
mode: "V"
---

As mentioned above, scan cells are the core element that makes Boundary Scan
possible. These cells can be programmatically configured to perform various
functions, such as transmitting or receiving data, allowing you to test
connections between chips without having to physically access the pins.



  


Each boundary-scan cell can:

- Capture data on its parallel input `PI`
- Update data onto its parallel output `PO`
- Serially scan data from `SO` to its neighbor's `SI`
- Behave transparently: `PI` passes to `PO`

At the device level, the boundary-scan elements contribute nothing to the
functionality of the internal logic. The boundary-scan path is independent of
the function of the device.

The boundary-scan cells must be provided on all device digital input and digital
output signal pins, except Power and Ground.

Scan cells can be categorized by functionality into the following types:

- **Input Cells:** Used to monitor input signals.

- **Output Cells:** Used to control the output signals:

  - `Output2`: This cell type does not support three-state logic. It can set the
    pin to state "`0`" or "`1`".
  - `Output3`: This cell type supports three-state logic, allowing a pin to be
    in the "`0`", "`1`" or "`Hi-Z`" (high impedance) state.

- **Bidirectional Cells**: Can be used for both input and output. Cells of this
  type typically support three-state logic.

- **Control Cells**: Used to control other cell types:

  - `Control`: This cell type can control the functionality of one or more other
    cells, for example, by switching them between input and output modes. This
    cell is not connected to the chip pins
  - `ControlR`: This cell type is similar to the `Control` type but with the
    additional ability to read the state of the controlled cells. This cell is
    not connected to the chip pins.

- **\*Clock Cell**: This function indicates that this cell is connected to the
  system clock frequency, which allows `INTEST` mode operation.

Each scan cell typically consists of a small set of flip-flops and logic
elements that allow it to perform various functions such as storing data,
transferring data to other cells, etc.

In general, a scan cell can be represented by the following scheme:



  


A Boundary Scan cell's internal architecture can be highly different. In its
version from 2001, the IEEE Std. 1149.1 describes ten different cell types
(`BC_1` to `BC_10`):

- `BC_1` – The basic Boundary Scan cell that can be used as input, output,
  control, and internal cells. Supports all instructions.
- `BC_2` – Boundary Scan cell that can be used as an input cell. Cell
  architecture is like `BC_1` except a multiplexer in the signal patch at the
  entrance to the cell from the Parallel input.
- `BC_3` – Cell only used for inputs or internal cells as it does not possess an
  Update latch, but it does support the `INTEST` instruction.
- `BC_4` – Like the `BC_3`, this cell does not possess an Update latch. Also, a
  multiplexer has been removed from the system signal path. Removing the
  multiplexer removes some potential signal delay through the cell. This cell
  cannot be used on any input pin except a system clock.
- `BC_5` – Cell can be used as a merged cell application. Merged cells act as an
  input cell, thus satisfying the requirement that an input pin have a cell and
  it can also serve to drive the enable of an output driver.
- `BC_7` – Cell can provide data to the output driver and also monitor pin
  activity even when the output drive is driving the pin.
- `BC_8` – Cell monitors only the pin driver output and therefore does not
  support the `INTEST` instruction.
- `BC_9` – A self-monitoring cell for outputs that support the `INTEST`
  instruction.
- `BC_10` – A self-monitoring cell that does not support the `INTEST`
  instruction.

The number of cells need not necessarily match the number of chip pins. For
example, if the chip pin is bidirectional (pin `B2` in Figure 4), conceptually
at least, three boundary-scan cells are required: one on the input side, one on
the output side, and one to allow control of the IO status. In practice, the two
IO scan cells are usually combined into a single multi-function cell called a
`BC_7`.
