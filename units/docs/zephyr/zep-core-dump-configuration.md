---
id: "zep-core-dump-configuration"
type: "concept"
domain: "debug"
title: "Core Dump: Configuration"
summary: "Configure this module using the following options."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/services/debugging/coredump.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/services/debugging/coredump.rst"
license: "Apache-2.0"
mode: "V"
---

Configure this module using the following options.

* `DEBUG_COREDUMP`: enable the module.

Here are the options to enable output backends for core dump:

* `DEBUG_COREDUMP_BACKEND_LOGGING`: use log module for core dump output.
* `DEBUG_COREDUMP_BACKEND_LOGGING_UDP`: same as logging backend with optional
  raw UDP transfer; the peer is `DEBUG_COREDUMP_LOGGING_UDP_HOST`, a string
  parsed by `net_ipaddr_parse()` (IPv4 or IPv6, optional `:port` with default
  UDP port `17777` when omitted). Use
  `scripts/coredump/coredump_udp_receiver.py` to build the binary
  for `scripts/coredump/coredump_gdbserver.py`.
* `DEBUG_COREDUMP_BACKEND_FLASH_PARTITION`: use flash partition for core
  dump output.
* `DEBUG_COREDUMP_BACKEND_NULL`: fallback core dump backend if other
  backends cannot be enabled. All output is sent to null.

Here are the choices regarding memory dump:

* `DEBUG_COREDUMP_MEMORY_DUMP_MIN`: only dumps the stack of the exception
  thread, its thread struct, and some other bare minimal data to support
  walking the stack in the debugger. Use this only if absolute minimum of data
  dump is desired.

* `DEBUG_COREDUMP_MEMORY_DUMP_THREADS`: Dumps the thread struct and stack of all
  threads and all data required to debug threads.

* `DEBUG_COREDUMP_MEMORY_DUMP_LINKER_RAM`: Dumps the memory region between
  _image_ram_start[] and _image_ram_end[]. This includes at least data, noinit,
  and BSS sections. This is the default.

Additional memory can be included in a dump (even with the "DEBUG_COREDUMP_MEMORY_DUMP_MIN"
config selected) through one or more coredump devices
