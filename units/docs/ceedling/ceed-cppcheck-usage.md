---
id: "ceed-cppcheck-usage"
type: "concept"
domain: "test"
title: "Cppcheck: Usage"
summary: "Cppcheck: Usage"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/plugins/cppcheck.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/cppcheck/#usage"
license: "MIT"
mode: "V"
---

### Analyze whole project

Run analysis for all project sources:

```shell
$ ceedling cppcheck:all
```

*Note: Analysis is run with* all *checks enabled.*

### Analyze single file

Run analysis for single source file:

```shell
$ ceedling cppcheck:<filename>
```

*Note: Analysis will run with the checks in [`:enable_checks`](#checks) list enabled.*
