---
id: "ceed-sanitize-usage"
type: "concept"
domain: "test"
title: "Sanitize: Usage"
summary: "The Sanitize plugin follows the conventions of test: tasks."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/plugins/sanitize.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/sanitize/#usage"
license: "MIT"
mode: "V"
---

The Sanitize plugin follows the conventions of `test:` tasks.

### Run sanitizers for all tests

```shell
$ ceedling sanitize:all
```

### Run sanitizers for a single test file

Pass the test filename, no path:

```shell
$ ceedling sanitize:test_my_module.c
```

You can also pass just the source filename. Ceedling locates the corresponding
test file:

```shell
$ ceedling sanitize:my_module.c
```
