---
id: "tfm-hardware-abstraction-layer-source-files"
type: "concept"
domain: "security"
title: "Hardware Abstraction Layer: Source Files"
summary: "This section describes the source file of the TF-M HAL, including the header and c files."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/software/hardware_abstraction_layer.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/software/hardware_abstraction_layer.html#source-files"
license: "BSD-3-Clause"
mode: "V"
---

This section describes the source file of the `TF-M` `HAL`,
including the header and c files.


### tfm_hal_defs.h

This header file contains the definitions of common macros and types used by all
`HAL` APIs. Please refer to Status Codes for detailed definitions.


### tfm_hal_[module].[h/c]

All other headers and c files are classified by the modules, such as isolation,
platform, interrupt, devices, etc.


**Note:** There are common files in the platform folder include the implemented implement all the sub APIs.
