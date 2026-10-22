---
id: "ceed-defines-simple-defines-configuration"
type: "concept"
domain: "test"
title: "`:defines`: Simple `:defines` configuration"
summary: "A simple and common need is configuring conditionally compiled features in a code base. The following example illustrates using simple YAML lists for symbol definitions at compile time."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/configuration/reference/defines.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/defines/#simple-defines-configuration"
license: "MIT"
mode: "V"
---

A simple and common need is configuring conditionally compiled features in a
code base. The following example illustrates using simple YAML lists for symbol
definitions at compile time.

```yaml
:defines:
  :test:     # All compilation of all C files for all test executables
    - FEATURE_X=ON
    - PRODUCT_CONFIG_C
  :release:  # All compilation of all C files in a release artifact
    - FEATURE_X=ON
    - PRODUCT_CONFIG_C
```

Given the YAML blurb above, the two symbols will be defined in the compilation
command lines for all C files in all test executables within a test suite build
and for all C files in a release build.
