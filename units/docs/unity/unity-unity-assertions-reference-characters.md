---
id: "unity-unity-assertions-reference-characters"
type: "concept"
domain: "test"
title: "Unity Assertions Reference: The Assertions in All Their Blessed Glory / Characters"
summary: "Part of: The Assertions in All Their Blessed Glory"
status: "draft"
collection: "unity"
source: "ThrowTheSwitch/Unity@7f1a686:docs/UnityAssertionsReference.md"
doc_source: "https://github.com/ThrowTheSwitch/Unity/blob/7f1a686/docs/UnityAssertionsReference.md#characters"
license: "MIT"
mode: "V"
---

_Part of: The Assertions in All Their Blessed Glory_

While you can use the 8-bit integer assertions to compare `char`, another option is
to use this specialized assertion which will show printable characters as printables,
otherwise showing the HEX escape code for the characters.

#### `TEST_ASSERT_EQUAL_CHAR (expected, actual)`
