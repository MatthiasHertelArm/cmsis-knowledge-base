---
id: "ceed-valgrind-console-output"
type: "concept"
domain: "test"
title: "Valgrind: Console output"
summary: "These excerpts come from real runs. Build progress lines are left out."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/plugins/valgrind.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/valgrind/#console-output"
license: "MIT"
mode: "V"
---

These excerpts come from real runs. Build progress lines are left out.

A clean run adds one notice after the test summary:

```
VALGRIND: ✅ OVERALL TEST SUMMARY
TESTED:  2
PASSED:  1
FAILED:  0
IGNORED: 1

ℹ️ NOTICE: Wrote 1 Valgrind report to build/artifacts/valgrind/
```

A test that a memory error ends gets a notice naming the first error and its
report. It replaces Ceedling’s generic crash notice:

```
☠️ ERROR: Test executable `test_nosanitize_crash_sigsegv.out` terminated with Valgrind memory errors.
> Invalid read of size 4 at test_nosanitize_crash_sigsegv.c:32
> Boom log: build/artifacts/valgrind/test_nosanitize_crash_sigsegv.log

VALGRIND: FAILED TEST SUMMARY
[test/test_nosanitize_crash_sigsegv.c]
  Test: test_add_numbers_will_fail
  At line (28): "Test case crashed >> Segmentation fault"

VALGRIND: ❌ OVERALL TEST SUMMARY
TESTED:  2
PASSED:  1
FAILED:  1
IGNORED: 0

ℹ️ NOTICE: Wrote 1 Valgrind report to build/artifacts/valgrind/

❌ BUILD FAILURE SUMMARY
 • [VALGRIND] Unit test failures
 • [VALGRIND] Valgrind detected 2 memory errors across 1 test
```

With [`:fail_build:`](#fail_build) set to `false`, the same run omits the last
line. Only the test failure fails the build.

A test that completes despite memory errors logs one line as it runs:

```
🪲 ERROR: Valgrind detected 2 memory errors in test_example ➡️ see build/artifacts/valgrind/test_example.log
```

A test whose report is missing logs a warning, since its memory error status
is unknown:

```
⚠️ WARNING: Valgrind wrote no report for test_example at build/artifacts/valgrind/test_example.log. Memory error status is unknown.
```
