---
id: "ceed-how-does-a-test-case-even-work-behold-assertions"
type: "concept"
domain: "test"
title: "How Does a Test Case Even Work?: Behold assertions"
summary: "In its simplest form, a test case is just a C function with no parameters and no return value that packages up logical assertions. If no assertions fail, the test case passes."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/testing-guide/test-cases.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/testing-guide/test-cases/#behold-assertions"
license: "MIT"
mode: "V"
---

In its simplest form, a test case is just a C function with no 
parameters and no return value that packages up logical assertions. 
If no assertions fail, the test case passes. Technically, an empty
test case function is a passing test since there can be no failing
assertions.

Ceedling relies on the [Unity] project for its unit test framework
(i.e. the thing that provides assertions and counts up passing
and failing tests).

An assertion is simply a logical comparison of expected and actual
values. Unity provides a wide variety of different assertions to 
cover just about any scenario you might encounter. Getting 
assertions right is actually a bit tricky. Unity does all that 
hard work for you and has been thoroughly tested itself and battle
hardened through use by many, many developers.
