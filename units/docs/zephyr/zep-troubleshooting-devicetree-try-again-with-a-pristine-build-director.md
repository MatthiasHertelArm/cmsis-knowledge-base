---
id: "zep-troubleshooting-devicetree-try-again-with-a-pristine-build-director"
type: "concept"
domain: "project"
title: "Troubleshooting devicetree: Try again with a pristine build directory"
summary: "See west-building-pristine for examples, or just delete the build directory completely and retry."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/build/dts/troubleshooting.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/build/dts/troubleshooting.rst"
license: "Apache-2.0"
mode: "V"
---

**Important:** Try this first, before doing anything else.

See west-building-pristine for examples, or just delete the build
directory completely and retry.

This is general advice which is especially applicable to debugging devicetree
issues, because the outputs are created during the CMake configuration phase,
and are not always regenerated when one of their inputs changes.
