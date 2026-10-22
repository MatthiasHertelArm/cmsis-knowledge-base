---
id: "zep-devicetree-howtos-write-device-drivers-using-devicetree-ap"
type: "concept"
domain: "project"
title: "Devicetree HOWTOs: Write device drivers using devicetree APIs"
summary: "\"Devicetree-aware\" device drivers should create a struct device for each status = \"okay\" devicetree node with a particular compatible (or related set of compatibles) supported by the driver."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/build/dts/howtos.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/build/dts/howtos.rst"
license: "Apache-2.0"
mode: "V"
---

"Devicetree-aware" device drivers should create a
`struct device` for each `status = "okay"` devicetree node with a
particular compatible (or related set of
compatibles) supported by the driver.

Writing a devicetree-aware driver begins by defining a :ref:`devicetree binding
<dt-bindings>` for the devices supported by the driver. Use existing bindings
from similar drivers as a starting point. A skeletal binding to get started
needs nothing more than this:

```yaml

description: <Human-readable description of your binding>
compatible: "foo-company,bar-device"
include: base.yaml
```
See dts-find-binding for more advice on locating existing bindings.

After writing your binding, your driver C file can then use the devicetree API
to find `status = "okay"` nodes with the desired compatible, and instantiate
a `struct device` for each one. There are two options for instantiating each
`struct device`: using instance numbers, and using node labels.

In either case:

- Each `struct device`\ 's name should be set to its devicetree node's
  `label` property. This allows the driver's users to dt-get-device in
  the usual way.

- Each device's initial configuration should use values from devicetree
  properties whenever practical. This allows users to configure the driver
  using devicetree overlays.

Examples for how to do this follow. They assume you've already implemented the
device-specific configuration and data structures and API functions, like this:

```c

/* my_driver.c */
#include <zephyr/drivers/some_api.h>

/* Define data (RAM) and configuration (ROM) structures: */
struct my_dev_data {
    /* per-device values to store in RAM */
};
struct my_dev_cfg {
    uint32_t freq; /* Just an example: initial clock frequency in Hz */
    /* other configuration to store in ROM */
};

/* Implement driver API functions (drivers/some_api.h callbacks): */
static int my_driver_api_func1(const struct device *dev, uint32_t *foo) { /* ... */ }
static int my_driver_api_func2(const struct device *dev, uint64_t bar) { /* ... */ }
static struct some_api my_api_funcs = {
    .func1 = my_driver_api_func1,
    .func2 = my_driver_api_func2,
};
```

### Option 1: create devices using instance numbers


Use this option, which uses devicetree-inst-apis, if possible. However,
they only work when devicetree nodes for your driver's `compatible` are all
equivalent, and you do not need to be able to distinguish between them.

To use instance-based APIs, begin by defining `DT_DRV_COMPAT` to the
lowercase-and-underscores version of the compatible that the device driver
supports. For example, if your driver's compatible is `"vnd,my-device"` in
devicetree, you would define `DT_DRV_COMPAT` to `vnd_my_device` in your
driver C file:

```c

/*
 * Put this near the top of the file. After the includes is a good place.
 * (Note that you can therefore run "git grep DT_DRV_COMPAT drivers" in
 * the zephyr Git repository to look for example drivers using this style).
 */
#define DT_DRV_COMPAT vnd_my_device
```

**Important:** As shown, the DT_DRV_COMPAT macro should have neither quotes nor special characters. Remove quotes and convert special characters to underscores when creating `DT_DRV_COMPAT` from the compatible property.

Finally, define an instantiation macro, which creates each `struct device`
using instance numbers. Do this after defining `my_api_funcs`.

```c

/*
 * This instantiation macro is named "CREATE_MY_DEVICE".
 * Its "inst" argument is an arbitrary instance number.
 *
 * Put this near the end of the file, e.g. after defining "my_api_funcs".
 */
#define CREATE_MY_DEVICE(inst)                    \
    static struct my_dev_data my_data_##inst = {            \
        /* initialize RAM values as needed, e.g.: */        \
        .freq = DT_INST_PROP(inst, clock_frequency),        \
    };                                \
    static const struct my_dev_cfg my_cfg_##inst = {        \
        /* initialize ROM values as needed. */            \
    };                                \
    DEVICE_DT_INST_DEFINE(inst,                    \
                  my_dev_init_function,            \
               NULL,                         \
                  &my_data_##inst,                \
                  &my_cfg_##inst,                \
                  MY_DEV_INIT_LEVEL, MY_DEV_INIT_PRIORITY,    \
                  &my_api_funcs);
```
Notice the use of APIs like `DT_INST_PROP` and
`DEVICE_DT_INST_DEFINE` to access devicetree node data. These
APIs retrieve data from the devicetree for instance number `inst` of
the node with compatible determined by `DT_DRV_COMPAT`.

Finally, pass the instantiation macro to `DT_INST_FOREACH_STATUS_OKAY`:

```c

/* Call the device creation macro for each instance: */
DT_INST_FOREACH_STATUS_OKAY(CREATE_MY_DEVICE)
```
`DT_INST_FOREACH_STATUS_OKAY` expands to code which calls
`CREATE_MY_DEVICE` once for each enabled node with the compatible determined
by `DT_DRV_COMPAT`. It does not append a semicolon to the end of the
expansion of `CREATE_MY_DEVICE`, so the macro's expansion must end in a
semicolon or function definition to support multiple devices.


### Option 2: create devices using node labels


Some device drivers cannot use instance numbers. One example is an SoC
peripheral driver which relies on vendor HAL APIs specialized for individual IP
blocks to implement Zephyr driver callbacks. Cases like this should use
`DT_NODELABEL` to refer to individual nodes in the devicetree
representing the supported peripherals on the SoC. The devicetree.h
devicetree-generic-apis can then be used to access node data.

For this to work, your SoC's dtsi file must define node
labels like `mydevice0`, `mydevice1`, etc. appropriately for the IP blocks
your driver supports. The resulting devicetree usually looks something like
this:

```devicetree

/ {
        soc {
                mydevice0: dev@0 {
                        compatible = "vnd,my-device";
                };
                mydevice1: dev@1 {
                        compatible = "vnd,my-device";
                };
        };
};
```
The driver can use the `mydevice0` and `mydevice1` node labels in the
devicetree to operate on specific device nodes:

```c

/*
 * This is a convenience macro for creating a node identifier for
 * the relevant devices. An example use is MYDEV(0) to refer to
 * the node with label "mydevice0".
 */
#define MYDEV(idx) DT_NODELABEL(mydevice ## idx)

/*
 * Define your instantiation macro; "idx" is a number like 0 for mydevice0
 * or 1 for mydevice1. It uses MYDEV() to create the node label from the
 * index.
 */
#define CREATE_MY_DEVICE(idx)                    \
 static struct my_dev_data my_data_##idx = {            \
     /* initialize RAM values as needed, e.g.: */        \
     .freq = DT_PROP(MYDEV(idx), clock_frequency),        \
 };                                \
 static const struct my_dev_cfg my_cfg_##idx = { /* ... */ };    \
    DEVICE_DT_DEFINE(MYDEV(idx),                    \
            my_dev_init_function,                \
         NULL,                           \
         &my_data_##idx,                    \
         &my_cfg_##idx,                    \
         MY_DEV_INIT_LEVEL, MY_DEV_INIT_PRIORITY,    \
         &my_api_funcs)
```
Notice the use of APIs like `DT_PROP` and
`DEVICE_DT_DEFINE` to access devicetree node data.

Finally, manually detect each enabled devicetree node and use
`CREATE_MY_DEVICE` to instantiate each `struct device`:

```c

#if DT_NODE_HAS_STATUS(DT_NODELABEL(mydevice0), okay)
CREATE_MY_DEVICE(0)
#endif

#if DT_NODE_HAS_STATUS(DT_NODELABEL(mydevice1), okay)
CREATE_MY_DEVICE(1)
#endif
```
Since this style does not use `DT_INST_FOREACH_STATUS_OKAY()`, the driver
author is responsible for calling `CREATE_MY_DEVICE()` for every possible
node, e.g. using knowledge about the peripherals available on supported SoCs.
