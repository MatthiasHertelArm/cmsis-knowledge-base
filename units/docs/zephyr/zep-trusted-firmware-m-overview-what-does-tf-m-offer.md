---
id: "zep-trusted-firmware-m-overview-what-does-tf-m-offer"
type: "concept"
domain: "security"
title: "Trusted Firmware-M Overview: What Does TF-M Offer?"
summary: "Through a set of secure services and by design, TF-M provides:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/services/tfm/overview.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/services/tfm/overview.rst"
license: "Apache-2.0"
mode: "V"
---

Through a set of secure services and by design, TF-M provides:

* Isolation of secure and non-secure resources
* Embedded-appropriate crypto
* Management of device secrets (keys, etc.)
* Firmware verification (and encryption)
* Protected off-chip data storage and retrieval
* Proof of device identity (device attestation)
* Audit logging
