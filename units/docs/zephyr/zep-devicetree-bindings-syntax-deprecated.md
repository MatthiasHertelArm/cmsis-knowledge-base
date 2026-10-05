---
id: "zep-devicetree-bindings-syntax-deprecated"
type: "concept"
domain: "project"
title: "Devicetree bindings syntax: Properties / deprecated"
summary: "A property with deprecated: true indicates to both the user and the tooling that the property is meant to be phased out."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/build/dts/bindings-syntax.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/build/dts/bindings-syntax.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: Properties_

A property with `deprecated: true` indicates to both the user and the tooling
that the property is meant to be phased out.

The tooling will report a warning if the devicetree includes the property that
is flagged as deprecated. (This warning is upgraded to an error in the
twister_script for upstream pull requests.)

The default setting is `deprecated: false`. Using `deprecated: false` is
therefore redundant and strongly discouraged.
