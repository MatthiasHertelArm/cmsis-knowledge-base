---
id: "zep-iterable-sections-step-2-declare-the-section-in-cmake"
type: "concept"
domain: "rtos"
title: "Iterable Sections: Step 2: Declare the section in CMake"
summary: "The NAME argument to zephyr_iterable_section() must match the struct name passed to STRUCT_SECTION_ITERABLE. The GROUP argument selects the linker group that the resulting output section is placed inside."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/iterable_sections/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/iterable_sections/index.rst"
license: "Apache-2.0"
mode: "V"
---

The `NAME` argument to `zephyr_iterable_section()` must match the struct
name passed to `STRUCT_SECTION_ITERABLE`. The `GROUP` argument
selects the linker group that the resulting output section is placed inside.

RAM-resident example:

```cmake

# CMakeLists.txt
zephyr_iterable_section(NAME my_data GROUP DATA_REGION ${XIP_ALIGN_WITH_INPUT})
```
ROM-resident example (instances declared `const` in C):

```cmake

# CMakeLists.txt
zephyr_iterable_section(NAME my_data GROUP RODATA_REGION)
```
See `zephyr_iterable_section()` in `cmake/modules/extensions.cmake` for the full argument list
and a more detailed explanation of the available `GROUP` options.
