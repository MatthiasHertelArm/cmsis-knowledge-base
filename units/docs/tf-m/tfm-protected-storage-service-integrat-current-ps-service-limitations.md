---
id: "tfm-protected-storage-service-integrat-current-ps-service-limitations"
type: "concept"
domain: "security"
title: "Protected Storage Service Integration Guide: Current PS Service Limitations"
summary: "Protected Storage Service Integration Guide: Current PS Service Limitations"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/integration_guide/services/tfm_ps_integration_guide.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/services/tfm_ps_integration_guide.html#current-ps-service-limitations"
license: "BSD-3-Clause"
mode: "V"
---

- **Asset size limitation** - An asset is stored in a contiguous space in a
  block/sector. Hence, the maximum asset size can be up-to the size of the
  data block/sector. Detailed information about the maximum asset size can be
  found in the section `Maximum asset size` below.

- **Fragmentation** - The current design does not support fragmentation, as an
  asset is stored in a contiguous space in a block.
  Each block can potentially store multiple assets.
  A delete operation implicitly moves all the assets towards the top of the
  block to avoid fragmentation within block. However, this may also result in
  unutilized space at the end of each block.

- **Non-hierarchical storage model** - The current design uses a
  non-hierarchical storage model, as a filesystem, where all the assets are
  managed by a linearly indexed list of metadata. This model locates the
  metadata in blocks which are always stored in the same flash location. That
  increases the number of writes in a specific flash location as every change in
  the storage area requires a metadata update.

- **PSA internal trusted storage API** - In the current design, the service does
  not use the PSA Internal Trusted Storage API to write the rollback protection
  values stored in the internal storage.

- **Protection against physical storage medium failure** - Complete handling of
  inherent failures of storage mediums (e.g. bad blocks in a NAND based device)
  is not supported by the current design.

- **Key diversification** - In a more robust design, each asset would be
  encrypted through a different key.

- **Lifecycle management** - Currently, it does not support any subscription
  based keys and certificates required in a secure lifecycle management. Hence,
  an asset's validity time-stamp can not be invalidated based on the system
  time.

- **Provisioning vs user/device data** - In the current design, all assets are
  treated in the same manner. In an alternative design, it may be required to
  create separate partitions for provisioning content and user/device generated
  content. This is to allow safe update of provisioning data during firmware
  updates without the need to wipe out the user/device generated data.
