---
id: "zep-additional-zephyr-extension-comman-working-with-the-zephyr-sdk-west-sdk"
type: "concept"
domain: "project"
title: "Additional Zephyr extension commands: Working with the Zephyr SDK: `west sdk`"
summary: "The west sdk command is a Zephyr-specific west command used to list and install the Zephyr SDK and its toolchains."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/west/zephyr-cmds.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/west/zephyr-cmds.rst"
license: "Apache-2.0"
mode: "V"
---

The `west sdk` command is a Zephyr-specific west command used to list
and install the Zephyr SDK and its toolchains.


### Listing SDKs and toolchains


To list installed Zephyr SDKs as well as available SDK releases and
toolchains, run:

```console

west sdk list
```
This command shows:

- Installed SDK versions
- Available SDK releases
- Toolchains included in each SDK


### Installing the Zephyr SDK


To install the Zephyr SDK, run:

```console

west sdk install
```
This command may run in interactive mode and prompt for SDK or
toolchain selection. When specific toolchains are provided via
`--toolchains`, the command runs non-interactively, which is
recommended for automation.

To install specific toolchains only, use the `--toolchains` option:

```console

west sdk install --toolchains arm-zephyr-eabi riscv64-zephyr-elf
```
If you are unsure which toolchains you need, run `west sdk list` first
to see the available options and avoid downloading unnecessary
toolchains, which can save gigabytes of disk space and download time.
