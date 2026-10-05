---
id: "dap-host-os-drivers-additional-requirements-for-linux"
type: "concept"
domain: "debug"
title: "Host OS Drivers: Additional requirements for Linux"
summary: "On Linux, permission to access USB devices from user space must be explicitly granted via udev rules."
status: "draft"
collection: "cmsis-dap"
source: "ARM-software/CMSIS-DAP@1263659:Documentation/Doxygen/src/dap_drv_install.md"
doc_source: "https://arm-software.github.io/CMSIS-DAP/latest/dap_drv_install.html"
license: "Apache-2.0"
mode: "V"
---

On Linux, permission to access USB devices from user space must be explicitly granted via udev rules. Exemplary udev rules are available in the [pyOCD GitHub repo](https://github.com/pyocd/pyOCD/tree/main/udev) that allow to access common debug probes without requiring it to be run as root.
