---
id: "pyocd-user-scripts-examples"
type: "concept"
domain: "debug"
title: "user scripts: Examples"
summary: "This example user script shows how to add a new memory region."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@d1974ff:docs/user_scripts.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/d1974ff/docs/user_scripts.md#examples"
license: "Apache-2.0"
mode: "V"
---

This example user script shows how to add a new memory region.

```py
# This example applies to the Nordic nRF52 devices.

def will_connect(board):
    # Create the new ROM region for the FICR.
    ficr = RomRegion(
                name="ficr",
                start=0x10000000,
                length=0x460
                )

    # Add the FICR region to the memory map.
    target.memory_map.add_region(ficr)
```

This example shows how to override the flash algorithm for an external flash memory.

```py
# This example applies to the NXP i.MX RT10x0 devices.

# Unlike the previous example, the board argument is excluded here.
def will_connect():
    # Look up the external flash memory region.
    extFlash = target.memory_map.get_first_matching_region(name="flexspi")

    # Set the path to an .FLM flash algorithm.
    extFlash.flm = "MIMXRT105x_QuadSPI_4KB_SEC.FLM"
```

This example demonstrates setting the DBGMCU_CR register after connecting for STM32 devices.

```py
# This example applies to the ST STM32L0x1 devicess.

DBG_CR = 0x40015804

def did_connect():
    # Set STANDBY, STOP, and SLEEP bits all to 1.
    target.write32(DBG_CR, 0x7)
```

Another common use for a script is to initialize external memory such as SDRAM.
