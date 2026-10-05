---
id: "tfm-physical-attack-mitigation-in-trus-physical-attacks"
type: "concept"
domain: "security"
title: "Physical attack mitigation in Trusted Firmware-M: Physical attacks"
summary: "The goal of physical attacks is to alter the expected behavior of a circuit. This can be achieved by changing the device's normal operating conditions to untested operating conditions."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/tfm_physical_attack_mitigation.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/tfm_physical_attack_mitigation.html#physical-attacks"
license: "BSD-3-Clause"
mode: "V"
---

The goal of physical attacks is to alter the expected behavior of a circuit.
This can be achieved by changing the device's normal operating conditions to
untested operating conditions. As a result a hazard might be triggered on the
circuit level, whose impact is unpredictable in advance but its effect can be
observed. With frequent attempts, a weak point of the system could be identified
and the attacker could gain access to the entire device. There is a wide variety
of physical attacks, the following is not a comprehensive list rather just give
a taste of the possibilities:

  - Inject a glitch into the device power supply or clock line.
  - Operate the device outside its temperature range: cool down or warm it up.
  - Shoot the chip with an electromagnetic field. This can be done by passing
    current through a small coil close to the chip surface, no physical contact
    or modification of the PCB (soldering) is necessary.
  - Point a laser beam on the chip surface. It could flip bits in memory or a
    register, but precise knowledge of chip layout and design is necessary.

The required equipment and cost of these attacks varies. There are commercial
products to perform such attacks. Furthermore, they are shipped with a scripting
environment, good documentation, and a lot of examples. In general, there is a
ton of videos, research paper and blogs about fault injection attacks. As a
result the threshold, that even non-proficient can successfully perform such
attack, gets lower over time.
