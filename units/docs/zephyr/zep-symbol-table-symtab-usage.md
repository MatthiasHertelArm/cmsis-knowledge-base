---
id: "zep-symbol-table-symtab-usage"
type: "concept"
domain: "debug"
title: "Symbol Table (Symtab): Usage"
summary: "Application can gain access to the symbol table data structure by including the symtab.h header file and call symtab_get. For now, we only provide symtab_find_symbol_name function to look-up the symbol name and offset of an address."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/services/debugging/symtab.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/services/debugging/symtab.rst"
license: "Apache-2.0"
mode: "V"
---

Application can gain access to the symbol table data structure by including the `symtab.h` header
file and call `symtab_get`. For now, we only provide `symtab_find_symbol_name`
function to look-up the symbol name and offset of an address. More advanced functionalities and be
achieved by directly accessing the members of the data structure.
