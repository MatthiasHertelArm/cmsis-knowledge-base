---
id: "zep-devicetree-bindings-syntax-specifier-space"
type: "concept"
domain: "project"
title: "Devicetree bindings syntax: Properties / specifier-space"
summary: "This property, if present, manually sets the specifier space associated with a property with type phandle-array."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/build/dts/bindings-syntax.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/build/dts/bindings-syntax.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: Properties_

**Warning:** It is an abuse of this feature to use it to name properties in unconventional ways. For example, this feature is not meant for cases like naming a property `my-pin`, then assigning it to the "gpio" specifier space using this feature. Properties which refer to GPIOs should use conventional names, i.e. end in `-gpios` or `-gpio`.

This property, if present, manually sets the specifier space associated with a
property with type `phandle-array`.

Normally, the specifier space is encoded implicitly in the property name. A
property named `foos` with type `phandle-array` implicitly has specifier
space `foo`. As a special case, `*-gpios` properties have specifier space
"gpio", so that `foo-gpios` will have specifier space "gpio" rather than
"foo-gpio".

You can use `specifier-space` to manually provide a space if
using this convention would result in an awkward or unconventional name.

For example:

```YAML

compatible: ...
properties:
  bar:
    type: phandle-array
    specifier-space: my-custom-space
```
Above, the `bar` property's specifier space is set to "my-custom-space".

You could then use the property in a devicetree like this:

```DTS

controller1: custom-controller@1000 {
        #my-custom-space-cells = <2>;
};

controller2: custom-controller@2000 {
        #my-custom-space-cells = <1>;
};

my-node {
        bar = <&controller1 10 20>, <&controller2 30>;
};
```
Generally speaking, you should reserve this feature for cases where the
implicit specifier space naming convention doesn't work. One appropriate
example is an `mboxes` property with specifier space "mbox", not "mboxe". You
can write this property as follows:

```YAML

properties:
  mboxes:
    type: phandle-array
    specifier-space: mbox
```
