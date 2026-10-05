---
id: "zep-device-driver-model-driver-data-structures"
type: "concept"
domain: "rtos"
title: "Device Driver Model: Driver Data Structures"
summary: "The device initialization macros populate some data structures at build time which are split into read-only and runtime-mutable parts. At a high level we have:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/drivers/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/drivers/index.rst"
license: "Apache-2.0"
mode: "V"
---

The device initialization macros populate some data structures at build time
which are
split into read-only and runtime-mutable parts. At a high level we have:

```C

struct device {
  const char *name;
  const void *config;
  const void *api;
  void * const data;
};
```
The `config` member is for read-only configuration data set at build time. For
example, base memory mapped IO addresses, IRQ line numbers, or other fixed
physical characteristics of the device. This is the `config` pointer
passed to `DEVICE_DEFINE()` and related macros.

The `data` struct is kept in RAM, and is used by the driver for
per-instance runtime housekeeping. For example, it may contain reference counts,
semaphores, scratch buffers, etc.

The `api` struct maps generic subsystem APIs to the device-specific
implementations in the driver. It is typically read-only and populated at
build time. The next section describes this in more detail.
