---
id: "tfm-platform-service-integration-guide-introduction"
type: "concept"
domain: "security"
title: "Platform Service Integration Guide: Introduction"
summary: "TF-M Platform service is a trusted service which allows secure partitions and non-secure applications to interact with some platform-specific components."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/integration_guide/services/tfm_platform_integration_guide.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/services/tfm_platform_integration_guide.html#introduction"
license: "BSD-3-Clause"
mode: "V"
---

TF-M Platform service is a trusted service which allows secure partitions and
non-secure applications to interact with some platform-specific components.
There are a number of features which requires some interaction with
platform-specific components which are at the same time essential for the
security of the system.
Therefore, those components need to be handled by a secure partition which is
part of the trusted compute base.

These platform-specific components include system reset, power management,
Debug, GPIO, etc.
