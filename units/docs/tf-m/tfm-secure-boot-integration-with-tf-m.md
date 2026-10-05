---
id: "tfm-secure-boot-integration-with-tf-m"
type: "concept"
domain: "security"
title: "Secure boot: Integration with TF-M"
summary: "MCUBoot assumes a predefined memory layout which is described below (applicable for AN521). It is mandatory to define the primary slot and the secondary slot partitions, but their size and location can be changed::"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/booting/tfm_secure_boot.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/booting/tfm_secure_boot.html#integration-with-tf-m"
license: "BSD-3-Clause"
mode: "V"
---

MCUBoot assumes a predefined memory layout which is described below (applicable
for AN521). It is mandatory to define the primary slot and the secondary slot
partitions, but their size and location can be changed::
```
- 0x0000_0000 - 0x0007_FFFF:    BL2 bootloader - MCUBoot
- 0x0008_0000 - 0x000F_FFFF:    Primary slot : Single binary blob:
                                Secure + Non-Secure image;
                                Primary memory partition
  - 0x0008_0000 - 0x0008_03FF:  Common image header
  - 0x0008_0400 - 0x0008_xxxx:  Secure image
  - 0x0008_xxxx - 0x0010_03FF:  Padding (with 0xFF)
  - 0x0010_0400 - 0x0010_xxxx:  Non-secure image
  - 0x0010_xxxx - 0x0010_xxxx:  Hash value(SHA256), RSA signature and other
                                metadata of combined image

- 0x0018_0000 - 0x0027_FFFF:    Secondary slot : Secure + Non-Secure image;
                                Secondary memory partition, structured
                                identically to the primary slot
- 0x0028_0000 - 0x0037_FFFF:    Scratch area, only used during image
                                swapping
```
Multiple image boot requires a slightly different layout::
```
- 0x0000_0000 - 0x0007_FFFF:    BL2 bootloader - MCUBoot
- 0x0008_0000 - 0x000F_FFFF:    Primary slot : Secure image
  - 0x0008_0000 - 0x0008_03FF:  Secure image header
  - 0x0008_0400 - 0x000x_xxxx:  Secure image
  - 0x000x_xxxx - 0x000x_xxxx:  Hash value(SHA256), RSA signature and other
                                metadata of secure image

- 0x0010_0000 - 0x0017_FFFF:    Primary slot : Non-secure image
  - 0x0010_0000 - 0x0010_03FF:  Non-secure image header
  - 0x0010_0400 - 0x001x_xxxx:  Non-secure image
  - 0x001x_xxxx - 0x001x_xxxx:  Hash value(SHA256), RSA signature and other
                                metadata of non-secure image

- 0x0018_0000 - 0x001F_FFFF:    Secondary slot : Secure image
- 0x0020_0000 - 0x0027_FFFF:    Secondary slot : Non-secure image

- 0x0028_0000 - 0x002F_FFFF:    Scratch area, only used during image
                                swapping, used for secure and non-secure
                                image as well

## Firmware upgrade operation

MCUBoot handles only the firmware authenticity check after start-up and the
firmware switch part of the firmware update process. Downloading the new version
of the firmware is out-of-scope for MCUBoot. MCUBoot supports three different
ways to switch to the new firmware and it is assumed that firmware images are
executed-in-place (XIP). The default behaviour is the overwrite-based image
upgrade. In this case the active firmware is always executed from the primary
slot and the secondary slot is a staging area for new images. Before executing
the new firmware image, the content of the primary slot must be overwritten with
the content of the secondary slot (the new firmware image). The second option is
the image swapping strategy when the content of the two memory slots must be
physically swapped. This needs the scratch area to be defined in the memory
layout. The third option is the direct execute-in-place version, which
eliminates the complexity of image swapping and its administration. Active image
can be executed from either memory slot, but new firmware must be linked to the
address space of the proper (currently inactive) memory slot.


### Overwrite operation

Active image is stored in the primary slot, and this image is started always by
the bootloader. Therefore images must be linked to the primary slot. If the
bootloader finds a valid image in the secondary slot, which is marked for
upgrade, then the content of the primary slot will be simply overwritten with
the content of the secondary slot, before starting the new image from the
primary slot. After the content of the primary slot has been successfully
overwritten, the header and trailer of the new image in the secondary slot is
erased to prevent the triggering of another unnecessary image upgrade after a
restart. The overwrite operation is fail-safe and resistant to power-cut
failures. For more details please refer to the MCUBoot
[documentation](https://docs.mcuboot.com/).


### Swapping operation

This operation can be set with the `MCUBOOT_UPGRADE_STRATEGY` compile time
switch (see Build time configuration). With swapping image upgrade strategy
the active image is also stored in the primary slot and it will always be
started by the bootloader. If the bootloader finds a valid image in the
secondary slot, which is marked for upgrade, then contents of the primary slot
and the secondary slot will be swapped, before starting the new image from the
primary slot. Scratch area is used as a temporary storage place during image
swapping. Update mark from the secondary slot is removed when the swapping is
successful. The boot loader can revert the swapping as a fall-back mechanism to
recover the previous working firmware version after a faulty update. The swap
operation is fail-safe and resistant to power-cut failures. For more details
please refer to the MCUBoot
[documentation](https://docs.mcuboot.com/).


After a successful image upgrade, user can mark the image as "OK"
at runtime by explicitly calling `psa_fwu_accept`. When this happens,
the swap is made "permanent" and MCUBoot will then still choose to run it
during the next boot.

TF-M does not set the image_ok flag, because it is user's duty to determine
whether the image is acceptable. Therefore the bootloader will always
perform a "revert" (swap the images back) during the next boot.

### Direct execute-in-place operation

This operation can be set with the `MCUBOOT_UPGRADE_STRATEGY` compile time
switch (see Build time configuration). When enabling direct-xip operation
then the active image flag is moved between slots during firmware upgrade. If
firmware is executed-in-place (XIP), then two firmware images must be generated.
One of them is linked to be executed from the primary slot memory region and the
other from the secondary slot. The firmware upgrade client, which downloads the
new image, must be aware, which slot hosts the active firmware and which acts as
a staging area and it is responsible for downloading the proper firmware image.
At boot time MCUBoot inspects the version number in the image header and passes
execution to the newer firmware version. New image must be marked for upgrade
which is automatically done by Python scripts at compile time. Image
verification is done the same way in all operational modes. If new image fails
during authentication then MCUBoot erases the memory slot and starts the other
image, after successful authentication.

To select which slot the image is to be executed from, set
`MCUBOOT_EXECUTION_SLOT` to the desired index. It is suggested that you create
two build directories when building images using this mode, as intermediate
dependencies cannot be reused due to changes in the flash layout.


Only single image boot is supported with direct-xip upgrade mode.

### RAM Loading firmware upgrade

Musca-S supports an image upgrade mode that is separate to the other (overwrite,
swapping and dirext-xip) modes. This is the `RAM load` mode (please refer
to the table below). Like the direct-xip mode, this selects the newest image
by reading the image version numbers in the image headers, but instead of
executing it in place, the newest image is copied to RAM for execution. The load
address, the location in RAM where the image is copied to, is stored in the
image header.


### Summary of different modes for image upgrade

Different implementations of the image upgrade operation (whether through
overwriting, swapping, direct-xip or loading into RAM and executing from
there) are supported by the platforms. The table below shows which of these
modes are supported by which platforms:

+---------------------+-----------------+----------------------------------------------------------+
|                     | Without BL2 [1]_| With BL2 [2]_                                            |
+=====================+=================+===============+==========+================+==============+
|                     | XIP             | XIP           | XIP      | XIP            | Not XIP      |
+---------------------+-----------------+---------------+----------+----------------+--------------+
|                     |                 | Overwrite [3]_| Swap [4]_| direct-xip [5]_| RAM load [6]_|
+---------------------+-----------------+---------------+----------+----------------+--------------+
| AN521               | Yes             | Yes           | Yes      | Yes            | No           |
+---------------------+-----------------+---------------+----------+----------------+--------------+
| AN519               | Yes             | Yes           | Yes      | Yes            | No           |
+---------------------+-----------------+---------------+----------+----------------+--------------+
| FVP_SSE300_MPS3     | No              | Yes           | Yes      | Yes            | No           |
+---------------------+-----------------+---------------+----------+----------------+--------------+
| Corstone-310 FVP    | Yes             | Yes           | Yes      | Yes            | No           |
+---------------------+-----------------+---------------+----------+----------------+--------------+
| LPC55S69            | Yes             | Yes           | No       | Yes            | No           |
+---------------------+-----------------+---------------+----------+----------------+--------------+
| Musca-B1            | Yes             | Yes           | Yes      | Yes            | No           |
+---------------------+-----------------+---------------+----------+----------------+--------------+
| AN524               | Yes             | No            | No       | Yes            | No           |
+---------------------+-----------------+---------------+----------+----------------+--------------+
| AN547               | No              | Yes           | Yes      | Yes            | No           |
+---------------------+-----------------+---------------+----------+----------------+--------------+
| AN552               | No              | Yes           | Yes      | Yes            | No           |
+---------------------+-----------------+---------------+----------+----------------+--------------+
| PSoC64              | Yes             | No            | No       | No             | No           |
+---------------------+-----------------+---------------+----------+----------------+--------------+
| STM_DISCO_L562QE    | No              | Yes           | No       | No             | No           |
+---------------------+-----------------+---------------+----------+----------------+--------------+
| STM_NUCLEO_L552ZE_Q | No              | Yes           | No       | No             | No           |
+---------------------+-----------------+---------------+----------+----------------+--------------+
| nRF9160 DK          | Yes             | Yes           | No       | No             | No           |
+---------------------+-----------------+---------------+----------+----------------+--------------+
| nRF5340 DK          | Yes             | Yes           | No       | No             | No           |
+---------------------+-----------------+---------------+----------+----------------+--------------+
| RSE                 | No              | No            | No       | No             | Yes          |
+---------------------+-----------------+---------------+----------+----------------+--------------+
| LP_MSPM33C321A      | Yes             | No            | No       | No             | No           |
+---------------------+-----------------+---------------+----------+----------------+--------------+

.. [1] To disable BL2, please set the `BL2` cmake option to `OFF`

.. [2] BL2 is enabled by default

.. [3] The image executes in-place (XIP) and is in Overwrite mode for image
    update by default

.. [4] To enable XIP Swap mode, assign the "SWAP_USING_SCRATCH" or
    "SWAP_USING_MOVE" string to the `MCUBOOT_UPGRADE_STRATEGY`
    configuration variable in the build configuration file, or include this
    macro definition in the command line

.. [5] To enable direct-xip, assign the "DIRECT_XIP" string to the
    `MCUBOOT_UPGRADE_STRATEGY` configuration variable in the build
    configuration file, or include this macro definition in the command line

.. [6] To enable RAM load, assign the "RAM_LOAD" string to the
    `MCUBOOT_UPGRADE_STRATEGY` configuration variable in the build
    configuration file, or include this macro definition in the command line


## Multiple image boot

It is possible to update the firmware images independently to support the
scenario when secure and non-secure images are provided by different vendors.
Multiple image boot is supported only together with the overwrite and swap
firmware upgrade modes.

It is possible to describe the dependencies of the images on each other in
order to avoid a faulty upgrade when incompatible versions would be installed.
These dependencies are part of the image manifest area.
The dependencies are composed from two parts:

 - **Image identifier:** The number of the image which the current image (whose
   manifest area contains the dependency entry) depends on. The image identifier
   starts from 0.

 - **Minimum version:** The minimum version of other image must be present on
   the device by the end of the upgrade (both images might be updated at the
   same time).

Dependencies can be added to the images at compile time with the following
compile time switches:

 - `MCUBOOT_S_IMAGE_MIN_VER` It is added to the non-secure image and specifies the
   minimum required version of the secure image.
 - `MCUBOOT_NS_IMAGE_MIN_VER` It is added to the secure image and specifies the
   minimum required version of the non-secure image.

Example of how to provide the secure image minimum version::
```
cmake -DTFM_PLATFORM=arm/musca_b1 -DMCUBOOT_S_IMAGE_MIN_VER=1.2.3+4 ..
