---
id: "tfm-platform-provisioning-provisioning-development-hardware"
type: "concept"
domain: "security"
title: "Platform Provisioning: Provisioning development hardware"
summary: "If TFM_DUMMY_PROVISIONING is enabled in the cmake config (as it is by default), a set of dummy keys / data will be provisioned."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/integration_guide/platform_provisioning.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/platform_provisioning.html#provisioning-development-hardware"
license: "BSD-3-Clause"
mode: "V"
---

If `TFM_DUMMY_PROVISIONING` is enabled in the cmake config (as it is by
default), a set of dummy keys / data will be provisioned. The dummy IAK matches
the IAK tested by the TF-M tests, and the dummy bl2 ROTPKs match the dummy bl2
keys used by default. `TFM_DUMMY_PROVISIONING` _MUST_ not be used in
production hardware, as the keys are insecure.
