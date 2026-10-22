---
id: "zep-thread-analyzer-configuration"
type: "concept"
domain: "debug"
title: "Thread analyzer: Configuration"
summary: "Configure this module using the following options."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/services/debugging/thread-analyzer.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/services/debugging/thread-analyzer.rst"
license: "Apache-2.0"
mode: "V"
---

Configure this module using the following options.

`CONFIG_THREAD_ANALYZER`
   Enable the module.
`CONFIG_THREAD_ANALYZER_USE_PRINTK`
   Use printk for thread statistics.
`CONFIG_THREAD_ANALYZER_USE_LOG`
   Use the logger for thread statistics.
`CONFIG_THREAD_ANALYZER_AUTO`
   Run the thread analyzer automatically.
   You do not need to add any code to the application when using this option.
`CONFIG_THREAD_ANALYZER_AUTO_INTERVAL`
   The time for which the module sleeps between consecutive printing of thread analysis in automatic
   mode.
`CONFIG_THREAD_ANALYZER_AUTO_STACK_SIZE`
  The stack for thread analyzer automatic thread.
`CONFIG_THREAD_NAME`
  Print the name of the thread instead of its ID.
`CONFIG_THREAD_RUNTIME_STATS`
  Print thread runtime data such as utilization.
  This options is automatically selected by `CONFIG_THREAD_ANALYZER`.
`CONFIG_THREAD_ANALYZER_LONG_FRAME_PER_INTERVAL`
  Reset Longest Frame value statistics after printing.
  When using `SCHED_THREAD_USAGE_ANALYSIS` to get average and longest
  frame thread statistics, reset the Longest Frame value to zero after each time
  printing the thread statistics.  This enables observation of the longest frame
  during the most recent interval rather than longest frame since startup.
`CONFIG_THREAD_ANALYZER_PRINT_THREAD_PRIORITY`
  Print each thread's priority.
