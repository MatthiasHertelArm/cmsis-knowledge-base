---
id: "unity-unity-assertions-reference-structs-and-strings"
type: "concept"
domain: "test"
title: "Unity Assertions Reference: The Assertions in All Their Blessed Glory / Structs and Strings"
summary: "Part of: The Assertions in All Their Blessed Glory"
status: "draft"
collection: "unity"
source: "ThrowTheSwitch/Unity@2b80d1a:docs/UnityAssertionsReference.md"
doc_source: "https://github.com/ThrowTheSwitch/Unity/blob/2b80d1a/docs/UnityAssertionsReference.md#structs-and-strings"
license: "MIT"
mode: "V"
---

_Part of: The Assertions in All Their Blessed Glory_

#### `TEST_ASSERT_EQUAL_PTR (expected, actual)`

Asserts that the pointers point to the same memory location.

#### `TEST_ASSERT_NOT_EQUAL_PTR (expected, actual)`

Asserts that the pointers DO NOT point to the same memory location. Two NULL
pointers are considered equal and will cause this assertion to fail. A NULL
pointer and a non-NULL pointer are considered not equal and will pass.

#### `TEST_ASSERT_EQUAL_STRING (expected, actual)`

Asserts that the null terminated (`’\0’`) strings are identical. If strings are
of different lengths or any portion of the strings before their terminators
differ, the assertion fails. Two NULL strings (i.e. zero length) are considered
equivalent.

#### `TEST_ASSERT_NOT_EQUAL_STRING (expected, actual)`

Asserts that the null terminated (`’\0’`) strings are NOT identical. The
assertion passes if the strings differ in length or content at any point before
their null terminators. A NULL pointer and a non-NULL string are considered not
equal and will pass. Two NULL pointers are considered equal and will fail.

#### `TEST_ASSERT_EQUAL_STRING_LEN (expected, actual, len)`

Asserts that the null terminated (`’\0’`) strings are identical up to the specified length.
It checks only the first `len` characters, not the entire string.

#### `TEST_ASSERT_NOT_EQUAL_STRING_LEN (expected, actual, len)`

Asserts that the null terminated (`’\0’`) strings are NOT identical within the
first `len` characters. The assertion passes if the strings differ at any
position within the specified length. A NULL pointer and a non-NULL string are
considered not equal and will pass. Two NULL pointers are considered equal and
will fail. Specifying a `len` of zero is considered pointless and will fail.

#### `TEST_ASSERT_EQUAL_MEMORY (expected, actual, len)`

Asserts that the contents of the memory specified by the `expected` and `actual`
pointers is identical. The size of the memory blocks in bytes is specified by
the `len` parameter.

#### `TEST_ASSERT_NOT_EQUAL_MEMORY (expected, actual, len)`

Asserts that the contents of the memory specified by the `expected` and `actual`
pointers is NOT identical within the first `len` bytes. The assertion passes if
any byte differs within that range. A NULL pointer and a non-NULL pointer are
considered not equal and will pass. Two NULL pointers (or the same pointer) are
considered equal and will fail. Specifying a `len` of zero is considered
pointless and will fail.
