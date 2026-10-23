---
id: "tfm-non-secure-client-extension-integr-what-is-nsce-for"
type: "concept"
domain: "security"
title: "Non-secure Client Extension Integration Guide: What is NSCE for"
summary: "Besides the secure services provided via PSA APIs, there are two interactions between TF-M and NSPE RTOS."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/integration_guide/non-secure_client_extension_integration_guide.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/non-secure_client_extension_integration_guide.html#what-is-nsce-for"
license: "BSD-3-Clause"
mode: "V"
---

Besides the secure services provided via PSA APIs, there are two interactions
between TF-M and NSPE RTOS.

- Non-secure context management in TF-M

  When a NS task calls a secure service, a context is maintained in TF-M. If
  TF-M supports multiple secure service calls, the context needs to be loaded
  and saved with the corresponding NS task when the RTOS kernel (the kernel)
  does scheduling.

- Non-secure client ID (NSID) management

  As per PSA Firmware Framework specification, NSID is required for a secure
  service call from the NSPE. The NSID can be managed by either SPM (the same
  NSID must be used for all connections) or the NSPE RTOS. For the latter case,
  the NSPE RTOS must provide the NSID for each connection.

NSCE is implemented to support the interactions above.

- Provide the interface to NSPE RTOS for managing the context in TF-M.

- Provide a mechanism to NSPE RTOS for providing the NSID for each connection.
