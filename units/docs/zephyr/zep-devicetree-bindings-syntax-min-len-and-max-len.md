---
id: "zep-devicetree-bindings-syntax-min-len-and-max-len"
type: "concept"
domain: "project"
title: "Devicetree bindings syntax: Properties / min-len and max-len"
summary: "The min-len: and max-len: keys constrain the number of elements (length) for array-type properties (array, uint8-array, string-array, phandles, and phandle-array). If the length of a property value in DTS is outside the [min-len, max-len] range, an error is raised."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/build/dts/bindings-syntax.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/build/dts/bindings-syntax.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: Properties_

The `min-len:` and `max-len:` keys constrain the number of elements (length)
for array-type properties (`array`, `uint8-array`, `string-array`,
`phandles`, and `phandle-array`). If the length of a property value in DTS
is outside the `[min-len, max-len]` range, an error is raised.

Both keys are optional and independent; you may specify just `min-len:`, just
`max-len:`, or both.

Example:

```YAML

properties:
  # An array of exactly 3 integers
  coordinates:
    type: array
    min-len: 3
    max-len: 3
    description: 3D coordinates

  # A list of up to 4 GPIO phandles
  gpios:
    type: phandle-array
    max-len: 4
    description: Up to 4 GPIOs
```
