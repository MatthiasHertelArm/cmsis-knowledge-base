---
id: "unity-unity-assertions-reference-unsigned-integers-of-all-sizes-in-hexade"
type: "concept"
domain: "test"
title: "Unity Assertions Reference: The Assertions in All Their Blessed Glory / Unsigned Integers (of all sizes) in Hexadecimal"
summary: "Part of: The Assertions in All Their Blessed Glory"
status: "draft"
collection: "unity"
source: "ThrowTheSwitch/Unity@7f1a686:docs/UnityAssertionsReference.md"
doc_source: "https://github.com/ThrowTheSwitch/Unity/blob/7f1a686/docs/UnityAssertionsReference.md#unsigned-integers-of-all-sizes-in-hexadecimal"
license: "MIT"
mode: "V"
---

_Part of: The Assertions in All Their Blessed Glory_

All `_HEX` assertions are identical in function to unsigned integer assertions
but produce failure messages with the `expected` and `actual` values formatted
in hexadecimal. Unity output is big endian.

#### `TEST_ASSERT_EQUAL_HEX (expected, actual)`

#### `TEST_ASSERT_EQUAL_HEX8 (expected, actual)`

#### `TEST_ASSERT_EQUAL_HEX16 (expected, actual)`

#### `TEST_ASSERT_EQUAL_HEX32 (expected, actual)`

#### `TEST_ASSERT_EQUAL_HEX64 (expected, actual)`
