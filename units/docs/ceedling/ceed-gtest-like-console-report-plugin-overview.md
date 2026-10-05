---
id: "ceed-gtest-like-console-report-plugin-overview"
type: "concept"
domain: "test"
title: "GTest-like Console Report: Plugin Overview"
summary: "This plugin is intended to be used in place of the more commonly used \"pretty\" test report plugin."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/plugins/report-tests-gtestlike-stdout.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/report-tests-gtestlike-stdout/#plugin-overview"
license: "MIT"
mode: "V"
---

This plugin is intended to be used in place of the more commonly used "pretty" 
test report plugin. Like its sibling, this plugin ollects raw test results from
the individual test executables of your test suite and presents them in a more 
readable summary form — specifically the GoogleTest format.

This plugin is most useful when using an IDE or working with a CI system that
understands the GTest console logging format.
