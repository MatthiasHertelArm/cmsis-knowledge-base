---
id: "zep-west-aliases-examples"
type: "concept"
domain: "project"
title: "West aliases: Examples"
summary: "Add west run and west menuconfig shortcuts to your global configuration to call west build with the corresponding CMake targets:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/west/alias.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/west/alias.rst"
license: "Apache-2.0"
mode: "V"
---

Add `west run` and `west menuconfig` shortcuts to your global configuration to
call `west build` with the corresponding CMake targets:

```shell

west config --global alias.run "build --pristine=never --target run"
west config --global alias.menuconfig "build --pristine=never --target menuconfig"
```
Create an alias for the sample you are actively developing with additional options:

```shell

west config alias.sample "build -b native_sim samples/hello_world -t run -- -DCONFIG_ASSERT=y"
```
Override `west update` to check a local cache:

```shell

west config alias.update "update --path-cache $HOME/.cache/zephyrproject"
```
Automatically exclude the 32-bit native simulator target when running :ref:`Twister
<twister_script>` via west. This is especially useful when running on hosts systems without a 32-bit
host C library (i.e. Linux/AArch64):

```shell

west config alias.twister "twister --exclude-platform native_sim/native"
```
