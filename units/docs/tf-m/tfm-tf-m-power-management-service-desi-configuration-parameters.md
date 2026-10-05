---
id: "tfm-tf-m-power-management-service-desi-configuration-parameters"
type: "concept"
domain: "security"
title: "TF-M Power Management Service design (RFC): Configuration parameters"
summary: "To enable the partition in the build, use TFM_PARTITION_POWER_MGMT so that all the relevant interface code will be made available to NS callers."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/services/tfm_power_mgmt.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/services/tfm_power_mgmt.html#configuration-parameters"
license: "BSD-3-Clause"
mode: "V"
---

To enable the partition in the build, use TFM_PARTITION_POWER_MGMT so that all
the relevant interface code will be made available to NS callers.

By default, the service is disabled.

The service supports CPU power states only for CM55 & CM85
via the internal build-derived TFM_POWER_MGMT_ARCH_SUPPORTED option.
For other cores, the service only supports CUSTOM power state transitions.

Non-M55/M85 platforms can still use custom/device states through callbacks,
but generic CPU states are not supported.
