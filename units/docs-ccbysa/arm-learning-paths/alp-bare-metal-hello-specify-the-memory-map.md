---
id: "alp-bare-metal-hello-specify-the-memory-map"
type: "concept"
domain: "project"
title: "Create an Armv8-A embedded application: Create and build a Hello World example project: Specify the memory map"
summary: "The default memory map used by the linker does not match the memory map of the FVP."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/bare-metal/hello.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/bare-metal/hello/#specify-the-memory-map"
license: "CC-BY-SA-4.0"
mode: "V"
---

The [default memory map](https://developer.arm.com/documentation/100748/latest/Embedded-Software-Development/Default-memory-map) used by the linker does not match the [memory map](https://developer.arm.com/documentation/100964/latest/Base-Platform/Base---memory/Base-Platform-memory-map) of the FVP.

You must specify a memory map that matches the target. The Arm linker feature [scatter-loading](https://developer.arm.com/documentation/101754/latest/armlink-Reference/Scatter-loading-Features) is used.

Create a file `scatter.txt` with the following contents:
#### scatter.txt
```console
ROM_LOAD 0x00000000 0x00010000
{
    ROM_EXEC +0x0 0x10000
    {
      * (InRoot$$Sections)
      * (+RO)
    }

    RAM_EXEC 0x04000000 0x10000
    {
      * (+RW, +ZI)
    }
    ARM_LIB_STACKHEAP 0x04010000 EMPTY 0x10000 {}
}
```
and link the image using the scatter file.
```console
armlink --scatter=scatter.txt hello.o -o hello.axf
```
### Understanding the scatter file

The statements in the scatter file define the different regions of memory and their purpose. The following defines a `load region`, starting at address 0x0, and of size 0x10000 bytes. A `load region` is an area of memory that contains the image file at reset before execution starts (typically defining the Flash memory addresses of a real system).
```output
ROM_LOAD 0x00000000 0x00010000
{...}
```

Within the `load region` define `execution region(s)`, where the code/data will be located at run-time:
```output
  ROM_EXEC +0x0 0x10000
  {
    * (InRoot$$Sections)
    * (+RO)
  }
```
An execution region is called a `root region` if it has the same load-time and execute-time address. The initial entry point of an image must be in a root region, as this is executed before scatterloading can occur to relocate that code. You can use the `InRoot$$Sections` section name to ensure the appropriate C library code for scatterloading is in this section (useful when there are multiple code regions).

In the scatter file, all read-only (`RO`) code/data (including the entry point `__main()`) is placed in the `ROM_EXEC` root region.
```output
  RAM_EXEC 0x04000000 0x10000
  {
    * (+RW, +ZI)
  }
```
`RAM_EXEC` contains any read-write (`RW`) or zero-initialised (`ZI`) data. Because this has been located at a different address (0x04000000, in SRAM), it's not a root region.

Region names (such as `ROM_LOAD`, `ROM_EXEC`, and `RAM_EXEC` above) are arbitrary. However there are [reserved names](https://developer.arm.com/documentation/100748/latest/Embedded-Software-Development/Placing-the-stack-and-heap) for the Stack and Heap regions. This example uses a single region (`ARM_LIB_STACKHEAP`) for both.
```output
ARM_LIB_STACKHEAP 0x04010000 EMPTY 0x10000{}
```
* The heap will start at `0x04010000` and grows upwards.
* The stack will start at `0x04020000` (`0x04010000 + 0x10000`) and grows downwards.
* Specify the region is `EMPTY` as there are no explicit sections to locate there.
