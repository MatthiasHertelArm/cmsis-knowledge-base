---
id: "zep-generating-coverage-reports-coverage-reports-using-the-posix-archite"
type: "concept"
domain: "test"
title: "Generating coverage reports: Coverage reports using the POSIX architecture"
summary: "When compiling for the POSIX architecture, you utilize your host native tooling to build a native executable which contains your application, the Zephyr OS, and some basic HW emulation."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/test/coverage.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/test/coverage.rst"
license: "Apache-2.0"
mode: "V"
---

When compiling for the POSIX architecture, you utilize your host native tooling
to build a native executable which contains your application, the Zephyr OS,
and some basic HW emulation.

That means you can use the same tools you would while developing any
other desktop application.

To build your application with `gcc`'s gcov, simply set
`CONFIG_COVERAGE` before compiling it.
When you run your application, `gcov` coverage data will be dumped into the
respective `gcda` and `gcno` files.
You may postprocess these with your preferred tools. For example:

```console

$ ./build/zephyr/zephyr.exe
# Press Ctrl+C to exit
$ lcov --capture --directory ./ --output-file lcov.info -q --rc lcov_branch_coverage=1
$ genhtml lcov.info --output-directory lcov_html -q --ignore-errors source --branch-coverage --highlight --legend
```

**Note:** You need a recent version of lcov (at least 1.14) with support for intermediate text format. Such packages exist in recent Linux distributions. Alternatively, you can use gcovr (at least version 4.2).
