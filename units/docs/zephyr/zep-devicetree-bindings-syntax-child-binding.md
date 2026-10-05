---
id: "zep-devicetree-bindings-syntax-child-binding"
type: "concept"
domain: "project"
title: "Devicetree bindings syntax: Child-binding"
summary: "child-binding can be used when a node has children that all share the same properties. Each child gets the contents of child-binding as its binding, though an explicit compatible = ..."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/build/dts/bindings-syntax.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/build/dts/bindings-syntax.rst"
license: "Apache-2.0"
mode: "V"
---

`child-binding` can be used when a node has children that all share the same
properties. Each child gets the contents of `child-binding` as its binding,
though an explicit `compatible = ...` on the child node takes precedence, if
a binding is found for it.

Consider a binding for a PWM LED node like this one, where the child nodes are
required to have a `pwms` property:

```devicetree

pwmleds {
        compatible = "pwm-leds";

        red_pwm_led {
                pwms = <&pwm3 4 15625000>;
        };
        green_pwm_led {
                pwms = <&pwm3 0 15625000>;
        };
        /* ... */
};
```
The binding would look like this:

```YAML

compatible: "pwm-leds"

child-binding:
  description: LED that uses PWM

  properties:
    pwms:
      type: phandle-array
      required: true
```
`child-binding` also works recursively. For example, this binding:

```YAML

compatible: foo

child-binding:
  child-binding:
    properties:
      my-property:
        type: int
        required: true
```
will apply to the `grandchild` node in this DTS:

```devicetree

parent {
        compatible = "foo";
        child {
                grandchild {
                        my-property = <123>;
                };
        };
};
```
