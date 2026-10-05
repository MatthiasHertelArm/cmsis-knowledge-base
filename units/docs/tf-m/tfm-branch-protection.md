---
id: "tfm-branch-protection"
type: "concept"
domain: "security"
title: "Branch Protection"
summary: "The Branch Protection is an optional feature that can help with mitigation of common exploits through undesired branching in code."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/integration_guide/branch_protection.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/branch_protection.html"
license: "BSD-3-Clause"
mode: "V"
---

The Branch Protection is an optional feature that can help with mitigation of
common exploits through undesired branching in code.

The Branch Protection feature leverages the Pointer Authentication and Branch
Target Identification extension (PACBTI) which is optional and available in
Armv8.1-M architecture.

PACBTI is designed to mitigate Return-Oriented Programming (ROP) and
Jump-Oriented Programming (JOP) security exploit attacks.
