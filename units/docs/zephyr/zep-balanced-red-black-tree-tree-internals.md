---
id: "zep-balanced-red-black-tree-tree-internals"
type: "concept"
domain: "rtos"
title: "Balanced Red/Black Tree: Tree Internals"
summary: "As described, the Zephyr rbtree implementation is a conventional red/black tree as described pervasively in academic sources. Low level details about the algorithm are out of scope for this document, as they match existing conventions."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/data_structures/rbtree.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/data_structures/rbtree.rst"
license: "Apache-2.0"
mode: "V"
---

As described, the Zephyr rbtree implementation is a conventional
red/black tree as described pervasively in academic sources.  Low
level details about the algorithm are out of scope for this document,
as they match existing conventions.  This discussion will be limited
to details notable or specific to the Zephyr implementation.

The core invariant guaranteed by the tree is that the path from the root of
the tree to any leaf is no more than twice as long as the path to any
other leaf.  This is achieved by associating one bit of "color" with
each node, either red or black, and enforcing a rule that no red child
can be a child of another red child (i.e. that the number of black
nodes on any path to the root must be the same, and that no more than
that number of "extra" red nodes may be present).  This rule is
enforced by a set of rotation rules used to "fix" trees following
modification.

These rotations are conceptually implemented on top of a primitive
that "swaps" the position of one node with another in the list.
Typical implementations effect this by simply swapping the nodes
internal "data" pointers, but because the Zephyr `rbnode` is
intrusive, that cannot work.  Zephyr must include somewhat more
elaborate code to handle the edge cases (for example, one swapped node
can be the root, or the two may already be parent/child).

The `rbnode` struct for a Zephyr rbtree contains only two
pointers, representing the "left", and "right" children of a node
within the binary tree.  Traversal of a tree for rebalancing following
modification, however, routinely requires the ability to iterate
"upwards" from a node as well.  It is very common for red/black trees
in the industry to store a third "parent" pointer for this purpose.
Zephyr avoids this requirement by building a "stack" of node pointers
locally as it traverses downward through the tree and updating it
appropriately as modifications are made.  So a Zephyr rbtree can be
implemented with no more runtime storage overhead than a dlist.

These properties, of a balanced tree data structure that works with
only two pointers of data per node and that works without any need for
a memory allocation API, are quite rare in the industry and are
somewhat unique to Zephyr.
