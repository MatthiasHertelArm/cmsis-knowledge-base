---
id: "intr-step-through-debugging-with-no-deb-enabling-the-debugmonitor-exception"
type: "concept"
domain: "debug"
title: "Step-through debugging with no debugger on Cortex-M: Enabling the DebugMonitor Exception"
summary: "Debug monitor mode based debugging works by triggering an exception known as the \"DebugMonitor Exception\" when debug events take place. We'll explore how to configure the handler in the following sections."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-07-29-cortex-m-debug-monitor.md"
doc_source: "https://interrupt.memfault.com/blog/cortex-m-debug-monitor#enabling-the-debugmonitor-exception"
license: "CC-BY-SA-4.0"
mode: "V"
---

Debug monitor mode based debugging works by triggering an exception known as the "DebugMonitor
Exception" when debug events take place. We'll explore how to configure the handler in the
following sections.

### Debug Halting Control and Status Register (DHCSR), 0xE000EDF0



Monitor Mode Debug only works if halting debug is disabled. Notably, the `C_DEBUGEN` setting
above must be cleared. This bit can _only_ be set via the JTAG/SWD connection and is _only_ reset when a full
Power-On-Reset (POR) occurs or a debugger clears the bit on exit.

If you are trying to use Monitor Mode Debug, I recommend adding a check on boot for
this. Otherwise, you are bound to confuse yourself when you are trying to test the feature and have a debugger connected via JTAG/SWD:

```c
bool debug_monitor_enable(void) {
  volatile uint32_t *dhcsr = (uint32_t*)0xE000EDF0;
  if ((*dhcsr & 0x1) != 0) {
    EXAMPLE_LOG("Halting Debug Enabled - "
                "Can't Enable Monitor Mode Debug!");
    return;
  }
  // code to set up debug monitor mode
}
```

#### TIP: Disabling Halting Debug from GDB

If you are using GDB, Halting Mode debug can be disabled manually by clearing `C_DEBUGEN` and setting
the appropriate value for `DBGKEY` (0xA05F):

```
(gdb) set *(uint32_t*)0xE000EDF0=(0xA05F<<16)
```

This can also be a useful way to keep an active GDB session open and probe its state while
the system is running!

### Debug Exception and Monitor Control Register (DEMCR), 0xE000EDFC

The core configuration for the DebugMonitor exception is controlled in the upper 16 bits of the
`DEMCR` register:



where:

- `MON_EN` - Controls whether the DebugMonitor exception is enabled or not. When enabled, debug
  "events" will cause the exception to fire.
- `MON_PEND` - Can be used to trigger a DebugMonitor exception irrespective of whether or not
  `MON_EN` is set to 1.
- `MON_REQ` - Not used by the MCU. Software can use this bit to convey state about monitor mode.
- `MON_STEP` - Can be toggled from the DebugMonitor exception to enable hardware
  single-stepping. When set, upon return from the exception handler, the core will execute a single instruction and then return to the DebugMonitor exception.

> NOTE: The lower bits (`VC_HARDERR`, etc) controls whether or not a debug trap occurs automatically when
> various types of exceptions take place. These _only_ take effect when using **halting debug**
> mode. They allow you to guarantee the system is halted any time an exception path is hit which can be useful
> when trying to debug!

#### DebugMonitor Exception Configuration Nuances

The DebugMonitor exception will only be triggered for debug events when the group priority of the
exception is greater than the current execution priority.

This can be a useful feature to guarantee that certain high priority operations (i.e Bluetooth
radio scheduling) continue to run while you step through the code in other parts of the system.

An important consequence however is it does mean any interrupts running above this priority of the
DebugMonitor exception will not be debuggable when using debug monitor support.

Configuring the DebugMonitor exception priority will require updating `SHPR3`. More details can be
found in [our post about ARM Cortex-M exception handling](https://interrupt.memfault.com/blog/arm-cortex-m-exceptions-and-nvic#system-handler-priority-register-shpr1-shpr3---0xe000ed18---0xe000ed20).

### C Code to Enable the DebugMonitor Exception

For simplicity in our example app we will set the DebugMonitor exception to the lowest configurable
interrupt priority. This means all other interrupts will be able to run while debugging code not
running from an interrupt.

Putting it all together, we have:

```c
bool debug_monitor_enable(void) {
  volatile uint32_t *dhcsr = (uint32_t*)0xE000EDF0;
  if ((*dhcsr & 0x1) != 0) {
    EXAMPLE_LOG("Halting Debug Enabled - "
                "Can't Enable Monitor Mode Debug!");
    return false;
  }

  volatile uint32_t *demcr = (uint32_t*)0xE000EDFC;
  const uint32_t mon_en_bit = 16;
  *demcr |= 1 << mon_en_bit;

  // Priority for DebugMonitor Exception is bits[7:0].
  // We will use the lowest priority so other ISRs can
  // fire while in the DebugMonitor Interrupt
  volatile uint32_t *shpr3 = (uint32_t *)0xE000ED20;
  *shpr3 = 0xff;

  EXAMPLE_LOG("Monitor Mode Debug Enabled!");
  return true;
}
```
