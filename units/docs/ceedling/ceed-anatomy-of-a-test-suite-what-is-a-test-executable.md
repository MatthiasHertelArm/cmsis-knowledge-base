---
id: "ceed-anatomy-of-a-test-suite-what-is-a-test-executable"
type: "concept"
domain: "test"
title: "Anatomy of a Test Suite: What is a test executable?"
summary: "Put simply, in a Ceedling test suite, each test file becomes a test executable. Your test code file becomes a single test executable."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/testing-guide/test-suite-anatomy.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/testing-guide/test-suite-anatomy/#what-is-a-test-executable"
license: "MIT"
mode: "V"
---

Put simply, in a Ceedling test suite, each test file becomes a test executable.
Your test code file becomes a single test executable.

`test_foo.c` ➡️ `test_foo.out` (or `test_foo.exe` on Windows)

A single test executable generally comprises the following. Each item in this
list is a C file compiled into an object file. The entire list is linked into
a final test executable.

* One or more release C code files under test (`foo.c`)
* `unity.c`.
* A test C code file (`test_foo.c`).
* A generated test runner C code file (`test_foo_runner.c`). `main()` is located
  in the runner.
* If using mocks:
    * `cmock.c`
    * One more mock C code files generated from source header files (`mock_bar.c`)
