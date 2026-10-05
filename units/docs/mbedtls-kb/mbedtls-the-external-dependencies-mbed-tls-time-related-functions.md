---
id: "mbedtls-the-external-dependencies-mbed-tls-time-related-functions"
type: "concept"
domain: "security"
title: "The external dependencies Mbed TLS relies on: Time related functions"
summary: "The Timing module (timing.c) uses gettimeofday() to determine the elapsed time with a millisecond resolution. This is optionally used in the TLS layer for DTLS retransmission timers through callbacks."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/development/what-external-dependencies-does-mbedtls-rely-on.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/development/what-external-dependencies-does-mbedtls-rely-on.md#time-related-functions"
license: "Apache-2.0"
mode: "V"
---

The *Timing* module (`timing.c`) uses `gettimeofday()` to determine the elapsed time with a millisecond resolution. This is optionally used in the TLS layer for DTLS retransmission timers through callbacks. You can avoid this dependency by providing your own implementation of these callbacks to the TLS layer, with the definition of `MBEDTLS_TIMING_ALT`.

The *Timing* module may also use `gettimeofday()` if it doesn't know how to access the CPU cycle counter on your platform, or if `MBEDTLS_HAVE_ASM` is disabled. This is used in the example programs (currently only `benchmark.c`) as a support function, as a weak entropy source, and as a weak `RNG` algorithm (`havege`). You can remove this dependency by using stronger `RNG` algorithms and stronger entropy sources.

**Functions covered:** `gettimeofday()`

The `time()` function is abstracted as `mbedtls_time()`, in case `MBEDTLS_HAVE_TIME` is defined, and no alternative implementation was given with the definition of `MBEDTLS_PLATFORM_TIME_ALT` or no `MBEDTLS_PLATFORM_TIME_MACRO` was set. The `mbedtls_timetime()` function will be used by the *TLS core* modules, as well as the provided implementation of the following callbacks: SSL session cache, SSL session tickets, DTLS hello cookies. All these modules only rely on time differences. In other words, they do not need `time()` to return the correct time, much less the correct date. You can remove this dependency by disabling `MBEDTLS_HAVE_TIME` in the `mbedtls_config.h` file, but you may loose some features, such as time-based rotation of session ticket keys. Alternatively, you can supply a different implementation for `mbedtls_time()`, by defining `MBEDTLS_PLATFORM_TIME_ALT()` and call `mbedtls_platform_set_time()` to set your own time function.

If your platform supports a time function, with a different name, but same functionality, you can set it as `MBEDTLS_PLATFORM_TIME_MACRO` (with a possibility of defining `MBEDTLS_PLATFORM_TIME_TYPE_MACRO` as well).

**Functions covered:** `time()` (relative)

If `MBEDTLS_HAVE_TIME_DATE` is defined, `mbedtls_time()` and `mbedtls_platform_gmtime_r()` are used by `x509.c` to check if a certificate has expired. `mbedtls_platform_gmtime_r` is an abstraction layer for the thread safe version of `gmtime()`, which is automatically configured by the library according to the underlying system, or falling back to `gmtime()` if not supported by the system, protected by a mutex `mbedtls_threading_gmtime_mutex`. Note that this mutex should be shared across the entire system, in order for the `gmtime()` to be truly thread safe. Alternatively, you can implement your own thread safe version of `mbedtls_platform_gmtime_r()` with the definition of `MBEDTLS_PLATFORM_GMTIME_R_ALT`.
You can remove this dependency by disabling `MBEDTLS_HAVE_TIME_DATE`, but then the date-based certificate expiration will not be used (revocation through CRLs, for example, will still work).

**Functions covered:** 

- `time()` (absolute)
- `gmtime()`, `gmtime_r()` or `gmtime_s()` (depending on the system)
