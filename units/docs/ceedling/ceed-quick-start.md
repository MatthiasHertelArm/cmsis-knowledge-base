---
id: "ceed-quick-start"
type: "concept"
domain: "test"
title: "Quick Start"
summary: "For a test suite project using the default toolchain gcc, Ceedling’s configuration file could be as simple as this:"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/getting-started/quick-start.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/getting-started/quick-start/"
license: "MIT"
mode: "V"
---

For a test suite project using the default toolchain `gcc`, Ceedling’s
configuration file could be as simple as this:

```yaml
:project:
  :build_root: project/build/

:paths:
  :test:
    - tests/**
  :source:
    - source/**
  :include:
    - inc/**
```

To execute all your unit tests, you would run `ceedling test:all`.

---
