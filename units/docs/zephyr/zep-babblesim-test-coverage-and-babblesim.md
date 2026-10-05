---
id: "zep-babblesim-test-coverage-and-babblesim"
type: "concept"
domain: "test"
title: "BabbleSim: Test coverage and BabbleSim"
summary: "As the bsim boards are based on the POSIX architecture, you can easily collect test coverage information."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/test/bsim.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/test/bsim.rst"
license: "Apache-2.0"
mode: "V"
---

As the bsim boards are based on the POSIX architecture, you can easily collect
test coverage information.

Check the page on coverage generation for more info, and note you can
just pass the `--coverage` option to twister to automatically build with
`CONFIG_COVERAGE` and generate the coverage report.
