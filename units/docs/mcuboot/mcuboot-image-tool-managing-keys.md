---
id: "mcuboot-image-tool-managing-keys"
type: "concept"
domain: "boot-update"
title: "Image tool: Managing keys"
summary: "This tool currently supports rsa-2048, rsa-3072, ecdsa-p256 and ed25519 keys. You can generate a keypair for one of these types using the 'keygen' command:"
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@725d63c:docs/imgtool.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/725d63c/docs/imgtool.md#managing-keys"
license: "Apache-2.0"
mode: "V"
---

This tool currently supports rsa-2048, rsa-3072, ecdsa-p256 and ed25519 keys.
You can generate a keypair for one of these types using the 'keygen' command:

    ./scripts/imgtool.py keygen -k filename.pem -t rsa-2048

or use rsa-3072, ecdsa-p256, or ed25519 for the type.  The key type used
should match what MCUboot is configured to verify.

This key file is what is used to sign images, this file should be
protected, and not widely distributed.

You can add the `-p` argument to `keygen`, which will cause it to
prompt for a password.  You will need to enter this password in every
time you use the private key.
