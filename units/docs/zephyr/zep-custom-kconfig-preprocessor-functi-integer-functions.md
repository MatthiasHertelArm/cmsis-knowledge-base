---
id: "zep-custom-kconfig-preprocessor-functi-integer-functions"
type: "concept"
domain: "project"
title: "Custom Kconfig Preprocessor Functions: Integer functions"
summary: "The functions listed below can be used to do arithmetic operations on integer variables, such as addition, subtraction and more. Functions with and without the hex suffix in their names return hexadecimal and decimal values respectively."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/build/kconfig/preprocessor-functions.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/build/kconfig/preprocessor-functions.rst"
license: "Apache-2.0"
mode: "V"
---

The functions listed below can be used to do arithmetic operations
on integer variables, such as addition, subtraction and more.
Functions with and without the `_hex` suffix in their names
return hexadecimal and decimal values respectively.

```none

$(add,<value>[,value]...)
$(add_hex,<value>[,value]...)
$(dec,<value>[,value]...)
$(dec_hex,<value>[,value]...)
$(div,<value>[,value]...)
$(div_hex,<value>[,value]...)
$(inc,<value>[,value]...)
$(inc_hex,<value>[,value]...)
$(max,<value>[,value]...)
$(max_hex,<value>[,value]...)
$(min,<value>[,value]...)
$(min_hex,<value>[,value]...)
$(mod,<value>[,value]...)
$(mod_hex,<value>[,value]...)
$(mul,<value>[,value]...)
$(mul_hex,<value>[,value]...)
$(sub,<value>[,value]...)
$(sub_hex,<value>[,value]...)
```
