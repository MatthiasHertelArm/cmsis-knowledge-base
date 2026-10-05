---
id: "zep-phandles-specifier-spaces"
type: "concept"
domain: "project"
title: "Phandles: Specifier spaces"
summary: "We'll start with an abstract, high level description of how specifier spaces work in DTS files, before moving on to a concrete example and providing references to further reading for how this all works in practice using DTS …"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/build/dts/phandles.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/build/dts/phandles.rst"
license: "Apache-2.0"
mode: "V"
---

*Specifier spaces* are a way to allow nodes to describe how you should
use them in phandle-array properties.

We'll start with an abstract, high level description of how specifier spaces
work in DTS files, before moving on to a concrete example and providing
references to further reading for how this all works in practice using DTS
files and bindings files.


### High level description


As described above, a phandle-array property is a sequence of "groups" of
phandles followed by some number of cells:

```dts

node {
        phandle-array-prop = <&foo 1 2>, <&bar 3>;
};
```
The cells that follow each phandle are called a *specifier*. In this example,
there are two specifiers:

#. `1 2`: two cells
#. `3`: one cell

Every phandle-array property has an associated *specifier space*. This sounds
complex, but it's really just a way to assign a meaning to the cells that
follow each phandle in a hardware specific way. Every specifier space has a
unique name. There are a few "standard" names for commonly used hardware, but
you can create your own as well.

Devicetree nodes encode the number of cells that must appear in a specifier, by
name, using the `#SPACE_NAME-cells` property. For example, let's assume that
`phandle-array-prop`\ 's specifier space is named `baz`. Then we would need
the `foo` and `bar` nodes to have the following `#baz-cells` properties:

```DTS

foo: node@1000 {
        #baz-cells = <2>;
};

bar: node@2000 {
        #baz-cells = <1>;
};
```
Without the `#baz-cells` property, the devicetree tooling would not be able
to validate the number of cells in each specifier in `phandle-array-prop`.

This flexibility allows you to write down an array of hardware resources in a
single devicetree property, even though the amount of metadata you need to
describe each resource might be different for different nodes.

A single node can also have different numbers of cells in different specifier
spaces. For example, we might have:

```DTS

foo: node@1000 {
        #baz-cells = <2>;
        #bob-cells = <1>;
};
```
With that, if `phandle-array-prop-2` has specifier space `bob`, we could
write:

```DTS

node {
        phandle-array-prop = <&foo 1 2>, <&bar 3>;
        phandle-array-prop-2 = <&foo 4>;
};
```
This flexibility allows you to have a node that manages multiple different
kinds of resources at the same time. The node describes the amount of metadata
needed to describe each kind of resource (how many cells are needed in each
case) using different `#SPACE_NAME-cells` properties.


### Example specifier space: gpio


From the above example, you're already familiar with how one specifier space
works: in the "gpio" space, specifiers almost always have two cells:

#. a pin number
#. a bit mask of flags related to the pin

Therefore, almost all GPIO controller nodes you will see in practice will look
like this:

```DTS

gpioX: gpio-controller@deadbeef {
        gpio-controller;
        #gpio-cells = <2>;
};
```
