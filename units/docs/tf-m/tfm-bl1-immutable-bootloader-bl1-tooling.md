---
id: "tfm-bl1-immutable-bootloader-bl1-tooling"
type: "concept"
domain: "security"
title: "BL1 Immutable bootloader: BL1 tooling"
summary: "Image signing scripts are provided for BL1_1 and BL1_2. While the script is named create_bl2_img.py, it can be used for any next stage image."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/booting/bl1.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/booting/bl1.html#bl1-tooling"
license: "BSD-3-Clause"
mode: "V"
---

Image signing scripts are provided for BL1_1 and BL1_2. While the script is
named `create_bl2_img.py`, it can be used for any next stage image.

- `bl1/bl1_1/scripts/create_bl1_2_img.py`
- `bl1/bl1_2/scripts/create_bl2_img.py`

These sign (and encrypt in the case of `create_bl2_img.py`) a given image file
and append the required headers.
