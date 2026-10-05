---
id: "zep-zyclictest-usage"
type: "concept"
domain: "debug"
title: "Zyclictest: Usage"
summary: "zyclictest start [options] -i <interval> Interval in microseconds -l <loops> Use loop mode with predefined number of cycles -p <prio> Setup priority of Thread"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/services/debugging/zyclictest.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/services/debugging/zyclictest.rst"
license: "Apache-2.0"
mode: "V"
---

zyclictest start [options]
  -i <interval>  Interval in microseconds
  -l <loops>     Use loop mode with predefined number of cycles
  -p <prio>      Setup priority of Thread

zyclictest stop [options]
  -c             Cancel loop mode prematurely
  -q             Quiet mode, print summary, but no histogram data
