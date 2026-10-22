---
id: "pyocd-command-reference-symbols"
type: "concept"
domain: "debug"
title: "Command reference: Symbols"
summary: "These commands require an ELF to be set."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@a743211:docs/command_reference.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/a743211/docs/command_reference.md#symbols"
license: "Apache-2.0"
mode: "V"
---

These commands require an ELF to be set.

##### `symbol`

**Usage**: symbol NAME \
Show a symbol's value. An ELF file must have been specified with the --elf option.


##### `where`

**Usage**: where [ADDR] \
Show symbol, file, and line for address. The symbol name, source file path, and line number are displayed for the specified address. If no address is given then current PC is used. An ELF file must have been specified with the --elf option.
