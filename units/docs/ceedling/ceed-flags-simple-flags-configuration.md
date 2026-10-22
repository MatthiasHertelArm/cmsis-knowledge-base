---
id: "ceed-flags-simple-flags-configuration"
type: "concept"
domain: "test"
title: "`:flags`: Simple `:flags` configuration"
summary: "A simple and common need is enforcing a particular C standard. The following example illustrates simple YAML lists for flags."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/configuration/reference/flags.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/flags/#simple-flags-configuration"
license: "MIT"
mode: "V"
---

A simple and common need is enforcing a particular C standard. The following
example illustrates simple YAML lists for flags.

```yaml
:flags:
  :release:
    :compile:
      # Add `-std=c99` to compilation of all C files in the release build
      - -std=c99
  :test:
    :compile:
      # Add `-std=c99` to the compilation of all C files in all test executables
      - -std=c99
```

Given the YAML above, when test or release compilation occurs, the flag
specifying the C standard will be in the command line for compilation of all C
files.
