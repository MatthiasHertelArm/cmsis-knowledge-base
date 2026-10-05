---
id: "tfm-physical-attack-mitigation-in-trus-physical-attack-target"
type: "concept"
domain: "security"
title: "Physical attack mitigation in Trusted Firmware-M: TF-M Threat Model against physical attacks / Physical attack target"
summary: "Part of: TF-M Threat Model against physical attacks"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/tfm_physical_attack_mitigation.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/tfm_physical_attack_mitigation.html#physical-attack-target"
license: "BSD-3-Clause"
mode: "V"
---

_Part of: TF-M Threat Model against physical attacks_

A malicious actor performs physical attack against TF-M to retrieve assets from
device. These assets can be sensitive data, credentials, crypto keys. These
assets are protected in TF-M by proper isolation.

For example, a malicious actor can perform the following attacks:

  - Reopen the debug port or hinder the closure of it then connect to the device
    with a debugger and dump memory.
  - Bypass secure boot to replace authentic firmware with a malicious image.
    Then arbitrary memory can be read.
  - Assuming that secure boot cannot be bypassed then an attacker can try to
    hinder the setup of the memory isolation hardware by TF-M
    `Secure Partition Manager` (SPM) and manage to execute the non-secure
    image in secure state. If this is achieved then still an exploitable
    vulnerability is needed in the non-secure code which can be used to inject
    and execute arbitrary code to read the assets.
  - Device might contain unsigned binary blob next to the official firmware.
    This can be any data, not necessarily code. If an attacker manages to
    replace this data with arbitrary content (e.g. a NOP slide leading to a
    malicious code) then they can try to manipulate the program counter to jump
    to this area before setting up the memory isolation.
