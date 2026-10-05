---
id: "zep-generating-coverage-reports"
type: "concept"
domain: "test"
title: "Generating coverage reports"
summary: "With Zephyr, you can generate code coverage reports to analyze which parts of the code are covered by a given test or application."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/test/coverage.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/test/coverage.rst"
license: "Apache-2.0"
mode: "V"
---

With Zephyr, you can generate code coverage reports to analyze which parts of
the code are covered by a given test or application.

You can do this in two ways:

* In a real embedded target or QEMU, using Zephyr's gcov integration
* Directly in your host computer, by compiling your application targeting
  the POSIX architecture
