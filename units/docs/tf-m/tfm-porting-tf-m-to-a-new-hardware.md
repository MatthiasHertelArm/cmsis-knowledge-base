---
id: "tfm-porting-tf-m-to-a-new-hardware"
type: "concept"
domain: "security"
title: "Porting TF-M to a New Hardware"
summary: "The purpose of this document is to provide a guide on how to integrate TF-M with another hardware platform."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/integration_guide/platform/porting_tfm_to_a_new_hardware.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/platform/porting_tfm_to_a_new_hardware.html"
license: "BSD-3-Clause"
mode: "V"
---

The purpose of this document is to provide a guide on how to integrate TF-M
with another hardware platform. This document will give general guidance on
how to port a platform on the TF-M build system and which interfaces must
exist on the platform for TF-M (S and NS) to run on this new platform.
