---
id: "tfm-spm-backends-tf-m-configuration-switches"
type: "concept"
domain: "security"
title: "SPM Backends: TF-M Configuration Switches"
summary: "In the TF-M build system, the CONFIG_TFM_SPM_BACKEND configuration is used to select the backend of SPM. The valid values are SFN and IPC."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/integration_guide/spm_backends.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/spm_backends.html#tf-m-configuration-switches"
license: "BSD-3-Clause"
mode: "V"
---

In the TF-M build system, the `CONFIG_TFM_SPM_BACKEND` configuration is used
to select the backend of SPM.
The valid values are `SFN` and `IPC`.

```bash

-DCONFIG_TFM_SPM_BACKEND=SFN
```
If `CONFIG_TFM_SPM_BACKEND` is not set, then `IPC` is the default value.
