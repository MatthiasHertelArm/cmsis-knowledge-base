---
id: "ceed-set-up-configuration-toolchain-dependencies"
type: "concept"
domain: "test"
title: "Set up & Configuration: Toolchain dependencies"
summary: "This plugin relies on the GNU compiler collection. Coverage instrumentation is enabled through gcc compiler flags. Coverage-insrumented executables (i.e. test suites) output coverage result files to disk when run."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/plugins/gcov/setup.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/gcov/setup/#toolchain-dependencies"
license: "MIT"
mode: "V"
---

### GNU Compiler Collection

This plugin relies on the GNU compiler collection. Coverage instrumentation
is enabled through `gcc` compiler flags. Coverage-insrumented executables 
(i.e. test suites) output coverage result files to disk when run. `gcov`,
`gcovr`, and `reportgenerator` (the tools managed by this plugin) all produce
their coverage tallies from these files. `gcov` is part of the GNU compiler
collection. The other tools — detailed below — require separate installation.

Ceedling’s default toolchain is the same as needed by this plugin. If you
are already running Ceedling test suites with the GNU compiler toolchain, 
you are good to go. If you are using another toolchain for test suite and/or
release builds you will need to install the GNU compiler collection to use
this plugin. Depending on your needs you may also need to install the reporting
utilities, `gcovr` and/or `reportgenerator`.

### `gcovr` and `reportgenerator`’s dependence on `gcov`

Both the `gcovr` and `reportgenerator` tools depend on the `gcov` tool. This
dependency plays out in two different ways. In both cases, the report
generation utilities ingest `gcov`’s output to produce their artifacts. As
such, `gcov` must be available in your environment if using report generation.

1. `gcovr` calls `gcov` directly.

    Because it calls `gcov` directly, you are limited as to the
    advanced Ceedling features you can employ to modify `gcov`’s execution.
    However, with a configuration option (see below) you can instruct `gcovr`
    to call something other than `gcov` (e.g. a script that intercepts and
    modifies how `gcovr` calls out to `gcov`).

    `gcovr` instructs `gcov` to generate `.gcov` files that it processes and
    discards. A `gcovr` option documented below will retain the `.gcov` files.

2. `reportgenerator` expects the existence of `.gcov` files to do its work.

    This Ceedling plugin calls `gcov` appropriately to generate the `.gcov` 
    files `reportgenerator` needs before then calling the report utility. 

    You can use Ceedling’s features to modify how `gcov` is run before 
    `reportgenerator`.
