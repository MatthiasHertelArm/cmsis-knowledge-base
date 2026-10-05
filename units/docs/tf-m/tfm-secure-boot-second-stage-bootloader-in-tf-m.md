---
id: "tfm-secure-boot-second-stage-bootloader-in-tf-m"
type: "concept"
domain: "security"
title: "Secure boot: Second stage bootloader in TF-M"
summary: "By default, the MCUboot project from GitHub is used as the secure bootloader in TF-M. The repository is going to be automatically downloaded by CMake. The version downloaded can be controlled by the MCUBOOT_VERSION CMake variable."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/booting/tfm_secure_boot.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/booting/tfm_secure_boot.html#second-stage-bootloader-in-tf-m"
license: "BSD-3-Clause"
mode: "V"
---

By default, the MCUboot project from
[GitHub](https://github.com/mcu-tools/mcuboot) is used as the secure
bootloader in TF-M. The repository is going to be automatically downloaded by
CMake. The version downloaded can be controlled by the `MCUBOOT_VERSION`
CMake variable. If you wish to use a locally downloaded copy, the CMake variable
`MCUBOOT_PATH` can be set to its location. This document contains information
about how MCUboot has been integrated to TF-M. For further information about
MCUboot design please refer to the [MCUBoot homepage](https://www.trustedfirmware.org/projects/mcuboot/index.html).

Bootloader is started when CPU is released from reset. It runs in secure mode.
It authenticates the firmware image by hash (SHA-256) and digital signature
(RSA-3072) validation. Public key, that the checks happens against, can be built
into the bootloader image or can be provisioned to the SoC during manufacturing.
Metadata of the image is delivered together with the image itself in a header
and trailer section. In case of successful authentication, bootloader passes
execution to the secure image. Execution never returns to bootloader until
next reset.

A default RSA key pair is stored in the repository, public key is in `keys.c`
and private key is in `root-RSA-3072.pem`.

DO NOT use the default keys in a production code, they are exclusively
for testing!
The private key must be stored in a safe place outside of the repository.
`imgtool.py` (found in the `scripts` directory in the MCUBoot repository,
or installed through the pip package manager) can be used to generate new key
pairs.

The bootloader can handle the secure and non-secure images independently
(multiple image boot) or together (single image boot). In case of multiple image
boot they are signed independently with different keys and they can be updated
separately. In case of single image boot the secure and non-secure image is
handled as a single blob, therefore they must be contiguous in the device
memory. In this case they are signed together and also they can be updated only
together. In order to have the same artefacts at the end of the build regardless
of how the images are handled (independently or together) the images are always
concatenated. In case of single image boot they are concatenated first and then
signed. In case of multiple image boot they are separately signed first and then
concatenated. Preparation of payload is done by Python scripts:
`bl2/ext/mcuboot/scripts/`. At the end of a successful build the signed TF-M
payload can be found in: `<build_dir>/bin/tfm_s_ns_signed.bin`
