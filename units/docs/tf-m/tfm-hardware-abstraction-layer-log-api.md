---
id: "tfm-hardware-abstraction-layer-log-api"
type: "concept"
domain: "security"
title: "Hardware Abstraction Layer: API Definition for TF-M SPM / Log API"
summary: "The log API is used by the TF-M log system. The log device could be uart, memory, usb, etc."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/software/hardware_abstraction_layer.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/software/hardware_abstraction_layer.html#log-api"
license: "BSD-3-Clause"
mode: "V"
---

_Part of: API Definition for TF-M SPM_

The log API is used by the `TF-M` log system.
The log device could be uart, memory, usb, etc.


##### APIs


###### tfm_hal_output_partition_log()

**Prototype**

```c

int32_t tfm_hal_output_partition_log(const unsigned char *str, uint32_t len)
```
**Description**

This API is called by Secure Partition to output logs.

**Parameter**

- `str` - The string to output.
- `len` - Length of the string in bytes.

**Return Values**

- Positive values - Number of bytes output.
- `TFM_HAL_ERROR_NOT_INIT` - The log device has not been initialized.
- `TFM_HAL_ERROR_INVALID_INPUT` - Invalid inputs when `str` is `NULL` or
  `len` is zero.

**Note**

None.


###### tfm_hal_output_spm_log()

**Prototype**

```c

int32_t tfm_hal_output_spm_log(const unsigned char *str, uint32_t len)
```
**Description**

This API is called by `SPM` to output logs.

**Parameter**

- `str` - The string to output.
- `len` - Length of the string in bytes.

**Return Values**

- Positive numbers - Number of bytes output.
- `TFM_HAL_ERROR_NOT_INIT` - The log device has not been initialized.
- `TFM_HAL_ERROR_INVALID_INPUT` - Invalid inputs when `str` is `NULL`
  or `len` is zero.

**Note**

Please check TF-M log system
for more information.
