---
id: "zep-device-driver-model-error-handling"
type: "concept"
domain: "rtos"
title: "Device Driver Model: Error handling"
summary: "In general, it's best to use _ASSERT() macros instead of propagating return values unless the failure is expected to occur during the normal course of operation (such as a storage device full)."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/drivers/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/drivers/index.rst"
license: "Apache-2.0"
mode: "V"
---

In general, it's best to use `__ASSERT()` macros instead of
propagating return values unless the failure is expected to occur
during the normal course of operation (such as a storage device
full). Bad parameters, programming errors, consistency checks,
pathological/unrecoverable failures, etc., should be handled by
assertions.

When it is appropriate to return error conditions for the caller to
check, 0 should be returned on success and a POSIX `errno.h` code
returned on failure.  See
https://github.com/zephyrproject-rtos/zephyr/wiki/Naming-Conventions#return-codes
for details about this.
