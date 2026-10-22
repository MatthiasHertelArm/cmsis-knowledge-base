---
id: "tfm-platform-service-integration-guide-platform-hal"
type: "concept"
domain: "security"
title: "Platform Service Integration Guide: Platform HAL"
summary: "The Platform Service relies on a platform-specific implementation to perform some functionalities. Mandatory functionality (e.g. system reset) that are required to be implemented for a platform to be supported by TF-M have their dedicated HAL API functions."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/integration_guide/services/tfm_platform_integration_guide.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/services/tfm_platform_integration_guide.html#platform-hal"
license: "BSD-3-Clause"
mode: "V"
---

The Platform Service relies on a platform-specific implementation to
perform some functionalities. Mandatory functionality (e.g. system reset)
that are required to be implemented for a platform to be supported by TF-M have
their dedicated HAL API functions. Additional platform-specific services can be
provided using the IOCTL function call.

For API specification, please check: `platform/include/tfm_platform_system.h`

An implementation is provided in all the supported platforms. Please, check
`platform/ext/target/<SPECIFIC_TARGET_FOLDER>/services/src/tfm_platform_system.c`
for examples.

The API **must** be implemented by the system integrators for their targets.


### IOCTL


A single entry point to platform-specific code across the HAL is provided by the
IOCTL service and HAL function:

```c

enum tfm_platform_err_t tfm_platform_hal_ioctl(tfm_platform_ioctl_req_t request,
                                               psa_invec *in_vec,
                                               psa_outvec *out_vec);
```
A request type is provided by the client, with additional parameters contained
in the optional `in_vec` parameter. An optional output buffer can be passed to
the service in `out_vec`.
An IOCTL request type not supported on a particular platform should return
`TFM_PLATFORM_ERR_NOT_SUPPORTED`


### Non-Volatile counters


The Platform Service provides an abstracted service for exposing the NV counters
to secure partitions or non-secure callers. The following operations are
supported:

- Increment a counter.
- Read a counter value to a preallocated buffer.

```c

enum tfm_platform_err_t
tfm_platform_nv_counter_increment(uint32_t counter_id);

enum tfm_platform_err_t
tfm_platform_nv_counter_read(uint32_t counter_id,
                             uint32_t size, uint8_t *val);
```
The range of counters id is defined in :
`platform/include/tfm_plat_nv_counters.h`

For Level 2,3 isolation implementations, secure partitions in the
Application Root of Trust, should have `TFM_PLATFORM_SERVICE` set as a
dependency for access to the NV counter API.
