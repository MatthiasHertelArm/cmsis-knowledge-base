---
id: "tfm-hw-crypto-key-integration-in-tf-m-abstract"
type: "concept"
domain: "security"
title: "HW crypto key integration in TF-M secure boot: Abstract"
summary: "PSA Trusted Boot and Firmware Update specification requires the support of at least one immutable root of trust public key (ROTPK) for firmware verification. This can be stored using a locked on-chip flash memory, a secure-element or on-chip OTP memory."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/booting/secure_boot_hw_key_integration.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/booting/secure_boot_hw_key_integration.html#abstract"
license: "BSD-3-Clause"
mode: "V"
---

[PSA Trusted Boot and Firmware Update](https://developer.arm.com/-/media/Arm%20Developer%20Community/PDF/PSA/DEN0072-PSA_TBFU_1.1-BETA0.pdf?revision=3ce2513a-ae0f-4b43-96a0-851ed67a640b)
specification requires the support of at least one immutable root of trust
public key (ROTPK) for firmware verification. This can be stored using a locked
on-chip flash memory, a secure-element or on-chip OTP memory. It also beneficial
to be able to provision these keys during the factory life-cycle of the device
independently from any software components. The current key handling solution
in TF-M secure boot does not supports this key provisioning process. MCUBoot
requires compile time built-in public key(s) for image verification. This
limitation does not fit well with a scenario with multiple vendors where
multiple MCU software components might be deployed by different vendors in
different points in the life-cycle of the device and they do not want to share
the keys in-advance for embedding in the bootloader code. The goal of this
document to propose a solution to decouple MCUBoot from public key(s) and
enable the independent deployment of ROTPK.
