---
id: "pyocd-gdb-remote-server-rtos-thread-awareness"
type: "concept"
domain: "debug"
title: "gdb remote server: RTOS thread awareness"
summary: "The gdbserver supports thread awareness for several RTOSes. Additional RTOS support can be added with plugins."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@a743211:docs/gdbserver.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/a743211/docs/gdbserver.md#rtos-thread-awareness"
license: "Apache-2.0"
mode: "V"
---

The gdbserver supports thread awareness for several RTOSes. Additional RTOS support can be added with plugins.

When gdb connects, pyOCD will attempt to enable thread awareness. By default, all available RTOS plugins are queried. When the first one is successfully enabled, the process stops. If the `rtos.name` session option is set to the name of an RTOS plugin, only that one will be queried. To completely disable thread awareness, set the `rtos.enable` session option to false.

Builtin RTOS plugins are shown in the following table.

  RTOS Plugin Name   |   Description
---------------------|----------------
  argon              |   Argon RTOS
  freertos           |   FreeRTOS
  rtx5               |   RTX5
  threadx            |   ThreadX
  zephyr             |   Zephyr


### Viewing and selecting threads

Within gdb, the set of current threads can be printed with `info threads`. gdb assigns each thread a unique integer identifier used to reference the thread in other commands.

This example shows a gdb thread listing for a Zephyr RTOS program.



`  Id   Target Id                                            Frame
* 3    Thread 536871784 "idle" (Running; Priority 15)       arch_cpu_idle ()
    at /Users/creed/projects/zephyrproject/zephyr/arch/arm/core/aarch32/cpu_idle.S:126
  4    Thread 536871584 "uart_out_id" (Pending; Priority 7) arch_swap (key=0)
    at /Users/creed/projects/zephyrproject/zephyr/arch/arm/core/aarch32/swap.c:53
  5    Thread 536871416 "blink1_id" (Suspended; Priority 7) arch_swap (key=key@entry=0)
    at /Users/creed/projects/zephyrproject/zephyr/arch/arm/core/aarch32/swap.c:53
  6    Thread 536871248 "blink0_id" (Suspended; Priority 7) arch_swap (key=key@entry=0)
    at /Users/creed/projects/zephyrproject/zephyr/arch/arm/core/aarch32/swap.c:53
  7    Thread 536872152 "sysworkq" (Pending; Priority -1)   arch_swap (key=0)
    at /Users/creed/projects/zephyrproject/zephyr/arch/arm/core/aarch32/swap.c:53
`

Note how the thread name is shown in quotes, and thread state and priority are shown in parentheses. The actual description of threads is specific to each RTOS plugin.

The `thread` command takes a gdb thread ID to switches between threads; after switching, `backtrace` will show the selected thread's state.

### Thread reporting

There can be issues caused by a mismatch between the target's current memory contents and the expected location of RTOS related symbols. For instance, if a new version of firmware is being debugged but the target's flash has not been reprogrammed yet, or if there is stale data in RAM. If this happens, an out of date or corrupt view of the RTOS state could be reported.

To prevent this from happening, pyOCD will disable reporting threads to gdb (and reading the RTOS data from target memory) until the first time the target is resumed after any of these events:
- gdb connects to pyOCD
- Target reset
- Flash is reprogrammed using gdb commands

Note that a single instruction step will not enable thread reporting. A full resume is required. Gdb will see the list of threads when the target halts after the first resume, eg which a breakpoint is hit or the target is manually halted.

The actual behaviour depends on the plugin, so there is some slight variation between RTOSes. But the general sequence applies.

This logic not perfect, so there is a [`threads` command]({% link _docs/command_reference.md %}#threads-1) that provides manual control. It takes an argument with one of these actions:
- `status`: Show whether thread reporting is enabled.
- `enable`: Enable thread reporting.
- `disable`: Disallow thread reporting.
- `flush`: Forcibly invalidate the threads list.

If `threads` is executed and an RTOS plugin has not successfully loaded, it will print "Threads are unavailable".

After thread reporting is enabled or disabled manually, you must step or resume in gdb to force gdb to refresh its view of threads. (There is no flush or invalidate for threads in gdb.)

When thread reporting is disabled, gdb will see a single thread just like when no RTOS plugin is loaded.


### RTOS notes

These sections document specific features or requirements for using thread awareness with different RTOSes.

#### Zephyr RTOS

To enable thread awareness, the `CONFIG_DEBUG_THREAD_INFO` Kconfig setting must be enabled.


### Handler mode thread

The RTOS plugins will report an artificial thread when an M-profile core is in Handler mode, eg in an exception or interrupt handler. This lets you view the state of the exception handler separately from RTOS threads.
