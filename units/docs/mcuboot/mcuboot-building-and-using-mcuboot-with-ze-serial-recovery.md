---
id: "mcuboot-building-and-using-mcuboot-with-ze-serial-recovery"
type: "concept"
domain: "boot-update"
title: "Building and using MCUboot with Zephyr: Serial recovery"
summary: "A serial recovery protocol is available over either a hardware serial port or a USB CDC ACM virtual serial port. The SMP server implementation can be enabled by the CONFIG_MCUBOOT_SERIAL=y Kconfig option."
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@725d63c:docs/readme-zephyr.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/725d63c/docs/readme-zephyr.md#serial-recovery"
license: "Apache-2.0"
mode: "V"
---

### Interface selection

A serial recovery protocol is available over either a hardware serial port or a USB CDC ACM virtual serial port.
The SMP server implementation can be enabled by the ``CONFIG_MCUBOOT_SERIAL=y`` Kconfig option.
To set a type of an interface, use the ``BOOT_SERIAL_DEVICE`` Kconfig choice, and select either the ``CONFIG_BOOT_SERIAL_UART`` or the ``CONFIG_BOOT_SERIAL_CDC_ACM`` value.
Which interface belongs to the protocol shall be set by the devicetree-chosen node:
- `zephyr,console` - If a hardware serial port is used.
- `zephyr,cdc-acm-uart` - If a virtual serial port is used.

When ``CONFIG_BOOT_SERIAL_CDC_ACM=y`` is selected, MCUboot manages the USB device stack
internally and only initializes it when serial recovery is actually triggered — not on every boot.
This avoids consuming hardware USB events that the application would otherwise receive.
The USB device descriptors can be configured with the following Kconfig options:

| Option                                             | Default                       | Description                                                                              |
| -------------------------------------------------- | ----------------------------- | ---------------------------------------------------------------------------------------- |
| ``CONFIG_BOOT_SERIAL_CDC_ACM_VID``                 | ``0x2fe3``                    | USB Vendor ID                                                                            |
| ``CONFIG_BOOT_SERIAL_CDC_ACM_PID``                 | ``0x0004``                    | USB Product ID                                                                           |
| ``CONFIG_BOOT_SERIAL_CDC_ACM_MANUFACTURER_STRING`` | ``"MCUBoot"``                 | Manufacturer string descriptor                                                           |
| ``CONFIG_BOOT_SERIAL_CDC_ACM_PRODUCT_STRING``      | ``"CDC ACM serial recovery"`` | Product string descriptor                                                                |
| ``CONFIG_BOOT_SERIAL_CDC_ACM_SELF_POWERED``        | ``n``                         | Set the self-powered attribute in the USB configuration descriptor                       |
| ``CONFIG_BOOT_SERIAL_CDC_ACM_MAX_POWER``           | ``125``                       | ``bMaxPower`` value in the USB configuration descriptor, in 2 mA units (default: 250 mA) |

### Entering the serial recovery mode

To enter the serial recovery mode, the device has to initiate rebooting, and a triggering event has to occur (for example, pressing a button).

By default, the serial recovery GPIO pin active state enters the serial recovery mode.
Use the ``mcuboot_button0`` devicetree button alias to assign the GPIO pin to the MCUboot.

Alternatively, MCUboot can wait for a limited time to check if DFU is invoked by receiving an MCUmgr command.
Select ``CONFIG_BOOT_SERIAL_WAIT_FOR_DFU=y`` to use this mode. ``CONFIG_BOOT_SERIAL_WAIT_FOR_DFU_TIMEOUT`` option defines
the amount of time in milliseconds the device will wait for the trigger.

### Direct image upload

By default, the SMP server implementation will only use the first slot.
To change it, invoke the `image upload` MCUmgr command with a selected image number, and make sure the ``CONFIG_MCUBOOT_SERIAL_DIRECT_IMAGE_UPLOAD=y`` Kconfig option is enabled.
Note that the ``CONFIG_UPDATEABLE_IMAGE_NUMBER`` Kconfig option adjusts the number of image-pairs supported by the MCUboot.

The mapping of image number to partition is as follows:
* 0 and 1 - image-0, the primary slot of the first image.
* 2 - image-1, the secondary slot of the first image.
* 3 - image-2.
* 4 - image-3.

0 is a default upload target when no explicit selection is done.

### System-specific commands

Use the ``CONFIG_ENABLE_MGMT_PERUSER=y`` Kconfig option to enable the following additional commands:
* Storage erase - This command allows erasing the storage partition (enable with ``CONFIG_BOOT_MGMT_CUSTOM_STORAGE_ERASE=y``).

### More configuration

For details on other available configuration options for the serial recovery protocol, check the Kconfig options  (for example by using ``menuconfig``).
