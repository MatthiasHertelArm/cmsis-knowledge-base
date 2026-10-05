---
id: "tfm-initial-attestation-service-integr-service-interface-definitions"
type: "concept"
domain: "security"
title: "Initial Attestation Service Integration Guide: Code structure / Service interface definitions"
summary: "Initial Attestation Service Integration Guide: Code structure / Service interface definitions"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/integration_guide/services/tfm_attestation_integration_guide.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/services/tfm_attestation_integration_guide.html#service-interface-definitions"
license: "BSD-3-Clause"
mode: "V"
---

_Part of: Code structure_

- **Boot loader interface**: The attestation service might include data
  in the token about the distinct software components in the device. This data
  is provided by the boot loader and must be encoded in the TLV format,
  definition is described below in the boot loader interface paragraph. Possible
  claims in the boot status are described above in the software components
  paragraph.
- **Hardware abstraction layer**:
    - Headers are located in `platform/include` folder.
    - `tfm_attest_hal.h`: Expose an API to get the following claims:
      security lifecycle, verification service indicator, profile definition.
    - `tfm_plat_boot_seed.h`: Expose an API to get the boot seed claim.
    - `tfm_plat_device_id.h`: Expose an API to get the following claims:
      implementation ID, hardware version.
- **SPM interface**:
    - `attestation.h`: Expose an API to bind attestation service to an SPM
      implementation.
- **PSA interface**:
    - `psa/initial_attestation.h`: Public API definition of initial
      attestation service.
- **Crypto interface**:
    - `t_cose_crypto.h`: Expose an API to bind the `t_cose` implementation
      to any cryptographic library.
