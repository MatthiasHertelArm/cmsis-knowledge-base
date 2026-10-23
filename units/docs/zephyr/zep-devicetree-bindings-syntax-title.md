---
id: "zep-devicetree-bindings-syntax-title"
type: "concept"
domain: "project"
title: "Devicetree bindings syntax: Title"
summary: "An optional, short description of the bound device, typically the hardware model. It should typically be of the format \"Vendor Family Model\". If acronyms are used, they should be spelled out in parentheses."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/build/dts/bindings-syntax.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/build/dts/bindings-syntax.rst"
license: "Apache-2.0"
mode: "V"
---

An *optional*, short description of the bound device, typically the hardware model.
It should typically be of the format "Vendor Family Model". If acronyms are used,
they should be spelled out in parentheses. The naming should stay as close to the
vendor datasheet as possible.

Titles should not exceed 100 characters. The description field should be used
for longer descriptions. The words "binding", "schema" or "driver" should not
be used in the title, everything is a binding.

```YAML

title: Acme Foo UART (Universal Asynchronous Receiver/Transmitter)
```
