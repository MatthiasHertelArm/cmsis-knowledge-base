---
id: "tfm-devicetree-concept"
type: "concept"
domain: "security"
title: "Devicetree: Concept"
summary: "There are two types of devicetree input files: devicetree sources (dts, dtsi) and devicetree bindings (yaml). The sources contain the devicetree itself. The bindings describe its contents, including data types."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/platform/stm/stm32mp2/technical/devicetree.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/platform/stm/stm32mp2/technical/devicetree.html#concept"
license: "BSD-3-Clause"
mode: "V"
---

There are two types of devicetree input files: devicetree sources (dts, dtsi)
and devicetree bindings (yaml). The sources contain the devicetree itself.
The bindings describe its contents, including data types.
The build system uses devicetree sources and bindings to produce a generated C header.

To simplify, gen_defines.py script creates for each information a define with
specific name and its value.

```devicetree

/ {
 first_node {
     second_node_label: second_node@10000000 {
                     compatible = "foo,foo-compatible";
                     foo-val = <3>;
                     status = "okay";
     };
     };
  };
```
Example of define's generated in `devicetree_generated.h`

```c

#define DT_N_S_first_node_S_second_node_10000000_PATH "/first_node/second_node@10000000"
#define DT_N_S_first_node_S_second_node_10000000_P_compatible {"foo,foo-compatible"}
#define DT_N_S_first_node_S_second_node_10000000_P_foo_val 3
#define DT_N_S_first_node_S_second_node_10000000_STATUS_okay 1
```
The name is built from the devicetree path and key word like (list is not exhaustive):

* `DT_N` header for devicetree node
* `S` for `/`
* `P` for property

To easily exploit the generated define, some macros are available in "devicetree.h"
or framework include files (clk.h..). All macro names start with `DT_`.

Example:

```c

// return node's label property value
#define DT_LABEL(node_id)
// return 1 if the node has the property, 0 otherwise.
#define DT_NODE_HAS_PROP(node_id, prop)
// return a representation of the property's value
#define DT_PROP(node_id, prop)
// return node's register block address
#define DT_REG_ADDR(node_id)

## How to add devicetree support


To add devicetree support on your target, include:

- the devicetree config file `config.cmake` which defines the default devicetree variables.
- the devicetree cmake file `gen_dt.cmake` and call the
  `add_devicetree_target()` function on an existing CMake target.

This function generates the `devicetree_generated.h` header for the target,
creates an `INTERFACE` library `dt_<TARGET>_header` exposing the include
directories, and a `STATIC` library `dt_<TARGET>_libs` where devicetree
based drivers (see How to add device) can be added with
`target_sources()`. Both libraries are automatically linked to
`<TARGET>`, and a custom target `dt_<TARGET>_gen_h` is created to drive
the header generation.

add_devicetree_target() arguments:


* - Argument
  - Required
  - Description
* - `TARGET`
  - Yes
  - Name of an existing CMake target on which devicetree support is
    added. It is used as a prefix to name every generated file, target
    and library (`dt_<TARGET>_gen_h`, `dt_<TARGET>_header`,
    `dt_<TARGET>_libs`...).
* - `DTS_BOARD`
  - Yes
  - File name of the board devicetree source (dts) to build, e.g.
    `stm32mp257f-dk.dts`. This file is looked up in the directories
    listed by `DTS_DIR` (see below).
* - `DTS_DIR`
  - No
  - List of extra directories to search for devicetree sources (dts,
    dtsi) and includes, in addition to the default ones already known
    by the build system (SoC, boards, extension and include
    directories).
* - `DTC_FLAGS`
  - No
  - List of extra flags forwarded to the devicetree compiler frontend
    (`gen_edt.py`), e.g. to suppress specific warnings/checks.
* - `EXTRA_CPPFLAGS`
  - No
  - List of extra flags forwarded to the C preprocessor used to
    preprocess the devicetree sources, e.g. extra `-D` defines used
    by `#if` guards in your dts/dtsi files.
Include devicetree config:

```CMake

# set devicetree config
if (EXISTS ${STM_DEVICETREE_DIR}/config.cmake)
    include(${STM_DEVICETREE_DIR}/config.cmake)
endif()
```
Add devicetree on target:

```CMake

# include devicetree cmake file in your project
include(${DEVICETREE_DIR}/gen_dt.cmake)

# add devicetree support to the "tfm_s" target
add_devicetree_target(
    TARGET tfm_s
    DTS_BOARD ${DTS_BOARD_S}
    DTS_DIR
        ${MY_DTS_DIR}/devicetree
    DTC_FLAGS
        -Wno-unique_unit_address
    EXTRA_CPPFLAGS
        -DMY_BOARD_VARIANT
)

# add devicetree based drivers to the generated static library
target_sources(dt_tfm_s_libs
    PRIVATE
        ${MY_DRIVER_PATH}/foo.c
)
