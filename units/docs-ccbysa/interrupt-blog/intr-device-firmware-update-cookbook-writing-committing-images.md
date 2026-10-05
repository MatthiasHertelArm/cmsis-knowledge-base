---
id: "intr-device-firmware-update-cookbook-writing-committing-images"
type: "concept"
domain: "debug"
title: "Device Firmware Update Cookbook: Design Patterns & Recipes / Writing & Committing Images"
summary: "Writing a new firmware image is the whole purpose of this exercise, so how do we do the deed?"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-06-23-device-firmware-update-cookbook.md"
doc_source: "https://interrupt.memfault.com/blog/device-firmware-update-cookbook#writing-committing-images"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Design Patterns & Recipes_

Writing a new firmware image is the whole purpose of this exercise, so how do we
do the deed? We won't cover *transferring* the image over to your firmware,
that varies greatly depending on your use, but once the transfer has occurred
we must:

1. Write the image
2. Verify it, and
3. Mark it as valid.

At the high level, here's our flow:

```c
int perform_update(void *fw_payload, size_t fw_payload_len) {
    uint8_t *data_ptr = fw_payload;
    image_hdr_t *hdr = (image_hdr_t *)data_ptr;
    data_ptr += sizeof(image_hdr_t);

    if (dfu_write_data(IMAGE_SLOT_2,
                data_ptr,
                fw_payload_len)) {
        return -1;
    }

    if (image_validate(IMAGE_SLOT_2, hdr)) {
        return -1;
    };

    if (dfu_commit_image(IMAGE_SLOT_2, hdr)) {
        return -1;
    };

    scb_reset_system();
    __builtin_unreachable();
}
```

Writing the data is relatively straightforward. For flash memory, you'll
typically erase the relevant sector, then use the `page_program` function
provided with your flash driver to write new data. Make sure however that you do
not write the image header during this process. The header will only be written
during the "commit" phase.

We've covered how to verify an image in the previous section. Here again, we may
check the CRC, or verify a cryptographic signature.

If at any point the update is interrupted, the header will be missing and our
Loader will refuse to load the image. Once everything checks out, we *commit* the
image by writing the header. This marks the image as valid and allows it to be
loaded.

Here is my implementation of the `commit` step, it's nothing too complicated:

```c
int dfu_commit_image(image_slot_t slot, const image_hdr_t *hdr) {
    uint32_t addr = (uint32_t)(slot == IMAGE_SLOT_1 ?
                               &__slot1rom_start__ : &__slot2rom_start__);

    uint8_t *data_ptr = (uint8_t *)hdr;
    for (int i = 0; i < sizeof(image_hdr_t); ++i) {
        flash_program_byte(addr + i, data_ptr[i]);
    }

    return 0;
}
```

Just as writing the header marks an image as valid, we can invalidate an
image simply by zeroing it out. This is much faster than erasing the whole
flash, and won't leave us in a half-working state (e.g. having erased only half
of the image).

```c
int dfu_invalidate_image(image_slot_t slot) {
    // We just write 0s over the image header
    uint32_t addr = (uint32_t)(slot == IMAGE_SLOT_1 ?
                               &__slot1rom_start__ : &__slot2rom_start__);
    for (int i = 0; i < sizeof(image_hdr_t); ++i) {
        flash_program_byte(addr + i, 0);
    }

    return 0;
}
```
