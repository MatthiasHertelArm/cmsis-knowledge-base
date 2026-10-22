---
id: "mcuboot-bootloader-reset-recovery"
type: "concept"
domain: "boot-update"
title: "Bootloader: Reset recovery"
summary: "If the bootloader resets in the middle of a swap operation, the two images may be discontiguous in flash. Bootutil recovers from this condition by using the image trailers to determine how the image parts are distributed in flash."
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@725d63c:docs/design.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/725d63c/docs/design.md#reset-recovery"
license: "Apache-2.0"
mode: "V"
---

If the bootloader resets in the middle of a swap operation, the two images may
be discontiguous in flash.  Bootutil recovers from this condition by using the
image trailers to determine how the image parts are distributed in flash.

The first step is determine where the relevant swap status region is located.
Because this region is embedded within the image slots, its location in flash
changes during a swap operation.  The below set of tables map image trailers
contents to swap status location.  In these tables, the "source" field
indicates where the swap status region is located. In case of multi image boot
the images primary area and the single scratch area is always examined in pairs.
If swap status found on scratch area then it might not belong to the current
image. The swap_info field of swap status stores the corresponding image number.
If it does not match then "source: none" is returned.

```
              | primary slot | scratch      |
    ----------+--------------+--------------|
        magic | Good         | Any          |
    copy-done | 0x01         | N/A          |
    ----------+--------------+--------------'
    source: none                            |
    ----------------------------------------'

              | primary slot | scratch      |
    ----------+--------------+--------------|
        magic | Good         | Any          |
    copy-done | 0xff         | N/A          |
    ----------+--------------+--------------'
    source: primary slot                    |
    ----------------------------------------'

              | primary slot | scratch      |
    ----------+--------------+--------------|
        magic | Any          | Good         |
    copy-done | Any          | N/A          |
    ----------+--------------+--------------'
    source: scratch                         |
    ----------------------------------------'

              | primary slot | scratch      |
    ----------+--------------+--------------|
        magic | Unset        | Any          |
    copy-done | 0xff         | N/A          |
    ----------+--------------+--------------|
    source: primary slot                    |
    ----------------------------------------+------------------------------+
    This represents one of two cases:                                      |
    o No swaps ever (no status to read, so no harm in checking).           |
    o Mid-revert; status in the primary slot.                              |
    For this reason we assume the primary slot as source, to trigger a     |
    check of the status area and find out if there was swapping under way. |
    -----------------------------------------------------------------------'
```

If the swap status region indicates that the images are not contiguous, MCUboot
determines the type of swap operation that was interrupted by reading the `swap
info` field in the active image trailer and extracting the swap type from bits
0-3 then resumes the operation. In other words, it applies the procedure defined
in the previous section, moving image 1 into the primary slot and image 0 into
the secondary slot. If the boot status indicates that an image part is present
in the scratch area, this part is copied into the correct location by starting
at step e or step h in the area-swap procedure, depending on whether the part
belongs to image 0 or image 1.

After the swap operation has been completed, the bootloader proceeds as though
it had just been started.
