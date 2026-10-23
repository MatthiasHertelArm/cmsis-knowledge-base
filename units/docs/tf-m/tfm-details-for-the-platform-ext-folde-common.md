---
id: "tfm-details-for-the-platform-ext-folde-common"
type: "concept"
domain: "security"
title: "Details for the platform/ext folder: Sub-folders / common"
summary: "These contain the linker scripts used to configure the memory regions in TF-M regions."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/integration_guide/source_structure/platform_ext_folder.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/source_structure/platform_ext_folder.html#common"
license: "BSD-3-Clause"
mode: "V"
---

_Part of: Sub-folders_

#### armclang and gcc

These contain the linker scripts used to configure the memory regions in TF-M
regions.


#### template

This directory contains platform-independent dummy implementations of the
interfaces in `platform/include`. These implementations can be built directly
for initial testing of a platform port, or used as a basic template for a real
implementation for a particular target. They **must not** be used in production
systems.
