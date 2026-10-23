---
id: "tfm-devicetree-how-to-add-device"
type: "concept"
domain: "security"
title: "Devicetree: How to add device"
summary: "In this section we would to add and enable device using a new driver that requires some ressources (reg, int value)."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/platform/stm/stm32mp2/technical/devicetree.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/platform/stm/stm32mp2/technical/devicetree.html#how-to-add-device"
license: "BSD-3-Clause"
mode: "V"
---

In this section we would to add and enable device using a new driver that requires some ressources
(reg, int value).



### Devicetree (dts) and bindings (yaml)


Files location:

- The devicetree source (dts, dtsi):

  * SoC: `devicetree/dts/soc/<soc-family>/`
  * Boards: `devicetree/dts/boards/<board-name>/`

```devicetree

/* Node in a DTS file */
my-device@10000000 {
  compatible = "foo-company,my-device";
  reg = <0x10000000 0x400>;
  num-foos = <3>;
  status = "okay";
};
```
- Bindings (yaml): `devicetree/bindings/<framework>/`

```yaml

description: my-device description

compatible: "foo-company,my-device"

include: [base.yaml]

properties:
   reg:
      required: true

   num-foos:
      type: int
      description: integer value
```
With the `compatible` field, the build system matches `my-device` node to its yaml file.
Yaml file allows checking the `properties:` (type, required) and generates defines adapted
to type.

Bindings can include other files, which can be used to share common property definitions between bindings.
Use the `include:` key for this. Its value is either a string or a list.



### Drivers


```c

// define compatible value, needed for DT_INST_XX macro
#define DT_DRV_COMPAT foo_company_my_device

// include generic device api and devicetree
#include <device.h>
#include <debug.h>

struct my_device_config {
 uintptr_t base;
 uint32_t num_foos;
};

struct my_device_data {
};

int my_device_init(const struct device *dev)
{
 const struct my_device_config *dev_cfg = dev_get_config(dev);

 IMSG("my property num-foos:%d", dev_cfg->num_foos);

 return 0;
}

#define MY_DEVICE_INIT(n)                    \
                             \
static const struct my_device_config my_dev_cfg_##n = {    \
 .base = DT_INST_REG_ADDR(n),                \
 .num_foos = DT_INST_PROP_OR(n, num_foos, 0),        \
};                                \
                             \
static struct my_device_data my_dev_data_##n = {        \
};                                \
                             \
DEVICE_DT_INST_DEFINE(n,                    \
       &my_device_init,                    \
       &my_dev_data_##n,                    \
       &my_dev_cfg_##n,                    \
       POST_CORE, 10,                    \
       /*&fw_controller_api*/ NULL);

DT_INST_FOREACH_STATUS_OKAY(MY_DEVICE_INIT)
```
For each instances with compatible `foo-company,my-device` and status
`okay` a device structure is defined with:

* A pointer to the device’s initialization function, which will be called during
  system initialization.
* A private data structure by instance.
* A config structure (constant) by instance.
* The device’s initialization level (see init_level).
* A framework API, if this controller is under a framework.


**Note:** Tips to debug this part: * Check devicetree source (dts) preprocessing in `<BUILD_PATH>/generated/devicetree/<tfm_s|tfm_ns|bl2>` files `*.dts.pre.tmp` or `out.dts` * Check if `devicetree_generated.h` contains your device and its properties * Preprocess your C file to check that `DT_INST_*` macros are expanded with the expected devicetree values in your device instance. .. code-block:: bash # From the build directory, find the preprocessing rule generated for your driver source file grep -r 'foo.i:' * # platform/target/CMakeFiles/dt_tfm_s_libs.dir/build.make:platform/target/CMakeFiles/dt_tfm_s_libs.dir/__/common/stm32mp2xx/native_driver/src/foo.i: cmake_force # Run the matching make rule. make -f platform/target/CMakeFiles/dt_tfm_s_libs.dir/build.make platform/target/CMakeFiles/dt_tfm_s_libs.dir/__/common/stm32mp2xx/native_driver/src/foo.i # Edit the foo.i generated

--------------

*Copyright (c) 2026 STMicroelectronics. All rights reserved.*
*SPDX-License-Identifier: BSD-3-Clause*
