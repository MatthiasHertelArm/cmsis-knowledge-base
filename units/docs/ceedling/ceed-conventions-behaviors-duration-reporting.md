---
id: "ceed-conventions-behaviors-duration-reporting"
type: "concept"
domain: "test"
title: "Conventions & Behaviors: Duration reporting"
summary: "Ceedling logs two execution times for every project run."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/testing-guide/conventions.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/testing-guide/conventions/#duration-reporting"
license: "MIT"
mode: "V"
---

### Logged run times

Ceedling logs two execution times for every project run.

It first logs the set up time necessary to process your project file, parse code
files, build an internal representation of your project, etc. This duration does
not capture the time necessary to load the Ruby runtime itself.

```
Ceedling set up completed in 223 milliseconds
```

Secondly, each Ceedling run also logs the time necessary to run all the tasks 
you specify at the command line.

```
Ceedling operations completed in 1.03 seconds
```

### Test suite & executable durations

A test suite comprises one or more Unity test executables (see 
[Anatomy of a Test Suite](https://throwtheswitch.github.io/Ceedling/testing-guide/conventions/test-suite-anatomy.md)). Ceedling times indvidual Unity 
test executable run durations. It also sums these into a total test suite 
execution time. These duration values are typically used in generating test 
reports via plugins.

Not all test report formats utilize duration values. For those that do, some
effort is usually required to map Ceedling duration values to a relevant test 
suite abstraction within a given test report format.

Because Ceedling can execute builds with multiple threads, care must be taken
to interpret test suite duration values — particularly in relation to 
Ceedling's logged run times.

In a multi-threaded build it's quite common for the logged Ceedling project run
time to be less than the total suite time in a test report. In multi-threaded 
builds on multi-core machines, test executables are run on different processors
simultaneously. As such, the total on-processor time in a test report can 
exceed the operation time Ceedling itself logs to the console. Further, because
multi-threading tends to introduce context switching and processor scheduling 
overhead, the run duration of a test executable may be reported as longer than
a in a comparable single-threaded build.

### Test case run times

Individual test case exection time tracking is specifically a [Unity] feature 
(see its documentation for more details). If enabled and if your platform 
supports the time mechanism Unity relies on, Ceedling will automatically 
collect test case time values — generally made use of by test report plugins.

To enable test case duration measurements, they must be enabled as a Unity
compilation option. Add `UNITY_INCLUDE_EXEC_TIME` to Unity's compilation
symbols (`:unity` ↳ `:defines`) in your Ceedling project file (see example
below). Unity test case durations as reported by Ceedling default to 0 if the
compilation option is not set.

```yaml
:unity:
  :defines:
    - UNITY_INCLUDE_EXEC_TIME
```

_NOTE:_ Most test cases are quite short, and most computers are quite fast. As
 such, Unity test case execution time is often reported as 0 milliseconds as
 the CPU execution time for a test case typically remains in the microseconds
 range. Unity would require special rigging that is inconsistently available
 across platforms to measure test case durations at a finer resolution.
