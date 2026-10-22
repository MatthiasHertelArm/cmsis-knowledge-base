---
id: "ceed-test-runner-test-runner-overview"
type: "concept"
domain: "test"
title: "`:test_runner`: Test runner overview"
summary: "The format of Ceedling test files — the C files that contain unit test cases — is intentionally simple. It’s pure code and all legit C with #include statements, simple functions for test cases, and optional setUp() and tearDown() functions."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/configuration/reference/test-runner.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/test-runner/#test-runner-overview"
license: "MIT"
mode: "V"
---

The format of Ceedling test files — the C files that contain unit test cases —
is intentionally simple. It’s pure code and all legit C with `#include`
statements, simple functions for test cases, and optional `setUp()` and 
`tearDown()` functions.

To create test executables, we need a `main()` and a variety of calls to the
Unity framework to “hook up” all your test cases into a test suite. You can do
this by hand, of course, but it’s tedious and needed updates as code evolves 
are easily forgotten.
