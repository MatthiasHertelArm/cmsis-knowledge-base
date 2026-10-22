---
id: "ceed-mixins-built-in-toolchain-targets"
type: "concept"
domain: "test"
title: "Mixins: Built-in toolchain targets"
summary: "Ceedling bundles a set of ready-made toolchain target mixins sourced from Unity's targets/ folder. Each file configures the compiler, linker, output extensions, and Unity-specific compilation symbols for a particular toolchain or target environment."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/configuration/mixins.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/mixins/#built-in-toolchain-targets"
license: "MIT"
mode: "V"
---

Ceedling bundles a set of ready-made toolchain target mixins sourced from
Unity's `targets/` folder. Each file configures the compiler, linker,
output extensions, and Unity-specific compilation symbols for a particular
toolchain or target environment.

Because the Unity targets folder is a default mixin load path (searched
after the project directory), you can activate any of these by name
alone — no `:load_paths` configuration required:

```sh
ceedling build test:all --mixin clang
```

Or via the project configuration:

```yaml
:mixins:
  :enabled:
    - clang
```

### Available built-in targets

| Mixin name      | Toolchain / target |
|-----------------|--------------------|
| `clang`         | Clang local host configuration with common warnings and errors enabled   |
| `gcc`           | GCC local host configuration with common warnings and errors enabled     |
| `hitech_picc18` | HI-TECH PICC-18 (PIC18)                                                  |
| `iar_arm`       | IAR ARM configuration that likely requires customization for your target |

### Using a built-in target as a starting point

A built-in target mixin sets only the toolchain-specific knobs. Your
project configuration (or other mixins) supplies everything else —
source paths, plugins, test file patterns, and so on. This means you
can use a built-in target as a drop-in starting point and layer your
own settings on top without duplicating the full tool configuration.

For example, a minimal project targeting a GCC host build might
look like:

```yaml
# project.yml
:project:
  :build_root: build/

:paths:
  :test:
    - test/**
  :source:
    - src/**

:plugins:
  :enabled:
    - report_tests_pretty_stdout

:mixins:
  :enabled:
    - gcc   # Pulls in compiler, linker, and Unity symbol config for GCC
```

If your project needs a tweak — say, an extra compiler flag or a different
optimization level — merge an additional mixin after the built-in target:

```sh
ceedling build test:all --mixin clang --mixin "=tools: {test_compiler: {arguments: ['-O0']}}"
```

Because command line mixins are merged last, the extra argument is appended
after the built-in target's argument list and takes effect.

!!! tip "Override a built-in target for a single project"
    Drop a YAML file with the same name as a built-in target (e.g.
    `gcc.yml`) into your project directory. Ceedling searches the
    project directory before the built-in targets folder, so your local
    file silently takes precedence — no `:load_paths` entry required.
