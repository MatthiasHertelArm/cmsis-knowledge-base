---
id: "tfm-physical-attack-mitigation-in-trus-assumptions-on-attacker-capability"
type: "concept"
domain: "security"
title: "Physical attack mitigation in Trusted Firmware-M: TF-M Threat Model against physical attacks / Assumptions on attacker capability"
summary: "Part of: TF-M Threat Model against physical attacks"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/tfm_physical_attack_mitigation.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/tfm_physical_attack_mitigation.html#assumptions-on-attacker-capability"
license: "BSD-3-Clause"
mode: "V"
---

_Part of: TF-M Threat Model against physical attacks_

It is assumed that the attacker owns the following capabilities to perform
physical attack against devices protected by TF-M.

  - Has physical access to the device.
  - Able to access external memory, read and possibly tamper it.
  - Able to load arbitrary candidate images for firmware upgrade.
  - Able to manage that bootloader tries to upgrade the arbitrary image from
    staging area.
  - Able to inject faults on hardware level (voltage or power glitch, EM pulse,
    etc.) to the system.
  - Precise timing of fault injection is possible once or a few times, but in
    general the more intervention is required for a successful attack the harder
    will be to succeed.

It is out of the scope of TF-M mitigation if an attacker is able to directly
tamper or disclose the assets. It is assumed that an attacker has the following
technical limitations.

  - No knowledge of the image signing key. Not able to sign an arbitrary image.
  - Not able to directly access to the chip through debug port.
  - Not able to directly access internal memory.
  - No knowledge of the layout of the die or the memory arrangement of the
    secure code, so precise attack against specific registers or memory
    addresses are out of scope.
