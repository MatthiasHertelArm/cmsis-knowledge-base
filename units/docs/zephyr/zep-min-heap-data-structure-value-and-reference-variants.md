---
id: "zep-min-heap-data-structure-value-and-reference-variants"
type: "concept"
domain: "rtos"
title: "Min-Heap Data Structure: Value and reference variants"
summary: "Two variants are provided, differing only in how elements are stored:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/data_structures/min_heap.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/data_structures/min_heap.rst"
license: "Apache-2.0"
mode: "V"
---

Two variants are provided, differing only in how elements are stored:

- `min_heap` (described above) stores elements **by value** in a contiguous
  buffer. An arbitrary element is removed by content (search) or by index.
  This suits priority queues of small values looked up by content.

- `min_heap_ref` stores **references** to caller-owned nodes, each embedding
  a `min_heap_handle`. Insertion is zero-copy, and a specific node is removed
  in `O(\log n)` using the handle the caller already holds, with no
  search. This suits long-lived objects removed by identity rather than by
  content, such as kernel timeouts.

The two are complementary: the value heap cannot remove by identity in better
than `O(n)`, while the reference heap is a poor fit for
value-with-search use. `min_heap_ref` is header-only and requires no
Kconfig.
