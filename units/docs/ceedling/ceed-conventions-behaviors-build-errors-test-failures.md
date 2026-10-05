---
id: "ceed-conventions-behaviors-build-errors-test-failures"
type: "concept"
domain: "test"
title: "Conventions & Behaviors: Build errors, test failures"
summary: "Ceedling will run a specified build until an error. An error refers to a build step encountering an unrecoverable problem. Files not found, nonexistent paths, compilation errors, missing symbols, plugin exceptions, etc."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/testing-guide/conventions.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/testing-guide/conventions/#build-errors-test-failures"
license: "MIT"
mode: "V"
---

### Errors vs. Failures

Ceedling will run a specified build until an **_error_**. An error 
refers to a build step encountering an unrecoverable problem. Files 
not found, nonexistent paths, compilation errors, missing symbols, 
plugin exceptions, etc. are all errors that will cause Ceedling 
to immediately end a build.

A **_failure_** refers to a test failure. That is, an assertion of 
an expected versus actual value failed within a unit test case. 
A test failure will not stop a build. Instead, the suite will run 
to completion with test failures collected and reported along with 
all test case statistics.

### Ceedling Exit Codes

In its default configuration, Ceedling terminates with an exit code 
of `1`:

* On any build error and immediately terminates upon that build 
   error.
* On any test case failure but runs the build to completion and
   shuts down normally.

This behavior can be especially handy in Continuous Integration 
environments where you typically want an automated CI build to break 
upon either build errors or test failures.

If this exit code convention for test failures does not work for you, 
no problem-o. You may be of the mind that running a test suite to 
completion should yield a successful exit code (even if tests failed).
Add the following to your project file to force Ceedling to finish a 
build with an exit code of 0 even upon test case failures.

```yaml
# Ceedling terminates with happy `exit(0)` even if test cases fail
:test_build:
   :graceful_fail: true
```

If you use the option for graceful failures in CI, you'll want to
rig up some kind of logging monitor that scans Ceedling's test
summary report sent to `$stdout` and/or a log file. Otherwise, you
could have a successful build but failing tests.

### Test executable exit codes

Ceedling works by collecting multiple Unity test executables together 
into a test suite (more here: [Anatomy of a Test Suite](https://throwtheswitch.github.io/Ceedling/testing-guide/conventions/test-suite-anatomy.md)).

A Unity test executable's exit code is the number of failed tests. An
exit code of `0` means all tests passed while anything larger than zero
is the number of test failures.

Because of platform limitations on how big an exit code number can be
and because of the logical complexities of distinguishing test failure
counts from build errors or plugin problems, Ceedling conforms to a
much simpler exit code convention than Unity: `0` = 🙂 while `1` = ☹️.

[CMock]: http://github.com/ThrowTheSwitch/CMock
[Unity]: http://github.com/ThrowTheSwitch/Unity
