---
id: "mcuboot-bootloader-image-swapping"
type: "concept"
domain: "boot-update"
title: "Bootloader: Image swapping"
summary: "The bootloader swaps the contents of the two image slots for two reasons:"
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@725d63c:docs/design.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/725d63c/docs/design.md#image-swapping"
license: "Apache-2.0"
mode: "V"
---

The bootloader swaps the contents of the two image slots for two reasons:

  * User has issued a "set pending" operation; the image in the secondary slot
    should be run once (state I) or repeatedly (state II), depending on
    whether a permanent swap was specified.
  * Test image rebooted without being confirmed; the bootloader should
    revert to the original image currently in the secondary slot (state III).

If the image trailers indicates that the image in the secondary slot should be
run, the bootloader needs to copy it to the primary slot.  The image currently
in the primary slot also needs to be retained in flash so that it can be used
later.  Furthermore, both images need to be recoverable if the bootloader
resets in the middle of the swap operation.  The two images are swapped
according to the following procedure:

1. Determine if both slots are compatible enough to have their images swapped.
   To be compatible, both have to have only sectors that can fit into the
   scratch area and if one of them has larger sectors than the other, it must
   be able to entirely fit some rounded number of sectors from the other slot.
   In the next steps we'll use the terminology "region" for the total amount of
   data copied/erased because this can be any amount of sectors depending on
   how many the scratch is able to fit for some swap operation.
2. Iterate the list of region indices in descending order (i.e., starting
   with the greatest index); only regions that are predetermined to be part of
   the image are copied; current element = "index".
    + a. Erase scratch area.
    + b. Copy secondary_slot[index] to scratch area.
        - If this is the last region in the slot, scratch area has a temporary
          status area initialized to store the initial state, because the
          primary slot's last region will have to be erased. In this case,
          only the data that was calculated to amount to the image is copied.
        - Else if this is the first swapped region but not the last region in
          the slot, initialize the status area in primary slot and copy the
          full region contents.
        - Else, copy entire region contents.
    + c. Write updated swap status (i).
    + d. Erase secondary_slot[index]
    + e. Copy primary_slot[index] to secondary_slot[index] according to amount
         previosly copied at step b.
        - If this is not the last region in the slot, erase the trailer in the
          secondary slot, to always use the one in the primary slot.
    + f. Write updated swap status (ii).
    + g. Erase primary_slot[index].
    + h. Copy scratch area to primary_slot[index] according to amount
         previously copied at step b.
        - If this is the last region in the slot, the status is read from
          scratch (where it was stored temporarily) and written anew in the
          primary slot.
    + i. Write updated swap status (iii).
3. Persist completion of swap procedure to the primary slot image trailer.

The additional caveats in step 2f are necessary so that the secondary slot image
trailer can be written by the user at a later time.  With the image trailer
unwritten, the user can test the image in the secondary slot
(i.e., transition to state I).

---
***Note***

*If the region being copied contains the last sector, then swap status is*
*temporarily maintained on scratch for the duration of this operation, always*
*using the primary slot's area otherwise.*

---
***Note***

*The bootloader tries to copy only used sectors (based on largest image*
*installed on any of the slots), minimizing the amount of sectors copied and*
*reducing the amount of time required for a swap operation.*

---

The particulars of step 3 vary depending on whether an image is being tested,
permanently used, reverted or a validation failure of the secondary slot
happened when a swap was requested:

    * test:
        o Write primary_slot.copy_done = 1
        (swap caused the following values to be written:
            primary_slot.magic = BOOT_MAGIC
            secondary_slot.magic = UNSET
            primary_slot.image_ok = Unset)

    * permanent:
        o Write primary_slot.copy_done = 1
        (swap caused the following values to be written:
            primary_slot.magic = BOOT_MAGIC
            secondary_slot.magic = UNSET
            primary_slot.image_ok = 0x01)

    * revert:
        o Write primary_slot.copy_done = 1
        o Write primary_slot.image_ok = 1
        (swap caused the following values to be written:
            primary_slot.magic = BOOT_MAGIC)

    * failure to validate the secondary slot:
        o Write primary_slot.image_ok = 1

After completing the operations as described above the image in the primary slot
should be booted.
