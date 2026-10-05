---
id: "mbedtls-porting-the-non-volatile-nv-seed-using-platform-specific-functions"
type: "concept"
domain: "security"
title: "Porting the non-volatile (NV) seed: Using platform specific functions"
summary: "This option can be used if your platform has its own file system functionality, but the functions have the same prototypes as mbedtls_nv_seed_write() and mbedtls_nv_seed_read()."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/how-to/how_to_integrate_nv_seed.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/how_to_integrate_nv_seed.md#using-platform-specific-functions"
license: "Apache-2.0"
mode: "V"
---

This option can be used if your platform has its own file system functionality, but the functions have the same prototypes as `mbedtls_nv_seed_write()` and `mbedtls_nv_seed_read()`.

In your configuration file:
1. Define `MBEDTLS_PLATFORM_NV_SEED_ALT` to suggest that there are alternative implementations for the NV seed functions.
1. Define `MBEDTLS_PLATFORM_STD_NV_SEED_READ` as your platform's file system read function.
1. Define `MBEDTLS_PLATFORM_STD_NV_SEED_WRITE` as your platform's file system write function.
