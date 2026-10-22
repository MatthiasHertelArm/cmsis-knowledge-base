---
id: "tfm-secure-boot-build-time-configuration"
type: "concept"
domain: "security"
title: "Secure boot: Build time configuration"
summary: "MCUBoot related compile time switches can be set by cmake variables."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/booting/tfm_secure_boot.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/booting/tfm_secure_boot.html#build-time-configuration"
license: "BSD-3-Clause"
mode: "V"
---

MCUBoot related compile time switches can be set by cmake variables.

- BL2 (default: True):
    - **True:** TF-M built together with bootloader. MCUBoot is executed after
      reset and it authenticates TF-M and starts secure code.
    - **False:** TF-M built without bootloader. Secure image linked to the
      beginning of the device memory and executed after reset. If it is false
      then using any of the further compile time switches is invalid.
- MCUBOOT_UPGRADE_STRATEGY (default: "OVERWRITE_ONLY"):
    - **"OVERWRITE_ONLY":** Default firmware upgrade operation with overwrite.
    - **"SWAP_USING_SCRATCH":** Activate swapping firmware upgrade operation
      with a scratch area in flash
    - **"SWAP_USING_MOVE":** Activate swapping firmware upgrade operation
      without a scratch area in flash
    - **"DIRECT_XIP":** Activate direct execute-in-place firmware upgrade
      operation.
    - **"RAM_LOAD":** Activate RAM loading firmware upgrade operation, where
      the latest image is copied to RAM and runs from there instead of being
      executed in-place.
- MCUBOOT_SIGNATURE_TYPE (default: RSA-3072):
    - **RSA-2048:** Image is signed with RSA algorithm and signed with 2048 bit key.
    - **RSA-3072:** Image is signed with RSA algorithm and signed with 3072 bit key.
    - **EC-P256:** Image is signed with ECDSA P-256 algorithm.
    - **EC-P384:** Image is signed with ECDSA P-384 algorithm.
- MCUBOOT_IMAGE_NUMBER (default: 2):
    - **1:** Single image boot, secure and non-secure images are signed and
      updated together.
    - **2:** Multiple image boot, secure and non-secure images are signed and
      updatable independently.
- MCUBOOT_HW_KEY (default: True):
    - **True:** The hash of public key is provisioned to the SoC and the image
      manifest contains the whole public key (imgtool uses
      `--public_key_format=full`). MCUBoot validates the key before using it
      for firmware authentication, it calculates the hash of public key from the
      manifest and compare against the retrieved key-hash from the hardware.
      This way MCUBoot is independent from the public key(s).  Key(s) can be
      provisioned any time and by different parties.
    - **False:** The whole public key is embedded to the bootloader code and the
      image manifest contains only the hash of the public key (imgtool uses
      `--public_key_format=hash`). MCUBoot validates the key before using it
      for firmware authentication, it calculates the hash of built-in public key
      and compare against the retrieved key-hash from the image manifest. After
      this the bootloader can verify that the image was signed with a private
      key that corresponds to the retrieved key-hash (it can have more public
      keys embedded in and it may have to look for the matching one). All the
      public key(s) must be known at MCUBoot build time.
- MCUBOOT_BUILTIN_KEY (default: False):
    - **True:** When enabled, the entire public key used for signature
      verification must be provisioned to the target device. In this case,
      neither the code nor the image metadata needs to contain any public
      key data. During image validation only a key ID is passed to the verifier
      function for the required key to be selected. The key handling is entirely
      the responsibility of the underlying crypto library and the details of the
      key handling mechanism are abstracted away from the boot code.
- TFM_BL2_LOG_LEVEL:
    Can be used to configure the level of logging in BL2/MCUBoot. The possible
    values are the following:

    - **LOG_LEVEL_NONE**
    - **LOG_LEVEL_ERROR**
    - **LOG_LEVEL_WARNING**
    - **LOG_LEVEL_INFO**
    - **LOG_LEVEL_VERBOSE**

    The logging in MCUBoot can be disabled and thus the code size can be reduced
    by setting it to `LOG_LEVEL_NONE`. Its value depends on the build type. If the build
    type is `Debug` then default value is `LOG_LEVEL_INFO`. In case of different kinds
    of `Release` builds the default value is `LOG_LEVEL_NONE`. The default value can
    be overridden through the command line or in the CMake GUI regardless of the
    build type.
- MCUBOOT_ENC_IMAGES (default: False):
    - **True:** Adds encrypted image support in the source and encrypts the
      resulting images using the keys given by `MCUBOOT_KEY_ENC` and
      `MCUBOOT_KEY_ENC_NS`.
    - **False:** Doesn't add encrypted image support and doesn't encrypt the
      image.

The decryption takes place during the upgrade process, when the images
are being moved between the slots. This means that boards that don't
already have an image on them with MCUBoot that has been compiled with
`MCUBOOT_ENCRYPT_RSA` enabled need special treatment. In order to load
an encrypted image to such boards, an upgrade needs to be executed. This
can be done by using MCUBoot, putting an image in the secondary image
area, and setting `MCUBOOT_ENCRYPT_RSA` to `ON`. When using the
`OVERWRITE_ONLY` upgrade strategy, this is enough. When using
`SWAP_USING_SCRATCH` or `SWAP_USING_MOVE`, an image is needed in
the primary image area as well, to trigger the update.
- MCUBOOT_KEY_ENC (default: "enc-rsa2048-priv.pem" or "enc-aeskw-128.b64"):
    Path to the key used to encrypt the secure image when
    `MCUBOOT_ENC_IMAGES` is enabled. With `MCUBOOT_ENCRYPT_RSA` this is
    the RSA private key, by default `enc-rsa2048-priv.pem` from the MCUBoot
    repository: the build embeds it in BL2, which uses it to unwrap the image
    encryption keys, and derives the public key with which the images are
    encrypted. With `MCUBOOT_ENCRYPT_KW` this is the AES key-wrapping key
    of the secure image, by default `enc-aeskw-128.b64` from the MCUBoot
    repository, a file holding `AES-KW:` followed by the base64 encoded
    key, which is embedded in BL2.
- MCUBOOT_KEY_ENC_NS (default: "enc-rsa2048-priv.pem" or "enc-aeskw-128_ns.b64"):
    Path to the key used to encrypt the non-secure image. With
    `MCUBOOT_ENCRYPT_RSA` BL2 holds a single key, so this must point to the
    same file as `MCUBOOT_KEY_ENC`. With `MCUBOOT_ENCRYPT_KW` this is the
    AES key-wrapping key of the non-secure image, by default
    `enc-aeskw-128_ns.b64` from the MCUBoot repository, in the same format
    as `MCUBOOT_KEY_ENC` and also embedded in BL2.

DO NOT use the default keys in production code, they are exclusively
for testing!

### Image versioning

An image version number is written to its header by one of the Python scripts,
and this number is used by the bootloader when the direct execute-in-place or
the RAM loading mode is enabled. It is also used in case of multiple image boot
when the bootloader checks the image dependencies if any have been added to the
images.

The version number of the image (single image boot) can manually be passed in
through the command line in the cmake configuration step::
```
cmake -DTFM_PLATFORM=arm/musca_b1 -DIMAGE_VERSION_S=1.2.3+4 ..
```
Alternatively, the version number can be less specific (e.g 1, 1.2, or 1.2.3),
where the missing numbers are automatically set to zero. The image version
number argument is optional, and if it is left out, then the version numbers of
the image(s) being built in the same directory will automatically change. In
this case, the last component (the build number) automatically increments from
the previous one: 0.0.0+1 -> 0.0.0+2, for as many times as the build is re-ran,
**until a number is explicitly provided**. If automatic versioning is in place
and then an image version number is provided for the first time, the new number
will take precedence and be used instead. All subsequent image versions are
then set to the last number that has been specified, and the build number would
stop incrementing. Any new version numbers that are provided will overwrite
the previous one: 0.0.0+1 -> 0.0.0+2. Note: To re-apply automatic image
versioning, please start a clean build without specifying the image version
number at all. In case of multiple image boot there are separate compile time
switches for both images to provide their version: `IMAGE_VERSION_S` and
`IMAGE_VERSION_NS`. These must be used instead of `IMAGE_VERSION_S`.


### Security counter

Each signed image contains a security counter in its manifest. It is used by the
bootloader and its aim is to have an independent (from the image version)
counter to ensure rollback protection by comparing the new image's security
counter against the original (currently active) image's security counter during
the image upgrade process. It is added to the manifest (to the TLV area that is
appended to the end of the image) by one of the Python scripts when signing the
image. The value of the security counter is security critical data and it is in
the integrity protected part of the image. The last valid security counter
should always be stored in a non-volatile and trusted component of the device
and its value should always be increased if a security flaw was fixed in the
current image version. The value of the security counter (single image boot) can
be specified at build time in the cmake configuration step::
```
cmake -DTFM_PLATFORM=arm/musca_b1 -DSECURITY_COUNTER_S=42 ../
```
The security counter can be independent from the image version, but not
necessarily. Alternatively, if it is not specified at build time with the
`SECURITY_COUNTER` option the Python script will automatically generate it
from the image version number (not including the build number) and this value
will be added to the signed image. In case of multiple image boot there are
separate compile time switches for both images to provide their security counter
value: `SECURITY_COUNTER_S` and `SECURITY_COUNTER_NS`. These must be used
instead of `SECURITY_COUNTER_S`. If these are not defined then the security
counter values will be derived from the corresponding image version similar to
the single image boot.
