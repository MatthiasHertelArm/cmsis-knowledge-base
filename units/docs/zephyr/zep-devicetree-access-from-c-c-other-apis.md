---
id: "zep-devicetree-access-from-c-c-other-apis"
type: "concept"
domain: "project"
title: "Devicetree access from C/C++: Other APIs"
summary: "Here are pointers to some other available APIs."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/build/dts/api-usage.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/build/dts/api-usage.rst"
license: "Apache-2.0"
mode: "V"
---

Here are pointers to some other available APIs.

- `DT_CHOSEN`, `DT_HAS_CHOSEN`: for properties
  of the special `/chosen` node
- `DT_HAS_COMPAT_STATUS_OKAY`, `DT_NODE_HAS_COMPAT`: global- and
  node-specific tests related to the `compatible` property
- `DT_BUS`: get a node's bus controller, if there is one
- `DT_ENUM_IDX`: for properties whose values are among a fixed list of
  choices
- devicetree-flash-api: APIs for managing fixed flash partitions and
  mapped flash partitions.
  Also see flash_map_api, which wraps this in a more user-friendly API.
