---
id: "zep-test-suites-purpose"
type: "concept"
domain: "security"
title: "Test Suites: Purpose"
summary: "The output of these test suites is required to obtain PSA Certification for your specific board, RTOS (Zephyr here), and PSA implementation (TF-M in this case)."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/services/tfm/testsuites.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/services/tfm/testsuites.rst"
license: "Apache-2.0"
mode: "V"
---

The output of these test suites is required to obtain PSA Certification for
your specific board, RTOS (Zephyr here), and PSA implementation (TF-M in this
case).

They also provide a useful test case to validate any PRs that make meaningful
changes to TF-M, such as enabling a new TF-M board target, or making changes
to the core TF-M module(s). They should generally be run as a coherence check
before publishing a new PR for new board support, etc.
