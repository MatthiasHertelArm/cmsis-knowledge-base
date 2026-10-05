---
id: "mcuboot-encrypted-images-creating-your-keys-with-imgtool-creating"
type: "concept"
domain: "boot-update"
title: "Encrypted images: [Creating your keys with imgtool](#creating-your-keys-with-imgtool)"
summary: "imgtool can generate keys by using imgtool keygen -k <output.pem> -t <type>, where type can be one of rsa-2048, rsa-3072, ecdsa-p256 or ed25519. This will generate a keypair or private key."
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@ba2099f:docs/encrypted_images.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/ba2099f/docs/encrypted_images.md#creating-your-keys-with-imgtool-creating-your-keys-with-imgtool"
license: "Apache-2.0"
mode: "V"
---

`imgtool` can generate keys by using `imgtool keygen -k <output.pem> -t <type>`,
 where type can be one of `rsa-2048`, `rsa-3072`, `ecdsa-p256`
or `ed25519`. This will generate a keypair or private key.

To extract the public key in source file form, use
`imgtool getpub -k <input.pem> -e <encoding>`, where `encoding` can be one of
`lang-c` or `lang-rust` (defaults to `lang-c`). To extract a public key in PEM
format, use `imgtool getpub -k <input.pem> -e pem`.

If using AES-KW, follow the steps in the next section to generate the
required keys.
