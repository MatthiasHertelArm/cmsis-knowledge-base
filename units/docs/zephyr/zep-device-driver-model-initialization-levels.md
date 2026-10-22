---
id: "zep-device-driver-model-initialization-levels"
type: "concept"
domain: "rtos"
title: "Device Driver Model: Initialization Levels"
summary: "Drivers may depend on other drivers being initialized first, or require the use of kernel services. DEVICE_DEFINE() and related APIs allow the user to specify at what time during the boot sequence the init function will be executed."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/drivers/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/drivers/index.rst"
license: "Apache-2.0"
mode: "V"
---

Drivers may depend on other drivers being initialized first, or require
the use of kernel services. `DEVICE_DEFINE()` and related APIs
allow the user to specify at what time during the boot sequence the init
function will be executed. Any driver will specify one of three
initialization levels:

`PRE_KERNEL_1`
        Used for devices that have no dependencies, such as those that rely
        solely on hardware present in the processor/SOC. These devices cannot
        use any kernel services during configuration, since the kernel services are
        not yet available. The interrupt subsystem will be configured however
        so it's OK to set up interrupts. Init functions at this level run on the
        interrupt stack.

`PRE_KERNEL_2`
        Used for devices that rely on the initialization of devices initialized
        as part of the `PRE_KERNEL_1` level. These devices cannot use any kernel
        services during configuration, since the kernel services are not yet
        available. Init functions at this level run on the interrupt stack.

`POST_KERNEL`
        Used for devices that require kernel services during configuration.
        Init functions at this level run in context of the kernel main task.

Within each initialization level you may specify a priority level, relative to
other devices in the same initialization level. The priority level is specified
as an integer value in the range 0 to 999; lower values indicate earlier
initialization.  The priority level must be a decimal integer literal without
leading zeroes or sign (e.g. 32), or an equivalent symbolic name (e.g.
`\#define MY_INIT_PRIO 32`); symbolic expressions are *not* permitted (e.g.
`CONFIG_KERNEL_INIT_PRIORITY_DEFAULT + 5`).

Drivers and other system utilities can determine whether startup is
still in pre-kernel states by using the `k_is_pre_kernel`
function.
