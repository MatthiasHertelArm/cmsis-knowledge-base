---
id: "mcuboot-signed-images-image-signing"
type: "concept"
domain: "boot-update"
title: "signed images: Image signing"
summary: "This signs the image by computing hash over the image, and then signing that hash. Signature is computed by newt tool when it's creating the image. This signature is placed in the image trailer."
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@ba2099f:docs/signed_images.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/ba2099f/docs/signed_images.md#image-signing"
license: "Apache-2.0"
mode: "V"
---

This signs the image by computing hash over the image, and then
signing that hash. Signature is computed by newt tool when it's
creating the image. This signature is placed in the image trailer.

The public key of this keypair must be included in the bootloader,
as it verifies it before allowing the image to run.

This facility allows you to use multiple signing keys. This would
be useful when you want to prevent production units from booting
development images, but want development units to be able to boot
both production images and development images.

On Zephyr, `CONFIG_BOOT_SIGNATURE_KEY_FILE` accepts a comma-separated
list of PEMs. Only the public-key bytes are embedded regardless of which
form is passed in. The first entry may be a keypair PEM (needed only if
the same file is also fed to `imgtool sign`) or a public-only PEM
(preferred when signing happens elsewhere); subsequent entries must be
public-only. The intended use is to separate signing custody (a
production private key, held only by a release team) from verification
custody (the production public key, embedded in development bootloaders
so dev units can boot prod-signed images). See
[readme-zephyr.md](https://github.com/mcu-tools/mcuboot/blob/ba2099f/docs/readme-zephyr.md) for the threat-model table and a
worked example.

For an alternative solution when the public key(s) doesn't need to be
included in the bootloader, see the [design](https://github.com/mcu-tools/mcuboot/blob/ba2099f/docs/design.md) document.
