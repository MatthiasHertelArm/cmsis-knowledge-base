---
id: "ceed-ide-test-suite-console-report-plugin-overview"
type: "concept"
domain: "test"
title: "IDE Test Suite Console Report: Plugin Overview"
summary: "This plugin is intended to be used in place of the more commonly used \"pretty\" test report plugin."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/plugins/report-tests-ide-stdout.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/report-tests-ide-stdout/#plugin-overview"
license: "MIT"
mode: "V"
---

This plugin is intended to be used in place of the more commonly used "pretty" 
test report plugin. Like its sibling, this plugin ollects raw test results from
the individual test executables of your test suite and presents them in a more 
readable summary form.

The format of test results produced by this plugin is identical to its prettier
sibling with one key difference — test failures are listed in such a way that 
filepaths, line numbers, and test case function names can be easily parsed by 
a typical IDE. The formatting of test failure messages uses a simple, defacto 
standard of a sort recognized almost universally.

The end result is that test failures in your IDE's build window can become 
links that jump directly to failing test cases.
