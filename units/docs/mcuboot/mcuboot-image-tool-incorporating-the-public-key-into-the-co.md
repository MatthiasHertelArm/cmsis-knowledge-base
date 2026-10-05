---
id: "mcuboot-image-tool-incorporating-the-public-key-into-the-co"
type: "concept"
domain: "boot-update"
title: "Image tool: Incorporating the public key into the code"
summary: "There is a development key distributed with MCUboot that can be used for testing. Since this private key is widely distributed, it should never be used for production."
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@ba2099f:docs/imgtool.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/ba2099f/docs/imgtool.md#incorporating-the-public-key-into-the-code"
license: "Apache-2.0"
mode: "V"
---

There is a development key distributed with MCUboot that can be used
for testing.  Since this private key is widely distributed, it should
never be used for production.  Once you have generated a production
key, as described above, you should replace the public key in the
bootloader with the generated one.

For Zephyr, the keys live in the file `boot/zephyr/keys.c`.  For
mynewt, follow the instructions in `doc/signed_images.md` to generate
the key file.

    ./scripts/imgtool.py getpub -k filename.pem

will extract the public key from the given key file, and output it as
a C data structure.  The input may be a keypair PEM (containing both
private and public material) or a public-key-only PEM: `getpub`
dispatches on the key format and requires no private key material.
This matters for production workflows where the signing private key
is held only by a release team, and the bootloader build consumes an
exported public-key PEM.  You can replace or insert the emitted code
into the key file. However, when the `MCUBOOT_HW_KEY` config option
is enabled, this last step is unnecessary and can be skipped.

When embedding more than one signing-verification key in the same image
(for example, a Zephyr build with a multi-key
`CONFIG_BOOT_SIGNATURE_KEY_FILE` list), pass `--name-suffix` to
distinguish the emitted symbol names:

    ./scripts/imgtool.py getpub -k dev-key.pem --name-suffix _2

emits `<shortname>_pub_key_2[]` and `<shortname>_pub_key_2_len` (the
same suffix is applied by `getpubhash` for the lang-c encoding). The
option is accepted only for the `lang-c` / `lang-rust` encodings; using
it with `--encoding pem` or `--encoding raw` is rejected.
