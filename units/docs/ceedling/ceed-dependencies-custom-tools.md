---
id: "ceed-dependencies-custom-tools"
type: "concept"
domain: "test"
title: "Dependencies: Custom tools"
summary: "The plugin’s tools are configured like any other Ceedling tool, and you can replace them under :tools:"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/plugins/dependencies.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/dependencies/#custom-tools"
license: "MIT"
mode: "V"
---

The plugin’s tools are configured like any other Ceedling tool, and you can replace them
under `:tools`:

| Tool | Default | Used for |
|---|---|---|
| `:deps_compiler` | `gcc` | `:build_lib` compiling |
| `:deps_assembler` | none | `:build_lib` assembling, needed only for assembly files |
| `:deps_linker` | `ar` | `:build_lib` archiving |
| `:deps_zip` | `unzip` | `:zip` fetching |
| `:deps_targzip` | `tar` | `:tar_gzip` fetching |
| `:deps_git_clone`, `:deps_git_checkout` | `git` | `:git` fetching |
| `:deps_subversion` | `svn` | `:svn` fetching |

The compiler, assembler, and archiver are checked just before `:build_lib` uses them, so
a project without `:build_lib` needs none of them.

`:build_lib` compiles every C file anywhere under the dependency’s `:source` path, with
every directory holding a header there as a search path. It then archives the objects
into the first library under `:artifacts` ↳ `:static_libraries`, built in the `:build`
path and copied to the `:artifact` path when the two differ. A dependency’s own
`:defines` and `:flags` apply to its compilation, and `:libraries` and `:libpaths` to its
archiving.

The compiler receives its search paths as `${5}` and its defines as `${6}`, as Ceedling’s
own compilers do:

```yaml
:tools:
  :deps_compiler:
    :executable: gcc
    :arguments:
      - -g
      - -I"${5}"
      - -D${6}
      - -c "${1}"
      - -o "${2}"
  :deps_linker:
    :executable: ar
    :arguments:
      - rcs
      - ${2}
      - ${1}
```

A dependency built with `:build_lib` looks like this:

```yaml
:dependencies:
  :deps:
    - :name: CaptainCrunch
      :paths:
        :source:   ../cc/
        :build:    ../cc/build
        :artifact: ../cc/build
      :fetch:
        :method: :none
      :build:
        - :build_lib
      :artifacts:
        :static_libraries:
          - release/cc.a
        :includes:
          - ./cc.h
      :defines:
        - THESE_GET_USED_DURING_COMPILATION
```
