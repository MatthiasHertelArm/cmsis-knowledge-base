---
id: "zep-cortex-m-debug-monitor-configuration"
type: "concept"
domain: "debug"
title: "Cortex-M Debug Monitor: Configuration"
summary: "Configure this module using the following options."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/services/debugging/debugmon.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/services/debugging/debugmon.rst"
license: "Apache-2.0"
mode: "V"
---

Configure this module using the following options.

* `CONFIG_CORTEX_M_DEBUG_MONITOR_HOOK`: enable the module. This option, by itself,
  requires an implementation of debug monitor interrupt that will be executed
  every time the program enters a breakpoint.

With a SEGGER debug probe, it's possible to use a ready, SEGGER-provided implementation
of the interrupt.

* `CONFIG_SEGGER_DEBUGMON`: enables SEGGER debug monitor interrupt. Can be
  used with SEGGER JLinkGDBServer and a SEGGER debug probe.
