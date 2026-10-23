---
id: "tfm-branch-protection-pac-and-bti"
type: "concept"
domain: "security"
title: "Branch Protection: PAC and BTI"
summary: "It is possible to have some combinations of the PAC and BTI options above. The allowed values for CONFIG_TFM_BRANCH_PROTECTION_FEAT are listed below, but only one option can be used:"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/integration_guide/branch_protection.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/branch_protection.html#pac-and-bti"
license: "BSD-3-Clause"
mode: "V"
---

It is possible to have some combinations of the PAC and BTI options above.
The allowed values for `CONFIG_TFM_BRANCH_PROTECTION_FEAT` are listed below,
but only one option can be used:

* `BRANCH_PROTECTION_DISABLED` - PACBTI feature is disabled
* `BRANCH_PROTECTION_NONE` - PACBTI instructions are not generated
* `BRANCH_PROTECTION_STANDARD` - Enables pointer authentication and branch target identification, leaf functions excluded
* `BRANCH_PROTECTION_PACRET` - Enables pointer authentication only, leaf functions excluded
* `BRANCH_PROTECTION_PACRET_LEAF` - Enables pointer authentication on all functions, including leaf functions
* `BRANCH_PROTECTION_BTI` - Enables branch target identification only

Note that PACBTI is conditional to both architecture support and compiler
support.

The build system performs checks to ensure that support is available and
terminates the build process if the required conditions are not met.
