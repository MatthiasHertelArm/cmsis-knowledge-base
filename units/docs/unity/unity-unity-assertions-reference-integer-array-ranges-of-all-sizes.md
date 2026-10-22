---
id: "unity-unity-assertions-reference-integer-array-ranges-of-all-sizes"
type: "concept"
domain: "test"
title: "Unity Assertions Reference: The Assertions in All Their Blessed Glory / Integer Array Ranges (of all sizes)"
summary: "Part of: The Assertions in All Their Blessed Glory"
status: "draft"
collection: "unity"
source: "ThrowTheSwitch/Unity@7f1a686:docs/UnityAssertionsReference.md"
doc_source: "https://github.com/ThrowTheSwitch/Unity/blob/7f1a686/docs/UnityAssertionsReference.md#integer-array-ranges-of-all-sizes"
license: "MIT"
mode: "V"
---

_Part of: The Assertions in All Their Blessed Glory_

These assertions verify that the `expected` array parameter is within +/- `delta`
(inclusive) of the `actual` array parameter. For example, if the expected value is
\[10, 12\] and the delta is 3 then the assertion will fail for any value
outside the range of \[7 - 13, 9 - 15\].

#### `TEST_ASSERT_INT_ARRAY_WITHIN (delta, expected, actual, num_elements)`

#### `TEST_ASSERT_INT8_ARRAY_WITHIN (delta, expected, actual, num_elements)`

#### `TEST_ASSERT_INT16_ARRAY_WITHIN (delta, expected, actual, num_elements)`

#### `TEST_ASSERT_INT32_ARRAY_WITHIN (delta, expected, actual, num_elements)`

#### `TEST_ASSERT_INT64_ARRAY_WITHIN (delta, expected, actual, num_elements)`

#### `TEST_ASSERT_UINT_ARRAY_WITHIN (delta, expected, actual, num_elements)`

#### `TEST_ASSERT_UINT8_ARRAY_WITHIN (delta, expected, actual, num_elements)`

#### `TEST_ASSERT_UINT16_ARRAY_WITHIN (delta, expected, actual, num_elements)`

#### `TEST_ASSERT_UINT32_ARRAY_WITHIN (delta, expected, actual, num_elements)`

#### `TEST_ASSERT_UINT64_ARRAY_WITHIN (delta, expected, actual, num_elements)`

#### `TEST_ASSERT_HEX_ARRAY_WITHIN (delta, expected, actual, num_elements)`

#### `TEST_ASSERT_HEX8_ARRAY_WITHIN (delta, expected, actual, num_elements)`

#### `TEST_ASSERT_HEX16_ARRAY_WITHIN (delta, expected, actual, num_elements)`

#### `TEST_ASSERT_HEX32_ARRAY_WITHIN (delta, expected, actual, num_elements)`

#### `TEST_ASSERT_HEX64_ARRAY_WITHIN (delta, expected, actual, num_elements)`

#### `TEST_ASSERT_CHAR_ARRAY_WITHIN (delta, expected, actual, num_elements)`
