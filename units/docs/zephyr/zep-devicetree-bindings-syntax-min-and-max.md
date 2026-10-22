---
id: "zep-devicetree-bindings-syntax-min-and-max"
type: "concept"
domain: "project"
title: "Devicetree bindings syntax: Properties / min and max"
summary: "The min: and max: keys constrain the range of valid values for properties with type: int or type: array. If a property value in DTS is outside the [min, max] range, an error is raised."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/build/dts/bindings-syntax.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/build/dts/bindings-syntax.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: Properties_

The `min:` and `max:` keys constrain the range of valid values for
properties with `type: int` or `type: array`. If a property value in DTS
is outside the `[min, max]` range, an error is raised.

Both keys are optional and independent; you may specify just `min:`, just
`max:`, or both. They cannot be combined with `enum:` on the same property.

For `type: array`, each element of the array is checked against the range.

Example:

```YAML

properties:
  # A brightness percentage between 0 and 100
  brightness:
    type: int
    min: 0
    max: 100
    description: LED brightness as a percentage

  # A timeout in milliseconds, with a minimum of 1 ms (no upper bound)
  timeout-ms:
    type: int
    min: 1
    description: Timeout in milliseconds
```
