---
id: "tfm-physical-attack-mitigation-in-trus-requirements"
type: "concept"
domain: "security"
title: "Physical attack mitigation in Trusted Firmware-M: Requirements"
summary: "PSA Certified Level 3 Lightweight Protection Profile [1] requires protection against physical attacks. This includes protection against manipulation of the hardware and any data, undetected manipulation of memory contents, physical probing on the chip's surface."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/tfm_physical_attack_mitigation.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/tfm_physical_attack_mitigation.html#requirements"
license: "BSD-3-Clause"
mode: "V"
---

PSA Certified Level 3 Lightweight Protection Profile [1]_ requires protection
against physical attacks. This includes protection against manipulation of the
hardware and any data, undetected manipulation of memory contents, physical
probing on the chip's surface. The RoT detects or prevents its operation outside
the normal operating conditions (such as voltage, clock frequency, temperature,
or external energy fields) where reliability and secure operation has not been
proven or tested.


**Note:** Mitigation against certain level of physical attacks is a mandatory requirement for PSA Level 3 certification. The tf-m-against-physical-attacks discussed below doesn't provide mitigation against all the physical attacks considered in scope for PSA L3 certification. Please check the Protection Profile document for an exhaustive list of requirements.
