---
id: "intr-diving-into-jtag-boundary-scan-par-the-boundary-scan-instructions"
type: "concept"
domain: "debug"
title: "Diving into JTAG — Boundary Scan (Part 3): The Boundary Scan Instructions"
summary: "This command reads the current values from the scan cells and passes them to the TDO output. This is useful for reading the current state of the chip pins."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-03-22-diving-into-jtag-part-3.md"
doc_source: "https://interrupt.memfault.com/blog/diving-into-jtag-part-3#the-boundary-scan-instructions"
license: "CC-BY-SA-4.0"
mode: "V"
---

### `SAMPLE` Instruction

This command reads the current values from the scan cells and passes them to the
`TDO` output. This is useful for reading the current state of the chip pins.
This command causes `TDI` and `TDO` to be shorted to the `BSR` register.
However, the chip remains in the normal operating state. During the execution of
this command, the `BSR` register can be used to capture the data exchanged by
the chip during normal operation. In other words, with this instruction, we can
read signals from the microcontroller output without disturbing its operation.



  


In step 3, when the `SAMPLE` instruction is loaded into the `IR` register, the
signal is read from the pins to the scan cell. In the next steps, we move to the
`Shift-DR` state and read the `BSR` register along with the value of the pins
received in the previous step. Note that when the read unit passes through the
scan cells bound to pins `B3`, `B4`, `B5` the LEDs connected to these pins do
not light up, because at the moment the scan cells are not connected to the chip
pins.

### `PRELOAD` Instruction

This command allows you to preload certain values into Boundary-Scan Cells for
later testing or other operations.



  


Here, everything is simple. After writing the command `PRELOAD`, we just need to
write the values in the scan cells to the register `BSR` for the corresponding
pins in the state `Shift-DR`. And again, note that after writing all the values
to the scan cells, the LEDs connected to pins `B3`, `B4`, `B5` do not light up
either.

### `SAMPLE/PRELOAD` Instruction

Sometimes two commands: `SAMPLE` and `PRELOAD` are combined into one. When
writing this command to the `IR` register, the values of the pins are read into
the scan cells (`BSR` register) and then in the `Shift-DR` state we read these
values and write new values for the pins into the scan cells (`BSR` register).
Again, after the `SAMPLE/PRELOAD` instruction is completed, has no effect on the
pins themselves.



  


Typically, the `SAMPLE/PRELOAD` command is the first command to be executed
during Boundary Scan testing, and it serves as the basis for many other
operations.

### `EXTEST` Instructions

The `EXTEST` command in JTAG is used to test external circuits connected to the
microcontroller pins. When the microcontroller is in `EXTEST` mode, all its
function blocks are disabled and the microcontroller pins can be used to test
the connected external circuits for short circuits, open circuits, etc. This
command can be used to verify the pins and circuits of a microcontroller during
the manufacturing process and to verify that external circuits are properly
wired during development.

This command is the one for which we wrote values to the scan cells in the
`PRELOAD` command. Because exactly `EXTEST` makes the scan cells transfer the
values of the signals stored in them to the output.



  


> _After using this command, the I/O pins are disconnected from the internal
> logic of the microcontroller and you can no longer control them from the
> program._

### `INTEST` Instructions

It is also possible to use boundary-scan cells to test the internal
functionality of a device. This use of the boundary-scan register is called
Internal Test, shortened to Intest. Intest is only really used for very limited
testing of the internal functionality to identify defects such as the wrong
variant of a device or to detect some gross internal defect.
