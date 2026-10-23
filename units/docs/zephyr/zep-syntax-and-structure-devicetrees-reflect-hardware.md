---
id: "zep-syntax-and-structure-devicetrees-reflect-hardware"
type: "concept"
domain: "project"
title: "Syntax and structure: Devicetrees reflect hardware"
summary: "In practice, devicetree nodes usually correspond to some hardware, and the node hierarchy reflects the hardware's physical layout. For example, let's consider a board with three I2C peripherals connected to an I2C bus controller on an SoC, like this:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/build/dts/intro-syntax-structure.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/build/dts/intro-syntax-structure.rst"
license: "Apache-2.0"
mode: "V"
---

In practice, devicetree nodes usually correspond to some hardware, and the node
hierarchy reflects the hardware's physical layout. For example, let's consider
a board with three I2C peripherals connected to an I2C bus controller on an SoC,
like this:

Nodes corresponding to the I2C bus controller and each I2C peripheral would be
present in the devicetree. Reflecting the hardware layout, the
I2C peripheral nodes would be children of the bus controller node.
Similar conventions exist for representing other types of hardware.

The DTS would look something like this:

```devicetree

/dts-v1/;

/ {
        soc {
                i2c-bus-controller {
                        i2c-peripheral-1 {
                        };
                        i2c-peripheral-2 {
                        };
                        i2c-peripheral-3 {
                        };
                };
        };
};
```
