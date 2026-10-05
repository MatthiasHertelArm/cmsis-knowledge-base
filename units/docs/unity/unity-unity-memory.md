---
id: "unity-unity-memory"
type: "concept"
domain: "test"
title: "Unity Memory"
summary: "This Framework is an optional add-on to Unity. By including unity.h and then unity_memory.h, you have the added ability to track malloc and free calls. This addon requires that the stdlib functions be overridden by its own defines."
status: "draft"
collection: "unity"
source: "ThrowTheSwitch/Unity@2b80d1a:extras/memory/readme.md"
doc_source: "https://github.com/ThrowTheSwitch/Unity/blob/2b80d1a/extras/memory/readme.md"
license: "MIT"
mode: "V"
---

This Framework is an optional add-on to Unity.
By including unity.h and then unity_memory.h, you have the added ability to track malloc and free calls.
This addon requires that the stdlib functions be overridden by its own defines.
These defines will still malloc / realloc / free etc, but will also track the calls in order to ensure that you don't have any memory leaks in your programs.

Note that this is only useful in situations where a unit is in charge of both the allocation and deallocation of memory.
When it is not symmetric, unit testing can report a number of false failures.
A more advanced runtime tool is required to track complete system memory handling.
