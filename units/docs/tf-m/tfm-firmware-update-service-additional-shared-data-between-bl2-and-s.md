---
id: "tfm-firmware-update-service-additional-shared-data-between-bl2-and-s"
type: "concept"
domain: "security"
title: "Firmware Update Service: Additional shared data between BL2 and SPE"
summary: "An additional TLV area \"image version\" is added into the shared memory between BL2 and TF-M. So that the firmware update partition can get the image version."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/services/tfm_fwu_service.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/services/tfm_fwu_service.html#additional-shared-data-between-bl2-and-spe"
license: "BSD-3-Clause"
mode: "V"
---

An additional TLV area "image version" is added into the shared memory between
BL2 and TF-M. So that the firmware update partition can get the image version.
Even though the image version information is also included in the `BOOT RECORD`
TLV area which is encoded by CBOR, adding a dedicated `image version` TLV area
is preferred to avoid involving the CBOR encoder which can increase the code
size. The FWU partition will read the shared data at the partition
initialization.
