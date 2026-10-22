---
id: "tfm-non-secure-client-extension-integr-nsce-component-diagram"
type: "concept"
domain: "security"
title: "Non-secure Client Extension Integration Guide: NSCE component diagram"
summary: "This diagram shows the components of NSCE."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/integration_guide/non-secure_client_extension_integration_guide.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/non-secure_client_extension_integration_guide.html#nsce-component-diagram"
license: "BSD-3-Clause"
mode: "V"
---

This diagram shows the components of NSCE.

- NSCE interface: The NSCE API interface to NSPE RTOS.

- NS Client Context Manager: It is the internal component of SPM that is used to
  manage the NS client context. It is not accessible to NSPE.
