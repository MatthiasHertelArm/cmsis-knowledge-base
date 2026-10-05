---
id: "rtx-cmsis-rtx-mainpage-security-considerations"
type: "concept"
domain: "rtos"
title: "cmsis-rtx mainpage: Security Considerations"
summary: "RTX5 has not been designed with strong security considerations in mind. The implementation has a focus on high code quality assured by applying coding rules according to MISRA-C:2012 and checking compliance using CodeQL."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/mainpage.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/mainpage.md#security-considerations"
license: "Apache-2.0"
mode: "V"
---

RTX5 has not been designed with strong security considerations in mind. The implementation has a focus on high code
quality assured by applying coding rules according to [MISRA-C:2012](https://misra.org.uk/) and checking compliance
using [CodeQL](https://codeql.github.com/). The analysis results are published on
[GitHub Code scanning page](https://github.com/ARM-software/CMSIS-RTX/security/code-scanning).

Users of RTX5 are strongly advised to run security analysis for their applications if any kind of exposure is given.
The main security assumption made for RTX5 is no untrusted code is ever executed on a device. This assumption is
expected to apply to the vast majority of use cases of an embedded RTOS like RTX5.

For use cases (such as firmware update) where the firmware image (or parts of it) can be modified/updated by an
untrusted user, the application developer must implement appropriate security measures to prevent execution of
untrusted code.

For use cases where executing untrusted code is required (like customizable plugins), the application developer must
carfully analyze the execution sandbox boundaries. Given that untrusted code is executed within an unprivileged
RTX5 thread, it must be assured that no RTOS operation can be used to run untrusted code as part of a service call
nor interrupt routine, see safetyConfig_safety.
