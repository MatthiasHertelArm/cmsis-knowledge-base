---
id: "tfm-hardware-abstraction-layer-isolation-api"
type: "concept"
domain: "security"
title: "Hardware Abstraction Layer: API Definition for TF-M SPM / Isolation API"
summary: "The PSA-FF-M defines three isolation levels and a memory access rule to provide diverse levels of security. The isolation API provides the functions to implement these requirements."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/software/hardware_abstraction_layer.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/software/hardware_abstraction_layer.html#isolation-api"
license: "BSD-3-Clause"
mode: "V"
---

_Part of: API Definition for TF-M SPM_

The `PSA-FF-M` defines three isolation levels and a memory access rule to
provide diverse levels of security. The isolation API provides the functions to
implement these requirements.

The Isolation API operates on boundaries. A boundary represents a set of
protection settings that isolates components and domains. Below are the
boundary examples in the current implementation:

  - Boundaries between SPM and Secure Partitions.
  - Boundaries between ARoT domain and PRoT domain.

There are two types of boundaries:

  - Static boundaries: Set up when the system is initializing and
    persistent after the initialization. This type of boundary needs the
    set-up operations only.
  - Partition boundaries: Keeps switching from one to another when the system
    is running. This type of boundary needs both set-up and switching
    operations.

The boundary operations are abstracted as HAL interfaces because isolation
hardwares can be different for platforms:

  - The set-up HAL interface creates a partition boundary based on given
    partition information. This created boundary is bound with the partition
    for subsequent usage. The binding is done by storing the boundary into
    partition runtime data.
  - The activation HAL interface activates the partition boundary to secure
    the execution for the partition to be switched. The target partition's
    information and boundary are given to the activation HAL to accomplish
    the operation.

The data representing the partition boundary in runtime is defined with the
opaque type `uintptr_t`:

  - It is required that one value represents one boundary. The different values
    represent different boundaries.
  - The value is created by HAL implementation with its own-defined encoding
    scheme.

The HAL implementation defined encoding scheme can be designed for
implementation convenience. For example:

  - The implementation scheme can encode attribute flags into integer bits.
    This could help the activation HAL to extract the protection settings
    quickly from this encoded value, or even write to hardware registers
    directly in the most ideal case. The initial TF-M Isolation HAL reference
    implementation applies this scheme.
  - The implementation scheme can reference the addresses of isolation
    hardware description data. This could help the activation HAL to reference
    the protection settings directly by pointers.

Multiple Secure Partitions can bind with the same boundary value. This
flexibility is useful for specific configurations. Take Isolation Level 2 as
an example, assigning PRoT and ARoT domain boundaries to respective partitions
can make execution more efficient, because switching two partitions in the
same domain does not need to change the activated boundary.

The boundary contains the partition's memory accessibility information, hence
memory access check shall be performed based on boundary.


##### Memory Access Attributes

The memory access attributes are encoded as bit fields, you can logic OR them to
have a combination of the attributes, for example
`TFM_HAL_ACCESS_UNPRIVILEGED | TFM_HAL_ACCESS_READABLE` is unprivileged
readable. The data type is `uint32_t`.


###### TFM_HAL_ACCESS_EXECUTABLE

The memory is executable.

```c

#define TFM_HAL_ACCESS_EXECUTABLE (1UL << 0)
```

###### TFM_HAL_ACCESS_READABLE

The memory is readable.

```c

#define TFM_HAL_ACCESS_READABLE (1UL << 1)
```

###### TFM_HAL_ACCESS_WRITABLE

The memory is writable.

```c

#define TFM_HAL_ACCESS_WRITABLE (1UL << 2)
```

###### TFM_HAL_ACCESS_UNPRIVILEGED

The memory is unprivileged mode accessible.

```c

#define TFM_HAL_ACCESS_UNPRIVILEGED (1UL << 3)
```

###### TFM_HAL_ACCESS_DEVICE

The memory is a MMIO device.

```c

#define TFM_HAL_ACCESS_DEVICE (1UL << 4)
```

###### TFM_HAL_ACCESS_NS

The memory is accessible from `NSPE`

```c

#define TFM_HAL_ACCESS_NS (1UL << 5)
```

##### APIs



###### tfm_hal_verify_static_boundaries()

**Prototype**

```c

fih_int tfm_hal_verify_static_boundaries(void)
```
**Description**

This API verifies the static isolation boundaries.

Refer to the `PSA-FF-M` for the definitions of the isolation boundaries.

**Parameter**

- `void` - None

**Return Values**

- `TFM_HAL_SUCCESS` - Verification has been successful.
- `TFM_HAL_ERROR_GENERIC` - Verification failed.


###### tfm_hal_set_up_static_boundaries()

**Prototype**

```c

enum tfm_hal_status_t tfm_hal_set_up_static_boundaries(void)
```
**Description**

This API sets up the static isolation boundaries which are constant throughout
the system runtime.

These boundaries include:

- The boundary between the `SPE` and the `NSPE`
- The boundary to protect the SPM execution. For example, the PSA RoT
  isolation boundary between the PSA Root of Trust and the Application Root of
  Trust which is for isolation level 2 and 3 only.

Refer to the `PSA-FF-M` for the definitions of the isolation boundaries.

**Parameter**

- `void` - None

**Return Values**

- `TFM_HAL_SUCCESS` - Isolation boundaries have been set up.
- `TFM_HAL_ERROR_GENERIC` - Failed to set up the static boundaries.


###### tfm_hal_bind_boundary()

**Prototype**

```c

enum tfm_hal_status_t tfm_hal_bind_boundary(
                                const struct partition_load_info_t *p_ldinf,
                                uintptr_t *p_boundary);
```
**Description**

This API binds partition with a platform-generated boundary. The boundary is
bound by writing the generated value into `p_boundary`. And this bound
boundary is used in subsequent calls to tfm_hal_activate_boundary() when
boundary's owner partition get scheduled for running.

**Parameter**

- `p_ldinf` - Load information of the partition that is under loading.
- `p_boundary` - Pointer for holding a partition's boundary.

**Return Values**

- `TFM_HAL_SUCCESS` - The boundary has been bound successfully.
- `TFM_HAL_ERROR_GENERIC` - Failed to bind the handle.


###### tfm_hal_activate_boundary()

**Prototype**

```c

enum tfm_hal_status_t tfm_hal_activate_boundary(
                            const struct partition_load_info_t *p_ldinf,
                            uintptr_t boundary);
```
**Description**

This API requires the platform to activate the boundary to ensure the given
Secure Partition can run successfully.

The access permissions outside the boundary is platform-dependent.

**Parameter**

- `p_ldinf` - The load information of the partition that is going to be run.
- `boundary` - The boundary for the owner partition of `p_ldinf`. This
  value is bound in function `tfm_hal_bind_boundary`.

**Return Values**

- `TFM_HAL_SUCCESS` - the isolation boundary has been set up.
- `TFM_HAL_ERROR_GENERIC` - failed to set up the isolation boundary.


###### tfm_hal_memory_check()

**Prototype**

```c

tfm_hal_status_t tfm_hal_memory_check(uintptr_t boundary,
                                      uintptr_t base,
                                      size_t size,
                                      uint32_t access_type)
```
**Description**

This API checks if a given range of memory can be accessed with specified
access types in boundary. The boundary belongs to a partition which
contains asset info.

**Parameter**

- `boundary` - Boundary of a Secure Partition.
  Check `tfm_hal_bind_boundary` for details.
- `base` - The base address of the region.
- `size` - The size of the region.
- `access_type` - The memory access types to be checked between given memory
  and boundaries. The Memory Access Attributes.

**Return Values**

- `TFM_HAL_SUCCESS` - The memory region has the access permissions.
- `TFM_HAL_ERROR_MEM_FAULT` - The memory region does not have the access
  permissions.
- `TFM_HAL_ERROR_INVALID_INPUT` - Invalid inputs.
- `TFM_HAL_ERROR_GENERIC` - An error occurred.

**Note**

If the implementation chooses to encode a pointer as the boundary,
a platform-specific pointer validation needs to be considered before
referencing the content in this pointer.


###### tfm_hal_boundary_need_switch()

**Prototype**

```c

bool tfm_hal_boundary_need_switch(uintptr_t boundary_from,
                                  uintptr_t boundary_to)
```
**Description**

This API let the platform decide if a boundary switch is needed.

**Parameter**

- `boundary_from` - Boundary to switch from.
- `boundary_to` - Boundary to switch to.

**Return Values**

- `true` - A switching is needed
- `false` - No need for a boundary switch


###### tfm_hal_post_partition_init_hook()

**Prototype**

```c

enum tfm_hal_status_t tfm_hal_post_partition_init_hook(void)
```
**Description**

This API let the platform to finish static isolation after all partitions have been bound.
It's called by SPM right before starting scheduler. Use CONFIG_TFM_POST_PARTITION_INIT_HOOK
to enable it.

**Parameter**

- `void` - None

**Return Values**

- `TFM_HAL_SUCCESS` - Booting has been successful.
- `TFM_HAL_ERROR_GENERIC` - Error occurred.


###### tfm_hal_shared_metadata_rw_enable()

**Prototype**

```c

void tfm_hal_shared_metadata_rw_enable(void);
```
**Description**

This API enables Read-Write access to the shared metadata section.
Available when CONFIG_TFM_PARTITION_META_DYNAMIC_ISOLATION is set to 1.

**Return Values**

- `void` - None

**Note**

This API is only available if CONFIG_TFM_PARTITION_META_DYNAMIC_ISOLATION is enabled.


###### tfm_hal_shared_metadata_rw_disable()

**Prototype**

```c

void tfm_hal_shared_metadata_rw_disable(void);
```
**Description**

This API disables Read-Write access to the shared metadata section, restoring
Read-Only access.
Available when CONFIG_TFM_PARTITION_META_DYNAMIC_ISOLATION is set to 1.

**Return Values**

- `void` - None

**Note**

This API is only available if CONFIG_TFM_PARTITION_META_DYNAMIC_ISOLATION is enabled.
