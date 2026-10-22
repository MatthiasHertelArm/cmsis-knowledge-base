---
id: "unity-unity-assertions-reference-arrays"
type: "concept"
domain: "test"
title: "Unity Assertions Reference: The Assertions in All Their Blessed Glory / Arrays"
summary: "Part of: The Assertions in All Their Blessed Glory"
status: "draft"
collection: "unity"
source: "ThrowTheSwitch/Unity@7f1a686:docs/UnityAssertionsReference.md"
doc_source: "https://github.com/ThrowTheSwitch/Unity/blob/7f1a686/docs/UnityAssertionsReference.md#arrays"
license: "MIT"
mode: "V"
---

_Part of: The Assertions in All Their Blessed Glory_

`expected` and `actual` parameters are both arrays. `num_elements` specifies the
number of elements in the arrays to compare.

`_HEX` assertions produce failure messages with expected and actual array
contents formatted in hexadecimal.

For array of strings comparison behavior, see comments for
`TEST_ASSERT_EQUAL_STRING` in the preceding section.

Assertions fail upon the first element in the compared arrays found not to
match. Failure messages specify the array index of the failed comparison.

#### `TEST_ASSERT_EQUAL_INT_ARRAY (expected, actual, num_elements)`

#### `TEST_ASSERT_EQUAL_INT8_ARRAY (expected, actual, num_elements)`

#### `TEST_ASSERT_EQUAL_INT16_ARRAY (expected, actual, num_elements)`

#### `TEST_ASSERT_EQUAL_INT32_ARRAY (expected, actual, num_elements)`

#### `TEST_ASSERT_EQUAL_INT64_ARRAY (expected, actual, num_elements)`

#### `TEST_ASSERT_EQUAL_UINT_ARRAY (expected, actual, num_elements)`

#### `TEST_ASSERT_EQUAL_UINT8_ARRAY (expected, actual, num_elements)`

#### `TEST_ASSERT_EQUAL_UINT16_ARRAY (expected, actual, num_elements)`

#### `TEST_ASSERT_EQUAL_UINT32_ARRAY (expected, actual, num_elements)`

#### `TEST_ASSERT_EQUAL_UINT64_ARRAY (expected, actual, num_elements)`

#### `TEST_ASSERT_EQUAL_HEX_ARRAY (expected, actual, num_elements)`

#### `TEST_ASSERT_EQUAL_HEX8_ARRAY (expected, actual, num_elements)`

#### `TEST_ASSERT_EQUAL_HEX16_ARRAY (expected, actual, num_elements)`

#### `TEST_ASSERT_EQUAL_HEX32_ARRAY (expected, actual, num_elements)`

#### `TEST_ASSERT_EQUAL_HEX64_ARRAY (expected, actual, num_elements)`

#### `TEST_ASSERT_EQUAL_CHAR_ARRAY (expected, actual, num_elements)`

#### `TEST_ASSERT_EQUAL_PTR_ARRAY (expected, actual, num_elements)`

#### `TEST_ASSERT_EQUAL_STRING_ARRAY (expected, actual, num_elements)`

#### `TEST_ASSERT_EQUAL_MEMORY_ARRAY (expected, actual, len, num_elements)`

`len` is the memory in bytes to be compared at each array element.
