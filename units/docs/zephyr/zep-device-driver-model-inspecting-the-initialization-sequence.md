---
id: "zep-device-driver-model-inspecting-the-initialization-sequence"
type: "concept"
domain: "rtos"
title: "Device Driver Model: Inspecting the initialization sequence"
summary: "Device drivers declared with DEVICE_DEFINE (or any variations of it) and SYS_INIT are processed at boot time and the corresponding initialization functions are called sequentially according to their specified level and priority."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/drivers/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/drivers/index.rst"
license: "Apache-2.0"
mode: "V"
---

Device drivers declared with `DEVICE_DEFINE` (or any variations of it)
and `SYS_INIT` are processed at boot time and the corresponding
initialization functions are called sequentially according to their specified
level and priority.

Sometimes it's useful to inspect the final sequence of initialization function
call as produced by the linker. To do that, use the `initlevels` CMake
target, for example `west build -t initlevels`.
