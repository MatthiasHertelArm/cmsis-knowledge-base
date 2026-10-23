---
id: "zep-syntax-and-structure-aliases-and-chosen-nodes"
type: "concept"
domain: "project"
title: "Syntax and structure: Aliases and chosen nodes"
summary: "There are two additional ways beyond node labels to refer to a particular node without specifying its entire path: by alias, or by chosen node."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/build/dts/intro-syntax-structure.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/build/dts/intro-syntax-structure.rst"
license: "Apache-2.0"
mode: "V"
---

There are two additional ways beyond node labels to
refer to a particular node without specifying its entire path: by alias, or by
chosen node.

Here is an example devicetree which uses both:

```devicetree

/dts-v1/;

/ {
    chosen {
        zephyr,console = &uart0;
     };

    aliases {
        my-uart = &uart0;
    };

    soc {
        uart0: serial@12340000 {
            ...
        };
    };
};
```
The `/aliases` and `/chosen` nodes do not refer to an actual hardware
device. Their purpose is to specify other nodes in the devicetree.

Above, `my-uart` is an alias for the node with path `/soc/serial@12340000`.
Using its node label `uart0`, the same node is set as the value of the chosen
`zephyr,console` node.

Zephyr sample applications sometimes use aliases to allow overriding the
particular hardware device used by the application in a generic way. For
example, blinky uses this to abstract the LED to blink via the
`led0` alias.

The `/chosen` node's properties are used to configure system- or
subsystem-wide values. See devicetree-chosen-nodes for more information.
