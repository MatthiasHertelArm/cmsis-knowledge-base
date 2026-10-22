---
id: "unity-unity-assertions-reference-masked-and-bit-level-assertions"
type: "concept"
domain: "test"
title: "Unity Assertions Reference: The Assertions in All Their Blessed Glory / Masked and Bit-level Assertions"
summary: "Part of: The Assertions in All Their Blessed Glory"
status: "draft"
collection: "unity"
source: "ThrowTheSwitch/Unity@7f1a686:docs/UnityAssertionsReference.md"
doc_source: "https://github.com/ThrowTheSwitch/Unity/blob/7f1a686/docs/UnityAssertionsReference.md#masked-and-bit-level-assertions"
license: "MIT"
mode: "V"
---

_Part of: The Assertions in All Their Blessed Glory_

Masked and bit-level assertions produce output formatted in hexadecimal. Unity
output is big endian.

#### `TEST_ASSERT_BITS (mask, expected, actual)`

Only compares the masked (i.e. high) bits of `expected` and `actual` parameters.

#### `TEST_ASSERT_BITS_HIGH (mask, actual)`

Asserts the masked bits of the `actual` parameter are high.

#### `TEST_ASSERT_BITS_LOW (mask, actual)`

Asserts the masked bits of the `actual` parameter are low.

#### `TEST_ASSERT_BIT_HIGH (bit, actual)`

Asserts the specified bit of the `actual` parameter is high.

#### `TEST_ASSERT_BIT_LOW (bit, actual)`

Asserts the specified bit of the `actual` parameter is low.
