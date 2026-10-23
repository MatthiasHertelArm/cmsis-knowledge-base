---
id: "zep-trusted-firmware-m-overview-build-system-integration"
type: "concept"
domain: "security"
title: "Trusted Firmware-M Overview: Build System Integration"
summary: "When using TF-M with a supported platform, TF-M will be automatically built and link in the background as part of the standard Zephyr build process."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/services/tfm/overview.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/services/tfm/overview.rst"
license: "Apache-2.0"
mode: "V"
---

When using TF-M with a supported platform, TF-M will be automatically built and
link in the background as part of the standard Zephyr build process. This
build process makes a number of assumptions about how TF-M is being used, and
has certain implications about what the Zephyr application image can and can
not do:

* The secure processing environment (secure boot and TF-M) starts first
* Resource allocation for Zephyr relies on choices made in the secure image.
