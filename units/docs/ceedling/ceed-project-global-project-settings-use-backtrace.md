---
id: "ceed-project-global-project-settings-use-backtrace"
type: "concept"
domain: "test"
title: "`:project`: Global project settings: `:use_backtrace`"
summary: "When a test executable encounters a ☠️ Segmentation Fault or other crash condition, the executable immediately terminates and no further details for test suite reporting are collected."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/configuration/reference/project.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/project/#use-backtrace"
license: "MIT"
mode: "V"
---

When a test executable encounters a ☠️ **Segmentation Fault** or other crash
condition, the executable immediately terminates and no further details for test
suite reporting are collected.

But, fear not. You can bring your dead unit tests back to life.

By default, in the case of a crash, Ceedling reruns the test executable for
each test case using a special mode to isolate that test case. In this way
Ceedling can iteratively identify which test cases are causing the crash or
exercising release code that is causing the crash. Ceedling then assembles the
final test reporting results from these individual test case runs.

You have three options for this setting, `:none`, `:simple`, or `:gdb`.

### `:none`
`:none` will simply cause a test report to list each test case as failed
due to a test executable crash.

Sample Ceedling run output with backtrace `:none`:

```
👟 Executing
------------
Running TestUsartModel.out...
☠️ ERROR: Test executable `TestUsartModel.out` seems to have crashed

-------------------
FAILED TEST SUMMARY
-------------------
[test/TestUsartModel.c]
  Test: testGetBaudRateRegisterSettingShouldReturnAppropriateBaudRateRegisterSetting
  At line (24): "Test executable crashed"

  Test: testCrash
  At line (37): "Test executable crashed"

  Test: testGetFormattedTemperatureFormatsTemperatureFromCalculatorAppropriately
  At line (44): "Test executable crashed"

  Test: testShouldReturnErrorMessageUponInvalidTemperatureValue
  At line (50): "Test executable crashed"

  Test: testShouldReturnWakeupMessage
  At line (56): "Test executable crashed"

-----------------------
❌ OVERALL TEST SUMMARY
-----------------------
TESTED:  5
PASSED:  0
FAILED:  5
IGNORED: 0
```

### `:simple`
`:simple` causes Ceedling to re-run each test case in the test executable
individually to identify and report the problematic test case(s). This is
the default option and is described above.

Sample Ceedling run output with backtrace `:simple`:

```
👟 Executing
------------
Running TestUsartModel.out...
☠️ ERROR: Test executable `TestUsartModel.out` seems to have crashed

-------------------
FAILED TEST SUMMARY
-------------------
[test/TestUsartModel.c]
  Test: testCrash
  At line (37): "Test case crashed >> Segmentation fault (core dumped)"

-----------------------
❌ OVERALL TEST SUMMARY
-----------------------
TESTED:  5
PASSED:  4
FAILED:  1
IGNORED: 0
```

### `:gdb`
`:gdb` uses the [`gdb`][gdb] debugger to identify and report the troublesome
line of code triggering the crash. If this option is enabled, but `gdb` is
not available to Ceedling, project configuration validation will terminate
with an error at startup.

With `gdb` in use, Ceedling will provide a brief crash summary from details
extracted from the `gdb` report. Ceedling will attempt to surface in the 
summary the offending line of code or failing `assert()` from the report.

The full `gdb` report is captured to a log file, and the log filepath is 
provided in the crash summary. The log filepath will comprise the containing 
test executable as a subdirectory and the name of the crashing test case 
function as the filename.

!!! warning "macOS: a working `gdb` can stop attaching to processes"
    macOS restricts which debuggers may attach to a process. A Homebrew `gdb`
    needs to be codesigned to attach at all, and that trust is fragile — a
    `brew upgrade`, a macOS system update, or a Gatekeeper/`taskgated` cache
    reset can silently revoke it, even for a `gdb` that worked yesterday.

    Ceedling checks for this at build startup. If `:use_backtrace:` is `:gdb`
    but `gdb` cannot actually attach to a process, Ceedling logs a warning and
    automatically falls back to `:simple` for that run rather than failing the
    build. To restore `:gdb` backtraces, re-codesign `gdb` following the
    [Homebrew `gdb` instructions][gdb-homebrew] and see `taskgated(8)`.

Sample Ceedling run output with backtrace `:gdb`:

```
👟 Executing
------------
Running TestUsartModel.out...
☠️ ERROR: Test executable `TestUsartModel.out` seems to have crashed

-------------------
FAILED TEST SUMMARY
-------------------
[test/TestUsartModel.c]
  Test: testCrash
  At line (40): "Test case crashed >> [SIGSEGV] Segmentation fault
                `uint32_t i = *null_ptr;`
                (build/logs/test/TestUsartModel/testCrash.gdb.log)"

-----------------------
❌ OVERALL TEST SUMMARY
-----------------------
TESTED:  5
PASSED:  4
FAILED:  1
IGNORED: 0
```

**_Notes:_**

1. The default of `:simple` only works in an environment capable of using
   command line arguments (passed to the test executable). If you are targeting
   a simulator with your test executable binaries, `:simple` is unlikely to
   work for you. In the simplest case, you may simply fall back to `:none`.
   With some work and using Ceedling's various features, much more sophisticated
   options are possible.
1. The `:gdb` option currently only supports the native build platform. That is,
   the `:gdb` backtrace option cannot handle backtrace for cross-compiled code
   or any sort of simulator-based test fixture.

[gdb]: https://www.sourceware.org/gdb/
[gdb-homebrew]: https://sourceware.org/gdb/wiki/PermissionsDarwin

**Default**: `:simple`
