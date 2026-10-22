---
id: "tfm-memory-access-check-of-trusted-fir-general-retrieval-functions"
type: "concept"
domain: "security"
title: "Memory Access Check of Trusted Firmware-M in Multi-Core Topology: Data Types and APIs / General retrieval functions"
summary: "TF-M implements 3 general retrieval functions to retrieve memory region security attributes or memory protection configurations, based on static system-level memory layout. Platform specific HAL functions can invoke those 3 general functions to simplify implementations."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/multi-cpu/tfm_multi_core_access_check.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/multi-cpu/tfm_multi_core_access_check.html#general-retrieval-functions"
license: "BSD-3-Clause"
mode: "V"
---

_Part of: Data Types and APIs_

TF-M implements 3 general retrieval functions to retrieve memory region security attributes or
memory protection configurations, based on static system-level memory layout. Platform specific HAL
functions can invoke those 3 general functions to simplify implementations.

- `tfm_get_mem_region_security_attr()` retrieves general security attributes from static
  system-level memory layout.
- `tfm_get_secure_mem_region_attr()` retrieves general secure memory protection configurations
  from static system-level memory layout.
- `tfm_get_ns_mem_region_attr()` retrieves general non-secure memory protection configurations
  from static system-level memory layout.

If a multi-core platform's memory layout may vary in runtime, it shall not rely on these 3 functions
to retrieve static configurations.
These 3 functions run through memory layout table to check against each memory section one by one,
with pure software implementation. It might cost more time compared to hardware-based memory access
check.


#### `tfm_get_mem_region_security_attr()`


`tfm_get_mem_region_security_attr()` retrieves security attributes of target memory region
according to the static system-level memory layout and fills the `security_attr_info_t`.

```c

void tfm_get_mem_region_security_attr(const void *p, size_t s,
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


#### `tfm_get_secure_mem_region_attr()`


`tfm_get_secure_mem_region_attr()` retrieves general secure memory protection configuration
information of the target memory region according to the static system-level memory layout and fills
the `mem_attr_info_t`.

```c

void tfm_get_secure_mem_region_attr(const void *p, size_t s,
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


#### `tfm_get_ns_mem_region_attr()`


`tfm_get_ns_mem_region_attr()` retrieves general non-secure memory protection configuration
information of the target memory region according to the static system-level memory layout and fills
the `mem_attr_info_t`.

```c

void tfm_get_ns_mem_region_attr(const void *p, size_t s,
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

--------------

*Copyright (c) 2019-2024, Arm Limited. All rights reserved.*
