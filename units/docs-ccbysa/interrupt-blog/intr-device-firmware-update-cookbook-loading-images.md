---
id: "intr-device-firmware-update-cookbook-loading-images"
type: "concept"
domain: "debug"
title: "Device Firmware Update Cookbook: Design Patterns & Recipes / Loading Images"
summary: "Both the Bootloader and the Loader need to load firmware images and start them. This includes:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-06-23-device-firmware-update-cookbook.md"
doc_source: "https://interrupt.memfault.com/blog/device-firmware-update-cookbook#loading-images"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Design Patterns & Recipes_

Both the Bootloader and the Loader need to load firmware images and start them.
This includes:

1. Locating them
2. Verifying them, and
3. Starting them.

The code may look something like this:

```c
// boot.c
for (image_slot_t slot = IMAGE_SLOT_1; slot < IMAGE_NUM_SLOTS; ++slot) {
    const image_hdr_t *hdr = image_get_header(slot);
    if (hdr == NULL) {
        continue;
    }
    if (image_validate(slot, hdr) != 0) {
        continue;
    }

    printf("Booting slot %d\n", slot);
    image_start(hdr);
}

// No image found, go into DFU mode
```

Here our approach to locating images is simple: we use hardcoded "slots" where
we expect images. Slot 1 is at `0x8004000`, and slot 2 is at `0x8020000`. We
simply iterate through the slots looking for valid headers.

Remember that the first field of our image header is the "magic" value. In
`image_get_header` we read the header and verify the magic value.

```c
// image.c
const image_hdr_t *image_get_header(image_slot_t slot) {
    const image_hdr_t *hdr = NULL;

    switch (slot) {
        case IMAGE_SLOT_1:
            hdr = (const image_hdr_t *)&__slot1rom_start__;
            break;
        case IMAGE_SLOT_2:
            hdr = (const image_hdr_t *)&__slot2rom_start__;
            break;
        default:
            break;
    }

    if (hdr && hdr->image_magic == IMAGE_MAGIC) {
        return hdr;
    } else {
        return NULL;
    }
}
```

To validate the image, we compute its CRC and compare it with the value written
in the header. This will allow you to catch data corruption or bit errors, and
save you some trouble down the line. Note that verifying CRC on boot is not
appropriate for every application, as it can slow down boot significantly.

```c
int image_validate(image_slot_t slot, const image_hdr_t *hdr) {
    void *addr = (slot == IMAGE_SLOT_1 ? &__slot1rom_start__ : &__slot2rom_start__);
    addr += sizeof(image_hdr_t);
    uint32_t len = hdr->data_size;
    uint32_t a = crc32(addr, len);
    uint32_t b = hdr->crc;
    if (a == b) {
        return 0;
    } else {
        printf("CRC Mismatch: %lx vs %lx\n", a, b);
        return -1;
    }
}
```

Last but not least we start the image by extracting the vector table address
from the header, writing it to the `VTOR` register (which tells the chip that
the vector table address has moved), and branching to it with a bit of assembly.

```c
static void prv_start_image(void *pc, void *sp) {
    __asm("           \n\
          msr msp, r1 \n\
          bx r0       \n\
    ");
}

void image_start(const image_hdr_t *hdr) {
    const vector_table_t *vectors = (const vector_table_t *)hdr->vector_addr;
    SCB_VTOR = (uint32_t)vectors;
    prv_start_image(vectors->reset, vectors->initial_sp_value);
     __builtin_unreachable();
}
```

If no image is found, the loader should go into DFU mode and waits for a new image to
be transferred.

> Note: The `VTOR` register is available on the Cortex-M0+,M3,M4,M7, but not on
> the older M0. Unfortunately, this makes building a bootloader much more
> complicated on that platform.
