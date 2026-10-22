---
id: "zep-test-suites"
type: "concept"
domain: "security"
title: "Test Suites"
summary: "These test suites can be run from Zephyr via an appropriate sample application in the samples/tfm_integration folder."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/services/tfm/testsuites.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/services/tfm/testsuites.rst"
license: "Apache-2.0"
mode: "V"
---

TF-M includes two sets of test suites:

* tf-m-tests - Standard TF-M specific regression tests
* psa-arch-tests - Test suites for specific PSA APIs (secure storage, etc.)

These test suites can be run from Zephyr via an appropriate sample application
in the samples/tfm_integration folder.
