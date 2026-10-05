---
id: "core-using-trustzone-for-armv8-m"
type: "concept"
domain: "core"
title: "Using TrustZone for Armv8-M"
summary: "The TrustZone for Cortex-M is a security extension for Armv8-M architecture that is optimized for ultra-low power embedded applications. It enables software security domains that restrict access to secure memory and I/O only for trusted software."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Core/src/using_tz.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Core/src/using_tz.md"
license: "Apache-2.0"
mode: "V"
---

The [TrustZone for Cortex-M](https://www.arm.com/technologies/trustzone-for-cortex-m) is a security extension for Armv8-M architecture that is optimized for ultra-low power embedded applications. It enables software security domains that restrict access to secure memory and I/O only for trusted software.

TrustZone for Armv8-M:

- preserves low interrupt latencies for both Secure and Non-secure domains.
- does not impose code overhead, cycle overhead or the complexity of a virtualization based solution.
- introduces the Secure Gateway (SG) processor instruction for calls to the secure domain.

**Notations**

This manual uses the following notations to identify functions and hardware resources that are related to TrustZone for Armv8-M:

 - prefix `TZ` or `__TZ` indicates a function that is available only in Armv8-M TrustZone enabled devices.
 - postfix `_NS` indicates a hardware resource that belongs to the Non-secure state.
 - postfix `_S` indicates a hardware resource that belongs to the Secure state.
