---
id: "zep-min-heap-data-structure-heap-structure"
type: "concept"
domain: "rtos"
title: "Min-Heap Data Structure: Heap Structure"
summary: "The heap is maintained as a complete binary tree stored in an array. Each node satisfies the min-heap property:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/data_structures/min_heap.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/data_structures/min_heap.rst"
license: "Apache-2.0"
mode: "V"
---

The heap is maintained as a complete binary tree stored in an array.
Each node satisfies the **min-heap** property:

   - The value of each node is less than or equal to the values of its children.

This property ensures that the **minimum element is always at the root**
(index 0).

```text

Index:      0   1   2   3   4   5   6
Values:    [1,  3,  5,  8,  9, 10, 12]

               1
             /   \
           3       5
          / \     / \
         8   9  10  12
```
For any node at index `i`, its children are at indices:

- Left child: `2*i + 1`

- Right child: `2*i + 2`

Its parent is at index:

- Parent: `(i - 1) / 2`
