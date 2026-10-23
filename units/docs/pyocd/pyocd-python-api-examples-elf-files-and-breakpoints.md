---
id: "pyocd-python-api-examples-elf-files-and-breakpoints"
type: "concept"
domain: "debug"
title: "Python API examples: ELF files and breakpoints"
summary: "Expanding on the above example, this code demonstrates reading a symbol address from an ELF file and setting a breakpoint. Then the target is reset and run until the breakpoint is hit."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@a743211:docs/api_examples.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/a743211/docs/api_examples.md#elf-files-and-breakpoints"
license: "Apache-2.0"
mode: "V"
---

Expanding on the above example, this code demonstrates reading a symbol address from an ELF file
and setting a breakpoint. Then the target is reset and run until the breakpoint is hit.

```python
#!/usr/bin/env python3
from pyocd.core.helpers import ConnectHelper
from pyocd.core.target import Target
from pyocd.debug.elf.symbols import ELFSymbolProvider

# Connect to the target.
with ConnectHelper.session_with_chosen_probe() as session:
    target = session.target

    # Set ELF file on target.
    target.elf = "my_firmware.elf"

    # Look up address of main().
    provider = ELFSymbolProvider(target.elf)
    addr = provider.get_symbol_value("main")
    print("main() address: 0x%X" % addr)

    # Set breakpoint.
    target.set_breakpoint(addr)

    # Reset and run.
    target.reset()

    # Wait until breakpoint is hit.
    while target.get_state() != Target.State.HALTED:
        pass

    # Print PC.
    pc = target.read_core_register("pc")
    print("pc: 0x%X" % pc)

    assert pc == addr & ~0x01                         # mask off LSB

    # Remove breakpoint.
    target.remove_breakpoint(addr)
```

Note that you currently need to manually remove a breakpoint in order to step or run over it.
