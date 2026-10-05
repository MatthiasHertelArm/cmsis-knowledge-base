---
id: "zep-assertions"
type: "concept"
domain: "rtos"
title: "Assertions"
summary: "Zephyr provides several assertion facilities for catching programming errors:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/services/other/assert.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/services/other/assert.rst"
license: "Apache-2.0"
mode: "V"
---

Zephyr provides several assertion facilities for catching programming errors:

- **Runtime assertions** check a condition while the code is running and, if it
  fails, induce a fatal error. The recommended API is the
  module-aware `ZASSERT() macro; the older ASSERT()` macro is now a thin
  compatibility layer on top of it and is deprecated.
- **Build assertions** (`BUILD_ASSERT()`) are evaluated entirely at
  compile-time and always checked.


**Note:** The runtime `ZASSERT()` macro documented here is unrelated to the lowercase `zassert_*` macros (`zassert_true()`, `zassert_equal()`, ...) provided by the The `zassert_*` macros report test failures, the `ZASSERT()` macro raises a fatal error when a programming error is detected.
