---
id: "zep-shields-shield-activation"
type: "concept"
domain: "bring-up"
title: "Shields: Shield activation"
summary: "Activate support for one or more shields by adding the matching --shield arguments to the west command:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/hardware/porting/shields.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/hardware/porting/shields.rst"
license: "Apache-2.0"
mode: "V"
---

Activate support for one or more shields by adding the matching `--shield` arguments
to the west command:

Alternatively, it could be set by default in a project's CMakeLists.txt:

```cmake

set(SHIELD x_nucleo_iks01a1)
```
