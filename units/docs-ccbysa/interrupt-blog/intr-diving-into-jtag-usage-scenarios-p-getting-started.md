---
id: "intr-diving-into-jtag-usage-scenarios-p-getting-started"
type: "concept"
domain: "debug"
title: "Diving into JTAG — Usage Scenarios (Part 5): Getting Started"
summary: "To make working on this use case more convenient you need a specialized program. In this article, we will look at working with the program TopJTAG Probe and debugger SEGGER J-Link."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-06-12-diving-into-jtag-part-5.md"
doc_source: "https://interrupt.memfault.com/blog/diving-into-jtag-part-5#getting-started"
license: "CC-BY-SA-4.0"
mode: "V"
---

To make working on this use case more convenient you need a specialized program.
In this article, we will look at working with the program
[TopJTAG Probe](http://www.topjtag.com/probe/) and debugger
[SEGGER J-Link](https://www.segger.com/products/debug-probes/j-link/). These
aren't the only tools suitable for this task, but I am a long-time fan of J-Link
debuggers, and the TopJTAG Probe program turned out to be the simplest and the
most accessible from a quick Google search.

While many people are familiar with SEGGER products, TopJTAG Probe requires an
introduction.

The TopJTAG Probe program is software that works with the JTAG interface and is
used for testing printed circuit boards (PCB). This software is commonly used to
diagnose and repair PCBs and work with microcontrollers and other devices that
support JTAG.

A boundary-scan (JTAG) based simple logic analyzer and circuit debugging
software. It provides the ability to monitor pin values in real-time without
interference with the normal operation of a working device and to interactively
set up pin values to test board-level interconnects or on-chip internal logic.

To start working with TopJTAG Probe, we need to create a new project. To do
this, go to the _File->New Project Wizard_ menu.



 


In the next window, select the required JTAG Probe and frequency. In my case, it
is SEGGER J-Link and 12 MHz.



 


Click _Next_.

The program will scan our JTAG circuit and display a list of available TAP IDs.

> You should already have a debugger connected to the board and the computer for
> this step to go well



 


Click _Next_.

At this point, you must specify .BSD files for each detected TAP. If you do not
specify a .BSD file for a TAP, it will be put into the `BYPASS` state.

We specify
[STM32F405\_415\_407\_417\_LQFP100.bsd](https://bsdl.info/details.htm?sid=61a8799988cb03f688ca59b002289d77)
file for the first TAP - SGS/Thomson (`06413041h`) as it is responsible for
Boundary Scan. We leave the second TAP in `BYPASS`. To select a file, click the
_CLICK HERE TO SET_ link and select the desired file.



 


After that, press _Finish_, and the program is ready.

Appearance of the program:



 


`1` - Pins Window. The _Pins window_ lists all pins belonging to the selected
device. Any pin can be quickly located by typing its name, number, or port name
into the search box. The pin or bus name, PIN, port name, type, and current
value are displayed for every pin.

`2` - JTAG Chain (Main) View. The _JTAG Chain view_ (main program's view) shows
package outlines with color-coded pin values. These values are updated while the
boundary scan is running.

Device instructions are displayed below the package outline.

Pin values are color-coded. Black means 0, red means 1, brown means high-Z, and
blue means linkage pin. For bidirectional pins, it is possible to display either
input or output values.

`3` - Watch Window. The _Watch window_ keeps pins of interest in one place to
simplify monitoring and control.

`4` - Waveform Window. The _Waveform window_ records and displays waveforms.
This is a wonderful tool to view and analyze a signal's history. It is
particularly useful for fast-changing signals.
