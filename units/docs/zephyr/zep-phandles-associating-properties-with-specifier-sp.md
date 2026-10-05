---
id: "zep-phandles-associating-properties-with-specifier-sp"
type: "concept"
domain: "project"
title: "Phandles: Associating properties with specifier spaces"
summary: "In this section, we explain how phandle-array properties get their specifier spaces."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/build/dts/phandles.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/build/dts/phandles.rst"
license: "Apache-2.0"
mode: "V"
---

Above, we have described that:

- each phandle-array property has an associated specifier space
- specifier spaces are identified by name
- devicetree nodes use `#SPECIFIER_NAME-cells` properties to
  configure the number of cells which must appear in a specifier

In this section, we explain how phandle-array properties get their specifier
spaces.


### High level description


In general, a `phandle-array` property named `foos` implicitly has
specifier space `foo`. For example:

```YAML

properties:
  dmas:
    type: phandle-array
  pwms:
    type: phandle-array
```
The `dmas` property's specifier space is "dma". The `pwms` property's
specifier space is `pwm`.


### Special case: GPIOs and IO channels


`*-gpios` and `*-io-channels` properties are special-cased so that e.g.
`foo-gpios` and `bar-io-channels` resolve to `#gpio-cells` and
`#io-channel-cells` respectively, rather than `#foo-gpio-cells` and
`#bar-io-channel-cells`.


### Manually specifying a space


You can manually specify the specifier space for any `phandle-array`
property. See dt-bindings-specifier-space.
