---
id: "zep-signing-binaries"
type: "concept"
domain: "project"
title: "Signing Binaries"
summary: "The west sign extension command can be used to sign a Zephyr application binary for consumption by a bootloader using an external tool."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/west/sign.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/west/sign.rst"
license: "Apache-2.0"
mode: "V"
---

The `west sign` extension command can be used to
sign a Zephyr application binary for consumption by a bootloader using an
external tool. In some configurations, `west sign` is also used to invoke
an external, post-processing tool that "stitches" the final components of
the image together. Run `west sign -h` for command line help.
