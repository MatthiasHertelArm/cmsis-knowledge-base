---
id: "ceed-sanitize-how-findings-are-reported"
type: "concept"
domain: "test"
title: "Sanitize: How findings are reported"
summary: "A sanitizer’s finding is reported where you would look for a test failure."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/plugins/sanitize.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/sanitize/#how-findings-are-reported"
license: "MIT"
mode: "V"
---

A sanitizer’s finding is reported where you would look for a test failure.

- **A halted test** fails, named by its finding. When a sanitizer stops a test,
  the test executable ends before Unity prints its summary, and Ceedling treats
  that as a crash. The crash notice names the sanitizer, the kind of finding,
  its location, and the test’s log. It replaces Ceedling’s generic crash notice
  and its backtrace advice:

  ```
  ☠️ ERROR: Test executable `test_buffer.out` was stopped by a sanitizer finding.
  > AddressSanitizer heap-buffer-overflow at test/test_buffer.c:21
  > Boom log: build/artifacts/sanitize/sanitize/test_buffer.log
  ```

  The test’s failure message carries the same on one line:

  ```
  AddressSanitizer heap-buffer-overflow at test/test_buffer.c:21 (Boom log: build/artifacts/sanitize/sanitize/test_buffer.log)
  ```

- **A leak** is a finding, not a test failure. Leaks are found as a test
  executable exits, after every test case has reported. Your test results stay
  as Unity reported them, and the leak is logged and counted.

- **A crash no sanitizer reported** keeps Ceedling’s usual crash message.

Each finding is also logged as the test runs, except one a crash notice
names. With [`:fail_build:`](#fail_build) enabled, the build failure summary
counts the findings and names the reports written:

```
 • [SANITIZE] Sanitizers found 2 problems in 2 tests. See the reports in build/artifacts/sanitize/sanitize: sanitize.log, sanitize.json.
```

### Example console output

These excerpts come from real runs. Build progress lines are left out.

A halted test, with `:reports` set to `[:text, :json, :sarif]`:

```
☠️ ERROR: Test executable `test_nosanitize_heap_buffer_overflow.out` was stopped by a sanitizer finding.
> AddressSanitizer heap-buffer-overflow at test/test_nosanitize_heap_buffer_overflow.c:29
> Boom log: build/artifacts/sanitize/sanitize/test_nosanitize_heap_buffer_overflow.log

SANITIZE: FAILED TEST SUMMARY
[test/test_nosanitize_heap_buffer_overflow.c]
  Test: test_writes_past_its_buffer
  At line (27): "AddressSanitizer heap-buffer-overflow at test/test_nosanitize_heap_buffer_overflow.c:29 (Boom log: build/artifacts/sanitize/sanitize/test_nosanitize_heap_buffer_overflow.log)"

SANITIZE: ❌ OVERALL TEST SUMMARY
TESTED:  2
PASSED:  1
FAILED:  1
IGNORED: 0

❌ BUILD FAILURE SUMMARY
 • [SANITIZE] Unit test failures
 • [SANITIZE] Sanitizers found 1 problem in 1 test. See the reports in build/artifacts/sanitize/sanitize: sanitize.log, sanitize.json, sanitize.sarif.
```

A leak. Every test passes, and the leak alone fails the build. The test’s
own output section shows the sanitizer’s report:

```
🪲 ERROR: test_nosanitize_leak: LeakSanitizer memory-leak at test/test_nosanitize_leak.c:32 ➡️ see build/artifacts/sanitize/sanitize/test_nosanitize_leak.log

SANITIZE: TEST OUTPUT
[test/test_nosanitize_leak.c]
  - "==456==ERROR: LeakSanitizer: detected memory leaks"
  - "Direct leak of 32 byte(s) in 1 object(s) allocated from:"
  - "    #1 0x55f0b16d72e9 in test_loses_its_allocation test/test_nosanitize_leak.c:32"
  - "SUMMARY: AddressSanitizer: 32 byte(s) leaked in 1 allocation(s)."

SANITIZE: ✅ OVERALL TEST SUMMARY
TESTED:  2
PASSED:  2
FAILED:  0
IGNORED: 0

❌ BUILD FAILURE SUMMARY
 • [SANITIZE] Sanitizers found 1 problem in 1 test. See the reports in build/artifacts/sanitize/sanitize: sanitize.log.
```

A clean build adds nothing to the test summary, even when JSON or SARIF
reports are written.

On macOS, a leak sanitizer or `:detect_leaks` logs this warning at startup:

```
⚠️ WARNING: Leak detection is not supported on macOS and has been disabled.
```

### Backtraces

With [`:use_backtrace`](https://throwtheswitch.github.io/Ceedling/plugins/sanitize/../configuration/reference/project.md#use_backtrace)
set to `:simple`, each crashed test executable reruns one test case at a time.
The reruns run with the sanitizers’ options too, so each crashed test case is
named by its own finding.

`:gdb` backtraces fall back to `:simple` in instrumented builds, with a notice.
The leak sanitizer cannot run under a debugger, and a sanitizer’s own report
already includes the stack.
