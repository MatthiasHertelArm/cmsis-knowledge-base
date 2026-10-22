---
id: "mcuboot-bootloader-image-format"
type: "concept"
domain: "boot-update"
title: "Bootloader: Image format"
summary: "The following definitions describe the image format."
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@725d63c:docs/design.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/725d63c/docs/design.md#image-format"
license: "Apache-2.0"
mode: "V"
---

The following definitions describe the image format.

``` c
#define IMAGE_MAGIC                 0x96f3b83d

#define IMAGE_HEADER_SIZE           32

struct image_version {
    uint8_t iv_major;
    uint8_t iv_minor;
    uint16_t iv_revision;
    uint32_t iv_build_num;
};

/** Image header.  All fields are in little endian byte order. */
struct image_header {
    uint32_t ih_magic;
    uint32_t ih_load_addr;
    uint16_t ih_hdr_size;           /* Size of image header (bytes). */
    uint16_t ih_protect_tlv_size;   /* Size of protected TLV area (bytes). */
    uint32_t ih_img_size;           /* Does not include header. */
    uint32_t ih_flags;              /* IMAGE_F_[...]. */
    struct image_version ih_ver;
    uint32_t _pad1;
};

#define IMAGE_TLV_INFO_MAGIC        0x6907
#define IMAGE_TLV_PROT_INFO_MAGIC   0x6908

/** Image TLV header.  All fields in little endian. */
struct image_tlv_info {
    uint16_t it_magic;
    uint16_t it_tlv_tot;  /* size of TLV area (including tlv_info header) */
};

/** Image trailer TLV format. All fields in little endian. */
struct image_tlv {
    uint16_t  it_type;  /* IMAGE_TLV_[...]. */
    uint16_t it_len;    /* Data length (not including TLV header). */
};

/*
 * Image header flags.
 */
#define IMAGE_F_PIC                      0x00000001 /* Not supported. */
#define IMAGE_F_ENCRYPTED_AES128         0x00000004 /* Encrypted using AES128. */
#define IMAGE_F_ENCRYPTED_AES256         0x00000008 /* Encrypted using AES256. */
#define IMAGE_F_NON_BOOTABLE             0x00000010 /* Split image app. */
#define IMAGE_F_RAM_LOAD                 0x00000020

/*
 * Image trailer TLV types.
 */
#define IMAGE_TLV_KEYHASH           0x01    /* hash of the public key */
#define IMAGE_TLV_PUBKEY            0x02    /* public key */
#define IMAGE_TLV_SHA256            0x10    /* SHA256 of image hdr and body */
#define IMAGE_TLV_SHA384            0x11    /* SHA384 of image hdr and body */
#define IMAGE_TLV_SHA512            0x12    /* SHA512 of image hdr and body */
#define IMAGE_TLV_RSA2048_PSS       0x20    /* RSA2048 of hash output */
#define IMAGE_TLV_ECDSA224          0x21    /* ECDSA of hash output - Not supported anymore */
#define IMAGE_TLV_ECDSA_SIG         0x22    /* ECDSA of hash output */
#define IMAGE_TLV_RSA3072_PSS       0x23    /* RSA3072 of hash output */
#define IMAGE_TLV_ED25519           0x24    /* ed25519 of hash output */
#define IMAGE_TLV_SIG_PURE          0x25    /* Indicator that attached signature has been prepared
                                             * over image rather than its digest.
                                             */
#define IMAGE_TLV_ENC_RSA2048       0x30    /* Key encrypted with RSA-OAEP-2048 */
#define IMAGE_TLV_ENC_KW            0x31    /* Key encrypted with AES-KW 128 or 256*/
#define IMAGE_TLV_ENC_EC256         0x32    /* Key encrypted with ECIES-EC256 */
#define IMAGE_TLV_ENC_X25519        0x33    /* Key encrypted with ECIES-X25519 */
#define IMAGE_TLV_ENC_X25519_SHA512 0x34    /* Key exchange using ECIES-X25519 and SHA512 for MAC
                                             * tag and HKDF in key derivation process
                                             */
#define IMAGE_TLV_DEPENDENCY        0x40    /* Image depends on other image */
#define IMAGE_TLV_SEC_CNT           0x50    /* security counter */
#define IMAGE_TLV_BOOT_RECORD       0x60    /* measured boot record */
/* The following flags relate to compressed images and are for the decompressed image data */
#define IMAGE_TLV_DECOMP_SIZE       0x70    /* Decompressed image size excluding header/TLVs */
#define IMAGE_TLV_DECOMP_SHA        0x71    /*
                                             * Decompressed image shaX hash, this field must match
                                             * the format and size of the raw slot (compressed)
                                             * shaX hash
                                             */
#define IMAGE_TLV_DECOMP_SIGNATURE  0x72    /*
                                             * Decompressed image signature, this field must match
                                             * the format and size of the raw slot (compressed)
                                             * signature
                                             */
#define IMAGE_TLV_COMP_DEC_SIZE     0x73    /* Compressed decrypted image size */
                                            /*
                                             * vendor reserved TLVs at xxA0-xxFF,
                                             * where xx denotes the upper byte
                                             * range.  Examples:
                                             * 0x00a0 - 0x00ff
                                             * 0x01a0 - 0x01ff
                                             * 0x02a0 - 0x02ff
                                             * ...
                                             * 0xffa0 - 0xfffe
                                             */
#define IMAGE_TLV_UUID_VID          0x74    /* Vendor unique identifier */
#define IMAGE_TLV_UUID_CID          0x75    /* Device class unique identifier */
```

Optional type-length-value records (TLVs) containing image metadata are placed
after the end of the image.

The `ih_protect_tlv_size` field indicates the length of the protected TLV area.
If protected TLVs are present then a TLV info header with magic equal to
`IMAGE_TLV_PROT_INFO_MAGIC` must be present and the protected TLVs (plus the
info header itself) have to be included in the hash calculation. Otherwise the
hash is only calculated over the image header and the image itself. In this
case the value of the `ih_protect_tlv_size` field is 0.

The `ih_hdr_size` field indicates the length of the header, and therefore the
offset of the image itself.  This field provides for backwards compatibility in
case of changes to the format of the image header.
