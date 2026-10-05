---
id: "intr-diving-into-jtag-bsdl-part-4-overview"
type: "concept"
domain: "debug"
title: "Diving into JTAG — BSDL (Part 4): Overview"
summary: "Files with the .bsd extension describe how to interface with a particular chip using the JTAG interface in the context of PCB and chip boundary-scan testing. The main functions of these files are:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-03-29-diving-into-jtag-part-4.md"
doc_source: "https://interrupt.memfault.com/blog/diving-into-jtag-part-4#overview"
license: "CC-BY-SA-4.0"
mode: "V"
---

Files with the `.bsd` extension describe how to interface with a particular chip
using the JTAG interface in the context of PCB and chip boundary-scan testing.
The main functions of these files are:

1. **Chip Configuration Description:** They provide a detailed description of
   the chip pin configuration, including which pins support JTAG.
2. **Testing and Diagnostics Support:** They support testing the PCB for shorts,
   open circuits, and other common problems. This is especially useful for
   verifying that components are properly mounted on the board.
3. **Test Automation:** They allow you to automate the testing process by
   providing the necessary information to the software that controls the test
   equipment.
4. **Test Portability:** Since BSDL is based on a standard, the files can be
   used with a variety of hardware and software that supports the standard,
   providing a high degree of test portability.

These files are a key component in the testing process of electronic devices,
especially in complex systems where accurate and efficient component testing is
important.

BSDL is a subset of VHDL, a hardware description language that describes how a
particular JTAG device must be implemented for boundary scan. You’ll find `.bsd`
files available from most vendors.

One of the major uses of BSDL is as an enabler for the development of tools to
automate the testing process based on IEEE 1149.1. Tools developed to support
the standard can control the TAP if they know how the boundary-scan architecture
was implemented in the device. Tools can also control the I/O pins of the
device. BSDL provides a standard machine and human-readable data format for
describing how IEEE 1149.1 is implemented in a device.

A BSDL description for a device consists of the following elements:

- Entity Descriptions
- Generic Parameters
- Logical Port Description
- Use Statements
- Pin Mapping(s)
- Scan Port Identification
- IDCODE Register Description
- Instruction Register Description
- Register Access Description
- Boundary Register Description

Let's jump into each of these and walk through some example snippets from `.bsd`
files.
