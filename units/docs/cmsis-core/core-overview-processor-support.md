---
id: "core-overview-processor-support"
type: "concept"
domain: "core"
title: "Overview: Processor Support"
summary: "CMSIS-Core supports the complete range of Cortex-M processors."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Core/src/mainpage.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Core/src/mainpage.md#processor-support"
license: "Apache-2.0"
mode: "V"
---

CMSIS-Core supports the complete range of [Cortex-M processors](https://www.arm.com/products/silicon-ip-cpu?families=cortex-m&showall=true).


**Cortex-M Generic User Guides**

Following Cortex-M Device Generic User Guides contain the programmers model and detailed information about the core peripherals:

 - [Cortex-M0 Devices Generic User Guide (Armv6-M architecture)](https://developer.arm.com/documentation/dui0497/latest/)
 - [Cortex-M0+ Devices Generic User Guide (Armv6-M architecture)](https://developer.arm.com/documentation/dui0662/latest/)
 - [Cortex-M3 Devices Generic User Guide (Armv7-M architecture)](https://developer.arm.com/documentation/dui0552/latest/)
 - [Cortex-M4 Devices Generic User Guide (Armv7-M architecture)](https://developer.arm.com/documentation/dui0553/latest/)
 - [Cortex-M7 Devices Generic User Guide (Armv7-M architecture)](https://developer.arm.com/documentation/dui0646/latest/)
 - [Cortex-M23 Devices Generic User Guide (Armv8-M architecture)](https://developer.arm.com/documentation/dui1095/latest/)
 - [Cortex-M33 Devices Generic User Guide (Armv8-M architecture)](https://developer.arm.com/documentation/100235/latest/)
 - [Cortex-M52 Devices Generic User Guide (Armv8.1-M architecture)](https://developer.arm.com/documentation/102776/latest/)
 - [Cortex-M55 Devices Generic User Guide (Armv8.1-M architecture)](https://developer.arm.com/documentation/101273/latest/)
 - [Cortex-M85 Devices Generic User Guide (Armv8.1-M architecture)](https://developer.arm.com/documentation/101928/latest/)

CMSIS-Core also supports the following Cortex-M processor variants:

 - [Cortex-M1](https://developer.arm.com/Processors/Cortex-M1) is a processor designed specifically for implementation in FPGAs (Armv6-M architecture).
 - [SecurCore SC000](https://developer.arm.com/Processors/SecurCore%20SC000) is designed specifically for smartcard and security applications (Armv6-M architecture).
 - [SecurCore SC300](https://developer.arm.com/Processors/SecurCore%20SC300) is designed specifically for smartcard and security applications (Armv7-M architecture).
 - [Cortex-M35P](https://developer.arm.com/Processors/Cortex-M35P) is a tamper resistant Cortex-M processor with optional software isolation using TrustZone for Armv8-M.
 - [STAR-MC1](https://www.armchina.com/mountain?infoId=160) is a variant of Armv8-M with TrustZone designed by Arm China.
 - [STAR-MC3](https://www.armchina.com/mountain?infoId=240) is a variant of Armv8.1-M with TrustZone and Helium designed by Arm China.


**Armv8-M and Armv8.1-M Architecture**

Armv8-M introduces two profiles **baseline** (for power and area constrained applications) and **mainline** (full-featured with optional SIMD, floating-point, and co-processor extensions). Both Armv8-M profiles and Armv8.1-M are supported by CMSIS.

The Armv8-M architecture is described in the [Armv8-M Architecture Reference Manual](https://developer.arm.com/documentation/ddi0553/latest/).

The Armv8.1-M architecture further extends Armv8-M with Helium (the so called M-Profile Vector Extension (MVE)), as well as further instruction set and debug extensions.

More information about Armv8.1-M architecture is available under [Arm Helium technology](https://developer.arm.com/Architectures/Helium).
