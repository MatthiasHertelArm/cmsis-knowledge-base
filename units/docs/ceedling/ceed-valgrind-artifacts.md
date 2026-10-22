---
id: "ceed-valgrind-artifacts"
type: "concept"
domain: "test"
title: "Valgrind: Artifacts"
summary: "Each test executable produces a Valgrind log file at:"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/plugins/valgrind.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/valgrind/#artifacts"
license: "MIT"
mode: "V"
---

Each test executable produces a Valgrind log file at:

```
build/artifacts/valgrind/<test_name>.log
```

With [`:xml_report:`](#xml_report) enabled, a machine-readable report is written
beside it:

```
build/artifacts/valgrind/<test_name>.xml
```

For example, running `ceedling valgrind:test_my_module.c` produces:

```
build/artifacts/valgrind/test_my_module.log
```

These log files contain the full Valgrind Memcheck output, including any
detected memory errors, leak summaries, and (with `--track-origins=yes`)
the origin of uninitialized values.

The log files are included in `ceedling clean` targets.
