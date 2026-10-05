---
id: "zep-devicetree-api-instance-based-apis"
type: "concept"
domain: "project"
title: "Devicetree API: Instance-based APIs"
summary: "These are recommended for use within device drivers. To use them, define DT_DRV_COMPAT to the lowercase-and-underscores compatible the device driver implements support for. Here is an example devicetree fragment:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/build/dts/api/api.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/build/dts/api/api.rst"
license: "Apache-2.0"
mode: "V"
---

These are recommended for use within device drivers. To use them, define
`DT_DRV_COMPAT` to the lowercase-and-underscores compatible the device driver
implements support for. Here is an example devicetree fragment:

```devicetree

serial@40001000 {
        compatible = "vnd,serial";
        status = "okay";
        current-speed = <115200>;
};
```
Example usage, assuming `serial@40001000` is the only enabled node
with compatible `vnd,serial`:

```c

#define DT_DRV_COMPAT vnd_serial
DT_DRV_INST(0)                  // node identifier for serial@40001000
DT_INST_PROP(0, current_speed)  // 115200
```

**Warning:** Be careful making assumptions about instance numbers. See `DT_INST` for the API guarantees.

As shown above, the `DT_INST_*` APIs are conveniences for addressing nodes by
instance number. They are almost all defined in terms of one of the
devicetree-generic-apis. The equivalent generic API can be found by
removing `INST_` from the macro name. For example, ``DT_INST_PROP(inst,
prop)` is equivalent to `DT_PROP(DT_DRV_INST(inst), prop)``. Similarly,
`DT_INST_REG_ADDR(inst)` is equivalent to `DT_REG_ADDR(DT_DRV_INST(inst))`,
and so on. There are some exceptions: `DT_ANY_INST_ON_BUS_STATUS_OKAY`
and `DT_INST_FOREACH_STATUS_OKAY` are special-purpose helpers without
straightforward generic equivalents.

Since `DT_DRV_INST()` requires `DT_DRV_COMPAT` to be defined, it's an error
to use any of these without that macro defined.

Note that there are also helpers available for
specific hardware; these are documented in devicetree-hw-api.
