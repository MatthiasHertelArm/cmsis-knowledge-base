---
id: "intr-faster-debugging-with-watchpoints-cortex-m-example-dwt-configurations"
type: "concept"
domain: "debug"
title: "Faster Debugging with Watchpoints: How do watchpoints work? / Cortex-M Example DWT Configurations"
summary: "Now that we have a basic understanding let's look at a few practical configurations made via GDB and what we would expect the settings to look like:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-09-16-cortex-m-watchpoints.md"
doc_source: "https://interrupt.memfault.com/blog/cortex-m-watchpoints#cortex-m-example-dwt-configurations"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: How do watchpoints work?_

Now that we have a basic understanding let's look at a few practical configurations made via GDB and what we would expect the settings to look like:

|                         GDB Command 
 Trigger Condition                         | DWT_FUNCTION | DWT_COMP   | DWT_MASK |
| :---------------------------------------------------------------------------------: | ------------ | ---------- | -------- |
|             `watch *(uint8_t *)0x20000001` 
 (Write to 0x20000001)             | 0x6          | 0x20000001 | 0x0      |
|  `watch *(uint16_t *)0x20000000` 
 (Any write between 0x20000000-0x20000002 )  | 0x6          | 0x20000000 | 0x1      |
| `watch *(uint8_t[4] *)0x20000010` 
 (Any write between 0x20000010- 0x20000014) | 0x6          | 0x20000010 | 0x2      |
| `rwatch *(uint8_t[16] *)0x20000020` 
 (Any read between 0x20000020-0x2000002F) | 0x5          | 0x20000020 | 0x4      |

{: #watchpoint-limitations}
> Note: An important observation here is it is only possible to watch ranges of addresses that are
> aligned on the size being watched. For example, if you wanted to watch 4 bytes starting at
> 0x20000002, you would need two watchpoints (`DWT_COMP=0x20000002`, `DWT_MASK=1` &
> `DWT_COMP=0x20000004`, `DWT_MASK=1`). GDB does not manage this for you so care should be taken to
> install watchpoints on aligned boundaries.

##### Examining DWT Configuration

Since watchpoints are disabled when GDB is halted, it will be useful to be able to inspect the watchpoint config from the CLI. I've added two commands to assist with this:

- `dwt_dump` Displays the current watchpoint configuration in the DWT
- `dwt_reset` Resets the DWT configuration

###### C Code to Dump and Reset DWT

```c
#include <stddef.h>
#include <stdint.h>

#include "hal/logging.h"

typedef struct {
  volatile uint32_t COMP;
  volatile uint32_t MASK;
  volatile uint32_t FUNCTION;
  volatile uint32_t RSVD;
} sDwtCompCfg;

typedef struct {
  volatile uint32_t CTRL;
  volatile uint32_t CYCCNT;
  volatile uint32_t CPICNT;
  volatile uint32_t EXCCNT;
  volatile uint32_t SLEEPCNT;
  volatile uint32_t LSUCNT;
  volatile uint32_t FOLDCNT;
  volatile const  uint32_t PCSR;
  sDwtCompCfg COMP_CONFIG[];
} sDWTUnit;

static sDWTUnit *const DWT = (sDWTUnit *)0xE0001000;

void dwt_dump(void) {
  EXAMPLE_LOG("DWT Dump:");
  EXAMPLE_LOG(" DWT_CTRL=0x%x", DWT->CTRL);

  const size_t num_comparators = (DWT->CTRL>>28) & 0xF;
  EXAMPLE_LOG("   NUMCOMP=0x%x", num_comparators);

  for (size_t i = 0; i < num_comparators; i++) {
    const sDwtCompCfg *config = &DWT->COMP_CONFIG[i];

    EXAMPLE_LOG(" Comparator %d Config", (int)i);
    EXAMPLE_LOG("  0x%08x DWT_FUNC%d: 0x%08x",
                &config->FUNCTION, (int)i, config->FUNCTION);
    EXAMPLE_LOG("  0x%08x DWT_COMP%d: 0x%08x",
                &config->COMP, (int)i, config->COMP);
    EXAMPLE_LOG("  0x%08x DWT_MASK%d: 0x%08x",
                &config->MASK, (int)i, config->MASK);
  }
}


void dwt_reset(void) {
  const size_t num_comparators = (DWT->CTRL>>28) & 0xF;

  for (size_t i = 0; i < num_comparators; i++) {
    sDwtCompCfg *config = &DWT->COMP_CONFIG[i];
    config->FUNCTION = config->COMP = config->MASK = 0;
  }
}
```

###### Inspecting watchpoints configured with GDB

Let's configure the watchpoints from [above](#dwt-cortex-m-examples) and examine the watchpoint configuration:

```
(gdb) watch *(uint8_t *)0x20000001
Hardware watchpoint 1: *(uint8_t *)0x20000001
(gdb) watch *(uint16_t *)0x20000000
Hardware watchpoint 2: *(uint16_t *)0x20000000
(gdb) watch *(uint8_t[4] *)0x20000010
Hardware watchpoint 3: *(uint8_t[16] *)0x20000010
(gdb) rwatch *(uint8_t[16] *)0x20000020
Hardware read watchpoint 4: *(uint8_t[16] *)0x20000020
(gdb) c
Continuing.
[...]
Sending packet: $Z2,20000000,2#98...Packet received: OK
Sending packet: $Z2,20000001,1#98...Packet received: OK
Sending packet: $Z2,20000010,4#c8...Packet received: OK
Sending packet: $Z3,20000020,10#ca...Packet received: OK
Sending packet: $c#63...
```

We see three `Z2` commands to install write watchpoints and one `Z3` command to install a read watchpoint. The `kind` values of 0x2, 0x1, 0x4, 0x10 line up with the sizes we requested as well.

###### Examining SEGGER JLinkGDBServer Configuration

Let's dump the config from the CLI and see how SEGGER's JLinkGDBServer did configuring our requests!

```bash
shell> dwt_dump
DWT Dump:
 DWT_CTRL=0x40000001
   NUMCOMP=0x4
 # Config for "watch *(uint8_t[4] *)0x20000010"
 Comparator 0 Config
  0xe0001028 DWT_FUNC0: 0x00000006
  0xe0001020 DWT_COMP0: 0x20000010
  0xe0001024 DWT_MASK0: 0x00000002
 # Config for "rwatch *(uint8_t[16] *)0x20000020"
 Comparator 1 Config
  0xe0001038 DWT_FUNC1: 0x00000a05
  0xe0001030 DWT_COMP1: 0x20000020
  0xe0001034 DWT_MASK1: 0x00000002
 # Config for "watch *(uint8_t *)0x20000001"
 Comparator 2 Config
  0xe0001048 DWT_FUNC2: 0x00000006
  0xe0001040 DWT_COMP2: 0x20000001
  0xe0001044 DWT_MASK2: 0x00000000
 # Config for "watch *(uint16_t *)0x20000000"
 Comparator 3 Config
  0xe0001058 DWT_FUNC3: 0x00000006
  0xe0001050 DWT_COMP3: 0x20000000
  0xe0001054 DWT_MASK3: 0x00000001
```

For the most part, things look like they line up with expectations. For the read watchpoint at `0x20000020`, we expect to see `0x00000006` for `DWT_FUNC1` but some extra bits were left set. These bits map to `DATAVSIZE` which is not used in our current config and `LNK1ENA` which is a read only bit so these settings are fine.

What is more problematic is the `DWT_MASK2` setting. It should be `4` to watch the 16 bytes that were requested. However, it was set to 2. It appears there is a limitation in the SEGGER watchpoint implementation and only 1, 2, and 4-byte watchpoints work!
