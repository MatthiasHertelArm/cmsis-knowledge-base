---
id: "zep-devicetree-bindings-syntax-default"
type: "concept"
domain: "project"
title: "Devicetree bindings syntax: Properties / default"
summary: "The optional default: setting gives a value that will be used if the property is missing from the devicetree node."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/build/dts/bindings-syntax.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/build/dts/bindings-syntax.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: Properties_

The optional `default:` setting gives a value that will be used if the
property is missing from the devicetree node.

For example, with this binding fragment:

```YAML

properties:
  foo:
    type: int
    default: 3
```
If property `foo` is missing in a matching node, then the output will be as
if `foo = <3>;` had appeared in the DTS (except YAML data types are used for
the default value).

Note that a binding which declares both `default:` and `required: true`
for the same property will produce a warning, since the two settings are
redundant: `required: true` already fails the build when the property is
missing, so the default can never apply. A binding may still override an
inherited `default:` with `required: true` to force an explicit value;
this is well defined and is not reported. A binding which is only ever
reached through `include:` is not loaded on its own during a build, so
the warning for it is seen when the documentation is generated rather
than when an application is built.

For rules related to `default` in upstream Zephyr bindings, see
dt-bindings-default-rules.

See dt-bindings-example-properties for examples. Putting `default:` on
any property type besides those used in dt-bindings-example-properties
will raise an error.
