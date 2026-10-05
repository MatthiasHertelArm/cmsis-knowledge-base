---
id: "zep-custom-kconfig-preprocessor-functi"
type: "concept"
domain: "project"
title: "Custom Kconfig Preprocessor Functions"
summary: "Kconfiglib supports custom Kconfig preprocessor functions written in Python. These functions are defined in scripts/kconfig/kconfigfunctions.py."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/build/kconfig/preprocessor-functions.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/build/kconfig/preprocessor-functions.rst"
license: "Apache-2.0"
mode: "V"
---

Kconfiglib supports custom Kconfig preprocessor functions written in Python.
These functions are defined in
`scripts/kconfig/kconfigfunctions.py`.


**Note:** The official Kconfig preprocessor documentation can be found [here](https://www.kernel.org/doc/html/latest/kbuild/kconfig-macro-language.html).

See the Python docstrings in `scripts/kconfig/kconfigfunctions.py`
for detailed documentation.
Most of the custom preprocessor functions are used to get devicetree
information into Kconfig. For example, the default value of a Kconfig symbol
can be fetched from a devicetree `reg` property.
