---
id: "zep-syntax-and-structure-properties"
type: "concept"
domain: "project"
title: "Syntax and structure: Properties"
summary: "Devicetree nodes can also have properties. Properties are name/value pairs. Property values can be any sequence of bytes. In some cases, the values are an array of what are called cells. A cell is just a 32-bit unsigned integer."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/build/dts/intro-syntax-structure.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/build/dts/intro-syntax-structure.rst"
license: "Apache-2.0"
mode: "V"
---

Devicetree nodes can also have *properties*. Properties are name/value pairs.
Property values can be any sequence of bytes. In some cases, the values are an
array of what are called *cells*. A cell is just a 32-bit unsigned integer.

Node `a-sub-node` has a property named `foo`, whose value is a cell with
value 3. The size and type of `foo`\ 's value are implied by the enclosing
angle brackets (`<` and `>`) in the DTS.

See dt-writing-property-values below for more example property values.
