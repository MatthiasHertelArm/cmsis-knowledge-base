---
id: "zep-rules-for-upstream-bindings-general-rules"
type: "concept"
domain: "project"
title: "Rules for upstream bindings: General rules"
summary: "Wherever possible, when writing Devicetree bindings for Zephyr, try to follow the same design guidelines laid out by Linux."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/build/dts/bindings-upstream.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/build/dts/bindings-upstream.rst"
license: "Apache-2.0"
mode: "V"
---

Wherever possible, when writing Devicetree bindings for Zephyr, try to follow
the same design guidelines laid out by Linux.


### File names


Bindings which match a compatible must have file names based on the compatible.

- For example, a binding for compatible `vnd,foo` must be named `vnd,foo.yaml`.
- If the binding is bus-specific, you can append the bus to the file name;
  for example, if the binding YAML has `on-bus: bar`, you may name the file
  `vnd,foo-bar.yaml`.


### Recommendations are requirements


All recommendations in dt-bindings-default are requirements when
submitting the binding.

In particular, if you use the `default:` feature, you must justify the
value in the property's description.


### Descriptions


There are only two acceptable ways to write property `description:`
strings.

If your description is short, it's fine to use this style:

```yaml

description: my short string
```
If your description is long or spans multiple lines, you must use this
style:

```yaml

title: I'm sure you need a short title.

description: |
  My very long string
  goes here.
  Look at all these lines!
```
This `|` style prevents YAML parsers from removing the newlines in
multi-line descriptions. This in turn makes these long strings
display properly in the devicetree_binding_index.

If using the binding’s properties gets complicated, you can use examples
to provide a minimal node. e.g.:

```yaml

description: ...

properties:
 ...

examples:
  - |
    leds {
      compatible = "gpio-leds";

      uled: led {
      gpios = <&gpioe 12 GPIO_ACTIVE_HIGH>;
      };
    };
```

### Naming conventions


Do not use uppercase letters (`A` through `Z`) or underscores (`_`) in
property names. Use lowercase letters (`a` through `z`) instead of
uppercase. Use dashes (`-`) instead of underscores. (The one exception to
this rule is if you are replicating a well-established binding from somewhere
like Linux.)
