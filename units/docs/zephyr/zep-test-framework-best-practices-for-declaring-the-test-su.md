---
id: "zep-test-framework-best-practices-for-declaring-the-test-su"
type: "concept"
domain: "test"
title: "Test Framework: Best practices for declaring the test suite"
summary: "This all is for the purpose of traceability. It's not enough to have only a semaphore test application."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/test/ztest.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/test/ztest.rst"
license: "Apache-2.0"
mode: "V"
---

*twister* and other validation tools need to obtain the list of
test cases that a Zephyr *ztest* test image will expose.


This all is for the purpose of traceability. It's not enough to
have only a semaphore test application.  We also need to show that we
have testpoints for all APIs and functionality, and we trace back
to documentation of the API, and functional requirements.

The idea is that test reports show results for every test case
as passed, failed, blocked, or skipped.  Reporting on only the
high-level test application, particularly when tests do too
many things, is too vague.
Other questions:

- Why not pre-scan with CPP and then parse? or post scan the ELF file?

  If C pre-processing or building fails because of any issue, then we
  won't be able to tell the subcases.

- Why not declare them in the YAML test configuration?

  A separate test case description file would be harder to maintain
  than just keeping the information in the test source files
  themselves -- only one file to update when changes are made
  eliminates duplication.
