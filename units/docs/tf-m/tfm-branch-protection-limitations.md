---
id: "tfm-branch-protection-limitations"
type: "concept"
domain: "security"
title: "Branch Protection: Limitations"
summary: "Currently PACBTI is supported only for Arm Compiler. Even though GNUARM supports PACBTI, some features are missing that prevent all the component integration to successfully work together. It may be possible in the future to extend support for other compilers."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/integration_guide/branch_protection.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/branch_protection.html#limitations"
license: "BSD-3-Clause"
mode: "V"
---

Currently PACBTI is supported only for Arm Compiler.
Even though GNUARM supports PACBTI, some features are missing that prevent all
the component integration to successfully work together.
It may be possible in the future to extend support for other compilers.

--------------

For further details on PACBTI features refer to:

[Armv8-M Architecture Reference Manual](https://developer.arm.com/documentation/ddi0553/latest)

[Armv8.1-M Pointer Authentication and Branch Target Identification Extension](https://community.arm.com/arm-community-blogs/b/architectures-and-processors-blog/posts/armv8-1-m-pointer-authentication-and-branch-target-identification-extension)

--------------

*Copyright (c) 2024, Arm Limited. All rights reserved.*
