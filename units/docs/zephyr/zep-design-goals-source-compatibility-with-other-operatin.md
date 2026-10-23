---
id: "zep-design-goals-source-compatibility-with-other-operatin"
type: "concept"
domain: "project"
title: "Design goals: Source compatibility with other operating systems"
summary: "Zephyr's devicetree tooling is based on a generic layer which is interoperable with other devicetree users, such as the Linux kernel."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/build/dts/design.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/build/dts/design.rst"
license: "Apache-2.0"
mode: "V"
---

Zephyr's devicetree tooling is based on a generic layer which is interoperable
with other devicetree users, such as the Linux kernel.

Zephyr's binding language *semantics* can support Zephyr-specific attributes,
but shall not express Zephyr-specific relationships.


### Examples


- Zephyr's devicetree source parser, dtlib.py, is
  source-compatible with other tools like dtc in both directions:
  `dtlib.py` can parse `dtc` output, and `dtc` can parse
  `dtlib.py` output.

- Zephyr's "extended dtlib" library, `edtlib.py`, shall not include
  Zephyr-specific features. Its purpose is to provide a higher-level view of the
  devicetree for common elements like interrupts and buses.

  Only the high-level `gen_defines.py` script, which is built on top of
  `edtlib.py`, contains Zephyr-specific knowledge and features.


### Example remaining work


- Zephyr has a custom dt-bindings language *syntax*. While Linux's
  dtschema does not yet meet Zephyr's needs, we should try to follow what it is
  capable of representing in Zephyr's own bindings.

- Due to inflexibility in the bindings language, Zephyr cannot support the full
  set of bindings supported by Linux.

- Devicetree source sharing between Zephyr and Linux is not done.
