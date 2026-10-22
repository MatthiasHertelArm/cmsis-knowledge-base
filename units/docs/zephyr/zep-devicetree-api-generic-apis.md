---
id: "zep-devicetree-api-generic-apis"
type: "concept"
domain: "project"
title: "Devicetree API: Generic APIs"
summary: "The APIs in this section can be used anywhere and do not require DT_DRV_COMPAT to be defined."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/build/dts/api/api.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/build/dts/api/api.rst"
license: "Apache-2.0"
mode: "V"
---

The APIs in this section can be used anywhere and do not require
`DT_DRV_COMPAT` to be defined.


### Node identifiers and helpers


A *node identifier* is a way to refer to a devicetree node at C preprocessor
time. While node identifiers are not C values, you can use them to access
devicetree data in C rvalue form using, for example, the
devicetree-property-access API.

The root node `/` has node identifier `DT_ROOT`. You can create node
identifiers for other devicetree nodes using `DT_PATH`,
`DT_NODELABEL`, `DT_ALIAS`, and `DT_INST`.

There are also `DT_PARENT` and `DT_CHILD` macros which can be
used to create node identifiers for a given node's parent node or a particular
child node, respectively.

The following macros create or operate on node identifiers.


### Property access


The following general-purpose macros can be used to access node properties.
There are special-purpose APIs for accessing the devicetree-ranges-property,
devicetree-reg-property and devicetree-interrupts-property.

Property values can be read using these macros even if the node is disabled,
as long as it has a matching binding.


### `ranges` property


Use these APIs instead of devicetree-property-access to access the
`ranges` property. Because this property's semantics are defined by the
devicetree specification, these macros can be used even for nodes without
matching bindings. However, they take on special semantics when the node's
binding indicates it is a PCIe bus node, as defined in the
PCI Bus Binding to: IEEE Std 1275-1994 Standard for Boot (Initialization Configuration) Firmware

.. _PCI Bus Binding to\: IEEE Std 1275-1994 Standard for Boot (Initialization Configuration) Firmware:
    https://www.devicetree.org/open-firmware/bindings/pci/pci2_1.pdf


### `reg` property


Use these APIs instead of devicetree-property-access to access the
`reg` property. Because this property's semantics are defined by the
devicetree specification, these macros can be used even for nodes without
matching bindings.


### `interrupts` property


Use these APIs instead of devicetree-property-access to access the
`interrupts` property.

Because this property's semantics are defined by the devicetree specification,
some of these macros can be used even for nodes without matching bindings. This
does not apply to macros which take cell names as arguments.


### For-each macros


The `DT_FOREACH_ANCESTOR` macro allows iterating over the ancestor node
of a devicetree node.
Additionally, the `DT_FOREACH_CHILD` macro allows iterating over the
children of a devicetree node.

There are special-purpose for-each macros, like
`DT_INST_FOREACH_STATUS_OKAY`, but these require `DT_DRV_COMPAT` to
be defined before use.


### Existence checks


This section documents miscellaneous macros that can be used to test if a node
exists, how many nodes of a certain type exist, whether a node has certain
properties, etc. Some macros used for special purposes (such as
`DT_IRQ_HAS_IDX` and all macros which require `DT_DRV_COMPAT`) are
documented elsewhere on this page.


### Inter-node dependencies


The `devicetree.h` API has some support for tracking dependencies between
nodes. Dependency tracking relies on a binary "depends on" relation between
devicetree nodes, which is defined as the `transitive closure
<https://en.wikipedia.org/wiki/Transitive_closure>`_ of the following "directly
depends on" relation:

- every non-root node directly depends on its parent node
- a node directly depends on any nodes its properties refer to by phandle, this
  can be changed with dt-bindings-dependency-mode in the node's binding
- a node directly depends on its `interrupt-parent` if it has an
  `interrupts` property
- a parent node inherits all dependencies from its child nodes

A *dependency ordering* of a devicetree is a list of its nodes, where each node
`n` appears earlier in the list than any nodes that depend on `n`. A node's
*dependency ordinal* is then its zero-based index in that list. Thus, for two
distinct devicetree nodes `n1` and `n2` with dependency ordinals `d1` and
`d2`, we have:

- `d1 != d2`
- if `n1` depends on `n2`, then `d1 > d2`
- `d1 > d2` does **not** necessarily imply that `n1` depends on `n2`

The Zephyr build system chooses a dependency ordering of the final devicetree
and assigns a dependency ordinal to each node. Dependency related information
can be accessed using the following macros. The exact dependency ordering
chosen is an implementation detail, but cyclic dependencies are detected and
cause errors, so it's safe to assume there are none when using these macros.

There are instance number-based conveniences as well; see
`DT_INST_DEP_ORD` and subsequent documentation.


### Bus helpers


Zephyr's devicetree bindings language supports a `bus:` key which allows
bindings to declare that nodes with a given compatible describe system buses.
In this case, child nodes are considered to be on a bus of the given type, and
the following APIs may be used.
