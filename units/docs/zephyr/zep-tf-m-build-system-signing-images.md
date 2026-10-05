---
id: "zep-tf-m-build-system-signing-images"
type: "concept"
domain: "security"
title: "TF-M Build System: Signing Images"
summary: "When CONFIG_TFM_BL2 is set to y, TF-M uses a secure bootloader (BL2) and firmware images must be signed with a private key."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/services/tfm/build.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/services/tfm/build.rst"
license: "Apache-2.0"
mode: "V"
---

When `CONFIG_TFM_BL2` is set to `y`, TF-M uses a secure bootloader
(BL2) and firmware images must be signed with a private key. The firmware image
is validated by the bootloader during updates using the corresponding public
key, which is stored inside the secure bootloader firmware image.

By default, `<tfm-dir>/bl2/ext/mcuboot/root-rsa-3072.pem` is used to sign secure
images, and `<tfm-dir>/bl2/ext/mcuboot/root-rsa-3072_1.pem` is used to sign
non-secure images. These default .pem keys can (and **should**) be overridden
using the `CONFIG_TFM_KEY_FILE_S` and
`CONFIG_TFM_KEY_FILE_NS` config flags.

To satisfy PSA Certified Level 1 requirements, **You MUST replace
the default .pem file with a new key pair!**

To generate a new public/private key pair, run the following commands:

```bash

$ imgtool keygen -k root-rsa-3072_s.pem -t rsa-3072
$ imgtool keygen -k root-rsa-3072_ns.pem -t rsa-3072
```
You can then place the new .pem files in an alternate location, such as your
Zephyr application folder, and reference them in the `prj.conf` file via the
`CONFIG_TFM_KEY_FILE_S` and `CONFIG_TFM_KEY_FILE_NS` config
flags.


**Warning:** Be sure to keep your private key file in a safe, reliable location! If you lose this key file, you will be unable to sign any future firmware images, and it will no longer be possible to update your devices in the field!

After the built-in signing script has run, it creates a `tfm_merged.hex`
(and `tfm_merged.bin`) file that contains all three binaries: bl2, tfm_s,
and the zephyr app. These files can then be flashed to your development board
or run in QEMU.
