---
id: "unity-unity-assertions-reference-signed-and-unsigned-integers-of-all-size"
type: "concept"
domain: "test"
title: "Unity Assertions Reference: The Assertions in All Their Blessed Glory / Signed and Unsigned Integers (of all sizes)"
summary: "Part of: The Assertions in All Their Blessed Glory"
status: "draft"
collection: "unity"
source: "ThrowTheSwitch/Unity@2b80d1a:docs/UnityAssertionsReference.md"
doc_source: "https://github.com/ThrowTheSwitch/Unity/blob/2b80d1a/docs/UnityAssertionsReference.md#signed-and-unsigned-integers-of-all-sizes"
license: "MIT"
mode: "V"
---

_Part of: The Assertions in All Their Blessed Glory_

Large integer sizes can be disabled for build targets that do not support them.
For example, if your target only supports up to 16 bit types, by defining the
appropriate symbols Unity can be configured to omit 32 and 64 bit operations
that would break compilation (see Unity documentation for more). Refer to
Advanced Asserting later in this document for advice on dealing with other word
sizes.

#### `TEST_ASSERT_EQUAL_INT (expected, actual)`

#### `TEST_ASSERT_EQUAL_INT8 (expected, actual)`

#### `TEST_ASSERT_EQUAL_INT16 (expected, actual)`

#### `TEST_ASSERT_EQUAL_INT32 (expected, actual)`

#### `TEST_ASSERT_EQUAL_INT64 (expected, actual)`

#### `TEST_ASSERT_EQUAL_UINT (expected, actual)`

#### `TEST_ASSERT_EQUAL_UINT8 (expected, actual)`

#### `TEST_ASSERT_EQUAL_UINT16 (expected, actual)`

#### `TEST_ASSERT_EQUAL_UINT32 (expected, actual)`

#### `TEST_ASSERT_EQUAL_UINT64 (expected, actual)`
