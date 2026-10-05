---
id: "tfm-rollback-protection-in-tf-m-secure-manifest-format-in-mcuboot"
type: "concept"
domain: "security"
title: "Rollback protection in TF-M secure boot: Manifest format in MCUBoot"
summary: "MCUBoot has a custom manifest format, which is composed of two parts:"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/booting/secure_boot_rollback_protection.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/booting/secure_boot_rollback_protection.html#manifest-format-in-mcuboot"
license: "BSD-3-Clause"
mode: "V"
---

MCUBoot has a custom manifest format, which is composed of two parts:

 - Image header: Prepended to the beginning of the image.
   It is integrity protected:
 - TLV section: Appended to the end of the image. It is not integrity protected:

  - Hash of public key, hash of image, signature of image

```c

struct image_header {
    uint32_t ih_magic;
    uint32_t ih_load_addr;
    uint16_t ih_hdr_size;
    uint16_t _pad1;
    uint32_t ih_img_size;
    uint32_t ih_flags;
    struct image_version ih_ver;
    uint32_t _pad2;
};
```
