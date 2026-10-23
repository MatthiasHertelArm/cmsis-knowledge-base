---
id: "tfm-secure-boot-signing-the-images-manually"
type: "concept"
domain: "security"
title: "Secure boot: Signing the images manually"
summary: "Normally the build system handles the signing (computing hash over the image and security critical manifest data and then signing the hash) of the firmware images."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/booting/tfm_secure_boot.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/booting/tfm_secure_boot.html#signing-the-images-manually"
license: "BSD-3-Clause"
mode: "V"
---

Normally the build system handles the signing (computing hash over the image
and security critical manifest data and then signing the hash) of the firmware
images. However, the images also can be signed manually by using the `imgtool`
Python program which is located in the MCUboot repository  in the `scripts`
folder or can be installed with the pip package manager.
Issue the `python3 imgtool.py sign --help` command in the directory for more
information about the mandatory and optional arguments. The tool takes an image
in binary or Intel Hex format and adds a header and trailer that MCUBoot is
expecting. In case of single image boot after a successful build the
`tfm_s_ns.bin` build artifact (contains the concatenated secure and non-secure
images) must be passed to the script and in case of multiple image boot the
`tfm_s.bin` and `tfm_ns.bin` binaries can be passed to prepare the signed
images.
