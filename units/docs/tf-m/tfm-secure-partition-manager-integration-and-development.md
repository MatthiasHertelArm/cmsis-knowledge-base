---
id: "tfm-secure-partition-manager-integration-and-development"
type: "concept"
domain: "security"
title: "Secure Partition Manager: Integration and development"
summary: "These modules are expected to be object/library level modularised, each module should be generated into object/library at build time:"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/services/secure_partition_manager.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/services/secure_partition_manager.html#integration-and-development"
license: "BSD-3-Clause"
mode: "V"
---

These modules are expected to be object/library level modularised, each
module should be generated into object/library at build time:


* - Name
  - Description
* - SPM
  - All SPM related modules such as SPM, system, and so on.
* - Platform
  - Platform sources are switchable.
* - Services and Secure Partition
  - These items should be standalone.
* - Service Runtime Library
  - This is a shared runtime library.

### HAL

The HAL here mainly refers to the SPM HAL. The SPM HAL implementation is
running with the same privilege level and hardware mode with SPM. The
implementation is object level modularized with SPM.

Check the `HAL` design document for details.


### Configurations

The same TF-M code base is flexible to address different implementation
requirements, from the simplest device with isolation level 1 to the most
complicated device with isolation level 3 and optional isolation rules.

These configurations are set by switches, during the build time, as runtime
support costs extra resources. The common configurations are named `profile`.
There are several profiles defined.
