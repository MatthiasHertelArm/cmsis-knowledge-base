---
id: "ceed-bullseye-plugin-overview"
type: "concept"
domain: "test"
title: "Bullseye: Plugin overview"
summary: "A bullseye: task compiles and links test executables with Bullseye instrumentation, runs them, and accumulates coverage data. All coverage data lands in a single coverage data file. Reports are generated from that file."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/plugins/bullseye/index.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/bullseye/#plugin-overview"
license: "MIT"
mode: "V"
---

A `bullseye:` task compiles and links test executables with Bullseye
instrumentation, runs them, and accumulates coverage data. All coverage data
lands in a single coverage data file. Reports are generated from that file.

Every `test:` task has a `bullseye:` counterpart.

```shell
 > ceedling bullseye:all
 > ceedling bullseye:Model
 > ceedling bullseye:pattern[Model*]
 > ceedling bullseye:path[controllers]
```

### Coverage metric

Bullseye measures two things. Function coverage records whether each function
was invoked at all. Condition/decision coverage is a hybrid metric. It records
whether each branch condition evaluated both true and false. It also records
whether each individual boolean operand did the same.

This plugin labels condition/decision coverage as BRANCHES in its console
output.

Bullseye's own site offers a [conceptual overview of code coverage][bullseye-coverage].
It includes suggested incremental coverage goals.

### The coverage data file

Coverage data accumulates in `test.cov` at your project root. Every
instrumented test executable writes to it. Every reporting tool reads from it.

This file lives at your project root rather than under `build/` for a specific
reason. Bullseye records each source path relative to the coverage data file's
own location. Report exclusions match against that stored path. Your project
root is the only common ancestor of every source location a project can have.
Those locations include `src/`, `test/`, vendored framework sources, and
generated test runners. Bullseye
[recommends this placement][bullseye-coverage-file] for the same reason.

Coverage data accumulates across runs. Use `ceedling clean` or
`ceedling clobber` to discard it and start fresh.

### Supported tool versions

This plugin is verified against Bullseye Coverage 9.25.9 on Linux x64. It
relies on command-line conventions that have been stable across Bullseye's
release history and across platforms.
