---
id: "mcuboot-encrypted-images-design"
type: "concept"
domain: "boot-update"
title: "Encrypted images: Design"
summary: "When encrypting an image, only the payload (FW) is encrypted. The header, TLVs are still sent as plain data."
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@ba2099f:docs/encrypted_images.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/ba2099f/docs/encrypted_images.md#design"
license: "Apache-2.0"
mode: "V"
---

When encrypting an image, only the payload (FW) is encrypted. The header,
TLVs are still sent as plain data.

Hashing and signing also remain functionally the same way as before,
applied over the un-encrypted data. Validation on encrypted images, checks
that the encrypted flag is set and TLV data is OK, then it decrypts each
image block before sending the data to the hash routines.

The image is encrypted using AES-CTR-128 or AES-CTR-256, with a counter
that starts from zero (over the payload blocks) and increments by 1 for each
16-byte block. AES-CTR was chosen for speed/simplicity and allowing for any
block to be encrypted/decrypted without requiring knowledge of any other
block (allowing for simple resume operations on swap interruptions).

The key used is a randomized when creating a new image, by `imgtool` or
`newt`. This key should never be reused and no checks are done for this,
but randomizing a 16-byte block with a TRNG should make it highly
improbable that duplicates ever happen.

To distribute this AES-CTR key, new TLVs were defined. The key can be
encrypted using either RSA-OAEP, AES-KW (128 or 256 bits depending on the
AES-CTR key length), ECIES-P256 or ECIES-X25519.

For RSA-OAEP a new TLV with value `0x30` is added to the image, for
AES-KW a new TLV with value `0x31` is added to the image, for
ECIES-P256 a new TLV with value `0x32` is added, and for ECIES-X25519 a
newt TLV with value `0x33` is added. The contents of those TLVs
are the results of applying the given operations over the AES-CTR key.
