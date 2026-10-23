---
id: "tfm-hw-crypto-key-integration-in-tf-m-design-proposal"
type: "concept"
domain: "security"
title: "HW crypto key integration in TF-M secure boot: Design proposal"
summary: "HW key(s) might stored in OTP memory which is an expensive resource, so storing a large key (such as RSA) is inefficient. Therefore, it is assumed that only the hash of the ROTPK will be stored in the HW."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/booting/secure_boot_hw_key_integration.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/booting/secure_boot_hw_key_integration.html#design-proposal"
license: "BSD-3-Clause"
mode: "V"
---

HW key(s) might stored in OTP memory which is an expensive resource, so
storing a large key (such as RSA) is inefficient. Therefore, it is assumed that
only the hash of the ROTPK will be stored in the HW. If only the hash of the
public key is stored in the HW then the whole public key must be transferred to
the device, because it must be available during image verification. This
transfer can be done in the same way as how the hash of the key is transferred
to the device with the current solution. A new TLV type (TLV_KEY) can be
introduced to carry the whole public key. The corresponding public key will be
appended to the image itself in the manifest area. It has the drawback that the
image will be bigger, but it is assumed that the additional cost of the bigger
image (extra flash area + power for download) is less than the cost of the OTP
area.

The verification flow:

 - Look up the TLV_KEY field to get the public key.
 - Calculates its hash(SHA256) value.
 - Get the hash of ROTPK from the platform layer (stored in HW)
 - Compare the two hash values, if they match then the key can be used to
   validate the image. In case of failure consider the images as unauthenticated.

Proposed memory layout::
```
|----------------------|
|                      |
|     MCUBoot code     |
|                      |
|    NO PUBLIC KEY     |
|                      |
|----------------------|
|                      |
|       Image          |
|                      |
|----------------------|
|  Image Manifest(TLV) |
|                      |
|   Full public key    |
|----------------------|
|                      |
|                      |
|   Rest of memory     |
|                      |
|                      |
|----------------------|
|   Immutable memory   |
|                      |
|  Hash of public key  |
|----------------------|
|                      |
```
