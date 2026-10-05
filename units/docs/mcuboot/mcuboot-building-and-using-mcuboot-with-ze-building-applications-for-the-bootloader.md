---
id: "mcuboot-building-and-using-mcuboot-with-ze-building-applications-for-the-bootloader"
type: "concept"
domain: "boot-update"
title: "Building and using MCUboot with Zephyr: Building applications for the bootloader (manually)"
summary: "In addition to flash partitions in DTS, some additional configuration is required to build applications for MCUboot."
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@ba2099f:docs/readme-zephyr.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/ba2099f/docs/readme-zephyr.md#building-applications-for-the-bootloader-manually"
license: "Apache-2.0"
mode: "V"
---

In addition to flash partitions in DTS, some additional configuration
is required to build applications for MCUboot.

This is handled internally by the Zephyr configuration system and is wrapped
in the `CONFIG_BOOTLOADER_MCUBOOT` Kconfig variable, which must be enabled in
the application's `prj.conf` file.

The directory `samples/subsys/mgmt/mcumgr/smp_svr` in the Zephyr tree contains
a simple application with everything you need. You can try it on your
board and then just make a copy of it to get started on your own
application; see samples/zephyr/README.md for a tutorial.

The Zephyr `CONFIG_BOOTLOADER_MCUBOOT` configuration option
[documentation](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOOTLOADER_MCUBOOT)
provides additional details regarding the changes it makes to the image
placement and generation in order for an application to be bootable by MCUboot.

With this, build the application as your normally would.

### Signing the application (manually)

In order to upgrade to an image (or even boot it, if
`MCUBOOT_VALIDATE_PRIMARY_SLOT` is enabled), the images must be signed.
To make development easier, MCUboot is distributed with some example
keys.  It is important to stress that these should never be used for
production, since the private key is publicly available in this
repository.  See below on how to make your own signatures.

With Zephyr images, they will be signed automatically by the build system if
`CONFIG_MCUBOOT_SIGNATURE_KEY_FILE` is set to the private key signing file, so
no manual steps are necessary in this case.

To sign images manually, use the `scripts/imgtool.py` script.  It is best
to look at `samples/zephyr/Makefile` for examples on how to use this.

### Flashing the application

The application itself can flashed with regular flash tools, but will
need to be programmed at the offset of the primary slot for this particular
target. Depending on the platform and flash tool you might need to manually
specify a flash offset corresponding to the primary slot starting address. This
is usually not relevant for flash tools that use Intel Hex images (.hex) instead
of raw binary images (.bin) since the former include destination address
information. Additionally you will need to make sure that the flash tool does
not perform a mass erase (erasing the whole of the flash) or else you would be
deleting MCUboot.
These images can also be marked for upgrade, and loaded into the secondary slot,
at which point the bootloader should perform an upgrade.  It is up to
the image to mark the primary slot as "image ok" before the next reboot,
otherwise the bootloader will revert the application.
