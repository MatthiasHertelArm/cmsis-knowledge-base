---
id: "zep-phandles-naming-the-cells-in-a-specifier"
type: "concept"
domain: "project"
title: "Phandles: Naming the cells in a specifier"
summary: "You should name the cells in each specifier space your hardware supports when writing bindings. For details on how to do this, see dt-bindings-cells."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/build/dts/phandles.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/build/dts/phandles.rst"
license: "Apache-2.0"
mode: "V"
---

You should name the cells in each specifier space your hardware supports when
writing bindings. For details on how to do this, see dt-bindings-cells.

This allows C code to query information about and retrieve the values of cells
in a specifier by name using devicetree APIs like these:

- `DT_PHA_BY_IDX`
- `DT_PHA_BY_NAME`

This feature and these macros are used internally by numerous hardware-specific
APIs. Here are a few examples:

- `DT_GPIO_PIN_BY_IDX`
- `DT_PWMS_CHANNEL_BY_IDX`
- `DT_DMAS_CELL_BY_NAME`
- `DT_IO_CHANNELS_INPUT_BY_IDX`
- `DT_CLOCKS_CELL_BY_NAME`
