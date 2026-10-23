---
id: "ceed-cppcheck-usage"
type: "concept"
domain: "test"
title: "Cppcheck: Usage"
summary: "Run analysis across all project sources:"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/plugins/cppcheck.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/cppcheck/#usage"
license: "MIT"
mode: "V"
---

### Analyze whole project

Run analysis across all project sources:

```shell
$ ceedling cppcheck:all
```

Every check is enabled for this mode. Configure at least one entry in
[`:reports:`](#reports) or enable [`:fail_build:`](#fail_build), or this task
has nothing to produce and says so.

### Analyze single file

Run analysis for one source file, by filename with no path:

```shell
$ ceedling cppcheck:example_file.c
```

Findings print to the console. This mode uses the checks in
[`:enable_checks:`](#enable_checks).

### List suppression files

Show which suppression files were collected from your configured paths and
files:

```shell
$ ceedling files:cppcheck
```

This task needs no Cppcheck installation.
