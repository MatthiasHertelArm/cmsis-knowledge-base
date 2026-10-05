---
id: "tfm-tf-m-power-management-service-desi-examples-integration"
type: "concept"
domain: "security"
title: "TF-M Power Management Service design (RFC): Examples: Integration"
summary: "TF-M Power Management Service design (RFC): Examples: Integration"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/services/tfm_power_mgmt.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/services/tfm_power_mgmt.html#examples-integration"
license: "BSD-3-Clause"
mode: "V"
---

1. Add the partition TFM_PARTITION_POWER_MGMT manifest entry into the
     platform's manifest list
  2. Add tfm_plat_power_mgmt.c source to `platform_s` build target,
     conditionally on TFM_PARTITION_POWER_MGMT
  3. Set TFM_PARTITION_POWER_MGMT to 'ON' in config.cmake
  4. Provide a minimal (at least) implementation of the required APIs in
     platform/ext/target/<platform>/<variant>/ps_service/tfm_plat_power_mgmt.c
  5. Provide a header file with definitions for
     TFM_POWER_MGMT_PWR_STATE_CUSTOM
     TFM_POWER_MGMT_PWR_STATE_DEVICE_CUSTOM
     in platform/ext/target/<platform>/<variant>/tfm_plat_power_mgmt_defs.h
  6. Configure wake sources and secure interrupt routing for needed states.
  7. Validate retained memory placement if SUSPEND is supported.
