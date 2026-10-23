---
id: "mcuboot-serial-recovery-serial-recovery-mode-usage"
type: "concept"
domain: "boot-update"
title: "Serial recovery: Serial recovery mode usage"
summary: "The MCUmgr command line tool can be used as an SMP client for evaluation purposes. The tool is available under the MCU Manager Github page and is described in the Zephyr MCU Manager CLI documentation."
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@725d63c:docs/serial_recovery.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/725d63c/docs/serial_recovery.md#serial-recovery-mode-usage"
license: "Apache-2.0"
mode: "V"
---

### MCU Manager CLI installation

The MCUmgr command line tool can be used as an SMP client for evaluation purposes.
The tool is available under the [MCU Manager](https://github.com/apache/mynewt-mcumgr-cli)
Github page and is described in the Zephyr 
[MCU Manager CLI](https://docs.zephyrproject.org/latest/services/device_mgmt/mcumgr.html#mcumgr-cli) documentation.

Use the following command to install the MCU Manager CLI tool:
``` console
go install github.com/apache/mynewt-mcumgr-cli/mcumgr@latest
```
Enter serial recovery mode in the device and use an SMP client application for communication with the MCUboot's SMP server.

### Connection configuration

Use the following command to set the connection configuration,
for linux:
``` console
mcumgr conn add serial_1 type="serial" connstring="dev=/dev/ttyACM0,baud=115200"
```
for windows:
``` console
mcumgr conn add serial_1 type="serial" connstring="COM1,baud=115200"
```

### Image management

The connection configuration must be established to perform the following image-related commands:

* Upload the image:
  ``` console
  mcumgr image upload <path-to-signed-image-bin-file> -c serial_1
  ```

  Once done successfully, the following notification will be displayed:
  ``` console
  20.25 KiB / 20.25 KiB [=================================] 100.00% 3.08 KiB/s 6s
  Done
  ```

* List all images:
  ``` console
  mcumgr image list -c serial_1
  ```
  The terminal will show the response from the module:
  ``` console
  Images:
   image=0 slot=0
      version: 0.0.0.0
      bootable: false
      flags: 
      hash: Unavailable
  Split status: N/A (0)
  ```

### Device reset

Reset your device with the following command:
``` console
mcumgr reset -c serial_1
```
The terminal should respond:
``` console
Done
```
