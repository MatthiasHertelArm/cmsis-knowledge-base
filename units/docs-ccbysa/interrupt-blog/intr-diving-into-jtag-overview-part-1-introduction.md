---
id: "intr-diving-into-jtag-overview-part-1-introduction"
type: "concept"
domain: "debug"
title: "Diving into JTAG - Overview (Part 1): Introduction"
summary: "JTAG (Joint Test Action Group) is a specialized hardware interface based on the IEEE 1149.1 standard. This interface is designed to connect complex chips and devices to standard test and debugging hardware."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-11-29-diving-into-jtag-part1.md"
doc_source: "https://interrupt.memfault.com/blog/diving-into-jtag-part1#introduction"
license: "CC-BY-SA-4.0"
mode: "V"
---

JTAG (Joint Test Action Group) is a specialized hardware interface based on the IEEE 1149.1 standard. This interface is designed to connect complex chips and devices to standard test and debugging hardware.

Nowadays JTAG is mainly used for:

- Output control of microcircuits
- Testing of printed circuit boards
- Flashing of microchips with memory
- Chip software debugging

The testing method implemented in the standard is called Boundary Scan. The name reflects the idea of the process: Functional blocks within the chip are isolated, and specific signal combinations are applied to their inputs. The state of each block’s output is then evaluated. The whole process is performed by special commands via the JTAG interface, and no physical intervention is required.
