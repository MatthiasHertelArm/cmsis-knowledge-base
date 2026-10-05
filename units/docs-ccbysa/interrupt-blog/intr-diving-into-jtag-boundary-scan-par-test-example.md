---
id: "intr-diving-into-jtag-boundary-scan-par-test-example"
type: "concept"
domain: "debug"
title: "Diving into JTAG — Boundary Scan (Part 3): Test Example"
summary: "Let's see how to use the SAMPLE/PRELOAD and EXTEST instructions to test the board for a fault."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-03-22-diving-into-jtag-part-3.md"
doc_source: "https://interrupt.memfault.com/blog/diving-into-jtag-part-3#test-example"
license: "CC-BY-SA-4.0"
mode: "V"
---

Let's see how to use the `SAMPLE/PRELOAD` and `EXTEST` instructions to test the
board for a fault.

Let's imagine that we have the following situation: two chips `D1` and `D2`
connected to each other through pins 5,6,7 for chip `D1` and 2,3,4 for chip `D2`
and we need to check that these connections work correctly. But let us assume
that a solder bridge has formed between pins `D1:6,7` and `D2:2,3`. The
described situation is presented in the figure 11.



  


So what can be done using JTAG to check the connection of chips `D1` and `D2`:

1. Load into chip `D1` using the `PRELOAD` command the template: `0b0101010000`.
2. Use the `EXTEST` command to output the generated test pattern to the chip
   pins.
3. Using the `SAMPLE` command for the `D2` chip, we read the pin states and
   expect the following result: `0b00001010`, but we get `0b00001000`, i.e.,
   there is an incorrect signal on pin 2 of chip `D2`, so the connection `D1:7`
   <--> `D2:2` has some problems.
