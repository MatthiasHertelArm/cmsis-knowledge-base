---
id: "tfm-hardware-abstraction-layer-status-codes"
type: "concept"
domain: "security"
title: "Hardware Abstraction Layer: Status Codes"
summary: "These are common status and error codes for all HAL APIs."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/software/hardware_abstraction_layer.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/software/hardware_abstraction_layer.html#status-codes"
license: "BSD-3-Clause"
mode: "V"
---

These are common status and error codes for all `HAL` APIs.


### Types


#### tfm_hal_status_t

This is a status code to be used as the return type of `HAL` APIs.

```c

enum tfm_hal_status_t {
    TFM_HAL_ERROR_MEM_FAULT = SCHAR_MIN,
    TFM_HAL_ERROR_MAX_VALUE,
    TFM_HAL_ERROR_BAD_STATE,
    TFM_HAL_ERROR_NOT_SUPPORTED,
    TFM_HAL_ERROR_INVALID_INPUT,
    TFM_HAL_ERROR_NOT_INIT,
    TFM_HAL_ERROR_GENERIC,
    TFM_HAL_SUCCESS = 0
};
```

### Error Codes

Negative values indicate an error. Zero and positive values indicate success.

Here is the general list. The detailed usages for each error code are described
in the API introduction sections.


##### TFM_HAL_SUCCESS

Status code to indicate general success.


##### TFM_HAL_ERROR_GENERIC

Status code to indicate an error that does not correspond to any defined failure
cause.


##### TFM_HAL_ERROR_NOT_INIT

Status code to indicate that the module is not initialed.


##### TFM_HAL_ERROR_INVALID_INPUT

Status code to indicate that the input is invalid.


##### TFM_HAL_ERROR_NOT_SUPPORTED

Status code to indicate that the requested operation or a parameter is not
supported.


##### TFM_HAL_ERROR_BAD_STATE

Status code to indicate that the requested action cannot be performed in the
current state.


##### TFM_HAL_ERROR_MAX_VALUE

Status code to indicate that the current number has got the max value.


##### TFM_HAL_ERROR_MEM_FAULT

Status code to indicate that the memory check failed.
