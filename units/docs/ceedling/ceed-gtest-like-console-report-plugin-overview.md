---
id: "ceed-gtest-like-console-report-plugin-overview"
type: "concept"
domain: "test"
title: "GTest-like Console Report: Plugin Overview"
summary: "This plugin reports test results the way GoogleTest prints them. It is intended to be used in place of the more commonly used \"pretty\" test report plugin."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/plugins/report-tests-gtestlike-stdout.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/report-tests-gtestlike-stdout/#plugin-overview"
license: "MIT"
mode: "V"
---

This plugin reports test results the way GoogleTest prints them. It is intended
to be used in place of the more commonly used "pretty" test report plugin. Like
its sibling, it collects raw test results from the individual test executables
of your test suite and presents them in summary form.

This plugin is most useful with an IDE or CI system that understands GoogleTest’s
console output. Its line formats follow GoogleTest’s own console printer, down to
singular and plural counts and the ordering of its summary.
