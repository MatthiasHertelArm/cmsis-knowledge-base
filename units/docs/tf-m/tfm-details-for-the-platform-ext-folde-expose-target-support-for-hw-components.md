---
id: "tfm-details-for-the-platform-ext-folde-expose-target-support-for-hw-components"
type: "concept"
domain: "security"
title: "Details for the platform/ext folder: Expose target support for HW components"
summary: "Services may require HW components to be supported by the target to enable some features (e.g. PS service with rollback protection, etc)."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/integration_guide/source_structure/platform_ext_folder.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/source_structure/platform_ext_folder.html#expose-target-support-for-hw-components"
license: "BSD-3-Clause"
mode: "V"
---

Services may require HW components to be supported by the target to enable some
features (e.g. PS service with rollback protection, etc). The following
definitions need to be set in the .cmake file if the target has the following
HW components:

- `TARGET_NV_COUNTERS_ENABLE` - Specifies that the target has non-volatile
  (NV) counters.

--------------

*Copyright (c) 2020-2022 Cypress Semiconductor Corporation (an Infineon company)
or an affiliate of Cypress Semiconductor Corporation. All rights reserved.*
*SPDX-FileCopyrightText: Copyright The TrustedFirmware-M Contributors*

*SPDX-License-Identifier: BSD-3-Clause*
