---
id: "zep-additional-zephyr-extension-comman-working-with-binary-descriptors-west-bin"
type: "concept"
domain: "project"
title: "Additional Zephyr extension commands: Working with binary descriptors: `west bindesc`"
summary: "The bindesc command allows users to read binary descriptors of executable files. It currently supports .bin, .hex, .elf and .uf2 files as input."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/west/zephyr-cmds.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/west/zephyr-cmds.rst"
license: "Apache-2.0"
mode: "V"
---

The `bindesc` command allows users to read binary descriptors
of executable files. It currently supports `.bin`, `.hex`, `.elf` and `.uf2` files
as input.

You can search for a specific descriptor in an image, for example::
```
west bindesc search KERNEL_VERSION_STRING build/zephyr/zephyr.bin
```
You can search for a custom descriptor by type and ID, for example::
```
west bindesc custom_search STR 0x200 build/zephyr/zephyr.bin
```
You can dump all of the descriptors in an image using::
```
west bindesc dump build/zephyr/zephyr.bin
```
You can extract the descriptor data area of the image to a file using::
```
west bindesc extract
```
You can list all known standard descriptor names using::
```
west bindesc list
```
You can print the offset of the descriptors inside the image using::
```
west bindesc get_offset
```
