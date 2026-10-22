---
id: "unity-unity-assertions-reference-integer-ranges-of-all-sizes"
type: "concept"
domain: "test"
title: "Unity Assertions Reference: The Assertions in All Their Blessed Glory / Integer Ranges (of all sizes)"
summary: "Part of: The Assertions in All Their Blessed Glory"
status: "draft"
collection: "unity"
source: "ThrowTheSwitch/Unity@7f1a686:docs/UnityAssertionsReference.md"
doc_source: "https://github.com/ThrowTheSwitch/Unity/blob/7f1a686/docs/UnityAssertionsReference.md#integer-ranges-of-all-sizes"
license: "MIT"
mode: "V"
---

_Part of: The Assertions in All Their Blessed Glory_

These assertions verify that the `expected` parameter is within +/- `delta`
(inclusive) of the `actual` parameter. For example, if the expected value is 10
and the delta is 3 then the assertion will fail for any value outside the range
of 7 - 13.

#### `TEST_ASSERT_INT_WITHIN (delta, expected, actual)`

#### `TEST_ASSERT_INT8_WITHIN (delta, expected, actual)`

#### `TEST_ASSERT_INT16_WITHIN (delta, expected, actual)`

#### `TEST_ASSERT_INT32_WITHIN (delta, expected, actual)`

#### `TEST_ASSERT_INT64_WITHIN (delta, expected, actual)`

#### `TEST_ASSERT_UINT_WITHIN (delta, expected, actual)`

#### `TEST_ASSERT_UINT8_WITHIN (delta, expected, actual)`

#### `TEST_ASSERT_UINT16_WITHIN (delta, expected, actual)`

#### `TEST_ASSERT_UINT32_WITHIN (delta, expected, actual)`

#### `TEST_ASSERT_UINT64_WITHIN (delta, expected, actual)`

#### `TEST_ASSERT_HEX_WITHIN (delta, expected, actual)`

#### `TEST_ASSERT_HEX8_WITHIN (delta, expected, actual)`

#### `TEST_ASSERT_HEX16_WITHIN (delta, expected, actual)`

#### `TEST_ASSERT_HEX32_WITHIN (delta, expected, actual)`

#### `TEST_ASSERT_HEX64_WITHIN (delta, expected, actual)`

#### `TEST_ASSERT_CHAR_WITHIN (delta, expected, actual)`
