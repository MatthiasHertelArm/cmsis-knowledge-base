---
id: "zep-syntax-and-structure-unit-addresses"
type: "concept"
domain: "project"
title: "Syntax and structure: Unit addresses"
summary: "In addition to showing more real-world names and properties, the above example introduces a new devicetree concept: unit addresses. Unit addresses are the parts of node names after an \"at\" sign (@), like 40003000 in i2c@40003000, or 39 in apds9960@39."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/build/dts/intro-syntax-structure.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/build/dts/intro-syntax-structure.rst"
license: "Apache-2.0"
mode: "V"
---

In addition to showing more real-world names and properties, the above example
introduces a new devicetree concept: unit addresses. Unit addresses are the
parts of node names after an "at" sign (`@`), like `40003000` in
`i2c@40003000`, or `39` in `apds9960@39`. Unit addresses are optional:
the `soc` node does not have one.

In devicetree, unit addresses give a node's address in the
address space of its parent node. Here are some example unit addresses for
different types of hardware.

Memory-mapped peripherals
    The peripheral's register map base address.
    For example, the node named `i2c@40003000` represents an I2C controller
    whose register map base address is 0x40003000.

I2C peripherals
    The peripheral's address on the I2C bus.
    For example, the child node `apds9960@39` of the I2C controller
    in the previous section has I2C address 0x39.

SPI peripherals
    An index representing the peripheral's chip select line number.
    (If there is no chip select line, 0 is used.)

Memory
    The physical start address.
    For example, a node named `memory@2000000` represents RAM starting at
    physical address 0x2000000.

Memory-mapped flash
    Like RAM, the physical start address.
    For example, a node named `flash@8000000` represents a flash device
    whose physical start address is 0x8000000.

Fixed flash partitions
    This applies when the devicetree is used to store a flash partition table.
    The unit address is the partition's start offset within the flash memory.
    For example, take this flash device and its partitions:

```devicetree

flash@8000000 {
    /* ... */
    partitions {
            partition@0 { /* ... */ };
            partition@20000 {  /* ... */ };
            /* ... */
    };
};
```
    The node named `partition@0` has offset 0 from the start of its flash
    device, so its base address is 0x8000000. Similarly, the base address of
    the node named `partition@20000` is 0x8020000.
