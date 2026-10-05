---
id: "unity-unity-assertions-reference-basic-fail-pass-and-ignore"
type: "concept"
domain: "test"
title: "Unity Assertions Reference: The Assertions in All Their Blessed Glory / Basic Fail, Pass and Ignore"
summary: "Part of: The Assertions in All Their Blessed Glory"
status: "draft"
collection: "unity"
source: "ThrowTheSwitch/Unity@2b80d1a:docs/UnityAssertionsReference.md"
doc_source: "https://github.com/ThrowTheSwitch/Unity/blob/2b80d1a/docs/UnityAssertionsReference.md#basic-fail-pass-and-ignore"
license: "MIT"
mode: "V"
---

_Part of: The Assertions in All Their Blessed Glory_

#### `TEST_FAIL()`

#### `TEST_FAIL_MESSAGE("message")`

This fella is most often used in special conditions where your test code is
performing logic beyond a simple assertion. That is, in practice, `TEST_FAIL()`
will always be found inside a conditional code block.

_Examples:_

- Executing a state machine multiple times that increments a counter your test
code then verifies as a final step.
- Triggering an exception and verifying it (as in Try / Catch / Throw - see the
[CException](https://github.com/ThrowTheSwitch/CException) project).

#### `TEST_PASS()`

#### `TEST_PASS_MESSAGE("message")`

This will abort the remainder of the test, but count the test as a pass. Under
normal circumstances, it is not necessary to include this macro in your tests…
a lack of failure will automatically be counted as a `PASS`. It is occasionally
useful for tests with `#ifdef`s and such.

#### `TEST_IGNORE()`

#### `TEST_IGNORE_MESSAGE("message")`

Marks a test case (i.e. function meant to contain test assertions) as ignored.
Usually this is employed as a breadcrumb to come back and implement a test case.
An ignored test case has effects if other assertions are in the enclosing test
case (see Unity documentation for more).

#### `TEST_MESSAGE(message)`

This can be useful for outputting `INFO` messages into the Unity output stream
without actually ending the test. Like pass and fail messages, it will be output
with the filename and line number.
