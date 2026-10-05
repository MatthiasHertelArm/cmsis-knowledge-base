---
id: "unity-unity-assertions-reference-integer-less-than-greater-than"
type: "concept"
domain: "test"
title: "Unity Assertions Reference: The Assertions in All Their Blessed Glory / Integer Less Than / Greater Than"
summary: "Part of: The Assertions in All Their Blessed Glory"
status: "draft"
collection: "unity"
source: "ThrowTheSwitch/Unity@2b80d1a:docs/UnityAssertionsReference.md"
doc_source: "https://github.com/ThrowTheSwitch/Unity/blob/2b80d1a/docs/UnityAssertionsReference.md#integer-less-than-greater-than"
license: "MIT"
mode: "V"
---

_Part of: The Assertions in All Their Blessed Glory_

These assertions verify that the `actual` parameter is less than or greater
than `threshold` (exclusive). For example, if the threshold value is 0 for the
greater than assertion will fail if it is 0 or less. There are assertions for
all the various sizes of ints, as for the equality assertions. Some examples:

#### `TEST_ASSERT_GREATER_THAN_INT8 (threshold, actual)`

#### `TEST_ASSERT_GREATER_OR_EQUAL_INT16 (threshold, actual)`

#### `TEST_ASSERT_LESS_THAN_INT32 (threshold, actual)`

#### `TEST_ASSERT_LESS_OR_EQUAL_UINT (threshold, actual)`

#### `TEST_ASSERT_NOT_EQUAL_UINT8 (threshold, actual)`
