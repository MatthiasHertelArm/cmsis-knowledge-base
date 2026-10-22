---
id: "zep-devicetree-bindings-syntax-required"
type: "concept"
domain: "project"
title: "Devicetree bindings syntax: Properties / required"
summary: "Adding required: true to a property definition will fail the build if a node matches the binding, but does not contain the property."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/build/dts/bindings-syntax.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/build/dts/bindings-syntax.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: Properties_

Adding `required: true` to a property definition will fail the build if a
node matches the binding, but does not contain the property.

The default setting is `required: false`; that is, properties are optional by
default. Using `required: false` is therefore redundant and strongly
discouraged.
