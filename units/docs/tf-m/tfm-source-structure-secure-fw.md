---
id: "tfm-source-structure-secure-fw"
type: "concept"
domain: "security"
title: "Source Structure: secure_fw"
summary: "This folder contains components needed by secure firmware and the exported interfaces for application, service development and HAL integration."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/integration_guide/source_structure/source_structure.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/source_structure/source_structure.html#secure-fw"
license: "BSD-3-Clause"
mode: "V"
---

This folder contains components needed by secure firmware and the exported
interfaces for application, service development and HAL integration.

========================= =============================================
Folder name               Description
========================= =============================================
include                   Public headers of `secure_fw`
partitions                Default services and SPRTL
spm                       PSA FF-M SPM implementation
shared                    Sources shared out of SPRTL
========================= =============================================

The shared sources can be referenced by the building system out of SPRTL.
Generally, they are runtime and PSA APIs.


### secure_fw/include

This folder holds public headers for external references by clients,
services and platforms. Avoid putting private headers, not referenced by
other modules in this `include` folder.


### secure_fw/partitions

This folder contains default services implemented as partitions and runtime
utilities used and provided by TF-M.

============================== =============================================
Folder name                    Description
============================== =============================================
lib/runtime                    The SPRTL sources and intermedia files
<partition_x>                  Sources of `partition_x`
<partition_x>/include          RoT Service API headers of `partition_x`
<partition_y>                  Sources of `partition_y`
<partition_y>/include          RoT Service API headers of `partition_y`
============================== =============================================

Here `partition_x` and `partition_y` are examples of RoT services without
detailed structure of them.


### secure_fw/spm

The SPM is the core component to provide a mechanism for providing secure
services complied with PSA FF-M.

============================== =============================================
Folder name                    Description
============================== =============================================
include                        SPM public headers.
core                           SPM base functionalities
\*ext                          Extended SPM functionalities
============================== =============================================

--------------

*Copyright (c) 2020-2023, Arm Limited. All rights reserved.*
