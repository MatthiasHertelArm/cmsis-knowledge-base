---
id: "tfm-bl1-immutable-bootloader-using-bl1-on-new-platforms"
type: "concept"
domain: "security"
title: "BL1 Immutable bootloader: Using BL1 on new platforms"
summary: "New platforms must define the following macros in their region_defs.h:"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/booting/bl1.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/booting/bl1.html#using-bl1-on-new-platforms"
license: "BSD-3-Clause"
mode: "V"
---

New platforms must define the following macros in their `region_defs.h`:

- `BL1_1_HEAP_SIZE`
- `BL1_1_STACK_SIZE`
- `BL1_2_HEAP_SIZE`
- `BL1_2_STACK_SIZE`
- `BL1_1_CODE_START`
- `BL1_1_CODE_LIMIT`
- `BL1_1_CODE_SIZE`
- `BL1_2_CODE_START`
- `BL1_2_CODE_LIMIT`
- `BL1_2_CODE_SIZE`
- `PROVISIONING_DATA_START`
- `PROVISIONING_DATA_LIMIT`
- `PROVISIONING_DATA_SIZE`

The `PROVISIONING_DATA_*` defines are used to locate where the data to be
provisioned into OTP can be found. These are required as the provisioning bundle
needs to contain the entire BL1_2 image, usually >= 8KiB in size, which is too
large to be placed in the static data area as is done for all other dummy
provisioning data. On development platforms with reprogrammable ROM, this is
often placed in unused ROM. On production platforms, this should be located in
RAM and then filled with provisioning data. The format of the provisioning data
that should be located in the `PROVISIONING_DATA_*` region can be found in
`bl1/bl1_1/lib/provisioning.c` in the struct
`bl1_assembly_and_test_provisioning_data_t`

If the platform is storing BL1_2 in flash, it must set
`BL1_2_IMAGE_FLASH_OFFSET` to the flash offset of the start of BL1_2.

The platform must also implement the HAL functions defined in the following
headers:

- `bl1/bl1_1/shared_lib/interface/trng.h`
- `bl1/bl1_1/shared_lib/interface/crypto.h`
- `bl1/bl1_1/shared_lib/interface/otp.h`

If the platform integrates a CryptoCell-312, then it can reuse the existing
implementation.
