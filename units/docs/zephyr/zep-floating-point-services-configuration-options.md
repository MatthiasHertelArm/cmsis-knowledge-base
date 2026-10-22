---
id: "zep-floating-point-services-configuration-options"
type: "concept"
domain: "rtos"
title: "Floating Point Services: Configuration Options"
summary: "To configure unshared FP registers mode, enable the CONFIG_FPU configuration option and leave the CONFIG_FPU_SHARING configuration option disabled."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/other/float.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/other/float.rst"
license: "Apache-2.0"
mode: "V"
---

To configure unshared FP registers mode, enable the `CONFIG_FPU`
configuration option and leave the `CONFIG_FPU_SHARING` configuration
option disabled.

To configure shared FP registers mode, enable both the `CONFIG_FPU`
configuration option and the `CONFIG_FPU_SHARING` configuration option.
Also, ensure that any thread that uses the floating point registers has
sufficient added stack space for saving floating point register values
during context switches, as described above.

For x86, use the `CONFIG_X86_SSE` configuration option to enable
support for SSEx instructions.
