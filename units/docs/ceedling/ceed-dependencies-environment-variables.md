---
id: "ceed-dependencies-environment-variables"
type: "concept"
domain: "test"
title: "Dependencies: Environment variables"
summary: "Many build systems take settings from environment variables. A dependency’s :environment sets variables while that dependency’s fetch and build commands run, then restores them, so they never reach another dependency or Ceedling itself."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/plugins/dependencies.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/dependencies/#environment-variables"
license: "MIT"
mode: "V"
---

Many build systems take settings from environment variables. A dependency’s
`:environment` sets variables while that dependency’s fetch and build commands run, then
restores them, so they never reach another dependency or Ceedling itself.

Ceedling’s project configuration also has a top-level `:environment` section, which
applies to all of Ceedling. The two sections differ in format and abilities.

Each entry sets a variable, adds to it, or removes from it:

```yaml
:dependencies:
  :deps:
    - :name: Engine
      :environment:
        - ARCHITECTURE=ARM9
        - CFLAGS+= -DADD_AWESOMENESS
        - CFLAGS-= -DWASTE
```

`ARCHITECTURE=ARM9` sets `ARCHITECTURE` to `ARM9`. `+=` appends to a variable, here
adding ` -DADD_AWESOMENESS` to `CFLAGS`, and `-=` removes text from it, here removing
` -DWASTE`. An entry in any other form stops the build with an error.

When appending, Ceedling cannot know which delimiter you expect, so include it yourself:
a space for compiler flags, or `:` (`;` on Windows) for `PATH`. Text after `+=` and `-=`
is used exactly as written, leading space included, while a value after `=` loses its
leading spaces. Removing text is case
sensitive and removes only an exact match. Appending to or removing from a variable that
is not set leaves it set, empty if nothing was appended.
