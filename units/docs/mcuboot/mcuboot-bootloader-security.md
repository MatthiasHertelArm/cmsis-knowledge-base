---
id: "mcuboot-bootloader-security"
type: "concept"
domain: "boot-update"
title: "Bootloader: Security"
summary: "As indicated above, the final step of the integrity check is signature verification. The bootloader can have one or more public keys embedded in it at build time."
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@ba2099f:docs/design.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/ba2099f/docs/design.md#security"
license: "Apache-2.0"
mode: "V"
---

As indicated above, the final step of the integrity check is signature
verification.  The bootloader can have one or more public keys embedded in it
at build time.  During signature verification, the bootloader verifies that an
image was signed with a private key that corresponds to the embedded KEYHASH
TLV.

For information on embedding public keys in the bootloader, as well as
producing signed images, see: [signed_images](https://github.com/mcu-tools/mcuboot/blob/ba2099f/docs/signed_images.md).

If you want to enable and use encrypted images, see:
[encrypted_images](https://github.com/mcu-tools/mcuboot/blob/ba2099f/docs/encrypted_images.md).

---
***Note***

*Image encryption is not supported when the direct-xip upgrade strategy*
*is selected.*

---

### [Using hardware keys for verification](#hw-key-support)

By default, the whole public key is embedded in the bootloader code and its
hash is added to the image manifest as a KEYHASH TLV entry. As an alternative
the bootloader can be made independent of the keys (avoiding the incorporation
of the public key into the code) by using one of the following options:
`MCUBOOT_HW_KEY` or `MCUBOOT_BUILTIN_KEY`.

Using any of these options makes MCUboot independent from the public key(s).
The key(s) can be provisioned any time and by different parties.

Hardware KEYs support options details:
- `MCUBOOT_HW_KEY`: In this case the hash of the public key must be
provisioned to the target device and MCUboot must be able to retrieve the
key-hash from there. For this reason the target must provide a definition
for the `boot_retrieve_public_key_hash()` function which is declared in
`boot/bootutil/include/bootutil/sign_key.h`. It is also required to use
the `full` option for the `--public-key-format` imgtool argument in order to
add the whole public key (PUBKEY TLV) to the image manifest instead of its
hash (KEYHASH TLV). During boot the public key is validated before using it for
signature verification, MCUboot calculates the hash of the public key from the
TLV area and compares it with the key-hash that was retrieved from the device.
- `MCUBOOT_BUILTIN_KEY`: With this option the whole public key(s) used for
signature verification must be provisioned to the target device and the used
[cryptographic library](https://github.com/mcu-tools/mcuboot/blob/ba2099f/docs/PORTING.md) must support the usage of builtin keys based
on key IDs. In this case, neither the code nor the image metadata needs to
contain any public key data. During image validation only a key ID is passed to
the verifier function. The key handling is entirely the responsibility of the
crypto library and the details of the key handling mechanism are abstracted away
from the boot code.\
***Note:*** *At the moment the usage of builtin keys is only available with the*
*PSA Crypto API based crypto backend (`MCUBOOT_USE_PSA_CRYPTO`) for ECDSA*
*signatures.*
