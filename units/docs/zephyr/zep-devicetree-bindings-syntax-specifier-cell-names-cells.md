---
id: "zep-devicetree-bindings-syntax-specifier-cell-names-cells"
type: "concept"
domain: "project"
title: "Devicetree bindings syntax: Specifier cell names (\\*-cells)"
summary: "This section documents how to name the cells in a specifier within a binding. These concepts are discussed in detail later in this guide in dt-phandle-arrays."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/build/dts/bindings-syntax.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/build/dts/bindings-syntax.rst"
license: "Apache-2.0"
mode: "V"
---

This section documents how to name the cells in a specifier within a binding.
These concepts are discussed in detail later in this guide in
dt-phandle-arrays.

Consider a binding for a node whose phandle may appear in a `phandle-array`
property, like the PWM controllers `pwm1` and `pwm2` in this example:

```DTS

pwm1: pwm@deadbeef {
    compatible = "foo,pwm";
    #pwm-cells = <2>;
};

pwm2: pwm@deadbeef {
    compatible = "bar,pwm";
    #pwm-cells = <1>;
};

my-node {
    pwms = <&pwm1 1 2000>, <&pwm2 3000>;
};
```
The bindings for compatible `"foo,pwm"` and `"bar,pwm"` must give a name to
the cells that appear in a PWM specifier using `pwm-cells:`, like this:

```YAML

# foo,pwm.yaml
compatible: "foo,pwm"
...
pwm-cells:
  - channel
  - period

# bar,pwm.yaml
compatible: "bar,pwm"
...
pwm-cells:
  - period
```
A `*-names` (e.g. `pwm-names`) property can appear on the node as well,
giving a name to each entry.

This allows the cells in the specifiers to be accessed by name, e.g. using APIs
like `DT_PWMS_CHANNEL_BY_NAME`.

If the specifier is empty (e.g. `#clock-cells = <0>`), then `*-cells` can
either be omitted (recommended) or set to an empty array. Note that an empty
array is specified as e.g. `clock-cells: []` in YAML.
