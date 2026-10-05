---
id: "mbedtls-porting-the-non-volatile-nv-seed-using-the-standard-libc-functions"
type: "concept"
domain: "security"
title: "Porting the non-volatile (NV) seed: Using the standard libc functions"
summary: "This option should be used if your platform supports standard libc file functions to read from and write to a predefined file name."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/how-to/how_to_integrate_nv_seed.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/how_to_integrate_nv_seed.md#using-the-standard-libc-functions"
license: "Apache-2.0"
mode: "V"
---

This option should be used if your platform supports standard libc file functions to read from and write to a predefined file name.

1. Define `MBEDTLS_PLATFORM_STD_NV_SEED_FILE` as your seed file name. Default is "seedfile".
1. Verify that `MBEDTLS_PLATFORM_NO_STD_FUNCTIONS` is undefined.
1. Define `MBEDTLS_FS_IO`.
