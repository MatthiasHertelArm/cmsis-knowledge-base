---
id: "tfm-memory-access-check-of-trusted-fir-hal-apis"
type: "concept"
domain: "security"
title: "Memory Access Check of Trusted Firmware-M in Multi-Core Topology: Data Types and APIs / HAL APIs"
summary: "tfm_hal_get_mem_security_attr() retrieves the current active security configuration information and fills the security_attr_info_t."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/multi-cpu/tfm_multi_core_access_check.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/multi-cpu/tfm_multi_core_access_check.html#hal-apis"
license: "BSD-3-Clause"
mode: "V"
---

_Part of: Data Types and APIs_

#### `tfm_hal_get_mem_security_attr()`


`tfm_hal_get_mem_security_attr()` retrieves the current active security configuration information
and fills the `security_attr_info_t`.

```c

void tfm_hal_get_mem_security_attr(const void *p, size_t s,
                                   struct security_attr_info_t *p_attr);
```
+--------------------------------------------------------------------+
| **Parameters**                                                     |
+-------------+------------------------------------------------------+
| `p`       | Base address of the target memory region             |
+-------------+------------------------------------------------------+
| `s`       | Size of the target memory region                     |
+-------------+------------------------------------------------------+
| `p_attr`  | Pointer to the `security_attr_info_t` to be filled |
+-------------+------------------------------------------------------+
| **Return**                                                         |
+-------------+------------------------------------------------------+
| `void`    | None                                                 |
+-------------+------------------------------------------------------+

The implementation should be decoupled from TF-M current isolation level or
access check policy.

All the fields in `security_attr_info_t` shall be explicitly set in
`tfm_hal_get_mem_security_attr()`.

If the target memory region crosses boundaries of different security regions or levels in security
isolation configuration, `tfm_hal_get_mem_security_attr()` should determine whether the memory
region violates current security isolation.
It is recommended to mark the target memory region as invalid in such case, even if the adjoining
regions or levels have the same security configuration.

If the target memory region is not explicitly specified in memory security configuration,
`tfm_hal_get_mem_security_attr()` can return the following values according to actual use case:

- Either set `is_valid = false`
- Or set `is_valid = true` and set `is_secure` according to platform specific policy.


#### `tfm_hal_get_secure_access_attr()`


`tfm_hal_get_secure_access_attr()` retrieves the secure memory protection configuration
information and fills the `mem_attr_info_t`.

```c

void tfm_hal_get_secure_access_attr(const void *p, size_t s,
                                    struct mem_attr_info_t *p_attr);
```
+--------------------------------------------------------------+
| **Parameters**                                               |
+------------+-------------------------------------------------+
| `p`      | Base address of the target memory region        |
+------------+-------------------------------------------------+
| `s`      | Size of the target memory region                |
+------------+-------------------------------------------------+
| `p_attr` | Pointer to the `mem_attr_info_t` to be filled |
+------------+-------------------------------------------------+
| **Return**                                                   |
+------------+-------------------------------------------------+
| `void`   | None                                            |
+------------+-------------------------------------------------+

The implementation should be decoupled from TF-M current isolation level or
access check policy.

All the fields in `mem_attr_info_t` shall be explicitly set in
`tfm_hal_get_secure_access_attr()`, according to current active memory protection configuration.
It is recommended to retrieve the attributes from secure MPU and other hardware memory protection
unit(s). The implementation can also be simplified by checking static system-level memory layout.

If the target memory region is not specified in current active secure memory protection
configuration, `tfm_hal_get_secure_access_attr()` can select the following values according to
actual use case.

- Either directly set `is_valid` to `false`
- Or set `is_valid` to `true` and set other fields according to other memory assignment
  information, such as static system-level memory layout.

If secure memory protection unit(s) is *disabled* and the target memory region is a valid area
according to platform resource assignment, `tfm_hal_get_secure_access_attr()` must set
`is_mpu_enabled` to `false` and set other fields according to current system-level memory
layout.


#### `tfm_hal_get_ns_access_attr()`


`tfm_hal_get_ns_access_attr()` retrieves the non-secure memory protection configuration
information and fills the `mem_attr_info_t`.

```c

void tfm_hal_get_ns_access_attr(const void *p, size_t s,
                                struct mem_attr_info_t *p_attr);
```
+--------------------------------------------------------------+
| **Parameters**                                               |
+------------+-------------------------------------------------+
| `p`      | Base address of the target memory region        |
+------------+-------------------------------------------------+
| `s`      | Size of the target memory region                |
+------------+-------------------------------------------------+
| `p_attr` | Pointer to the `mem_attr_info_t` to be filled |
+------------+-------------------------------------------------+
| **Return**                                                   |
+------------+-------------------------------------------------+
| `void`   | None                                            |
+------------+-------------------------------------------------+

The implementation should be decoupled from TF-M current isolation level or
access check policy.

Since non-secure core runs asynchronously, the non-secure MPU setting may be modified by NSPE OS and
therefore the attributes of the target memory region can be unavailable during
`tfm_hal_get_ns_access_attr()` execution in TF-M.
When the target memory region is not specified in non-secure MPU, `tfm_hal_get_ns_access_attr()`
can set the fields according to other memory setting information, such as static system-level memory
layout.

If non-secure memory protection unit(s) is *disabled* and the target memory region is a valid area
according to platform resource assignment, `tfm_hal_get_ns_access_attr()` can set the following
fields in `mem_attr_info_t` to default values:

- `is_mpu_enabled = false`
- `is_valid = true`
- `is_xn = true`
- `is_priv_rd_allow = true`
- `is_unpriv_rd_allow = true`

`is_priv_wr_allow` and `is_unpriv_wr_allow` can be set according to current system-level memory
layout, such as whether it is in code section or data section.
