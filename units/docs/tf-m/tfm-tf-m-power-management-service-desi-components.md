---
id: "tfm-tf-m-power-management-service-desi-components"
type: "concept"
domain: "security"
title: "TF-M Power Management Service design (RFC): Components"
summary: "The whole functionality is achieved by combining three parts: - Service: secure_fw/partitions/power_mgmt/ - NS/S client API: interface/include/power_mgmt/tfm_power_mgmt_api.h and interface/src/tfm_power_mgmt_api.c - Platform code/hooks: platform/include/tfm_plat_power_mgmt.h and tfm_plat_power_mgmt.c and tfm_plat_power_mgmt_defs.h"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/services/tfm_power_mgmt.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/services/tfm_power_mgmt.html#components"
license: "BSD-3-Clause"
mode: "V"
---

The whole functionality is achieved by combining three parts:
  - Service: secure_fw/partitions/power_mgmt/
  - NS/S client API:
    `interface/include/power_mgmt/tfm_power_mgmt_api.h` and
    `interface/src/tfm_power_mgmt_api.c`
  - Platform code/hooks:
    `platform/include/tfm_plat_power_mgmt.h` and
    `tfm_plat_power_mgmt.c` and
    `tfm_plat_power_mgmt_defs.h`
