---
id: "zep-device-driver-model-subsystems-and-api-structures"
type: "concept"
domain: "rtos"
title: "Device Driver Model: Subsystems and API Structures"
summary: "Most drivers will be implementing a device-independent subsystem API. Applications can simply program to that generic API, and application code is not specific to any particular driver implementation."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/drivers/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/drivers/index.rst"
license: "Apache-2.0"
mode: "V"
---

Most drivers will be implementing a device-independent subsystem API.
Applications can simply program to that generic API, and application
code is not specific to any particular driver implementation.

Driver API instances must be declared with `DEVICE_API()` so that they
are assigned to their respective API linker section. This is required for
`DEVICE_API_GET` and `DEVICE_API_IS` to validate at runtime
that a device's API belongs to the expected class.

A subsystem API definition typically looks like this:

```C

typedef int (*subsystem_do_this_t)(const struct device *dev, int foo, int bar);
typedef void (*subsystem_do_that_t)(const struct device *dev, void *baz);

__subsystem struct subsystem_driver_api {
      subsystem_do_this_t do_this;
      subsystem_do_that_t do_that;
};

static inline int subsystem_do_this(const struct device *dev, int foo, int bar)
{
      return DEVICE_API_GET(subsystem, dev)->do_this(dev, foo, bar);
}

static inline void subsystem_do_that(const struct device *dev, void *baz)
{
      DEVICE_API_GET(subsystem, dev)->do_that(dev, baz);
}
```
A driver implementing a particular subsystem will define the real implementation
of these APIs, and populate an instance of subsystem_driver_api structure using
the `DEVICE_API()` wrapper:

```C

static int my_driver_do_this(const struct device *dev, int foo, int bar)
{
      ...
}

static void my_driver_do_that(const struct device *dev, void *baz)
{
      ...
}

static DEVICE_API(subsystem, my_driver_api_funcs) = {
      .do_this = my_driver_do_this,
      .do_that = my_driver_do_that,
};
```
The driver would then pass `my_driver_api_funcs` as the `api` argument to
`DEVICE_DEFINE()`.


**Note:** Since pointers to the API functions are referenced in the `api` struct, they will always be included in the binary even if unused; `gc-sections` linker option will always see at least one reference to them. Providing for link-time size optimizations with driver APIs in most cases requires that the optional feature be controlled by a Kconfig option.
