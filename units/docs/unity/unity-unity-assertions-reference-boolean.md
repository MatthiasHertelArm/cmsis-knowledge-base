---
id: "unity-unity-assertions-reference-boolean"
type: "concept"
domain: "test"
title: "Unity Assertions Reference: The Assertions in All Their Blessed Glory / Boolean"
summary: "Part of: The Assertions in All Their Blessed Glory"
status: "draft"
collection: "unity"
source: "ThrowTheSwitch/Unity@2b80d1a:docs/UnityAssertionsReference.md"
doc_source: "https://github.com/ThrowTheSwitch/Unity/blob/2b80d1a/docs/UnityAssertionsReference.md#boolean"
license: "MIT"
mode: "V"
---

_Part of: The Assertions in All Their Blessed Glory_

#### `TEST_ASSERT (condition)`

#### `TEST_ASSERT_TRUE (condition)`

#### `TEST_ASSERT_FALSE (condition)`

#### `TEST_ASSERT_UNLESS (condition)`

A simple wording variation on `TEST_ASSERT_FALSE`.The semantics of
`TEST_ASSERT_UNLESS` aid readability in certain test constructions or
conditional statements.

#### `TEST_ASSERT_NULL (pointer)`

#### `TEST_ASSERT_NOT_NULL (pointer)`

Verify if a pointer is or is not NULL.

#### `TEST_ASSERT_EMPTY (pointer)`

#### `TEST_ASSERT_NOT_EMPTY (pointer)`

Verify if the first element dereferenced from a pointer is or is not zero. This
is particularly useful for checking for empty (or non-empty) null-terminated
C strings, but can be just as easily used for other null-terminated arrays.
