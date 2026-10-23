---
id: "tfm-tf-m-power-management-service-desi-introduction"
type: "concept"
domain: "security"
title: "TF-M Power Management Service design (RFC): Introduction"
summary: "The PWR-MGMT service provides a secure endpoint to perform power management operations for the core itself, devices and peripherals, and other cores."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/services/tfm_power_mgmt.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/services/tfm_power_mgmt.html#introduction"
license: "BSD-3-Clause"
mode: "V"
---

The PWR-MGMT service provides a secure endpoint to perform power management
operations for the core itself, devices and peripherals, and other cores.

When peripheral power and clock controls are mapped to SPE, then this service
can access such resources and query or change the status of them.

The partition brokers power-management requests from NS/S clients to SPE.
