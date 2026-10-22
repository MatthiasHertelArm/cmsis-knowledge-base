---
id: "mcuboot-bootloader-boot-swap-types"
type: "concept"
domain: "boot-update"
title: "Bootloader: Boot swap types"
summary: "When the device first boots under normal circumstances, there is an up-to-date firmware image in each primary slot, which MCUboot can validate and then chain-load. In this case, no image swaps are necessary."
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@725d63c:docs/design.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/725d63c/docs/design.md#boot-swap-types"
license: "Apache-2.0"
mode: "V"
---

When the device first boots under normal circumstances, there is an up-to-date
firmware image in each primary slot, which MCUboot can validate and then
chain-load. In this case, no image swaps are necessary. During device upgrades,
however, new candidate image(s) is present in the secondary slot(s), which
MCUboot must swap into the primary slot(s) before booting as discussed above.

Upgrading an old image with a new one by swapping can be a two-step process. In
this process, MCUboot performs a "test" swap of image data in flash and boots
the new image or it will be executed during operation. The new image can then
update the contents of flash at runtime to mark itself "OK", and MCUboot will
then still choose to run it during the next boot. When this happens, the swap is
made "permanent". If this doesn't happen, MCUboot will perform a "revert" swap
during the next boot by swapping the image(s) back into its original location(s)
, and attempting to boot the old image(s).

Depending on the use case, the first swap can also be made permanent directly.
In this case, MCUboot will never attempt to revert the images on the next reset.

Test swaps are supported to provide a rollback mechanism to prevent devices
from becoming "bricked" by bad firmware.  If the device crashes immediately
upon booting a new (bad) image, MCUboot will revert to the old (working) image
at the next device reset, rather than booting the bad image again. This allows
device firmware to make test swaps permanent only after performing a self-test
routine.

On startup, MCUboot inspects the contents of flash to decide for each images
which of these "swap types" to perform; this decision determines how it
proceeds.

The possible swap types, and their meanings, are:

- `BOOT_SWAP_TYPE_NONE`: The "usual" or "no upgrade" case; attempt to boot the
  contents of the primary slot.

- `BOOT_SWAP_TYPE_TEST`: Boot the contents of the secondary slot by swapping
  images.  Unless the swap is made permanent, revert back on the next boot.

- `BOOT_SWAP_TYPE_PERM`: Permanently swap images, and boot the upgraded image
  firmware.

- `BOOT_SWAP_TYPE_REVERT`: A previous test swap was not made permanent;
  swap back to the old image whose data are now in the secondary slot.  If the
  old image marks itself "OK" when it boots, the next boot will have swap type
  `BOOT_SWAP_TYPE_NONE`.

- `BOOT_SWAP_TYPE_FAIL`: Swap failed because image to be run is not valid.

- `BOOT_SWAP_TYPE_PANIC`: Swapping encountered an unrecoverable error.

The "swap type" is a high-level representation of the outcome of the
boot. Subsequent sections describe how MCUboot determines the swap type from
the bit-level contents of flash.

### [Revert mechanism in direct-xip and ram-load mode](#direct-xip-ram-load-revert)

The direct-xip and ram-load modes also support a "revert" mechanism which is the
equivalent of the swap mode's "revert" swap. When the direct-xip mode is
selected it can be enabled with the `MCUBOOT_DIRECT_XIP_REVERT` config option.
In ram-load mode, the feature is enabled with `MCUBOOT_RAM_LOAD_REVERT` config
option.  Note that an image trailer must also be added to the signed images (the
"--pad" option of the `imgtool` script must be used). Otherwise, MCUboot will
not recognize the image as valid and will attempt to revert it. For more
information on this please read the [Image Trailer](#image-trailer) section and
the [imgtool](https://github.com/mcu-tools/mcuboot/blob/725d63c/docs/imgtool.md) documentation. Making the images permanent (marking
them as confirmed in advance) is also supported just like in swap mode. The
individual steps of this "revert" mechanism are the following:

1. Select the slot which holds the newest potential image, based on the
   version number
2. Was the image previously selected to run (during a previous boot)?
    + Yes: Did the image mark itself "OK" (was the self-test successful)?
        + Yes.
            - Proceed to step 3.
        + No.
            - Erase the image from the slot to prevent it from being selected
              again during the next boot.
            - Return to step 1 (the bootloader will attempt to select and
              possibly boot the previous image if there is one).
    + No.
        - Mark the image as "selected" (set the copy_done flag in the trailer).
        - Proceed to step 3.
3. Proceed to image validation ...
