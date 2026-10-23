---
id: "zep-devicetree-bindings-syntax-type"
type: "concept"
domain: "project"
title: "Devicetree bindings syntax: Properties / type"
summary: "The type of a property constrains its values. The following types are available. See dt-writing-property-values for more details about writing values of each type in a DTS file. See dt-phandles for more information about the phandle type properties."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/build/dts/bindings-syntax.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/build/dts/bindings-syntax.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: Properties_

The type of a property constrains its values. The following types are
available. See dt-writing-property-values for more details about writing
values of each type in a DTS file. See dt-phandles for more information
about the `phandle*` type properties.


* - Type
  - Description
  - Example in DTS

* - `string`
  - exactly one string
  - `status = "disabled";`

* - `int`
  - exactly one 32-bit value (cell)
  - `current-speed = <115200>;`

* - `boolean`
  - flags that don't take a value when true, and are absent if false
  - `hw-flow-control;`

* - `array`
  - zero or more 32-bit values (cells)
  - `offsets = <0x100 0x200 0x300>;`

* - `uint8-array`
  - zero or more bytes, in hex ('bytestring' in the Devicetree specification)
  - `local-mac-address = [de ad be ef 12 34];`

* - `string-array`
  - zero or more strings
  - `dma-names = "tx", "rx";`

* - `phandle`
  - exactly one phandle
  - `interrupt-parent = <&gic>;`

* - `phandles`
  - zero or more phandles
  - `pinctrl-0 = <&usart2_tx_pd5 &usart2_rx_pd6>;`

* - `phandle-array`
  - a list of phandles and 32-bit cells (usually specifiers)
  - `dmas = <&dma0 2>, <&dma0 3>;`

* - `path`
  - a path to a node as a phandle path reference or path string
  - `zephyr,bt-c2h-uart = &uart0;` or
    `foo = "/path/to/some/node";`

* - `compound`
  - a catch-all for more complex types (no macros will be generated)
  - `foo = <&label>, [01 02];`
