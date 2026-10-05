---
id: "mcuboot-encrypted-images-ecies-encryption"
type: "concept"
domain: "boot-update"
title: "Encrypted images: ECIES encryption"
summary: "ECIES follows a well defined protocol to generate an encryption key. There are multiple standards which differ only on which building blocks are used; for MCUboot we settled on some primitives that are easily found on our crypto libraries."
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@ba2099f:docs/encrypted_images.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/ba2099f/docs/encrypted_images.md#ecies-encryption"
license: "Apache-2.0"
mode: "V"
---

ECIES follows a well defined protocol to generate an encryption key. There are
multiple standards which differ only on which building blocks are used; for
MCUboot we settled on some primitives that are easily found on our crypto
libraries. The whole key encryption can be summarized as:

* Generate a new private key and derive the public key; when using ECIES-P256
  this is a secp256r1 keypair, when using ECIES-X25519 this will be a x25519
  keypair. Those keys will be our ephemeral keys.
* Generate a new secret (DH) using the ephemeral private key and the public key
  that corresponds to the private key embedded in the HW.
* Derive the new keys from the secret using HKDF. We are not using a `salt`
  and using an `info` of `MCUBoot_ECIES_v1`, generating 48 bytes of key material.
* A new random encryption key is generated (for AES). This is
  the AES key used to encrypt the images.
* The key is encrypted with AES-128-CTR or AES-256-CTR and a `nonce` of 0 using
  the first 16 bytes of key material generated previously by the HKDF.
* The encrypted key now goes through a HMAC using the remaining 32
  bytes of key material from the HKDF.

There are different TLVs for ECIES-P256, ECIES-X25519 with SHA256 HKDF/HMAC
and ECIES-X25519 with SHA512 HKDF/HMAC.
The final TLV is built from the 65 bytes for ECIES-P256 or 32 bytes for
ECIES-X25519, which correspond to the ephemeral public key, followed by the
MAC tag and the 16 or 32 bytes of the encrypted key, resulting in final TLV
length:
 * ECIES-P256 has TLV length 113 to 129 bytes, depending on AES key length.
 * ECIES-X25519 on SHA256 TLV length is 80 or 96 bytes, depending on AES key
   length.
 * ECIES-X25519 on SHA512 TLV length is 112 or 128, depending on AES key
   length.

The implemenation of ECIES-P256 is named ENC_EC256 in the source code and
artifacts while ECIES-X25519 is named ENC_X25519.

Note that MCUboot is built to support only one ECIES and HMAC SHA at once,
and truncated HMAC is not supported at this time
