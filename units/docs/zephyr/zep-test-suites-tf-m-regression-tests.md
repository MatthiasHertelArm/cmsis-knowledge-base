---
id: "zep-test-suites-tf-m-regression-tests"
type: "concept"
domain: "security"
title: "Test Suites: TF-M Regression Tests"
summary: "The regression test suite can be run via the tests/modules/tf-m/regression test."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/services/tfm/testsuites.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/services/tfm/testsuites.rst"
license: "Apache-2.0"
mode: "V"
---

The regression test suite can be run via the
`tests/modules/tf-m/regression` test.

It tests various services and communication mechanisms across the
NS/S boundary via the PSA APIs. They provide a useful sanity check for proper
integration between the NS RTOS (Zephyr in this case) and the secure
application (TF-M).
