---
id: "mcuboot-serial-recovery"
type: "concept"
domain: "boot-update"
title: "Serial recovery"
summary: "MCUboot implements a Simple Management Protocol (SMP) server. SMP is a basic transfer encoding for use with the MCUmgr management protocol. See the Zephyr Device Management documentation for more information about MCUmgr and SMP."
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@ba2099f:docs/serial_recovery.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/ba2099f/docs/serial_recovery.md"
license: "Apache-2.0"
mode: "V"
---

MCUboot implements a Simple Management Protocol (SMP) server.
SMP is a basic transfer encoding for use with the MCUmgr management protocol. 
See the Zephyr [Device Management](https://docs.zephyrproject.org/latest/services/device_mgmt/index.html#device-mgmt) documentation for more information about MCUmgr and SMP.

MCUboot supports the following subset of the MCUmgr commands:
* echo (OS group)
* reset (OS group)
* MCUmgr parameters SMP buffer size (OS group), when ``MCUBOOT_BOOT_MGMT_MCUMGR_PARAMS`` is enabled
* image list (IMG group)
* image upload (IMG group)

It can also support system-specific MCUmgr commands depending on the given mcuboot-port
if the ``MCUBOOT_PERUSER_MGMT_GROUP_ENABLED`` option is enabled.

The serial recovery feature can use any serial interface provided by the platform.
