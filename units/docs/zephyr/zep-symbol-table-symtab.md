---
id: "zep-symbol-table-symtab"
type: "concept"
domain: "debug"
title: "Symbol Table (Symtab)"
summary: "The Symtab module, when enabled, will generate full symbol table during the Zephyr linking stage that keep tracks of the information about the functions' name and address, for advanced application with a lot of functions, this is expected …"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/services/debugging/symtab.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/services/debugging/symtab.rst"
license: "Apache-2.0"
mode: "V"
---

The Symtab module, when enabled, will generate full symbol table during the Zephyr linking
stage that keep tracks of the information about the functions' name and address, for advanced application
with a lot of functions, this is expected to consume a sizable amount of ROM.

Currently, this is being used to look up the function names during a stack trace in supported architectures.
