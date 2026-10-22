---
id: "tfm-memory-access-check-of-trusted-fir-data-types"
type: "concept"
domain: "security"
title: "Memory Access Check of Trusted Firmware-M in Multi-Core Topology: Data Types and APIs / Data Types"
summary: "The following flags are defined to indicate the access permission attributes. Each flag is mapped to the corresponding CMSE macro. Please refer to ARMv8-M Security Extensions: Requirements on Development Tools <http://infocenter.arm.com/help/topic/com.arm.doc.ecm0359818/ECM0359818_armv8m_security_extensions_reqs_on_dev_tools_1_0.pdf> for details of each CMSE macro."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/multi-cpu/tfm_multi_core_access_check.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/multi-cpu/tfm_multi_core_access_check.html#data-types"
license: "BSD-3-Clause"
mode: "V"
---

_Part of: Data Types and APIs_

#### Access Permission Flags


The following flags are defined to indicate the access permission attributes.
Each flag is mapped to the corresponding CMSE macro. Please refer to
`ARMv8-M Security Extensions: Requirements on Development Tools
<http://infocenter.arm.com/help/topic/com.arm.doc.ecm0359818/ECM0359818_armv8m_security_extensions_reqs_on_dev_tools_1_0.pdf>`_
for details of each CMSE macro.


##### `MEM_CHECK_MPU_READWRITE`


Mapped to CMSE macro `CMSE_MPU_READWRITE` to indicate that the access requires
both read and write permission to the target memory region.

```c

#define MEM_CHECK_MPU_READWRITE   (1 << 0x0)
```

##### `MEM_CHECK_MPU_UNPRIV`


Mapped to CMSE macro `CMSE_MPU_UNPRIV` to indicate that it is an unprivileged
access.

```c

#define MEM_CHECK_MPU_UNPRIV      (1 << 0x2)
```

##### `MEM_CHECK_MPU_READ`


Mapped to CMSE macro `CMSE_MPU_READ`. It indicates that it is a read-only
access to target memory region.

```c

#define MEM_CHECK_MPU_READ        (1 << 0x3)
```

##### `MEM_CHECK_NONSECURE`


Mapped to CSME macro `CMSE_NONSECURE` to indicate that it is a access from
non-secure client call request.
If this flag is unset, it indicates the access is required from SPE.

```c

#define MEM_CHECK_AU_NONSECURE    (1 << 0x1)
#define MEM_CHECK_MPU_NONSECURE   (1 << 0x4)
#define MEM_CHECK_NONSECURE       (MEM_CHECK_AU_NONSECURE | \
                                   MEM_CHECK_MPU_NONSECURE)
```

#### Security Attributes Information


The structure `security_attr_info_t` contains the security attributes
information of the target memory region.
`tfm_hal_get_mem_security_attr()` implementation should fill the structure
fields according to the platform specific secure isolation setting.

```c

struct security_attr_info_t {
    bool is_valid;
    bool is_secure;
};
```
| `is_valid` indicates whether the target memory region is valid according to
  platform resource assignment and security isolation configurations.
| `is_secure` indicates the target memory region is secure or non-secure. The
  value is only valid when `is_valid` is `true`.


#### Memory Attributes Information


The structure `mem_attr_info_t` contains the memory access attributes
information of the target memory region.
`tfm_hal_get_secure_access_attr()` and `tfm_hal_get_ns_access_attr()` implementations should
fill the structure fields according to the memory protection settings.

```c

struct mem_attr_info_t {
    bool is_mpu_enabled;
    bool is_valid;
    bool is_xn;
    bool is_priv_rd_allow;
    bool is_priv_wr_allow;
    bool is_unpriv_rd_allow;
    bool is_unpriv_wr_allow;
};
```
| `is_mpu_enabled` indicates whether the MPU and other management unit are
  enabled and work normally.
| `is_valid` indicates whether the target memory region is valid according to
  platform resource assignment and memory protection configurations.
| `is_xn` indicates whether the target memory region is Execute Never. This
  field is only valid when `is_valid` is `true`.
| `is_priv_rd_allow` and `is_priv_wr_allow` indicates whether the target
  memory region allows privileged read/write. Both the fields are valid only
  when  `is_valid` is `true`.
| `is_unpriv_rd_allow` and `is_unpriv_wr_allow` indicates whether the target
  memory region allows unprivileged read/write. Both the fields are valid only
  when  `is_valid` is `true`.
