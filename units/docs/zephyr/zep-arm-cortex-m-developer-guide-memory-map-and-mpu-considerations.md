---
id: "zep-arm-cortex-m-developer-guide-memory-map-and-mpu-considerations"
type: "concept"
domain: "rtos"
title: "Arm Cortex-M Developer Guide: OS features / Memory map and MPU considerations"
summary: "By default, when CONFIG_ARM_MPU is enabled a set of fixed MPU regions are programmed during system boot."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/hardware/arch/arm_cortex_m.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/hardware/arch/arm_cortex_m.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: OS features_

#### Fixed MPU regions


By default, when `CONFIG_ARM_MPU` is enabled a set of *fixed* MPU regions
are programmed during system boot.

* One MPU region programs the entire flash area as read-execute.
  User can override this setting by enabling `CONFIG_MPU_ALLOW_FLASH_WRITE`,
  which programs the flash with RWX permissions. If `CONFIG_USERSPACE` is
  enabled unprivileged access on the entire flash area is allowed.
* One MPU region programs the entire SRAM area with privileged-only
  RW permissions. That is, an  MPU region is utilized to disallow execute permissions on
  SRAM. (An exception to this setting is when `CONFIG_MPU_GAP_FILLING` is disabled (Arm v8-M only);
  in that case no SRAM MPU programming is done so the access is determined by the default
  Arm memory map policies, allowing for privileged-only RWX permissions on SRAM).
* All the memory regions defined in the devicetree with the property
  `zephyr,memory-attr` defining the MPU permissions for the memory region.
  See the next section for more details.

The above MPU regions are defined in `arch/arm/core/mpu/arm_mpu_regions.c`.
Alternative MPU configurations are allowed by enabling `CONFIG_CPU_HAS_CUSTOM_FIXED_SOC_MPU_REGIONS`.
When enabled, this option signifies that the Cortex-M SoC will define and
configure its own fixed MPU regions in the SoC definition.


#### Fixed MPU regions defined in devicetree


When the property `zephyr,memory-attr` is present in a memory node, a new MPU
region will be allocated and programmed during system boot. When used with the
`zephyr,memory-region` devicetree compatible, it will result in a
linker section being generated associated to that MPU region.

For example, to define a new non-cacheable memory region in devicetree:

```devicetree

sram_no_cache: memory@20300000 {
     compatible = "zephyr,memory-region", "mmio-sram";
     reg = <0x20300000 0x100000>;
     zephyr,memory-region = "SRAM_NO_CACHE";
     zephyr,memory-attr = <DT_MEM_ARM_MPU_RAM_NOCACHE>;
};
```
This will automatically create a new MPU entry in with the correct name, base,
size and attributes gathered directly from the devicetree. See cache_guide
and mem_mgmt_api for more details.


#### Static MPU regions


Additional *static* MPU regions may be programmed once during system boot. These regions
are required to enable certain features. See cache_guide for more details.

* a RX region to allow execution from SRAM, when `CONFIG_ARCH_HAS_RAMFUNC_SUPPORT` is
  enabled and users have defined functions to execute from SRAM.
* a RX region for relocating text sections to SRAM, when `CONFIG_CODE_DATA_RELOCATION_SRAM` is enabled
* a `nocache` region to allow for a non-cacheable SRAM area, when `CONFIG_NOCACHE_MEMORY` is enabled
* a possibly unprivileged RW region for GCOV code coverage accounting area, when `CONFIG_COVERAGE_GCOV` is enabled
* a no-access region to implement null pointer dereference detection, when `CONFIG_NULL_POINTER_EXCEPTION_DETECTION_MPU` is enabled

The boundaries of these static MPU regions are derived from symbols exposed by the linker, in
`include/linker/linker-defs.h`.


#### Dynamic MPU regions


Certain thread-specific MPU regions may be re-programmed dynamically, at each thread context switch:

* an unprivileged RW region for the current thread's stack area (for user threads)
* a read-only region for the MPU stack guard
* unprivileged RW regions for the partitions of the current thread's application memory
  domain.



#### Considerations


The number of available MPU regions for a Cortex-M platform is a limited resource.
Most platforms have 8 MPU regions, while some Cortex-M33 or Cortex-M7 platforms may
have up to 16 MPU regions. Therefore there is a relatively strict limitation on how
many fixed, static and dynamic MPU regions may be programmed simultaneously. For platforms
with 8 available MPU regions it might not be possible to enable all the aforementioned
features that require MPU region programming. In most practical applications, however,
only a certain set of features is required and 8 MPU regions are, in many cases, sufficient.

In Arm v8-M processors the MPU architecture does not allow programmed MPU regions to
overlap. `CONFIG_MPU_GAP_FILLING` controls whether the fixed MPU region
covering the entire SRAM is programmed. When it does, a full SRAM area partitioning
is required, in order to program the  static and the dynamic MPU regions. This increases
the total number of required MPU regions. When `CONFIG_MPU_GAP_FILLING` is not
enabled the fixed MPU region covering the entire SRAM is not programmed, thus, the static
and dynamic regions are simply programmed on top of the always-existing background region
(full-SRAM partitioning is not required).
Note, however, that the background SRAM region allows execution from SRAM, so when
`CONFIG_MPU_GAP_FILLING` is not set Zephyr is not protected against attacks
that attempt to execute malicious code from SRAM.
