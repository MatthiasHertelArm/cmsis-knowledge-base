---
id: "tfm-stm32u3-limitations-to-consider-when-using-the-p"
type: "concept"
domain: "security"
title: "STM32U3: Limitations to Consider When Using the Platform"
summary: "By default, TFM_OTP_DEFAULT_PROVISIONING and DEFAULT_SHARED_DATA switches are enabled in TF-M, to use dummy data in OTP and SRAM shared_data areas as BL2 not supported."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/platform/stm/nucleo_u3c5zi_q/readme.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/platform/stm/nucleo_u3c5zi_q/.html#limitations-to-consider-when-using-the-platform"
license: "BSD-3-Clause"
mode: "V"
---

TF-M Supported without BL1/BL2.

By default, TFM_OTP_DEFAULT_PROVISIONING and DEFAULT_SHARED_DATA switches are enabled in TF-M,
to use dummy data in OTP and SRAM shared_data areas as BL2 not supported.
