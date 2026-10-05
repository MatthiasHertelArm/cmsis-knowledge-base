---
id: "intr-diving-into-jtag-overview-part-1-control-signals"
type: "concept"
domain: "debug"
title: "Diving into JTAG - Overview (Part 1): Control signals"
summary: "The Test Access Port comprises four mandatory signals (TCK, TMS, TDI, TDO) and one optional signal (TRST)."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-11-29-diving-into-jtag-part1.md"
doc_source: "https://interrupt.memfault.com/blog/diving-into-jtag-part1#control-signals"
license: "CC-BY-SA-4.0"
mode: "V"
---

The Test Access Port comprises four mandatory signals (`TCK`, `TMS`, `TDI`, `TDO`) and one optional signal (`TRST`).

- `TDI` (Test Data Input) — test data input. The commands and data are inserted into the chip through this pin on the rising edge of the signal `TCK`.
- `TDO` (Test Data Output) — serial data output. Commands and data are output from the chip through this pin on the falling edge of the signal `TCK`.
- `TCK` (Test Clock) — clock input.
- `TMS` (Test Mode Select) — controls the transitions between states of the finite state machine TAP.
- `TRST` (Test Reset) — reset signal of the TAP finite state machine.

The standard is that the JTAG module reads data from the `TMS` and `TDI` lines on the rising edge of the `TCK` line. The JTAG module in any chip must also change the logic value on the `TDO` line on the falling edge of `TCK`. In the diagram below, the moments of reading data by the JTAG module are shown with the red dotted line and the moments of writing data are shown with the green dotted line.
