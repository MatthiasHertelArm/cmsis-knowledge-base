---
id: "zep-devicetree-access-from-c-c-device-driver-conveniences"
type: "concept"
domain: "project"
title: "Devicetree access from C/C++: Device driver conveniences"
summary: "Special purpose macros are available for writing device drivers, which usually rely on instance identifiers."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/build/dts/api-usage.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/build/dts/api-usage.rst"
license: "Apache-2.0"
mode: "V"
---

Special purpose macros are available for writing device drivers, which usually
rely on instance identifiers.

To use these, you must define `DT_DRV_COMPAT` to the `compat` value your
driver implements support for. This `compat` value is what you would pass to
`DT_INST`.

If you do that, you can access the properties of individual instances of your
compatible with less typing, like this:

```c

#include <zephyr/devicetree.h>

#define DT_DRV_COMPAT my_driver_compat

/* This is same thing as DT_INST(0, my_driver_compat): */
DT_DRV_INST(0)

/*
 * This is the same thing as
 * DT_PROP(DT_INST(0, my_driver_compat), clock_frequency)
 */
DT_INST_PROP(0, clock_frequency)
```
See devicetree-inst-apis for a generic API reference.
