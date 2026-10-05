---
id: "vsi-hello-vsi-example-build"
type: "concept"
domain: "debug"
title: "Hello VSI example: Build"
summary: "Use the cbuild tool or an IDE to build the application project in csolution format (see the main README)."
status: "draft"
collection: "avh-vsi"
source: "Arm-Examples/AVH-VSI@b897fa6:hello_vsi/README.md"
doc_source: "https://github.com/Arm-Examples/AVH-VSI/blob/b897fa6/hello_vsi/README.md#build"
license: "Apache-2.0"
mode: "V"
---

Use the cbuild tool or an IDE to build the application project in csolution format (see the main [README](https://github.com/Arm-Examples/AVH-VSI/blob/b897fa6/hello_vsi/../README.md)).

The build context is contructed as flow type (such as `.event`) and target type (such as `+Corstone_315`). To compile with **AC6** use `--toolchain AC6` and for **GCC** the `--toolchain GCC` option with the cbuild command. For example:

To build the project for **Corstone-315** target with GCC compiler use:

```bash
cbuild hello_vsi.csolution.yml --packs --rebuild --toolchain GCC --context .event+Corstone_315
```

To build with the gated fetch flow for the **Corstone-310** target and Arm Compiler 6:

```bash
cbuild hello_vsi.csolution.yml --packs --rebuild --toolchain AC6 --context .gated+Corstone_310
```
