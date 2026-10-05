---
id: "intr-faster-debugging-with-watchpoints-cortex-m-hardware-watchpoints"
type: "concept"
domain: "debug"
title: "Faster Debugging with Watchpoints: How do watchpoints work? / Cortex-M Hardware Watchpoints"
summary: "Now that we have a pretty good idea of how GDB sets and removes watchpoints, let's examine how they are implemented in hardware for Cortex-M targets. For our debug setup, it's SEGGER's JLinkGDBServer that will be responsible for this programming."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-09-16-cortex-m-watchpoints.md"
doc_source: "https://interrupt.memfault.com/blog/cortex-m-watchpoints#cortex-m-hardware-watchpoints"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: How do watchpoints work?_

Now that we have a pretty good idea of how GDB sets and removes watchpoints, let's examine how they are implemented in hardware for Cortex-M targets. For our debug setup, it's SEGGER's JLinkGDBServer that will be responsible for this programming.

#### Data Watchpoint and Trace Unit

For ARM Cortex-M MCUs, hardware watchpoint functionality is exposed via the "Data Watchpoint and Trace Unit" (**DWT**)[^10].

The DWT implements many tracing features and there are many articles to write on the topic. Today we will focus exclusively on the watchpoints and the registers needed to configure them.

#### DWT Control register, DWT_CTRL, 0xE0001000



The `DWT_CTRL` is where you can find out information about how many hardware watchpoints are supported. Notably,

- `NUMCOMP`: The number of watchpoint comparators implemented or 0 in the case the DWT is not included in the hardware.

Provided the Cortex-M supports at least one watchpoint, we can configure them using three registers, `DWT_FUNCTIONn`,`DWT_COMPn` & `DWT_MASKn`. We will explore the configuration setting for these registers in more detail below.

#### Comparator Function register DWT_FUNCTIONn, 0xE0001028 + 16n

The function register controls the type of memory to watch and what will happen when a watchpoint event occurs. We can configure a "watchpoint event" which either triggers a halting event or a DebugMonitor exception.

> Note: One can also configure the peripheral to emit events out via the tracing subsystem (i.e ITM, ETM) but that is outside the scope of this article.

The `DWT_FUNCTION` register definition looks like this:



where,

- `MATCHED` Indicates if there was a match since the last time the register was read. This can be used by a debugger to determine if this was the source of the debug event emitted. It's cleared on read so you will likely never see it set when using a debugger.
- `DATAVADDR1`, `DATAVADDR0`, `DATAVSIZE`, `LNK1ENA` We won't go into too many details but these
  registers can be used to trigger a watchpoint event when a certain "data value" pattern is
  written over an address range. I'm not aware of an easy way to configure this with most
  debuggers, but the feature is really neat! For example, you can use it to to halt at a specific
  index in a for loop or if a certain data pattern is written anywhere in RAM! This type of watchpoint is only implemented in comparator 1 for most Cortex-M targets.
- `CYCMATCH` Only implemented for comparator 0. This can be used to trigger a watchpoint after a certain number of CPU cycles have passed.
- `FUNCTION` - Controls the type of comparison which is performed. When this field is set to 0, the comparator is disabled.

##### FUNCTION values for typical watchpoint

For the typical, "data address" watchpoint we have talked about so far in the article, the following configurations can be used to generate watchpoint events:

| FUNCTION       | Evaluation Performed      | Event Generated           |
| -------------- | ------------------------- | ------------------------- |
| `0b0000` (0x0) | None                      | Comparator is Disabled    |
| `0b0100`(0x4)  | Instruction Fetch         | PC watchpoint debug event |
| `0b0101` (0x5) | Read/Load Data Access     | Watchpoint debug event    |
| `0b0110` (0x6) | Write/Store Data Access   | Watchpoint debug event    |
| `0b0111` (0x7) | Read or Write Data Access | Watchpoint debug event    |

#### Comparator registers, DWT_COMPn, 0xE0001020 + 16n

If we have configured the `DWT_FUNCTION` register to look for a data address access, this register simply holds that address.

#### Comparator Mask registers, DWT_MASK, 0xE0001024 + 16n

The setting in the `MASK` defines the number of bits to ignore when performing a comparison. The maximum mask size is implementation defined but you can easily figure out the max size by writing 0x1F to the field and seeing which bits remain set. For example, on the NRF52:

```
(gdb) set *(uint32_t*)0xE0001024=0x1f
(gdb) p/x *(uint32_t*)0xE0001024
$3 = 0xf
```

This means we can mask out up to 15 bits and that a single watchpoint can be used to monitor a data access over a 32kB aligned RAM region!

{: #dwt-cortex-m-examples}
