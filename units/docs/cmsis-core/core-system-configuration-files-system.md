---
id: "core-system-configuration-files-system"
type: "concept"
domain: "core"
title: "System Configuration Files system_<Device>.c and system_<Device>.h"
summary: "CMSIS-Core system configuration files provide as a minimum the functions for system initialization and clock configuration as described under system_init_gr. The file names use naming convention system<Device>.h and system<Device>.c, where <Device> corresponds to the device name."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Core/src/core_system_files.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Core/src/core_system_files.md"
license: "Apache-2.0"
mode: "V"
---

CMSIS-Core system configuration files provide as a minimum the functions for system initialization and clock configuration as described under system_init_gr. The file names use naming convention `system_<Device>.h` and `system_<Device>.c`, where `<Device>` corresponds to the device name.

`system_<Device>.h` file shall contain the prototypes for accessing the public functions and `system_<Device>.c` shall contain corresponding implementations.

The system configuration functions are device specific and need adaptation for the target device. The silicon vendor might expose other functions and configuration parameters such as XTAL, power configuration, etc.

Additional application-specific adaptations may be required in the initialization code and therefore the system configuration file shall be located in the application project. cmsis_files_dfps explains how this can be achieved when device support is provided in [CMSIS pack format](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/index.html).

# system_Device Template Files

CMSIS-Core cmsis_template_files include `system_Device.c` and `system_Device.h` files that can be used as a starting point for implementing device-specific system configuration files.
