---
id: "ceed-set-up-configuration-enable-this-plugin"
type: "concept"
domain: "test"
title: "Set up & Configuration: Enable this plugin"
summary: "To use this plugin it must be enabled in your Ceedling project file:"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/plugins/gcov/setup.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/gcov/setup/#enable-this-plugin"
license: "MIT"
mode: "V"
---

To use this plugin it must be enabled in your Ceedling project file:

```yaml
:plugins:
  :enabled:
    - gcov
```

This simple configuration will create new `gcov:` command line tasks to run 
tests with source coverage and output simple coverage summaries to the console 
as above.
