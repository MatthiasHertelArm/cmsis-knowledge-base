---
id: "mcuboot-encrypted-images-creating-your-keys-with-unix-tooling-cre"
type: "concept"
domain: "boot-update"
title: "Encrypted images: [Creating your keys with Unix tooling](#creating-your-keys-with-unix-tooling)"
summary: "Encrypted images: [Creating your keys with Unix tooling](#creating-your-keys-with-unix-tooling)"
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@ba2099f:docs/encrypted_images.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/ba2099f/docs/encrypted_images.md#creating-your-keys-with-unix-tooling-creating-your-keys-with-unix-tooling"
license: "Apache-2.0"
mode: "V"
---

* If using RSA-OAEP, generate a keypair following steps similar to those
  described in [signed_images](https://github.com/mcu-tools/mcuboot/blob/ba2099f/docs/signed_images.md) to create RSA keys.
* If using ECIES-P256, generate a keypair following steps similar to those
  described in [signed_images](https://github.com/mcu-tools/mcuboot/blob/ba2099f/docs/signed_images.md) to create ECDSA256 keys.
* If using ECIES-X25519, generate a private key passing the option `-t x25519`
  to `imgtool keygen` command. To generate public key PEM file the following
  command can be used: `openssl pkey -in <generated-private-key.pem> -pubout`
* If using AES-KW (`newt` only), the `kek` can be generated with a
  command like (change count to 32 for a 256 bit key)
  `dd if=/dev/urandom bs=1 count=16 | base64 > my_kek.b64`
