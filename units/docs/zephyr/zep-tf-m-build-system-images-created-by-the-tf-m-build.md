---
id: "zep-tf-m-build-system-images-created-by-the-tf-m-build"
type: "concept"
domain: "security"
title: "TF-M Build System: Images Created by the TF-M Build"
summary: "The TF-M build system creates the following executable files:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/services/tfm/build.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/services/tfm/build.rst"
license: "Apache-2.0"
mode: "V"
---

The TF-M build system creates the following executable files:

* tfm_s - TF-M secure firmware
* tfm_ns - TF-M non-secure app (only used by regression tests).
* bl2 - TF-M MCUboot, if enabled

For each of these, it creates .bin, .hex, .elf, and .axf files.

The TF-M build system also creates signed variants of tfm_s and tfm_ns, and a
file which combines them:

* tfm_s_signed
* tfm_ns_signed
* tfm_s_ns_signed

For each of these, only .bin files are created.

The TF-M non-secure app is discarded in favor of Zephyr non-secure app except
when running the TF-M regression test suite.

The Zephyr build system usually signs both tfm_s and the Zephyr non-secure app itself.
See below for details.

The 'tfm' target contains properties for all these paths.
For example, the following will resolve to `<path>/tfm_s.hex`:

```

$<TARGET_PROPERTY:tfm,TFM_S_HEX_FILE>
```
See the top level CMakeLists.txt file in the tfm module for an overview of all
the properties.
