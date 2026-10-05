---
id: "zep-troubleshooting-devicetree-check-for-missing-bindings"
type: "concept"
domain: "project"
title: "Troubleshooting devicetree: Check for missing bindings"
summary: "See dt-bindings for information about bindings, and devicetree_binding_index for information on bindings built into Zephyr."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/build/dts/troubleshooting.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/build/dts/troubleshooting.rst"
license: "Apache-2.0"
mode: "V"
---

See dt-bindings for information about bindings, and
devicetree_binding_index for information on bindings built into Zephyr.

If the build fails to dts-find-binding for a node, then either the
node's `compatible` property is not defined, or its value has no matching
binding. If the property is set, check for typos in its name. In a devicetree
source file, `compatible` should look like `"vnd,some-device"` --
dt-use-the-right-names.

If your binding file is not under `zephyr/dts`, you may need to set
DTS_ROOT; see dt-where-bindings-are-located.
