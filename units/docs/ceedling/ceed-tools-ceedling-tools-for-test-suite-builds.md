---
id: "ceed-tools-ceedling-tools-for-test-suite-builds"
type: "concept"
domain: "test"
title: "`:tools`: Ceedling tools for test suite builds"
summary: "Our recommended approach to writing and executing test suites relies on the GNU toolchain. Yes, even for embedded system work on platforms with their own, proprietary C toolchain."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/configuration/reference/tools.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/tools/#ceedling-tools-for-test-suite-builds"
license: "MIT"
mode: "V"
---

Our recommended approach to writing and executing test suites relies on the GNU
toolchain. _*Yes, even for embedded system work on platforms with their own,
proprietary C toolchain.*_ Please see
[this section of documentation][sweet-suite] to understand this recommendation
among all your options.

You can and sometimes must run a Ceedling test suite in an emulator or on
target, and Ceedling allows you to do this through tool definitions documented
here. Generally, you'll likely want to rely on the default definitions.

[sweet-suite]: ../../overview/test-environments.md#test-suite-execution-environments
