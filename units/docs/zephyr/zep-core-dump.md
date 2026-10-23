---
id: "zep-core-dump"
type: "concept"
domain: "debug"
title: "Core Dump"
summary: "The core dump module enables dumping the CPU registers and memory content for offline debugging. This module is called when a fatal error is encountered and prints or stores data according to which backends are enabled."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/services/debugging/coredump.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/services/debugging/coredump.rst"
license: "Apache-2.0"
mode: "V"
---

The core dump module enables dumping the CPU registers and memory content
for offline debugging. This module is called when a fatal error is
encountered and prints or stores data according to which backends
are enabled.
