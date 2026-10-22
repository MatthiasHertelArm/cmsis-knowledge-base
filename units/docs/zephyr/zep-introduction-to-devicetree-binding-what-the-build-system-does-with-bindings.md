---
id: "zep-introduction-to-devicetree-binding-what-the-build-system-does-with-bindings"
type: "concept"
domain: "project"
title: "Introduction to Devicetree Bindings: What the build system does with bindings"
summary: "The build system uses bindings both to validate devicetree nodes and to convert the devicetree's contents into the generated :ref:devicetree_generated.h <dt-outputs> header file."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/build/dts/bindings-intro.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/build/dts/bindings-intro.rst"
license: "Apache-2.0"
mode: "V"
---

The build system uses bindings both to validate devicetree nodes and to convert
the devicetree's contents into the generated :ref:`devicetree_generated.h
<dt-outputs>` header file.

For example, the build system would use the above binding to check that the
required `num-foos` property is present in the `bar-device` node, and that
its value, `<3>`, has the correct type.

The build system will then generate a macro for the `bar-device` node's
`num-foos` property, which will expand to the integer literal `3`. This
macro lets you get the value of the property in C code using the API which is
discussed later in this guide in dt-from-c.

For another example, the following node would cause a build error, because it
has no `num-foos` property, and this property is marked required in the
binding:

```devicetree

bad-node {
    compatible = "foo-company,bar-device";
};
```
