---
id: "tfm-firmware-update-service-limitations-of-current-implementation"
type: "concept"
domain: "security"
title: "Firmware Update Service: Limitations of current implementation"
summary: "Currently, the MCUboot based implementation does not record image update results like failure or success. And FWU partition does not detect failure errors in bootloader installation."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/services/tfm_fwu_service.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/services/tfm_fwu_service.html#limitations-of-current-implementation"
license: "BSD-3-Clause"
mode: "V"
---

Currently, the MCUboot based implementation does not record image update results like failure or
success. And FWU partition does not detect failure errors in bootloader installation. If an image
installation fails in the bootloader and the old image still runs after reboot, `PSA_FWU_READY`
state will be returned by `psa_fwu_query()` after reboot.

Currently, image download recovery after a reboot is not supported. If a reboot happens in image
preparation, the downloaded image data will be ignored after the reboot.

The MCUboot based implementation only fills the data structure
`psa_fwu_impl_info_t` in `psa_fwu_query()` when the component is in
CANDIDATE state. Otherwise, an empty `psa_fwu_impl_info_t` is returned when
the component is in other states.
