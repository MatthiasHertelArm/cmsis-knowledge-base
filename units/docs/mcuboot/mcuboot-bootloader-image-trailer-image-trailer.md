---
id: "mcuboot-bootloader-image-trailer-image-trailer"
type: "concept"
domain: "boot-update"
title: "Bootloader: [Image trailer](#image-trailer)"
summary: "For the bootloader to be able to determine the current state and what actions should be taken during the current boot operation, it uses metadata stored in the image flash areas."
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@ba2099f:docs/design.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/ba2099f/docs/design.md#image-trailer-image-trailer"
license: "Apache-2.0"
mode: "V"
---

For the bootloader to be able to determine the current state and what actions
should be taken during the current boot operation, it uses metadata stored in
the image flash areas. While swapping, some of this metadata is temporarily
copied into and out of the scratch area.

This metadata is located at the end of the image flash areas, and is called an
image trailer. An image trailer has the following structure:

```
     0                   1                   2                   3
     0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    ~                                                               ~
    ~    Swap status (BOOT_MAX_IMG_SECTORS * min-write-size * 3)    ~
    ~                                                               ~
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |                 Encryption key 0 (16 octets) [*]              |
    |                                                               |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |                    0xff padding as needed                     |
    |  (BOOT_MAX_ALIGN minus 16 octets from Encryption key 0) [*]   |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |                 Encryption key 1 (16 octets) [*]              |
    |                                                               |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |                    0xff padding as needed                     |
    |  (BOOT_MAX_ALIGN minus 16 octets from Encryption key 1) [*]   |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |                      Swap size (4 octets)                     |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |                    0xff padding as needed                     |
    |        (BOOT_MAX_ALIGN minus 4 octets from Swap size)         |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |   Unprotected TLV size [*2]   |   Unprotected TLV size [*2]   |
    |   Secondary slot (2 octets)   |    Primary slot (2 octets)    |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |                  0xff padding as needed [*2]                  |
    |  (BOOT_MAX_ALIGN minus 4 octets from unprotected TLV sizes)   |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |   Swap info   |  0xff padding (BOOT_MAX_ALIGN minus 1 octet)  |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |   Copy done   |  0xff padding (BOOT_MAX_ALIGN minus 1 octet)  |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |   Image OK    |  0xff padding (BOOT_MAX_ALIGN minus 1 octet)  |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |                    0xff padding as needed                     |
    |         (BOOT_MAX_ALIGN minus 16 octets from MAGIC)           |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |                       MAGIC (16 octets)                       |
    |                                                               |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

[*]: Only present if the encryption option is enabled (`MCUBOOT_ENC_IMAGES`).
[*2]: Only present if swap using offset mode is used (`MCUBOOT_SWAP_USING_OFFSET`).

The offset immediately following such a record represents the start of the next
flash area.

---
***Note***

*"min-write-size" is a property of the flash hardware.  If the hardware*
*allows individual bytes to be written at arbitrary addresses, then*
*min-write-size is 1.  If the hardware only allows writes at even addresses,*
*then min-write-size is 2, and so on.*

---

An image trailer contains the following fields:

1. Swap status: A series of records which records the progress of an image
   swap.  To swap entire images, data are swapped between the two image areas
   one or more sectors at a time, like this:

   - sector data in the primary slot is copied into scratch, then erased
   - sector data in the secondary slot is copied into the primary slot,
     then erased
   - sector data in scratch is copied into the secondary slot

As it swaps images, the bootloader updates the swap status field in a way that
allows it to compute how far this swap operation has progressed for each
sector.  The swap status field can thus used to resume a swap operation if the
bootloader is halted while a swap operation is ongoing and later reset. The
`BOOT_MAX_IMG_SECTORS` value is the configurable maximum number of sectors
MCUboot supports for each image; its value defaults to 128, but allows for
either decreasing this size, to limit RAM usage, or to increase it in devices
that have massive amounts of Flash or very small sized sectors and thus require
a bigger configuration to allow for the handling of all slot's sectors.
The factor of min-write-size is due to the behavior of flash hardware. The factor
of 3 is explained below.

2. Encryption keys: key-encrypting keys (KEKs).  These keys are needed for
   image encryption and decryption.  See the
   [encrypted images](https://github.com/mcu-tools/mcuboot/blob/ba2099f/docs/encrypted_images.md) document for more information.

3. Swap size: When beginning a new swap operation, the total size that needs
   to be swapped (based on the slot with largest image + TLVs) is written to
   this location for easier recovery in case of a reset while performing the
   swap.

4. Swap info: A single byte which encodes the following information:
    - Swap type: Stored in bits 0-3. Indicating the type of swap operation in
    progress. When MCUboot resumes an interrupted swap, it uses this field to
    determine the type of operation to perform. This field contains one of the
    following values in the table below.
    - Image number: Stored in bits 4-7. It has always 0 value at single image
    boot. In case of multi image boot it indicates, which image was swapped when
    interrupt happened. The same scratch area is used during in case of all
    image swap operation. Therefore this field is used to determine which image
    the trailer belongs to if boot status is found on scratch area when the swap
    operation is resumed.

| Name                      | Value |
| ------------------------- | ----- |
| `BOOT_SWAP_TYPE_TEST`     | 2     |
| `BOOT_SWAP_TYPE_PERM`     | 3     |
| `BOOT_SWAP_TYPE_REVERT`   | 4     |


5. Copy done: A single byte indicating whether the image in this slot is
   complete (0x01=done; 0xff=not done).

6. Image OK: A single byte indicating whether the image in this slot has been
   confirmed as good by the user (0x01=confirmed; 0xff=not confirmed).

7. MAGIC: A 16-byte field identifying the image trailer layout. It may assume
   distinct values depending on the maximum supported write alignment
   (`BOOT_MAX_ALIGN`) of the image, as defined by the following construct:

``` c
union boot_img_magic_t
{
    struct {
        uint16_t align;
        uint8_t magic[14];
    };
    uint8_t val[16];
};
```
  If `BOOT_MAX_ALIGN` is **8 bytes**, then MAGIC contains the following 16 bytes:

``` c
const union boot_img_magic_t boot_img_magic = {
    .val = {
        0x77, 0xc2, 0x95, 0xf3,
        0x60, 0xd2, 0xef, 0x7f,
        0x35, 0x52, 0x50, 0x0f,
        0x2c, 0xb6, 0x79, 0x80
    }
};
```

  In case `BOOT_MAX_ALIGN` is defined to any value different than **8**, then the maximum
  supported write alignment value is encoded in the MAGIC field, followed by a fixed
  14-byte pattern:

``` c
const union boot_img_magic_t boot_img_magic = {
    .align = BOOT_MAX_ALIGN,
    .magic = {
        0x2d, 0xe1,
        0x5d, 0x29, 0x41, 0x0b,
        0x8d, 0x77, 0x67, 0x9c,
        0x11, 0x0f, 0x1f, 0x8a
    }
};
```

---
***Note***
Be aware that the image trailers make the ending area of the image slot
unavailable for carrying the image data. In particular, the swap status size
could be huge. For example, for 128 slot sectors with a 4-byte alignment,
it would become 1536 B.

---
