---
id: "unity-unity-memory-module-api"
type: "concept"
domain: "test"
title: "Unity Memory: Module API"
summary: "These must be called at the beginning and end of each test. For simplicity, they can be added to setUp and tearDown in order to do their job."
status: "draft"
collection: "unity"
source: "ThrowTheSwitch/Unity@2b80d1a:extras/memory/readme.md"
doc_source: "https://github.com/ThrowTheSwitch/Unity/blob/2b80d1a/extras/memory/readme.md#module-api"
license: "MIT"
mode: "V"
---

### `UnityMalloc_StartTest` and `UnityMalloc_EndTest`

These must be called at the beginning and end of each test.
For simplicity, they can be added to `setUp` and `tearDown` in order to do their job.
When using the test runner generator scripts, these will be automatically added to the runner whenever unity_memory.h is included.

### `UnityMalloc_MakeMallocFailAfterCount`

This can be called from the tests themselves.
Passing this function a number will force the reference counter to start keeping track of malloc calls.
During that test, if the number of malloc calls exceeds the number given, malloc will immediately start returning `NULL`.
This allows you to test error conditions.
Think of it as a simplified mock.
