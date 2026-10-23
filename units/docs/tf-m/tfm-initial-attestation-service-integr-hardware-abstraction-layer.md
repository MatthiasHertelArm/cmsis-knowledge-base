---
id: "tfm-initial-attestation-service-integr-hardware-abstraction-layer"
type: "concept"
domain: "security"
title: "Initial Attestation Service Integration Guide: Code structure / Hardware abstraction layer"
summary: "The following API definitions are intended to retrieve the platform specific claims. System integrators must implement these interface according to their SoC and software design."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/integration_guide/services/tfm_attestation_integration_guide.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/services/tfm_attestation_integration_guide.html#hardware-abstraction-layer"
license: "BSD-3-Clause"
mode: "V"
---

_Part of: Code structure_

The following API definitions are intended to retrieve the platform specific
claims. System integrators **must** implement these interface according to their
SoC and software design. Detailed definition of the claims are above
in the claims in the initial attestation token paragraph.

- `tfm_attest_hal_get_security_lifecycle()`: Get the security lifecycle of the
  device.
- `tfm_attest_hal_get_verification_service()`: Get the verification
  service indicator for initial attestation.
- `tfm_attest_hal_get_profile_definition()`: Get the name of the profile
  definition document for initial attestation.
- `tfm_plat_get_boot_seed()`: Get the boot seed, which is a constant random
  number during a boot cycle.
- `tfm_plat_get_implementation_id`: Get the implementation ID of the
  device.
- `tfm_plat_get_cert_ref`: Get the hardware version of the device.
