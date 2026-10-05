---
id: "alp-bare-metal-reset-link-the-application"
type: "concept"
domain: "project"
title: "Create an Armv8-A embedded application: Write a reset handler: Link the application"
summary: "Modify the scatter file so that the startup code goes into the root region ROM_EXEC."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/bare-metal/reset.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/bare-metal/reset/#link-the-application"
license: "CC-BY-SA-4.0"
mode: "V"
---

Modify the scatter file so that the startup code goes into the root region `ROM_EXEC`. This must be located as the `FIRST` section in the region, so that it is at exactly `0x0`, and so is executed when the processors start.

#### scatter.txt
```console
  ROM_EXEC +0x0
  {
    startup_el3.o (BOOT, +FIRST)
    * (InRoot$$Sections)
    * (+RO)
  }
```
Link the objects, specifying the symbol `el3_entry` as the entry point.
```console
armlink --scatter=scatter.txt hello.o startup_el3.o -o hello.axf --entry=el3_entry
```
The entry point is used by the linker to determine which code is necessary to keep. It is also used by debuggers to know where to start execution from.
