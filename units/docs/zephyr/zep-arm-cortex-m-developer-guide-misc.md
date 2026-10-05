---
id: "zep-arm-cortex-m-developer-guide-misc"
type: "concept"
domain: "rtos"
title: "Arm Cortex-M Developer Guide: Misc"
summary: "Cortex-M applications may either be standalone images or chain-loadable, for instance, by a bootloader. Application images chain-loadable by bootloaders (or other applications) normally occupy a specific area in the flash denoted as their code partition."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/hardware/arch/arm_cortex_m.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/hardware/arch/arm_cortex_m.rst"
license: "Apache-2.0"
mode: "V"
---

### Chain-loadable images


Cortex-M applications may either be standalone images or chain-loadable, for instance,
by a bootloader. Application images chain-loadable by bootloaders (or other applications)
normally occupy a specific area in the flash denoted as their *code partition*.
`CONFIG_USE_DT_CODE_PARTITION` will ensure that a Zephyr chain-loadable image
will be linked into its code partition, specified in DeviceTree.


#### HW initialization at boot


In order to boot properly, chain-loaded applications may require that the core Arm
hardware registers and peripherals are initialized in their reset values. Enabling
`CONFIG_INIT_ARCH_HW_AT_BOOT` Zephyr to force the initialization of the
internal Cortex-M architectural state during boot to the reset values as specified
by the corresponding Arm architecture manual.


#### Software vector relaying


In Cortex-M platforms that implement the VTOR register (see `CONFIG_CPU_CORTEX_M_HAS_VTOR`),
chain-loadable images relocate the Cortex-M vector table by updating the VTOR register with the offset
of the image vector table.

Baseline Cortex-M platforms without VTOR register might not be able to relocate their
vector table which remains at a fixed location. Therefore, a chain-loadable image will
require an alternative way to route HW interrupts and system exceptions to its own vector
table; this is achieved with software vector relaying.

When a bootloader image enables `CONFIG_SW_VECTOR_RELAY`
it is able to relay exceptions and interrupts based on a vector table
pointer that is set by the chain-loadable application. The latter sets
the `CONFIG_SW_VECTOR_RELAY_CLIENT` option to instruct the boot
sequence to set the vector table pointer in SRAM so that the bootloader can
forward the exceptions and interrupts to the chain-loadable image's software
vector table.

While this feature is intended for processors without VTOR register, it
may also be used in Mainline Cortex-M platforms.


### Code relocation


Cortex-M support the code relocation feature. When
`CONFIG_CODE_DATA_RELOCATION_SRAM` is selected,
Zephyr will relocate .text, data and .bss sections
from the specified files and place it in SRAM. It is
possible to relocate only parts of the code sections
into SRAM, without relocating the whole image text
and data sections. More details on the code relocation
feature can be found in code_data_relocation.
