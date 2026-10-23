---
id: "zep-troubleshooting-devicetree-do-not-track-macro-expansion"
type: "concept"
domain: "project"
title: "Troubleshooting devicetree: Do not track macro expansion"
summary: "Compiler messages for devicetree errors can sometimes be very long. This typically happens when the compiler prints a message for every step of a complex macro expansion that has several intermediate expansion steps."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/build/dts/troubleshooting.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/build/dts/troubleshooting.rst"
license: "Apache-2.0"
mode: "V"
---

Compiler messages for devicetree errors can sometimes be very long. This
typically happens when the compiler prints a message for every step of a
complex macro expansion that has several intermediate expansion steps.

To prevent the compiler from doing this, you can disable the
`CONFIG_COMPILER_TRACK_MACRO_EXPANSION` option. This typically
reduces the output to one message per error.

For example, to build hello_world with west and this option disabled,
use:

```sh

west build -b BOARD samples/hello_world -- -DCONFIG_COMPILER_TRACK_MACRO_EXPANSION=n
```
