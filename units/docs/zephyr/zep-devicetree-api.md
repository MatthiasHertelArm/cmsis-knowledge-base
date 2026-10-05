---
id: "zep-devicetree-api"
type: "concept"
domain: "project"
title: "Devicetree API"
summary: "This is a reference page for the <zephyr/devicetree.h> API. The API is macro based. Use of these macros has no impact on scheduling. They can be used from any calling context and at file scope."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/build/dts/api/api.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/build/dts/api/api.rst"
license: "Apache-2.0"
mode: "V"
---

This is a reference page for the `<zephyr/devicetree.h>` API. The API is macro
based. Use of these macros has no impact on scheduling. They can be used from
any calling context and at file scope.

Some of these -- the ones beginning with `DT_INST_` -- require a special
macro named `DT_DRV_COMPAT` to be defined before they can be used; these are
discussed individually below. These macros are generally meant for use within
device drivers, though they can be used outside of
drivers with appropriate care.
