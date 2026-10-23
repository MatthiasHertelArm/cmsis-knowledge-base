---
id: "tfm-platform-service-integration-guide-current-service-limitations"
type: "concept"
domain: "security"
title: "Platform Service Integration Guide: Current Service Limitations"
summary: "Platform Service Integration Guide: Current Service Limitations"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/integration_guide/services/tfm_platform_integration_guide.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/services/tfm_platform_integration_guide.html#current-service-limitations"
license: "BSD-3-Clause"
mode: "V"
---

- **system reset** - The system reset functionality is only supported in
  isolation level 1. Currently the mechanism by which PSA-RoT services should
  run in privileged mode in level 3 is not in place due to an ongoing work in
  TF-M Core. So, the `NVIC_SystemReset` call performed by the service is
  expected to generate a memory fault when it tries to access the `SCB->AIRCR`
  register in level 3 isolation.

--------------

*Copyright (c) 2018-2022, Arm Limited. All rights reserved.*
