---
id: "tfm-branch-protection-branch-target-identification"
type: "concept"
domain: "security"
title: "Branch Protection: Branch target identification"
summary: "Branch Target Identification (BTI) can mitigate some of the JOP attacks so that indirect branches can only allow target instructions. Such instructions are also called landing pads."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/integration_guide/branch_protection.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/branch_protection.html#branch-target-identification"
license: "BSD-3-Clause"
mode: "V"
---

Branch Target Identification (BTI) can mitigate some of the JOP attacks so that
indirect branches can only allow target instructions. Such instructions are also
called landing pads.
In other words, an indirect branch can only "land" where a specific instruction
is present, otherwise the branch has been compromised and a UsageFault exception
is raised.

The above functionality is achieved by introducing specific instructions at the
beginning of executable code.

To enable BTI in your platform, TF-M supports the following build option:

  - BRANCH_PROTECTION_BTI

One of the above values can be assigned to `CONFIG_TFM_BRANCH_PROTECTION_FEAT`
