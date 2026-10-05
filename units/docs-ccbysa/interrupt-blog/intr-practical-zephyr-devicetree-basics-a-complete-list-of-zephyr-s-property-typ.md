---
id: "intr-practical-zephyr-devicetree-basics-a-complete-list-of-zephyr-s-property-typ"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Devicetree basics (Part 3): A complete list of Zephyr's property types"
summary: "Having explored phandle types and paths, we can complete the list of types that are used in Zephyr devicetrees. You can find the same information in Zephyr's documentation on bindings and Zephyr's how-to on property values."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-02-01-practical_zephyr_dt.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_dt#a-complete-list-of-zephyr-s-property-types"
license: "CC-BY-SA-4.0"
mode: "V"
---

Having explored `phandle` types and `paths`, we can complete the list of types that are used in Zephyr devicetrees. You can find the same information in [Zephyr's documentation on bindings](https://docs.zephyrproject.org/latest/build/dts/bindings-syntax.html#type) and [Zephyr's how-to on property values](https://docs.zephyrproject.org/latest/build/dts/intro-syntax-structure.html#writing-property-values).

| Zephyr type      | DTSpec equivalent              | Example                                            |
| :--------------- | :----------------------------- | :------------------------------------------------- |
| `boolean`        | `property with no value`       | `interrupt-controller;`                            |
| `string`         | `string`                       | `status = "disabled";`                             |
| `array`          | `32-bit integer cells`         | `reg = <0x40002000 0x1000>;`                       |
| `int`            | `A single 32-bit integer cell` | `current-speed = <115200>;`                        |
| `64-bit integer` | `32-bit integer cells`         | `value = <0xBAADF00D 0xDEADBEEF>;`                 |
| `uint8-array`    | `bytestring`                   | `mac-address = [ DE AD BE EF 12 34 ];`             |
| `string-array`   | `stringlist`                   | `compatible = "nordic,nrf-egu", "nordic,nrf-swi";` |
| `compound`       | "comma-separated components"   | `foo = <1 2>, [3, 4], "five"`                      |
| `path`           | `32-bit integer cells`         | `zephyr,console = &uart0;`                         |
| `phandle`        | `phandle`                      | `pinctrl-0 = <&uart0_default>;`                    |
| `phandles`       | `32-bit integer cells`         | `cpu-power-states = <&idle &suspend>;`             |
| `phandle-array`  | `32-bit integer cells`         | `gpios = <&gpio0 13 GPIO_ACTIVE_LOW>;`             |



Again, it is worth mentioning that the `compound` type is only a "catch-all" for custom types. Zephyr does **not** generate any macros for `compound` properties.
