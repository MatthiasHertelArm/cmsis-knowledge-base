---
id: "mcuboot-porting-how-to-main-app-and-calling-the-bootloader"
type: "concept"
domain: "boot-update"
title: "Porting how-to: Main app and calling the bootloader"
summary: "From the perspective of the target OS, the bootloader can be seen as a library, so an entry point must be provided."
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@ba2099f:docs/PORTING.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/ba2099f/docs/PORTING.md#main-app-and-calling-the-bootloader"
license: "Apache-2.0"
mode: "V"
---

From the perspective of the target OS, the bootloader can be seen as a library,
so an entry point must be provided. This is likely a typical `app` for the
target OS, and it must call the following function to run the bootloader:

```c
int boot_go(struct boot_rsp *rsp);
```

This function is located at `boot/bootutil/loader.c` and receives a `struct
boot_rsp` pointer. The `struct boot_rsp` is defined as:

```c
struct boot_rsp {
    /** A pointer to the header of the image to be executed. */
    const struct image_header *br_hdr;

    /**
     * The flash offset of the image to execute.  Indicates the position of
     * the image header.
     */
    uint8_t br_flash_id;
    uint32_t br_image_addr;
};
```

After running the management functions of the bootloader, `boot_go` returns
an initialized `boot_rsp` which has pointers to the location of the image
where the target firmware is located which can be used to jump to.
