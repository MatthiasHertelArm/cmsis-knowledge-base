---
id: "unity-unity-assertions-reference-table-of-contents"
type: "concept"
domain: "test"
title: "Unity Assertions Reference: Table of Contents"
summary: "Unity Assertions Reference: Table of Contents"
status: "draft"
collection: "unity"
source: "ThrowTheSwitch/Unity@2b80d1a:docs/UnityAssertionsReference.md"
doc_source: "https://github.com/ThrowTheSwitch/Unity/blob/2b80d1a/docs/UnityAssertionsReference.md#table-of-contents"
license: "MIT"
mode: "V"
---

1. [Background and Overview](#background-and-overview)
   1. [Super Condensed Version](#super-condensed-version)
   2. [Unity Is Several Things But Mainly It’s Assertions](#unity-is-several-things-but-mainly-its-assertions)
   3. [What’s an Assertion?](#whats-an-assertion)
   4. [Unity’s Assertions: Helpful Messages _and_ Free Source Code Documentation](#unitys-assertions-helpful-messages-and-free-source-code-documentation)
2. [Assertion Conventions and Configurations](#assertion-conventions-and-configurations)
   1. [Naming and Parameter Conventions](#naming-and-parameter-conventions)
   2. [TEST_ASSERT_EACH_EQUAL_X Variants](#test_assert_each_equal_x-variants)
   3. [Configuration](#configuration)
3. [The Assertions in All Their Blessed Glory](#the-assertions-in-all-their-blessed-glory)
   1. [Basic Fail, Pass and Ignore](#basic-fail-pass-and-ignore)
   2. [Boolean](#boolean)
   3. [Signed and Unsigned Integers (of all sizes)](#signed-and-unsigned-integers-of-all-sizes)
   4. [Unsigned Integers (of all sizes) in Hexadecimal](#unsigned-integers-of-all-sizes-in-hexadecimal)
   5. [Characters](#characters)
   6. [Masked and Bit-level Assertions](#masked-and-bit-level-assertions)
   7. [Integer Less Than / Greater Than](#integer-less-than--greater-than)
   8. [Integer Ranges (of all sizes)](#integer-ranges-of-all-sizes)
   9. [Structs and Strings](#structs-and-strings)
   10. [Arrays](#arrays)
   11. [Integer Array Ranges (of all sizes)](#integer-array-ranges-of-all-sizes)
   12. [Each Equal (Arrays to Single Value)](#each-equal-arrays-to-single-value)
   13. [Floating Point (If enabled)](#floating-point-if-enabled)
   14. [Double (If enabled)](#double-if-enabled)
4. [Advanced Asserting: Details On Tricky Assertions](#advanced-asserting-details-on-tricky-assertions)
   1. [How do the EQUAL assertions work for FLOAT and DOUBLE?](#how-do-the-equal-assertions-work-for-float-and-double)
   2. [How do we deal with targets with non-standard int sizes?](#how-do-we-deal-with-targets-with-non-standard-int-sizes)
