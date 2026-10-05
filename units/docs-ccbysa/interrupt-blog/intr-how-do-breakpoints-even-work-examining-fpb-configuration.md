---
id: "intr-how-do-breakpoints-even-work-examining-fpb-configuration"
type: "concept"
domain: "debug"
title: "How do breakpoints even work?: Cortex-M Hardware Breakpoints / Examining FPB Configuration"
summary: "Part of: Cortex-M Hardware Breakpoints"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-06-17-cortex-m-breakpoints.md"
doc_source: "https://interrupt.memfault.com/blog/cortex-m-breakpoints#examining-fpb-configuration"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Cortex-M Hardware Breakpoints_

Recall that GDB will uninstall breakpoints when the system halts so this is a rare situation where we can _only_ debug the configuration on a running system!

The nRF52 includes a Version 1 **FPB** so from here on out our code examples will make use of that implementation. Here's a minimal snippet of code which can be used to dump the config:

##### C Code to Dump FPB Config

```c
#include <stdint.h>
#include <stddef.h>

typedef struct {
  volatile uint32_t FP_CTRL;
  volatile uint32_t FP_REMAP;
  // Number Implemented determined by FP_CTRL
  volatile uint32_t FP_COMP[];
} sFpbUnit;

static sFpbUnit *const FPB = (sFpbUnit *)0xE0002000;

void fpb_dump_breakpoint_config(void) {
  const uint32_t fp_ctrl = FPB->FP_CTRL;
  const uint32_t fpb_enabled = fp_ctrl & 0x1;
  const uint32_t revision = (fp_ctrl >> 28) & 0xF;
  const uint32_t num_code_comparators =
      (((fp_ctrl >> 12) & 0x7) << 4) | ((fp_ctrl >> 4) & 0xF);

  EXAMPLE_LOG("FPB Revision: %d, Enabled: %d, Hardware Breakpoints: %d",
              revision, (int)fpb_enabled, (int)num_code_comparators);

  for (size_t i = 0; i < num_code_comparators; i++) {
    const uint32_t fp_comp = FPB->FP_COMP[i];
    const bool enabled = fp_comp & 0x1;
    const uint32_t replace = fp_comp >> 30;

    uint32_t instruction_address = fp_comp & 0x1FFFFFFC;
    if (replace == 0x2) {
      instruction_address |= 0x2;
    }

    EXAMPLE_LOG("  FP_COMP[%d] Enabled %d, Replace: %d, Address 0x%x",
                (int)i, (int)enabled, (int)replace, instruction_address);
  }
}
```

I've hooked `fpb_dump_breakpoint_config()` up to the`fpb_dump` shell command in the example app. Let's take a look at what we get with the breakpoint from `dummy_function_1` still set:

```
shell> fpb_dump
FPB Revision: 0, Enabled: 1, Hardware Breakpoints: 6
  FP_COMP[0] Enabled 1, Replace: 1, Address 0x240
  FP_COMP[1] Enabled 0, Replace: 0, Address 0x0
  FP_COMP[2] Enabled 0, Replace: 0, Address 0x0
  FP_COMP[3] Enabled 0, Replace: 0, Address 0x0
  FP_COMP[4] Enabled 0, Replace: 0, Address 0x0
  FP_COMP[5] Enabled 0, Replace: 0, Address 0x0
```

We can see that the JLinkGDBServer has installed a breakpoint in the first available comparator!
