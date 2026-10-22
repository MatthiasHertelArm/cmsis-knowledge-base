---
id: "mcuboot-signed-images-creating-signing-keys"
type: "concept"
domain: "boot-update"
title: "signed images: Creating signing keys"
summary: "First you need a keypair to use for signing. You can create one with openssl command line tool."
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@725d63c:docs/signed_images.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/725d63c/docs/signed_images.md#creating-signing-keys"
license: "Apache-2.0"
mode: "V"
---

First you need a keypair to use for signing. You can create
one with openssl command line tool.

openssl genrsa -out image_sign.pem 2048

This created a file which contains both the private and public key,
and will be used when signing images.

Then you need to extract the public key from this to include it
in the bootloader. Bootloader need to keep key parsing minimal,
so it expects simple key format.

openssl rsa -in image_sign.pem -pubout -out image_sign_pub.der -outform DER -RSAPublicKey_out

Now the public key is in file called image_sign_pub.der.

For ECDSA256 these commands are similar.
openssl ecparam -name prime256v1 -genkey -noout -out image_sign.pem
openssl ec -in image_sign.pem -pubout -outform DER -out image_sign_pub.der

Note that the bootloader build does not require the private key: the
exported public-key PEM (produced above, or via
`imgtool getpub -k image_sign.pem -e pem`) is itself a valid input to
`imgtool getpub`, and can be used as the
`CONFIG_BOOT_SIGNATURE_KEY_FILE` setting for a Zephyr-based bootloader
build. This supports a development workflow
in which the production signing team releases only the public key,
and the private key is never present on developer workstations.
Running `imgtool sign` requires the private key.
