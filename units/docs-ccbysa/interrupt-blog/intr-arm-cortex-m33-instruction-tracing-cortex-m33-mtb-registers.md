---
id: "intr-arm-cortex-m33-instruction-tracing-cortex-m33-mtb-registers"
type: "concept"
domain: "debug"
title: "ARM Cortex-M33 Instruction Tracing Without a Debugger: Cortex-M33 MTB Registers"
summary: "The MTB implementation present on the Cortex-M33 (MTB-M33) is comprised of seven registers:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-12-23-instruction-tracing-mtb-m33.md"
doc_source: "https://interrupt.memfault.com/blog/instruction-tracing-mtb-m33#cortex-m33-mtb-registers"
license: "CC-BY-SA-4.0"
mode: "V"
---

The MTB implementation present on the Cortex-M33 (MTB-M33) is comprised of seven registers:

| Address    | Name           | Description                                                                                    |
| ---------- | -------------- | ---------------------------------------------------------------------------------------------- |
| 0xE0043000 | `MTB_POSITION` | Holds current MTB write pointer offset                                                         |
| 0xE0043004 | `MTB_MASTER`   | Used to enable the MTB and configure its size                                                  |
| 0xE0043008 | `MTB_FLOW`     | Controls MTB behavior when full (default is to wrap and overwrite)                             |
| 0xE004300C | `MTB_BASE`     | Read only, reveals SRAM address where MTB packets are stored                                   |
| 0xE0043010 | `MTB_TSTART`   | No config necessary for typical setup. (Allows DWT events to start MTB traces)                 |
| 0xE0043014 | `MTB_TSTOP`    | No config necessary for typical setup. (Allows DWT events to stop MTB traces)                  |
| 0xE0043018 | `MTB_SECURE`   | No config necessary for typical setup. (Allows for MTB SRAM to be split when using Trustzones) |

### Typical Configuration

For a typical configuration, there are only three registers that need to be examined & updated: `MTB_POSITION`, `MTB_MASTER`, & `MTB_BASE`.

The MCU datasheet can be examined to determine the maximum amount of RAM that can be allocated to the MTB. In the Dialog datasheet we can find this in "Example of Memory Segments Mapping" [^2]:



### MTB_BASE, 0xE004300C



The `MTB_BASE` register describes where in SRAM MTB trace storage begins. We will use this value later in this article to read MTB data.

For the DA14695, we can confirm the location is at `0x2007e000` with gdb:

```
(gdb) p/x *(uint32_t*)0xE004300C
$1 = 0x2007e000
```

### MTB_POSITION, 0xE0043000



The `MTB_POSITION` register conveys two pieces of MTB state:

1. The current write "pointer" for trace packet information. This will be where information about the next non-sequential instruction change is written. The actual SRAM address stored to can be computed as `MTB_BASE` + `POINTER`.
2. Whether the data in the buffer has rolled around. If the storage has been filled and wrapped around, the "wrap" bit will be set. We can use this information to determine where the oldest trace packet is. If the "wrap" bit is set, the oldest record is at the "pointer" offset, otherwise it is at offset 0.

### MTB_MASTER, 0xE0043004



Among other things, the `MTB_MASTER` register is used to configure the amount of RAM to be used for tracing as well as actually enable the peripheral. The two fields you generally need to program are:

- `MASK` - This controls how much space is used for the trace buffer. The size of the circular
  buffer used will be 2 ^  MASK + 4  up to the maximum space available. So for the DA14695, valid values will be 0 (20 + 4 = 16 bytes) up to 9 (29 + 4 = 8192 bytes).
- `EN` - Setting this bit will turn on MTB tracing!
