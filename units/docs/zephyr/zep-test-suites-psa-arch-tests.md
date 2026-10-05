---
id: "zep-test-suites-psa-arch-tests"
type: "concept"
domain: "security"
title: "Test Suites: PSA Arch Tests"
summary: "The PSA Arch Test suite, available via tfm_psa_test, contains a number of test suites that can be used to validate that PSA API specifications are being followed by the secure application, TF-M being an implementation of the Platform …"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/services/tfm/testsuites.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/services/tfm/testsuites.rst"
license: "Apache-2.0"
mode: "V"
---

The PSA Arch Test suite, available via tfm_psa_test, contains a number of
test suites that can be used to validate that PSA API specifications are
being followed by the secure application, TF-M being an implementation of
the Platform Security Architecture (PSA).

Only one of these suites can be run at a time, with the available test suites
described via `CONFIG_TFM_PSA_TEST_*` KConfig flags:
