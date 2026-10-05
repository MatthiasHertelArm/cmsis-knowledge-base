---
id: "mbedtls-porting-mbed-tls-to-a-new-environm-real-time-clock"
type: "concept"
domain: "security"
title: "Porting Mbed TLS to a new environment or OS: Real time clock"
summary: "A few modules optionally access the current time, either to measure time intervals, or to know the absolute current time and date. You can disable those features at compilation time without affecting the rest of the library."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/how-to/how-do-i-port-mbed-tls-to-a-new-environment-OS.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/how-do-i-port-mbed-tls-to-a-new-environment-OS.md#real-time-clock"
license: "Apache-2.0"
mode: "V"
---

A few modules optionally access the current time, either to measure time intervals, or to know the absolute current time and date. You can disable those features at compilation time without affecting the rest of the library.

Every function that measures intervals has an alternate version of the code to provide similar functionality when time is not available (for example, rotating keys based on the number of uses rather than elapsed time). Absolute time and date are only used in X.509 in order to check the validity period of certificates. If time and date are not available, then this check is skipped.

**Warning:** Depending on how you use X.509 certificates to secure your platform, this could be a serious security risk.
