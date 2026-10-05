---
id: "intr-diving-into-jtag-boundary-scan-par-the-principle-of-boundary-scan"
type: "concept"
domain: "debug"
title: "Diving into JTAG — Boundary Scan (Part 3): The Principle of Boundary-Scan"
summary: "The principle of operation is that special cells — scan cells — are inserted between the physical pins of the chip and its internal logic."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-03-22-diving-into-jtag-part-3.md"
doc_source: "https://interrupt.memfault.com/blog/diving-into-jtag-part-3#the-principle-of-boundary-scan"
license: "CC-BY-SA-4.0"
mode: "V"
---

The principle of operation is that special cells — scan cells — are inserted
between the physical pins of the chip and its internal logic.



  


In normal mode, these cells are transparent and the core is connected to I/O
ports. In boundary scan mode, the core is isolated from the ports, and the port
signals are controlled by the JTAG interface.

The boundary scan cells are connected to a serial shift register, which is
referred to as the boundary scan register (`BSR`). This register can be used to
read and write port states.

In general, the principle of Boundary-Scan operation is that with the help of
special JTAG commands, it is possible to set values in the scan cells and,
through them, influence the chip pins.

Following boundary scan instructions are defined in the IEEE standard:

- `BYPASS` (mandatory): `TDI` is connected to `TDO` via a single-shift register.
- `SAMPLE` (mandatory): Takes a snapshot of the pins of the IC.
- `PRELOAD` (mandatory): Loads data to the boundary scan register.
- `EXTEST` (mandatory): Apply preloaded data of the boundary scan register to
  the ports.
- `INTEST` (optional): Apply preloaded data of the boundary scan register to the
  core logic.
- `CLAMP` (optional): Apply preloaded data of the boundary scan register to the
  ports and select the `BYPASS` register as the serial path between `TDI` and
  `TDO`.
- `HIGHZ` (optional): Places the IC in an inactive drive state (e.g. all ports
  are set to a high impedance state) and leaves `BYPASS` register as the
  selected register.

The structure of the boundary scan chain and the instruction set are described
with the Boundary Scan Description Language (BSDL). BSDL is a subset of the Very
High-level Design Language (VHDL). The BSDL files are provided by the IC
manufacturer. The BSDL language will be covered in the next article, so we will
not describe it in detail here.
