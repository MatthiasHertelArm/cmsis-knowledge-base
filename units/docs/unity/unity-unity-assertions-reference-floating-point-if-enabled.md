---
id: "unity-unity-assertions-reference-floating-point-if-enabled"
type: "concept"
domain: "test"
title: "Unity Assertions Reference: The Assertions in All Their Blessed Glory / Floating Point (If enabled)"
summary: "Part of: The Assertions in All Their Blessed Glory"
status: "draft"
collection: "unity"
source: "ThrowTheSwitch/Unity@7f1a686:docs/UnityAssertionsReference.md"
doc_source: "https://github.com/ThrowTheSwitch/Unity/blob/7f1a686/docs/UnityAssertionsReference.md#floating-point-if-enabled"
license: "MIT"
mode: "V"
---

_Part of: The Assertions in All Their Blessed Glory_

#### `TEST_ASSERT_FLOAT_WITHIN (delta, expected, actual)`

Asserts that the `actual` value is within +/- `delta` of the `expected` value.
The nature of floating point representation is such that exact evaluations of
equality are not guaranteed.

#### `TEST_ASSERT_FLOAT_NOT_WITHIN (delta, expected, actual)`

Asserts that the `actual` value is NOT within +/- `delta` of the `expected` value.

#### `TEST_ASSERT_EQUAL_FLOAT (expected, actual)`

Asserts that the `actual` value is “close enough to be considered equal” to the
`expected` value. If you are curious about the details, refer to the Advanced
Asserting section for more details on this. Omitting a user-specified delta in a
floating point assertion is both a shorthand convenience and a requirement of
code generation conventions for CMock.

#### `TEST_ASSERT_NOT_EQUAL_FLOAT (expected, actual)`

Asserts that the `actual` value is NOT “close enough to be considered equal” to the
`expected` value.

#### `TEST_ASSERT_FLOAT_ARRAY_WITHIN (delta, expected, actual, num_elements)`

See Array assertion section for details. Note that individual array element
uses user-provided delta plus default comparison delta for checking
and is based on `TEST_ASSERT_FLOAT_WITHIN` comparison.

#### `TEST_ASSERT_EQUAL_FLOAT_ARRAY (expected, actual, num_elements)`

See Array assertion section for details. Note that individual array element
float comparisons are executed using `TEST_ASSERT_EQUAL_FLOAT`. That is, user
specified delta comparison values requires a custom-implemented floating point
array assertion.

#### `TEST_ASSERT_LESS_THAN_FLOAT (threshold, actual)`

Asserts that the `actual` parameter is less than `threshold` (exclusive).
For example, if the threshold value is 1.0f, the assertion will fail if it is
greater than 1.0f.

#### `TEST_ASSERT_GREATER_THAN_FLOAT (threshold, actual)`

Asserts that the `actual` parameter is greater than `threshold` (exclusive).
For example, if the threshold value is 1.0f, the assertion will fail if it is
less than 1.0f.

#### `TEST_ASSERT_LESS_OR_EQUAL_FLOAT (threshold, actual)`

Asserts that the `actual` parameter is less than or equal to `threshold`.
The rules for equality are the same as for `TEST_ASSERT_EQUAL_FLOAT`.

#### `TEST_ASSERT_GREATER_OR_EQUAL_FLOAT (threshold, actual)`

Asserts that the `actual` parameter is greater than `threshold`.
The rules for equality are the same as for `TEST_ASSERT_EQUAL_FLOAT`.

#### `TEST_ASSERT_FLOAT_IS_INF (actual)`

Asserts that `actual` parameter is equivalent to positive infinity floating
point representation.

#### `TEST_ASSERT_FLOAT_IS_NEG_INF (actual)`

Asserts that `actual` parameter is equivalent to negative infinity floating
point representation.

#### `TEST_ASSERT_FLOAT_IS_NAN (actual)`

Asserts that `actual` parameter is a Not A Number floating point representation.

#### `TEST_ASSERT_FLOAT_IS_DETERMINATE (actual)`

Asserts that `actual` parameter is a floating point representation usable for
mathematical operations. That is, the `actual` parameter is neither positive
infinity nor negative infinity nor Not A Number floating point representations.

#### `TEST_ASSERT_FLOAT_IS_NOT_INF (actual)`

Asserts that `actual` parameter is a value other than positive infinity floating
point representation.

#### `TEST_ASSERT_FLOAT_IS_NOT_NEG_INF (actual)`

Asserts that `actual` parameter is a value other than negative infinity floating
point representation.

#### `TEST_ASSERT_FLOAT_IS_NOT_NAN (actual)`

Asserts that `actual` parameter is a value other than Not A Number floating
point representation.

#### `TEST_ASSERT_FLOAT_IS_NOT_DETERMINATE (actual)`

Asserts that `actual` parameter is not usable for mathematical operations. That
is, the `actual` parameter is either positive infinity or negative infinity or
Not A Number floating point representations.
