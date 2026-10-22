---
id: "unity-unity-assertions-reference-each-equal-arrays-to-single-value"
type: "concept"
domain: "test"
title: "Unity Assertions Reference: The Assertions in All Their Blessed Glory / Each Equal (Arrays to Single Value)"
summary: "Part of: The Assertions in All Their Blessed Glory"
status: "draft"
collection: "unity"
source: "ThrowTheSwitch/Unity@7f1a686:docs/UnityAssertionsReference.md"
doc_source: "https://github.com/ThrowTheSwitch/Unity/blob/7f1a686/docs/UnityAssertionsReference.md#each-equal-arrays-to-single-value"
license: "MIT"
mode: "V"
---

_Part of: The Assertions in All Their Blessed Glory_

`expected` are single values and `actual` are arrays. `num_elements` specifies
the number of elements in the arrays to compare.

`_HEX` assertions produce failure messages with expected and actual array
contents formatted in hexadecimal.

Assertions fail upon the first element in the compared arrays found not to
match. Failure messages specify the array index of the failed comparison.

#### `TEST_ASSERT_EACH_EQUAL_INT (expected, actual, num_elements)`

#### `TEST_ASSERT_EACH_EQUAL_INT8 (expected, actual, num_elements)`

#### `TEST_ASSERT_EACH_EQUAL_INT16 (expected, actual, num_elements)`

#### `TEST_ASSERT_EACH_EQUAL_INT32 (expected, actual, num_elements)`

#### `TEST_ASSERT_EACH_EQUAL_INT64 (expected, actual, num_elements)`

#### `TEST_ASSERT_EACH_EQUAL_UINT (expected, actual, num_elements)`

#### `TEST_ASSERT_EACH_EQUAL_UINT8 (expected, actual, num_elements)`

#### `TEST_ASSERT_EACH_EQUAL_UINT16 (expected, actual, num_elements)`

#### `TEST_ASSERT_EACH_EQUAL_UINT32 (expected, actual, num_elements)`

#### `TEST_ASSERT_EACH_EQUAL_UINT64 (expected, actual, num_elements)`

#### `TEST_ASSERT_EACH_EQUAL_HEX (expected, actual, num_elements)`

#### `TEST_ASSERT_EACH_EQUAL_HEX8 (expected, actual, num_elements)`

#### `TEST_ASSERT_EACH_EQUAL_HEX16 (expected, actual, num_elements)`

#### `TEST_ASSERT_EACH_EQUAL_HEX32 (expected, actual, num_elements)`

#### `TEST_ASSERT_EACH_EQUAL_HEX64 (expected, actual, num_elements)`

#### `TEST_ASSERT_EACH_EQUAL_CHAR (expected, actual, num_elements)`

#### `TEST_ASSERT_EACH_EQUAL_PTR (expected, actual, num_elements)`

#### `TEST_ASSERT_EACH_EQUAL_STRING (expected, actual, num_elements)`

#### `TEST_ASSERT_EACH_EQUAL_MEMORY (expected, actual, len, num_elements)`

`len` is the memory in bytes to be compared at each array element.
