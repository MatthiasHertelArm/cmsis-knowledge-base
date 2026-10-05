---
id: "zep-syntax-and-structure-nodes"
type: "concept"
domain: "project"
title: "Syntax and structure: Nodes"
summary: "Like any tree data structure, a devicetree has a hierarchy of nodes. The above tree has three nodes:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/build/dts/intro-syntax-structure.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/build/dts/intro-syntax-structure.rst"
license: "Apache-2.0"
mode: "V"
---

Like any tree data structure, a devicetree has a hierarchy of *nodes*.
The above tree has three nodes:

#. A root node: `/`
#. A node named `a-node`, which is a child of the root node
#. A node named `a-sub-node`, which is a child of `a-node`

Nodes can be assigned *node labels*, which are unique shorthands that refer to
the labeled node. Above, `a-sub-node` has the node label
`subnode_nodelabel`. A node can have zero, one, or multiple node labels. You
can use node labels to refer to the node elsewhere in the devicetree.

Devicetree nodes have *paths* identifying their locations in the tree. Like
Unix file system paths, devicetree paths are strings separated by slashes
(`/`), and the root node's path is a single slash: `/`. Otherwise, each
node's path is formed by concatenating the node's ancestors' names with the
node's own name, separated by slashes. For example, the full path to
`a-sub-node` is `/a-node/a-sub-node`.
