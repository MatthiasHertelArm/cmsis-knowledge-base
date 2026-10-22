---
id: "ceed-bullseye-additional-tasks"
type: "concept"
domain: "test"
title: "Bullseye: Additional tasks"
summary: "The bullseye:browser task opens Bullseye's graphical Coverage Browser against your project's coverage data file."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/plugins/bullseye/index.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/bullseye/#additional-tasks"
license: "MIT"
mode: "V"
---

### Coverage Browser

The `bullseye:browser` task opens Bullseye's graphical Coverage Browser
against your project's coverage data file.

```shell
 > ceedling bullseye:browser
```

### License status

The `bullseye:license` task reports your Bullseye license number, its expiry
date, and license manager utilization.

```shell
 > ceedling bullseye:license
```

See [Licensing](https://throwtheswitch.github.io/Ceedling/plugins/bullseye/licensing.md) for how to read its output.
