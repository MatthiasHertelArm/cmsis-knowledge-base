---
id: "pyocd-command-reference-registers"
type: "concept"
domain: "debug"
title: "Command reference: Registers"
summary: "Command reference: Registers"
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@d1974ff:docs/command_reference.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/d1974ff/docs/command_reference.md#registers"
license: "Apache-2.0"
mode: "V"
---

##### `reg`

**Aliases**: `rr` \
**Usage**: reg [-p] [-f] [REG...] \
Print core or peripheral register(s). If no arguments are provided, the 'general' core register group will be printed. Either a core register name, the name of a peripheral, or a peripheral.register can be provided. When a peripheral name is provided without a register, all registers in the peripheral will be printed. The -p option forces evaluating the register name as a peripheral register name. If the -f option is passed, then individual fields of peripheral registers will be printed in addition to the full value.


##### `wreg`

**Aliases**: `wr` \
**Usage**: wreg [-r] [-p] [-f] REG VALUE \
Set the value of a core or peripheral register. The REG parameter must be a core register name or a peripheral.register. When a peripheral register is written, if the -r option is passed then it is read back and the updated value printed. The -p option forces evaluating the register name as a peripheral register name. If the -f option is passed, then individual fields of peripheral registers will be printed in addition to the full value.
