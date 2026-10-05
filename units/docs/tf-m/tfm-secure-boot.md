---
id: "tfm-secure-boot"
type: "concept"
domain: "security"
title: "Secure boot"
summary: "For secure devices it is security critical to enforce firmware authenticity to protect against execution of malicious software. This is implemented by building a trust chain where each step in the execution chain authenticates the next step before execution."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/booting/tfm_secure_boot.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/booting/tfm_secure_boot.html"
license: "BSD-3-Clause"
mode: "V"
---

For secure devices it is security critical to enforce firmware authenticity to
protect against execution of malicious software. This is implemented by building
a trust chain where each step in the execution chain authenticates the next
step before execution. The chain of trust is based on a "Root of Trust" which
is implemented using asymmetric cryptography. The Root of Trust is a combination
of an immutable bootloader and a public key (ROTPK).

In order to implement a proper chain of trust functionality, it is
mandatory that the first stage bootloader and ROTPK is stored in an
**immutable** way. To achieve this the bootloader code must be stored and
executed from ROM or such part of flash memory which supports write
protection. ROTPK can be stored in a one-time-programmable (OTP) memory. If
the SoC has a built-in BL1 (immutable) bootloader and the immutability of
TF-M secure boot code is not guaranteed then TF-M secure boot code must be
authenticated by BL1 bootloader before execution. If immutability of root
of trust (first stage bootloader + ROTPK) is not ensured then there is a
risk that the secure boot process could be bypassed, which could lead to
arbitrary code execution on the device. Current TF-M secure boot code is
intended to be a second stage bootloader, therefore it requires
authentication before execution. If TF-M secure boot code is used as a first
stage bootloader then it must be stored according to the above requirements.
