---
id: "tfm-memory-access-check-of-trusted-fir-overall-design"
type: "concept"
domain: "security"
title: "Memory Access Check of Trusted Firmware-M in Multi-Core Topology: Overall Design"
summary: "The policies vary in diverse Isolation Levels."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/multi-cpu/tfm_multi_core_access_check.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/multi-cpu/tfm_multi_core_access_check.html#overall-design"
license: "BSD-3-Clause"
mode: "V"
---

### Memory Access Check Policy


The policies vary in diverse Isolation Levels.

When TF-M works in Isolation Level 1, the access check in multi-core topology
checks

- Memory region is valid according to system settings
- Non-secure client call request should not access secure memory.
- Secure services should not directly access non-secure memory. According to PSA
  Firmware Framework, Secure services should call Secure Partition APIs to ask
  TF-M SPM to fetch non-secure input/output buffer for them.
- Whether read/write attribute match between access and memory region

When TF-M works in Isolation Level 2, the access check in multi-core topology
checks:

- Memory region is valid according to system settings
- Non-secure client call request should not access secure memory.
- Secure services should not directly access non-secure memory. According to PSA
  Firmware Framework, Secure services should call Secure Partition APIs to ask
  TF-M SPM to fetch non-secure input/outputs buffer for them.
- Whether read/write attribute match between access and memory region
- Unprivileged secure access should not access privileged secure memory region

The check policy in Isolation Level 3 will be defined according to TF-M future
implementation.

The above policies will be adjusted according to TF-M implementation and PSA
specs.


### General Check Process in TF-M Core


The TF-M SPM calls the `tfm_hal_memory_check()` HAL API in both TrustZone-based and multi-core
topology platforms to keep a uniform interface between SPM and platform.

Multi-core platform specific `tfm_hal_memory_check()` implementations can invoke
`tfm_has_access_to_region()` to implement the entire memory access check routine.

During the check process, `tfm_has_access_to_region()` compares the access permission with memory
region attributes and determines whether the access is allowed to access the region according to
policy described in Memory Access Check Policy above.

`tfm_has_access_to_region()` invokes 3 HAL APIs to retrieve attributes of target memory region.

- `tfm_hal_get_mem_security_attr()` retrieves the security attributes of the target memory region.
- `tfm_hal_get_secure_access_attr()` retrieves secure access attributes of the target memory
  region.
- `tfm_hal_get_ns_access_attr()` retrieves non-secure access attributes of the target memory
  region.

All three functions are implemented by multi-core platform support. The definitions are specified in
the section HAL APIs below.

The pseudo code of `tfm_has_access_to_region()` is shown below.

```c

int32_t tfm_has_access_to_region(const void *p, size_t s, uint8_t flags)
{
    struct security_attr_info_t security_attr;
    struct mem_attr_info_t mem_attr;

    /* Validate input parameters */
    if (Validation failed) {
        return error;
    }

    /* The memory access check should be executed inside TF-M PSA RoT */
    if (Not in privileged level) {
        abort;
    }

    /* Set initial value */
    security_attr_init(&security_attr);

    /* Retrieve security attributes of memory region */
    tfm_hal_get_mem_security_attr(p, s, &security_attr);

    /* Compare according to current Isolation Level */
    if (Input flags mismatch security attributes) {
        return error;
    }

    /* Set initial value */
    mem_attr_init(&mem_attr);

    if (The target memory region is in secure memory space) {
        /* Retrieve access attributes of secure memory region */
        tfm_hal_get_secure_access_attr(p, s, &mem_attr);

        if (Not in Isolation Level 1) {
            /* Secure memory protection unit(s) must be enabled in Isolation Level 2 and 3 */
            if (Protection unit not enabled) {
                abort;
            }
        }
    } else {
        /* Retrieve access attributes of non-secure memory region. */
        tfm_hal_get_ns_access_attr(p, s, &mem_attr);
    }

    /* Compare according to current Isolation Level and non-secure/secure access. */
    if (Input flags match memory attributes) {
        return success;
    }

    return error;
}
```

**Note:** It cannot be guaranteed that TF-M provides a comprehensive memory access check on non-secure memory for NSPE client call. If non-secure memory protection or isolation is required in a multi-core system, NSPE software should implement and execute the check functionalities in NSPE, rather than relying on TF-M access check. For example, all the access from NSPE client calls to non-secure memory are classified as unprivileged in current TF-M implementation. Multi-core access check may skip the privileged/unprivileged permission check for non-secure access. If a multi-core system enforces the privileged/unprivileged isolation and protection of non-secure area, NSPE software should execute the corresponding check functionalities before submitting the NSPE client call request to SPE.
