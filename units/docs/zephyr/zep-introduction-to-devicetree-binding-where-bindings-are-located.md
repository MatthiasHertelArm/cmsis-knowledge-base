---
id: "zep-introduction-to-devicetree-binding-where-bindings-are-located"
type: "concept"
domain: "project"
title: "Introduction to Devicetree Bindings: Where bindings are located"
summary: "Binding file names usually match their compatible: lines. For example, the above example binding would be named foo-company,bar-device.yaml by convention."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/build/dts/bindings-intro.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/build/dts/bindings-intro.rst"
license: "Apache-2.0"
mode: "V"
---

Binding file names usually match their `compatible:` lines. For example, the
above example binding would be named `foo-company,bar-device.yaml` by
convention.

The build system looks for bindings in `dts/bindings`
subdirectories of the following places:

- the zephyr repository
- your application source directory
- your board directory
- any shield directories
- any directories manually included in the DTS_ROOT
  CMake variable
- any module that defines a `dts_root` in its
  modules_build_settings

The build system will consider any YAML file in any of these, including in any
subdirectories, when matching nodes to bindings. A file is considered YAML if
its name ends with `.yaml` or `.yml`.


**Warning:** The binding files must be located somewhere inside the `dts/bindings` subdirectory of the above places. For example, if `my-app` is your application directory, then you must place application-specific bindings inside `my-app/dts/bindings`. So found, but `my-app/my-company,my-serial-port.yaml` would be ignored.
