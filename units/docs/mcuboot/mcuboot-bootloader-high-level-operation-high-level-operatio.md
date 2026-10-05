---
id: "mcuboot-bootloader-high-level-operation-high-level-operatio"
type: "concept"
domain: "boot-update"
title: "Bootloader: [High-level operation](#high-level-operation)"
summary: "With the terms defined, we can now explore the bootloader's operation. First, a high-level overview of the boot process is presented. Then, the following sections describe each step of the process in more detail."
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@ba2099f:docs/design.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/ba2099f/docs/design.md#high-level-operation-high-level-operation"
license: "Apache-2.0"
mode: "V"
---

With the terms defined, we can now explore the bootloader's operation.  First,
a high-level overview of the boot process is presented.  Then, the following
sections describe each step of the process in more detail.

Procedure:

1. Inspect swap status region; is an interrupted swap being resumed?
    + Yes: Complete the partial swap operation; skip to step 3.
    + No: Proceed to step 2.

2. Inspect image trailers; is a swap requested?
    + Yes:
        1. Is the requested image valid (integrity and security check)?
            + Yes.
                a. Perform swap operation.
                b. Persist completion of swap procedure to image trailers.
                c. Proceed to step 3.
            + No.
                a. Erase invalid image.
                b. Persist failure of swap procedure to image trailers.
                c. Proceed to step 3.

    + No: Proceed to step 3.

3. Boot into image in primary slot.

### [Multiple image boot](#multiple-image-boot)

When the flash contains multiple executable images the bootloader's operation
is a bit more complex but similar to the previously described procedure with
one image. Every image can be updated independently therefore the flash is
partitioned further to arrange two slots for each image.
```
+--------------------+
| MCUboot            |
+--------------------+
        ~~~~~            <- memory might be not contiguous
+--------------------+
| Image 0            |
| primary   slot     |
+--------------------+
| Image 0            |
| secondary slot     |
+--------------------+
        ~~~~~            <- memory might be not contiguous
+--------------------+
| Image N            |
| primary   slot     |
+--------------------+
| Image N            |
| secondary slot     |
+--------------------+
| Scratch            |
+--------------------+
```
MCUboot is also capable of handling dependencies between images. For example
if an image needs to be reverted it might be necessary to revert another one too
(e.g. due to API incompatibilities) or simply to prevent from being updated
because of an unsatisfied dependency. Therefore all aborted swaps have to be
completed and all the swap types have to be determined for each image before
the dependency checks. Dependency handling is described in more detail in a
following section. The multiple image boot procedure is organized in loops which
iterate over all the firmware images. The high-level overview of the boot
process is presented below.

+  Loop 1. Iterate over all images
    1. Inspect swap status region of current image; is an interrupted swap being
       resumed?
        + Yes:
            + Review the validity of previously determined swap types
              of other images.
            + Complete the partial swap operation.
            + Mark the swap type as `None`.
            + Skip to next image.
        + No: Proceed to step 2.

    2. Inspect image trailers in the primary and secondary slot; is an image
       swap requested?
        + Yes: Review the validity of previously determined swap types of other
               images. Is the requested image valid (integrity and security
               check)?
            + Yes:
                + Set the previously determined swap type for the current image.
                + Skip to next image.
            + No:
                + Erase invalid image.
                + Persist failure of swap procedure to image trailers.
                + Mark the swap type as `Fail`.
                + Skip to next image.
        + No:
            + Mark the swap type as `None`.
            + Skip to next image.

+  Loop 2. Iterate over all images
    1. Does the current image depend on other image(s)?
        + Yes: Are all the image dependencies satisfied?
            + Yes: Skip to next image.
            + No:
                + Modify swap type depending on what the previous type was.
                + Restart dependency check from the first image.
        + No: Skip to next image.

+  Loop 3. Iterate over all images
    1. Is an image swap requested?
        + Yes:
            + Perform image update operation.
            + Persist completion of swap procedure to image trailers.
            + Skip to next image.
        + No: Skip to next image.

+  Loop 4. Iterate over all images
    1. Validate image in the primary slot (integrity and security check) or
       at least do a basic sanity check to avoid booting into an empty flash
       area.

+ Boot into image in the primary slot of the 0th image position\
  (other image in the boot chain is started by another image).

### [Multiple image boot for RAM loading and direct-xip](#multiple-image-boot-for-ram-loading-and-direct-xip)

The operation of the bootloader is different when the ram-load or the
direct-xip strategy is chosen. The flash map is very similar to the swap
strategy but there is no need for Scratch area.

+  Loop 1. Until all images are loaded and all dependencies are satisfied
    1. Subloop 1. Iterate over all images
        + Does any of the slots contain an image?
            + Yes:
                + Choose the newer image.
                + Copy it to RAM in case of ram-load strategy.
                + Validate the image (integrity and security check).
                + If validation fails delete the image from flash and try the other
                  slot. (Image must be deleted from RAM too in case of ram-load
                  strategy.)
            + No: Return with failure.

    2. Subloop 2. Iterate over all images
        + Does the current image depend on other image(s)?
            + Yes: Are all the image dependencies satisfied?
                + Yes: Skip to next image.
                + No:
                    + Delete the image from RAM in case of ram-load strategy, but
                      do not delete it from flash.
                    + Try to load the image from the other slot.
                    + Restart dependency check from the first image.
            + No: Skip to next image.

+  Loop 2. Iterate over all images
    + Increase the security counter if needed.
    + Do the measured boot and the data sharing if needed.

+ Boot the loaded slot of image 0.
