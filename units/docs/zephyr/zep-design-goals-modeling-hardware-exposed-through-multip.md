---
id: "zep-design-goals-modeling-hardware-exposed-through-multip"
type: "concept"
domain: "project"
title: "Design goals: Modeling hardware exposed through multiple Zephyr APIs"
summary: "When a hardware block can be used through different Zephyr APIs, devicetree should keep hardware identity separate from the way software drivers and subsystems use each hardware instance."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/build/dts/design.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/build/dts/design.rst"
license: "Apache-2.0"
mode: "V"
---

When a hardware block can be used through different Zephyr APIs, devicetree
should keep hardware identity separate from the way software drivers and
subsystems use each hardware instance.


### Guidelines


- Keep the `compatible` property focused on the device programming model.
  Avoid changing it only to route software API selection. A different
  `compatible` is appropriate when the hardware interfaces are
  architecturally distinct, for example because they use separate register
  blocks.

- Use `/chosen` for singleton system-wide selection. If the system must
  select exactly one instance for a global function, such as the system timer,
  console, or entropy source, represent that choice with a platform-agnostic
  chosen property, even if other identical hardware instances are used by
  other APIs. See also devicetree-zephyr-chosen-nodes.

- Place the selection at the right integration level. If it is a silicon-level
  fixed attribute, describe it in the SoC `.dtsi`. If it varies by board,
  product, or application, describe it in the board `.dts` or an overlay.

If different uses of the hardware device have different required
properties, child nodes, or bus semantics, then they do not have to share one
binding schema. In that case, use different `compatible` values or model the
device as a multifunction one.


### Examples


**Singleton selection with** `/chosen`

The system timer is a singleton function. The `zephyr,system-timer`
chosen property selects which hardware timer instance provides it, while
other identical instances remain available for other APIs.

For example, two identical LPTMR timer instances can share the same
`compatible` in the hardware description:

```devicetree

lptmr1: timer@44300000 {
    compatible = "nxp,lptmr";
    reg = <0x44300000 0x1000>;
    /* ... */
};

lptmr2: timer@424d0000 {
    compatible = "nxp,lptmr";
    reg = <0x424d0000 0x1000>;
    /* ... */
};
```
An integration layer can then select which one provides the singleton system
timer function:

```devicetree

/ {
    chosen {
        zephyr,system-timer = &lptmr1;
    };
};
```
The system-timer driver binds to the `/chosen` node. The counter
driver skips that instance and uses the remaining one.
