---
id: "ceed-set-up-configuration-disabling-automatic-coverage-summaries"
type: "concept"
domain: "test"
title: "Set up & Configuration: Disabling automatic coverage summaries"
summary: "To disable the coverage summaries generated immediately following gcov: tasks, simply add the following to a top-level :gcov: section in your project configuration file."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/plugins/gcov/setup.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/gcov/setup/#disabling-automatic-coverage-summaries"
license: "MIT"
mode: "V"
---

To disable the coverage summaries generated immediately following `gcov:` tasks,
simply add the following to a top-level `:gcov:` section in your project
configuration file.

```yaml
:plugins:
  :enabled:
    - gcov

:gcov:
  :summaries: FALSE
```
