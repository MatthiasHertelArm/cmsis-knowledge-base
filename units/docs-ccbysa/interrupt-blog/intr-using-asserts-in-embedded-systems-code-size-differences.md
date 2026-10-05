---
id: "intr-using-asserts-in-embedded-systems-code-size-differences"
type: "concept"
domain: "debug"
title: "Using Asserts in Embedded Systems: Custom Assert Implementation Examples / Code Size Differences"
summary: "Part of: Custom Assert Implementation Examples"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-11-05-asserts-in-embedded-systems.md"
doc_source: "https://interrupt.memfault.com/blog/asserts-in-embedded-systems#code-size-differences"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Custom Assert Implementation Examples_

Why did we compile in FreeRTOS to our examples? Because we can now check out the
differences in code sizes between our different assert implementations by
hooking up our `MY_ASSERT` macro to the FreeRTOS `configASSERT` macro.

Below are the results for compiling with `-O0` or `-Os` while only keeping in
the FreeRTOS asserts (removing those from `assert_path_A` and `assert_path_B`)

| Assert Impl #                              | `-Os` CFLAG (B) | Delta  |
| ------------------------------------------ | --------------- | ------ |
| None                                       | 17711           |        |
| [#1](#standard-library-assert-1) (Default) | 43477           | +25766 |
| [#3](#filepath-and-line-number-assert-3)   | 19404           | +1693  |
| [#4](#filename-and-line-number-assert-4)   | 18845           | +1134  |
| [#5](#register-values-only-assert-5)       | 18519           | +808   |

As one can see, there are significant code size wins over the standard
`__FILE__` assert implementations used by the common embedded platforms by using
the `__FILENAME__` approach, or by capturing the PC/LR registers on assert.
