---
id: "tfm-platform-service-integration-guide-tf-m-platform-service"
type: "concept"
domain: "security"
title: "Platform Service Integration Guide: TF-M Platform service"
summary: "The Platform service interfaces and types are defined and documented in interface/include/tfm_platform_api.h"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/integration_guide/services/tfm_platform_integration_guide.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/services/tfm_platform_integration_guide.html#tf-m-platform-service"
license: "BSD-3-Clause"
mode: "V"
---

The Platform service interfaces and types are defined and documented in
`interface/include/tfm_platform_api.h`

- `tfm_platform_sp.h/c` : These files define and implement functionalities
  related to the platform service.
- `tfm_platform_api.c` : This file implements `tfm_platform_api.h`
  functions to be called from the secure partitions. This is the entry point
  when the secure partitions request an action to the Platform service
  (e.g system reset).
