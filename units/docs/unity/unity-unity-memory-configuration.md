---
id: "unity-unity-memory-configuration"
type: "concept"
domain: "test"
title: "Unity Memory: Configuration"
summary: "By default, this module tries to use the real stdlib malloc and free internally. If you would prefer it to use something else, like FreeRTOS's pvPortMalloc and pvPortFree, then you can use these defines to make it so."
status: "draft"
collection: "unity"
source: "ThrowTheSwitch/Unity@7f1a686:extras/memory/readme.md"
doc_source: "https://github.com/ThrowTheSwitch/Unity/blob/7f1a686/extras/memory/readme.md#configuration"
license: "MIT"
mode: "V"
---

### `UNITY_MALLOC` and `UNITY_FREE`

By default, this module tries to use the real stdlib `malloc` and `free` internally.
If you would prefer it to use something else, like FreeRTOS's `pvPortMalloc` and `pvPortFree`, then you can use these defines to make it so.

### `UNITY_EXCLUDE_STDLIB_MALLOC`

If you would like this library to ignore stdlib or other heap engines completely, and manage the memory on its own, then define this. All memory will be handled internally (and at likely lower overhead).
Note that this is not a very featureful memory manager, but is sufficient for most testing purposes.

### `UNITY_INTERNAL_HEAP_SIZE_BYTES`

When using the built-in memory manager (see `UNITY_EXCLUDE_STDLIB_MALLOC`) this define allows you to set the heap size this library will use to manage the memory.
