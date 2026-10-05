---
id: "tfm-firmware-update-service-introduction-of-firmware-update-service"
type: "concept"
domain: "security"
title: "Firmware Update Service: Introduction of Firmware Update service"
summary: "The Firmware Update(FWU) service provides the functionality of updating firmware images. It provides a standard interface for updating firmware and it is platform independent. TF-M defines a shim layer to support cooperation between bootloader and FWU service."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/services/tfm_fwu_service.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/services/tfm_fwu_service.html#introduction-of-firmware-update-service"
license: "BSD-3-Clause"
mode: "V"
---

The Firmware Update(FWU) service provides the functionality of updating firmware
images. It provides a standard interface for updating firmware and it is
platform independent. TF-M defines a shim layer to support cooperation between
bootloader and FWU service.

This partition supports the following features:

- Query the firmware store information.
- Image preparation: prepare a new firmware image in the component's firmware store.
- Image installation: install prepared firmware images on all components that have been prepared for installation.
- Image trial: manage a trial of new firmware images atomically on all components that are in TRIAL state.

A typical flow through the component states is shown below [1]_.
