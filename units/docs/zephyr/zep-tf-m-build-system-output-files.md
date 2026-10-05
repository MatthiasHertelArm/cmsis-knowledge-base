---
id: "zep-tf-m-build-system-output-files"
type: "concept"
domain: "security"
title: "TF-M Build System: Output Files"
summary: "Upon completion of the Zephyr TF-M build, the following output files exist:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/services/tfm/build.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/services/tfm/build.rst"
license: "Apache-2.0"
mode: "V"
---

Upon completion of the Zephyr TF-M build, the following output files exist:


### Custom CMake arguments


When building a Zephyr application with TF-M it might be necessary to control
the CMake arguments passed to the TF-M build.

Zephyr TF-M build offers several Kconfig options for controlling the build, but
doesn't cover every CMake argument supported by the TF-M build system.

The `TFM_CMAKE_OPTIONS` property on the `zephyr_property_target` can be used
to pass custom CMake arguments to the TF-M build system.

To pass the CMake argument `-DFOO=bar` to the TF-M build system, place the
following CMake snippet in your CMakeLists.txt file.

```cmake

set_property(TARGET zephyr_property_target
             APPEND PROPERTY TFM_CMAKE_OPTIONS
             -DFOO=bar
)
```

**Note:** The `TFM_CMAKE_OPTIONS` is a list so it is possible to append multiple options. Also CMake generator expressions are supported, such as `$<1:-DFOO=bar>`

Since `TFM_CMAKE_OPTIONS` is a list argument it will be expanded before it is
passed to the TF-M build system.
Options that have list arguments must therefore be properly escaped to avoid
being expanded as a list.

```cmake

set_property(TARGET zephyr_property_target
             APPEND PROPERTY TFM_CMAKE_OPTIONS
             -DFOO="bar\\\;baz"
)
```
