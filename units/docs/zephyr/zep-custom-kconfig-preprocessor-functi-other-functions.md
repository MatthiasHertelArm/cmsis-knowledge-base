---
id: "zep-custom-kconfig-preprocessor-functi-other-functions"
type: "concept"
domain: "project"
title: "Custom Kconfig Preprocessor Functions: Other functions"
summary: "Functions to perform specific operations, currently only a check if a shield name is specified."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/build/kconfig/preprocessor-functions.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/build/kconfig/preprocessor-functions.rst"
license: "Apache-2.0"
mode: "V"
---

Functions to perform specific operations, currently only a check if a shield
name is specified.

```none

$(shields_list_contains,<shield name>)
```
Shield names cannot contain whitespace. A space after the comma, as in
`$(shields_list_contains, foo)`, is stripped and a warning is printed
so the lookup still matches `foo`.



### Example Usage


Assume that the devicetree for some board looks like this:

```devicetree

{
    soc {
        #address-cells = <1>;
        #size-cells = <1>;

        spi0: spi@10014000 {
            compatible = "sifive,spi0";
            reg = <0x10014000 0x1000 0x20010000 0x3c0900>;
            reg-names = "control", "mem";
            ...
        };
};
```
The second entry in `reg` in `spi@1001400` (`<0x20010000 0x3c0900>`)
corresponds to `mem`, and has the address `0x20010000`. This address can be
inserted into Kconfig as follows:

```kconfig

config FLASH_BASE_ADDRESS
    default $(dt_node_reg_addr_hex,/soc/spi@1001400,1)
```
After preprocessor expansion, this turns into the definition below:

```kconfig

config FLASH_BASE_ADDRESS
    default 0x20010000
```
