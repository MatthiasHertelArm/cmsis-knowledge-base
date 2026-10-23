---
id: "tfm-platform-provisioning"
type: "concept"
domain: "security"
title: "Platform Provisioning"
summary: "TF-M stores any data that should be provisioned at the factory in OTP memory. The default is that this OTP memory is actually implemented using on-chip flash, the same that is used to implement the ITS service."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/integration_guide/platform_provisioning.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/platform_provisioning.html"
license: "BSD-3-Clause"
mode: "V"
---

TF-M stores any data that should be provisioned at the factory in OTP memory.
The default is that this OTP memory is actually implemented using on-chip flash,
the same that is used to implement the ITS service.

If the lifecycle state is in the `TFM_SLC_ASSEMBLY_AND_TEST` [1]_ state (which
is the default for non-provisioned boards), then TF-M will attempt to provision
the:
- HUK
instead of booting. It will read the data from the
`assembly_and_test_prov_data` struct, and will then provision it to OTP. The
lifecycle state will then transition to `TFM_SLC_PSA_ROT_PROVISIONING` [1]_.

If the lifecycle state is in the `TFM_SLC_PSA_ROT_PROVISIONING` [1]_ state,
then TF-M will attempt to provision the:

- IAK
- boot seed
- implementation id
- certification reference
- bl2 ROTPKs (of which there are up to 4)
- entropy seed

Once all of these have been loaded from the `psa_rot_prov_data` struct and
provisioned to OTP, the LCS will transition to `TFM_SLC_SECURED` [1]_. Note
that this provisioning step will be run immediately after the
`TFM_SLC_ASSEMBLY_AND_TEST` [1]_ provisioning stage if the lifecycle
transition completed successfully.
