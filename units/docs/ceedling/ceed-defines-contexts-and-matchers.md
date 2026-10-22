---
id: "ceed-defines-contexts-and-matchers"
type: "concept"
domain: "test"
title: "`:defines`: Contexts and Matchers"
summary: "The basic layout of :defines involves the concept of contexts."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/configuration/reference/defines.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/defines/#contexts-and-matchers"
license: "MIT"
mode: "V"
---

The basic layout of `:defines` involves the concept of contexts.

General case:
```yaml
:defines:
  :<context>:   # :test, :release, etc.
    - <symbol>  # Simple list of symbols added to all compilation
    - ...
```

Advanced matching for **_test_** or **_preprocess_** build handling only:
```yaml
:defines:
  :test:
    :<matcher>   # Matches a subset of test executables
      - <symbol> # List of symbols added to that subset’s compilation
      - ...
  :preprocess:   # Only applicable if :project ↳ :use_test_preprocessor enabled
    :<matcher>   # Matches a subset of test executables
      - <symbol> # List of symbols added to that subset’s compilation
      - ...
```

A context is the build context you want to modify — `:release`, `:preprocess`,
or `:test`. Plugins can also hook into `:defines` with their own context.

You specify the symbols you want to add to a build step beneath a `:<context>`.
In many cases this is a simple YAML list of strings that will become symbols
defined in a compiler’s command line.

Specifically in the `:test` and `:preprocess` contexts you also have the option
to create test file matchers that create symbol definitions for some subset of
your build.
