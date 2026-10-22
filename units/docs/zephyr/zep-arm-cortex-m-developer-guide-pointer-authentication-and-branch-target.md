---
id: "zep-arm-cortex-m-developer-guide-pointer-authentication-and-branch-target"
type: "concept"
domain: "rtos"
title: "Arm Cortex-M Developer Guide: OS features / Pointer Authentication and Branch Target Identification (PACBTI)"
summary: "The Armv8.1-M Pointer Authentication and Branch Target Identification (PACBTI) extension is an optional extension for the Armv8.1-M architecture profile and consists of the implementation of the following control-flow integrity approaches:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/hardware/arch/arm_cortex_m.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/hardware/arch/arm_cortex_m.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: OS features_

The Armv8.1-M Pointer Authentication and Branch Target Identification (PACBTI) extension is an
optional extension for the Armv8.1-M architecture profile and consists of the implementation of the
following control-flow integrity approaches:

* Return address signing and authentication (PAC-RET) as a mitigation for Return Oriented Programming (ROP) style attack.
* BTI instruction placement (BTI) as a mitigation for Jump Oriented Programming (JOP) style attacks.

When hardware support is present (e.g., Cortex-M85) and compiler support is available, PACBTI can be
enabled at build time in Zephyr by selecting one of the below configs:

- `CONFIG_ARM_PACBTI_STANDARD`
- `CONFIG_ARM_PACBTI_PACRET`
- `CONFIG_ARM_PACBTI_PACRET_LEAF`
- `CONFIG_ARM_PACBTI_BTI`
- `CONFIG_ARM_PACBTI_PACRET_BTI`
- `CONFIG_ARM_PACBTI_PACRET_LEAF_BTI`
- `CONFIG_ARM_PACBTI_NONE`

The config options ensures that compiler flags enabling PACBTI instructions are added to the build,
specifically:

- `-mbranch-protection=` for GCC toolchains.

Further, `CONFIG_ARM_PAC` and `CONFIG_ARM_BTI` are
automatically selected based on the branch protection option chosen for
`CONFIG_ARM_PACBTI`. These configuration options enforce PACBTI by enabling
corresponding PACBTI bits in CONTROL register and in the FVP.

To further enhance pointer authentication, Zephyr supports using cryptographically secure,
per-thread PAC keys by enabling `CONFIG_ARM_PAC_PER_THREAD`.
For more details on key generation sources and configuration, refer to the Kconfig help for
`CONFIG_ARM_PAC_PER_THREAD`.

**Limitations:**

- Only builds targeting Armv8.1-M Mainline processors with PACBTI hardware support (e.g.,
  Cortex-M85) are able to fully use this feature.
- Zephyr’s integrated SDK currently includes GCC 12.2 which does not support PACBTI so external GCC
  toolchains (14.3 or later recommended) must be used for PACBTI support.
  Refer to [this document](https://docs.zephyrproject.org/latest/develop/toolchains/index.html) on how to set up
  toolchains.

For more information about PACBTI, refer to the official [Arm documentation](https://developer.arm.com/documentation/109576/latest/)
and also [Arm community blog](https://community.arm.com/arm-community-blogs/b/architectures-and-processors-blog/posts/armv8-1-m-pointer-authentication-and-branch-target-identification-extension)
