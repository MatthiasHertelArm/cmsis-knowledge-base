---
id: "ceed-plugin-overview-simple-coverage-summaries"
type: "concept"
domain: "test"
title: "Plugin Overview: Simple Coverage Summaries"
summary: "In its simplest usage, this plugin outputs coverage statistics to the console for each source file exercised by a test. These console-based coverage summaries are provided after the standard Ceedling test results summary."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/plugins/gcov/overview.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/gcov/overview/#simple-coverage-summaries"
license: "MIT"
mode: "V"
---

In its simplest usage, this plugin outputs coverage statistics to the console
for each source file exercised by a test. These console-based coverage 
summaries are provided after the standard Ceedling test results summary. Other 
than enabling the plugin and ensuring `gcov` is installed, no further set up 
is necessary to produce these summaries.

!!! tip
    [Automatic summaries may be disabled](https://throwtheswitch.github.io/Ceedling/plugins/gcov/overview/setup.md#disabling-automatic-coverage-summaries).

When the Gcov plugin is active it enables Ceedling tasks like this:

```shell
 > ceedling gcov:Model
```

… that then generate output like this:

```
--------------------------
GCOV: OVERALL TEST SUMMARY
--------------------------
TESTED:  1
PASSED:  1
FAILED:  0
IGNORED: 0

---------------------------
GCOV: CODE COVERAGE SUMMARY
---------------------------

TestModel
---------
Model.c | Lines executed:100.00% of 4
Model.c | No branches
Model.c | No calls
TimerModel.c | Lines executed:0.00% of 3
TimerModel.c | No branches
TimerModel.c | No calls
```
