---
id: "zep-rules-for-upstream-bindings-rules-for-default-values"
type: "concept"
domain: "project"
title: "Rules for upstream bindings: Rules for default values"
summary: "In any case where default: is used in a devicetree binding, the description: for that property must explain why the value was selected and any conditions that would make it necessary to provide a different value."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/build/dts/bindings-upstream.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/build/dts/bindings-upstream.rst"
license: "Apache-2.0"
mode: "V"
---

In any case where `default:` is used in a devicetree binding, the
`description:` for that property **must** explain *why* the value was
selected and any conditions that would make it necessary to provide a different
value. Additionally, if changing one property would require changing another to
create a consistent configuration, then those properties should be made
required.

There is no need to document the default value itself; this is already present
in the devicetree_binding_index output.

There is a risk in using `default:` when the value in the binding may be
incorrect for a particular board or hardware configuration.  For example,
defaulting the capacity of the connected power cell in a charging IC binding
is likely to be incorrect.  For such properties it's better to make the
property `required: true`, forcing the user to make an explicit choice.

Driver developers should use their best judgment as to whether a value can be
safely defaulted. Candidates for default values include:

- delays that would be different only under unusual conditions
  (such as intervening hardware)
- configuration for devices that have a standard initial configuration (such as
  a USB audio headset)
- defaults which match the vendor-specified power-on reset value
  (as long as they are independent from other properties)

Default values for `status`, `#address-cells` and `#size-cells` cannot be defined in the
bindings. The default behavior for these properties is already defined in the
devicetree specification [§2.3.4](https://devicetree-specification.readthedocs.io/en/latest/chapter2-devicetree-basics.html#status) and [§2.3.5](https://devicetree-specification.readthedocs.io/en/latest/chapter2-devicetree-basics.html#address-cells-and-size-cells).

Examples of how to write descriptions according to these rules:

```yaml

properties:
  cs-interval:
    type: int
    default: 0
    description: |
      Minimum interval between chip select deassertion and assertion.
      The default corresponds to the reset value of the register field.
  hold-time-ms:
    type: int
    default: 20
    description: |
      Amount of time to hold the power enable GPIO asserted before
      initiating communication. The default was recommended in the
      manufacturer datasheet, and would only change under very
      cold temperatures.
```
Some examples of what **not** to do, and why:

```yaml

properties:
  # Description doesn't mention anything about the default
  foo:
    type: int
    default: 1
    description: number of foos

  # Description mentions the default value instead of why it
  # was chosen
  bar:
    type: int
    default: 2
    description: bar size; default is 2

  # Explanation of the default value is in a comment instead
  # of the description. This won't be shown in the bindings index.
  baz:
    type: int
    # This is the recommended value chosen by the manufacturer.
    default: 2
    description: baz time in milliseconds
```
