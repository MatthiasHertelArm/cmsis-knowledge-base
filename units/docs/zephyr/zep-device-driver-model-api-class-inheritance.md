---
id: "zep-device-driver-model-api-class-inheritance"
type: "concept"
domain: "rtos"
title: "Device Driver Model: API Class Inheritance"
summary: "A subsystem API can extend another subsystem API, forming a parent-child relationship. This allows a device implementing the child API to also be recognized as implementing the parent API."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/drivers/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/drivers/index.rst"
license: "Apache-2.0"
mode: "V"
---

A subsystem API can extend another subsystem API, forming a parent-child
relationship. This allows a device implementing the child API to also be
recognized as implementing the parent API. For example, an I3C controller
extends the I2C API, so it can be used wherever an I2C device is expected.

To define a child API, embed the parent API struct as the **first member** of
the child struct and declare the relationship with `DEVICE_API_EXTENDS`:

```C

__subsystem struct child_driver_api {
      struct subsystem_driver_api parent_api;
      child_do_extra_t do_extra;
};

DEVICE_API_EXTENDS(child, subsystem, parent_api);
```
A driver implementing the child API populates both the parent and child
methods:

```C

static DEVICE_API(child, my_child_api) = {
      .parent_api = {
              .do_this = my_child_do_this,
              .do_that = my_child_do_that,
      },
      .do_extra = my_child_do_extra,
};
```
With this in place, `DEVICE_API_IS` returns true for both the child
and parent classes, and `DEVICE_API_GET` can retrieve the API as
either type:

```C

/* Both return true for a child device */
DEVICE_API_IS(subsystem, dev);
DEVICE_API_IS(child, dev);

/* Access through parent API */
DEVICE_API_GET(subsystem, dev)->do_this(dev, foo, bar);
```
Multi-level inheritance is supported (e.g. grandchild extends child extends
parent). Sibling relationships also work correctly: two different child APIs
extending the same parent are distinguished by `DEVICE_API_IS`.
