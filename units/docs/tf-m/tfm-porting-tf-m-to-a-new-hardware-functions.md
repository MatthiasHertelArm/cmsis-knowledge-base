---
id: "tfm-porting-tf-m-to-a-new-hardware-functions"
type: "concept"
domain: "security"
title: "Porting TF-M to a New Hardware: Platform Folder / Functions"
summary: "There are a few functions that need to be declared and properly initialized for TF-M to work. The function declarations can be found in platform/include/tfm_platform_system.h and platform/include/tfm_hal.h."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/integration_guide/platform/porting_tfm_to_a_new_hardware.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/platform/porting_tfm_to_a_new_hardware.html#functions"
license: "BSD-3-Clause"
mode: "V"
---

_Part of: Platform Folder_

There are a few functions that need to be declared and properly
    initialized for TF-M to work. The function declarations can be found in
    `platform/include/tfm_platform_system.h` and `platform/include/tfm_hal_*.h`.


#### tfm_platform_hal_system_reset:


    This function will in most cases end up calling the NVIC System Reset.

    The platform can uninitialize or store some resources before reset.

```c

void tfm_platform_hal_system_reset(void);
```

#### tfm_platform_hal_ioctl:


    A single entry point to platform-specific code across the HAL is provided by the
    IOCTL service.

```c

enum tfm_platform_err_t tfm_platform_hal_ioctl(tfm_platform_ioctl_req_t request, psa_invec  *in_vec, psa_outvec *out_vec);
```

#### tfm_hal_set_up_static_boundaries:


    Sets up the static isolation boundaries which are constant throughout the
    runtime of the system, including the SPE/NSPE and partition boundaries.

```c

enum tfm_hal_status_t tfm_hal_set_up_static_boundaries(uintptr_t *p_spm_boundary);
```

#### tfm_hal_activate_boundary:


    Activates one Secure Partition boundary.

```c

enum tfm_hal_status_t tfm_hal_activate_boundary(const struct partition_load_info_t *p_ldinf, uintptr_t boundary);
```

#### tfm_hal_memory_check:


    Checks if a given range of memory can be accessed with specified access
    types in boundary. The boundary belongs to a partition which contains all
    asset info.

    A default implementation for Armv8-M platforms with TrustZone is provided in
    `platform/ext/common/tfm_hal_isolation_v8m.c`. Multi-core topology
    platforms without TrustZone may use the
    Memory Check APIs
    to implement this HAL.

```c

enum tfm_hal_status_t tfm_hal_memory_check(uintptr_t boundary, uintptr_t base, size_t size, uint32_t access_type);
```

#### tfm_hal_bind_boundary:


    Binds partition boundaries with the platform. The platform maintains the
    platform-specific settings for SPM further usage, such as update partition
    boundaries or check resource accessibility. The platform needs to manage the
    settings with internal mechanism, and return a value to SPM. SPM delivers
    this value back to platform when necessary. And SPM checks this value to
    decide if the platform-specific settings need to be updated. Hence multiple
    partitions can have the same value if they have the same platform-specific
    settings, depending on isolation level.

```c

enum tfm_hal_status_t tfm_hal_bind_boundary(const struct partition_load_info_t *p_ldinf, uintptr_t *p_boundary);
```

#### tfm_hal_boundary_need_switch:


    Lets the platform decide if a boundary switch is needed.

```c

bool tfm_hal_boundary_need_switch(uintptr_t boundary_from, uintptr_t boundary_to);
```

#### tfm_hal_irq_clear_pending:


    This function clears any pending IRQ.

```c

void tfm_hal_irq_clear_pending(uint32_t irq_num);
```

#### tfm_hal_irq_enable:


    This function enable an IRQ.

```c

void tfm_hal_irq_enable(uint32_t irq_num);
```

#### tfm_hal_irq_disable:


    This function disable an IRQ.

```c

void tfm_hal_irq_disable(uint32_t irq_num);
```

#### platform_svc_handlers


    This function is the platform's SVC handler.
    It should return the result for callers and the SPM will then return it to the caller.

```c

int32_t platform_svc_handlers(uint8_t svc_num, uint32_t *svc_args, uint32_t exc_return);
```
