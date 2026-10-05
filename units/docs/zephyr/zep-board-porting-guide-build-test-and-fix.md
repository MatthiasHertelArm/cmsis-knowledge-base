---
id: "zep-board-porting-guide-build-test-and-fix"
type: "concept"
domain: "bring-up"
title: "Board Porting Guide: Build, test, and fix"
summary: "Now it's time to build and test the application(s) you want to run on your board until you're satisfied."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/hardware/porting/board_porting.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/hardware/porting/board_porting.rst"
license: "Apache-2.0"
mode: "V"
---

Now it's time to build and test the application(s) you want to run on your
board until you're satisfied.

For example:

```console

west build -b plank samples/hello_world
west flash
```
For `west flash` to work, see flash-and-debug-support below. You can
also just flash `build/zephyr/zephyr.elf`, `zephyr.hex`, or
`zephyr.bin` with any other tools you prefer.

Before submitting a board upstream, verify that every board target you add can
pass the project's minimum open source test suite using only code from the
mainline Zephyr repository and its modules. The suite currently consists of:

- `samples/philosophers`
- `tests/kernel`

For example, build the suite for a board target with:

```console

west twister -p plank -T samples/philosophers -T tests/kernel
```
For boards with multiple SoCs, CPU clusters, variants, or revisions, repeat the
test suite for each new board target. A hello_world build
is also recommended as a quick smoke check, for example:

```console

west build -p always -b plank/soc1/foo samples/hello_world
west build -p always -b plank@1.0.0/soc1/foo samples/hello_world
```
Use sysbuild if the board target requires it. When using board testing
metadata, such as `testing: only_tags` in the board target YAML file, make
sure the target is still validated against the minimum test suite in local
testing or CI.
