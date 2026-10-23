---
id: "zep-device-driver-model-system-drivers"
type: "concept"
domain: "rtos"
title: "Device Driver Model: System Drivers"
summary: "In some cases you may just need to run a function at boot. For such cases, the SYS_INIT can be used."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/drivers/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/drivers/index.rst"
license: "Apache-2.0"
mode: "V"
---

In some cases you may just need to run a function at boot. For such cases, the
`SYS_INIT` can be used. This macro does not take any config or runtime
data structures and there isn't a way to later get a device pointer by name. The
same device policies for initialization level and priority apply.
