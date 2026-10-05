---
id: "tfm-musca-b1-platform-specifics-platform-pin-service"
type: "concept"
domain: "security"
title: "Musca-B1 Platform Specifics: Platform pin service"
summary: "This service is designed to perform secure pin services of the platform (e.g alternate function setting, pin mode setting, etc)."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/platform/arm/musca_b1/readme.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/platform/arm/musca_b1/.html#platform-pin-service"
license: "BSD-3-Clause"
mode: "V"
---

This service is designed to perform secure pin services of the platform
(e.g alternate function setting, pin mode setting, etc).
The service uses the IOCTL API of TF-M's Platform Service, which allows the
non-secure application to make pin service requests on Musca B1 based on a
generic service request delivery mechanism.
