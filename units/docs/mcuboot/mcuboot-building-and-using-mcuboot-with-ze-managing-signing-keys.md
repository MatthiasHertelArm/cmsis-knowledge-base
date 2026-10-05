---
id: "mcuboot-building-and-using-mcuboot-with-ze-managing-signing-keys"
type: "concept"
domain: "boot-update"
title: "Building and using MCUboot with Zephyr: Managing signing keys"
summary: "The signing keys used by MCUboot are represented in standard formats, and can be generated and processed using conventional tools. However, scripts/imgtool.py is able to generate key pairs in all of the supported formats."
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@ba2099f:docs/readme-zephyr.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/ba2099f/docs/readme-zephyr.md#managing-signing-keys"
license: "Apache-2.0"
mode: "V"
---

The signing keys used by MCUboot are represented in standard formats,
and can be generated and processed using conventional tools.  However,
`scripts/imgtool.py` is able to generate key pairs in all of the
supported formats.  See [the docs](https://github.com/mcu-tools/mcuboot/blob/ba2099f/docs/imgtool.md) for more details on
this tool.

### Generating a new keypair

Generating a keypair with imgtool is a matter of running the keygen
subcommand:

```
    $ ./scripts/imgtool.py keygen -k mykey.pem -t rsa-2048
```

The argument to `-t` should be the desired key type.  See the
[the docs](https://github.com/mcu-tools/mcuboot/blob/ba2099f/docs/imgtool.md) for more details on the possible key types.

### Extracting the public key

The generated keypair above contains both the public and the private
key.  It is necessary to extract the public key and insert it into the
bootloader.  Use the ``CONFIG_BOOT_SIGNATURE_KEY_FILE`` Kconfig option to
provide the path to the key file so the build system can extract
the public key in a format usable by the C compiler.
The generated public key is saved in `build/zephyr/autogen-pubkey.h`, which is included
by the `boot/zephyr/keys.c`.

``CONFIG_BOOT_SIGNATURE_KEY_FILE`` accepts either a keypair PEM or a
public-key-only PEM: only the public key is consumed during the build.
This enables production flows in which the signing private key is held
by a release team and only an exported public key is provided to
bootloader builders. Signing images (`imgtool sign`) requires the
private key.

The Zephyr port supports embedding multiple verification keys in the
bootloader. `CONFIG_BOOT_SIGNATURE_KEY_FILE` accepts a single PEM path or
a comma-separated list, e.g.
`"prod_pubkey.pem,dev_pubkey.pem"` or
`"\${CMAKE_CURRENT_LIST_DIR}/prod_pubkey.pem,\${CMAKE_CURRENT_LIST_DIR}/dev_pubkey.pem"`.
Only the public-key bytes are ever embedded in the bootloader image,
regardless of which form is passed in. Up to eight total keys are
supported by the Zephyr port. All entries must use the same
`BOOT_SIGNATURE_TYPE`, and multi-key mode is mutually exclusive with
`BOOT_HW_KEY`, `BOOT_BUILTIN_KEY`, and `BOOT_BYPASS_KEY_MATCH`.

The first entry **may** be a keypair PEM or a public-only PEM. A
keypair is required only if the same file is also used with
`imgtool sign`; otherwise a public-only PEM is sufficient — and
preferred, since private material embedded in the bootloader image is
recoverable from flash. Subsequent entries (positions past the first)
**must** be public-only PEMs; the build is rejected at CMake time
otherwise (via `imgtool keyinfo --require public`).

### Custody model

The feature is for separating signing custody from verification custody.

| Key                       | Custody                                    | Distribution                                                      | Blast radius if lost                                                  |
| ------------------------- | ------------------------------------------ | ----------------------------------------------------------------- | --------------------------------------------------------------------- |
| Production private        | HSM, signing ceremony, release team only   | Never leaves the HSM                                              | Catastrophic: attacker can sign images that boot on the prod fleet    |
| Production public         | N/A (public material)                      | Embedded in dev bootloaders so dev units can verify prod images   | None: public by design                                                |
| Development private       | Loosely held by engineers                  | On dev workstations / dev signing infra                           | Bounded: only authorizes firmware on non-deployed dev hardware        |

Production bootloaders should embed only the production public key, so
that production units boot only production-signed images. Development
bootloaders embed both the production public key and the development
public key, so a dev unit can boot a production-signed image (verified
against the prod public key) without re-signing, while still allowing
engineers to flash development-signed images.

The bootloader's existing key-matching logic (`bootutil_find_key()`)
hashes the image's KEYHASH TLV against every embedded key and accepts
the first match. There is no per-key behaviour: multi-key mode is purely
about accepting more than one valid signer.

Once MCUboot is built, this new keypair file (`mykey.pem` in this
example) can be used to sign images.
