---
id: "zep-building-flashing-and-debugging-sysbuild-multi-domain-builds"
type: "concept"
domain: "project"
title: "Building, Flashing and Debugging: Building: `west build` / Sysbuild (multi-domain builds)"
summary: "sysbuild can be used to create a multi-domain build system combining multiple images for a single or multiple boards."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/west/build-flash-debug.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/west/build-flash-debug.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: Building: `west build`_

sysbuild can be used to create a multi-domain build system combining
multiple images for a single or multiple boards.

Use `--sysbuild` to select the sysbuild build infrastructure with
`west build` to build multiple domains.

More detailed information regarding the use of sysbuild can be found in the
sysbuild guide.


**Tip:** The `build.sysbuild` configuration option can be enabled to tell `west build` to default build using sysbuild. `--no-sysbuild` can be used to disable sysbuild for a specific build.

`west build` will build all domains through the top-level build folder of the
domains specified by sysbuild.

A single domain from a multi-domain project can be built by using `--domain`
argument.
