---
id: "tfm-hw-crypto-key-integration-in-tf-m-existing-key-handling-solution"
type: "concept"
domain: "security"
title: "HW crypto key integration in TF-M secure boot: Existing key handling solution"
summary: "MCUBoot code contains a compile-time built-in key array which can store any number of key(s) for firmware verification: bl2/ext/mcuboot/keys.c. These public key(s) must be available when MCUBoot image is built."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/booting/secure_boot_hw_key_integration.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/booting/secure_boot_hw_key_integration.html#existing-key-handling-solution"
license: "BSD-3-Clause"
mode: "V"
---

MCUBoot code contains a compile-time built-in key array which can store any
number of key(s) for firmware verification: `bl2/ext/mcuboot/keys.c`. These
public key(s) must be available when MCUBoot image is built. There is a script
`bl2/ext/mcuboot/scripts/imgtool.py` which can generate a new key pair, and
extract the public key part in the expected ASN.1 format and encode it as C
structure. The script is also capable of signing the image with the private key.
In order to identify and validate the corresponding public key during image
verification the hash of the public key is appended to the image manifest area
(TLV encoded metadata). During image verification the bootloader retrieves the
hash of the public key from the manifest area and compare against the on-the-fly
calculated hash value of the built-in public keys. An exact match identifies and
validates the public key which must be used for image verification.

Current memory layout::
```
|----------------------|
|                      |
|     MCUBoot code     |
|                      |
|   Full public key    |
|                      |
|----------------------|
|                      |
|       Image          |
|                      |
|----------------------|
|  Image Manifest(TLV) |
|                      |
|  Hash of public key  |
|----------------------|
|                      |
|   Rest of memory     |
|                      |
```
