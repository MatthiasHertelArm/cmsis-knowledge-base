---
id: "tfm-adding-secure-partition-add-source-folder"
type: "concept"
domain: "security"
title: "Adding Secure Partition: Process / Add source folder"
summary: "Add a source folder under <TF-M base folder>/secure_fw/partitions for the new secure partition (Let's take example as the folder name):"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/integration_guide/services/tfm_secure_partition_addition.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/services/tfm_secure_partition_addition.html#add-source-folder"
license: "BSD-3-Clause"
mode: "V"
---

_Part of: Process_

Add a source folder under `<TF-M base folder>/secure_fw/partitions` for the
new secure partition (Let's take `example` as the folder name):

This folder should include those parts:

- Manifest file
- CMake configuration files
- Source code files
