---
id: "zep-troubleshooting-devicetree-errors-with-dt-inst-apis"
type: "concept"
domain: "project"
title: "Troubleshooting devicetree: Errors with DT_INST_() APIs"
summary: "If you're using an API like DT_INST_PROP, you must define DT_DRV_COMPAT to the lowercase-and-underscores version of the compatible you are interested in. See dt-create-devices-inst."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/build/dts/troubleshooting.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/build/dts/troubleshooting.rst"
license: "Apache-2.0"
mode: "V"
---

If you're using an API like `DT_INST_PROP`, you must define
`DT_DRV_COMPAT` to the lowercase-and-underscores version of the compatible
you are interested in. See dt-create-devices-inst.
