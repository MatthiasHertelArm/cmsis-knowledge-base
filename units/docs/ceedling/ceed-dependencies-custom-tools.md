---
id: "ceed-dependencies-custom-tools"
type: "concept"
domain: "test"
title: "Dependencies: Custom Tools"
summary: "You can optionally specify a compiler, assembler, and linker, just as you would a release build:"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/plugins/dependencies.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/dependencies/#custom-tools"
license: "MIT"
mode: "V"
---

You can optionally specify a compiler, assembler, and linker, just as you would a release build:

```yaml
:tools:
  :deps_compiler:
    :executable: gcc
    :arguments:
      - -g
      - -I"$": COLLECTION_PATHS_SUBPROJECTS
      - -D$: COLLECTION_DEFINES_SUBPROJECTS
      - -c "${1}"
      - -o "${2}"
  :deps_linker:
    :executable: ar
    :arguments:
      - rcs
      - ${2}
      - ${1}
```

Then, once created, you can reference these tools in your build steps by using the `:build_lib` symbol instead
of a series of strings to explain all the steps. Ceedling will understand that it should build all the specified
source and/or assembly files into the specified library:

```yaml
:dependencies:
  :deps:
    - :name: CaptainCrunch
      :paths:
        :fetch:    ../cc/
        :source:   ../cc/
        :build:    ../cc/build
        :artifact: ../cc/build
      :fetch:
        :method: :none
      :environment: []
      :build:
        - :build_lib
      :artifacts:
        :static_libraries:
          - release/cc.a
        :dynamic_libraries: []
        :includes: 
          - ./cc.h
      :defines:
        - THESE_GET_USED_DURING_COMPILATION
```
