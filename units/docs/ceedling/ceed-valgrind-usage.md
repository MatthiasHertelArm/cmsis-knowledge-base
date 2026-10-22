---
id: "ceed-valgrind-usage"
type: "concept"
domain: "test"
title: "Valgrind: Usage"
summary: "The Valgrind plugin follows the conventions of test: tasks."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/plugins/valgrind.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/valgrind/#usage"
license: "MIT"
mode: "V"
---

The Valgrind plugin follows the conventions of `test:` tasks.

### Run Valgrind for all tests

Build all test executables and run each under Valgrind:

```shell
$ ceedling valgrind:all
```

### Run Valgrind for a single test file

Build and run Valgrind for one test file (pass the filename, no path):

```shell
$ ceedling valgrind:test_my_module.c
```

You can also pass just the source filename; Ceedling will locate the
corresponding test file automatically:

```shell
$ ceedling valgrind:my_module.c
```
