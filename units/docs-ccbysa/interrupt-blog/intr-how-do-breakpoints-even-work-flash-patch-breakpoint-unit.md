---
id: "intr-how-do-breakpoints-even-work-flash-patch-breakpoint-unit"
type: "concept"
domain: "debug"
title: "How do breakpoints even work?: Cortex-M Hardware Breakpoints / Flash Patch & Breakpoint Unit"
summary: "Part of: Cortex-M Hardware Breakpoints"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-06-17-cortex-m-breakpoints.md"
doc_source: "https://interrupt.memfault.com/blog/cortex-m-breakpoints#flash-patch-breakpoint-unit"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Cortex-M Hardware Breakpoints_

For ARM Cortex-M MCUs, hardware breakpoint functionality is exposed via the Flash Patch and Breakpoint Unit (**FPB**)[^10].

The FPB has two main features:

1. Allows hardware breakpoints to be configured and enabled.
2. Allows patching of Flash Code & Data. Historically this has been a popular way to debug ROM bootloaders or ship fixes for devices that can't perform full over the air updates. These days more and more embedded devices perform full firmware updates and so the practice is becoming less common. The art of flash patching deserves a post of its own so we won't be digging deeper here.

For breakpoint management, there are two register types you will care about inside the **FPB**, `FP_CTRL` & `FP_COMPn`.

#### Flash Patch Control Register, FP_CTRL, 0xE0002000



The `FP_CTRL` is where you can find out information about how many hardware breakpoints are supported and enable the **FPB**. Notably,

- `REV`: There are only two revisions available today, Version 1 (`REV=0`) & Version 2 (`REV=1`). Depending on the revision, the layout of the `FP_COMPn` register will be slightly different. The notable difference between the two versions is that for Version 1 breakpoints can _only_ be installed if the address is in the ARM Code Region range (`0x00000000-0x1FFFFFFF`) but with Version 2 breakpoints can be installed over the entire 4GB address space.
- Number of Available Hardware Breakpoints can be computed by: `FP_CTRL[6:4] << 4 | FP_CTRL[3:0]`
- `ENABLE` turns on the **FPB** Unit when set to 1 and disables it when set to 0.

> NOTE: A write to the `FP_CTRL` register will only take effect if the `KEY` bit is 1. Otherwise, the operation will be a no-op.

#### Flash Patch Comparator register, FP_COMPn, 0xE0002008- 0xE0002008+4n

Comparators for breakpoints will always be `FP_COMP0` up to the number of supported breakpoints minus 1. Technically up to 127 hardware breakpoints can be implemented but usually only 2-6 are.

##### Version 1 Layout



`ENABLE` flips on the individual comparator and `REPLACE` controls the behavior as follows:

| Replace | Behavior                                                                                       |
| ------- | ---------------------------------------------------------------------------------------------- |
| 0b00    | N/A - Used to enable Flash Patching                                                            |
| 0b01    | Install breakpoint on instruction at `0b000:FP_COMP[28:2]:00`.                                 |
| 0b10    | Install breakpoint on instruction at `0b000:FP_COMP[28:2]:10`.                                 |
| 0b11    | Install breakpoint on instructions at both `0b000:FP_COMP[28:2]:00` & `0b000:FP_COMP[28:2]:10` |

##### Version 2 Layout

The Version 2 Layout is a little more straightforward. Bit 0, Breakpoint Enable (**BE**), controls whether or not the breakpoint is enabled:



Bit 31:1 is the address to break on:



> Note this is able to cover the entire 32-bit address space even though the bottom bit is used
> for **BE** because bit 0 is used to convey whether the ARM or Thumb instruction set is
> being used rather than encoding any address information _and_ instructions must be aligned by their width.
