---
id: "mbedtls-porting-the-non-volatile-nv-seed"
type: "concept"
domain: "security"
title: "Porting the non-volatile (NV) seed"
summary: "If a hardware platform cannot take advantage of a hardware entropy source, alternatives have to be considered. A strong entropy source is crucial for the security of cryptographic and TLS operations."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/how-to/how_to_integrate_nv_seed.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/how_to_integrate_nv_seed.md"
license: "Apache-2.0"
mode: "V"
---

If a hardware platform cannot take advantage of a hardware entropy source, alternatives have to be considered. A strong entropy source is crucial for the security of cryptographic and TLS operations. For platforms that support non-volatile (NV) memory, an option is to use the NV seed entropy source that Mbed TLS provides.

This feature can be used *in addition* to a hardware entropy source as well, however, it is not mandatory as the hardware entropy source should be strong enough.

This makes Mbed TLS use a fixed amount of entropy as a seed and update this seed each time entropy is gathered with an Mbed TLS entropy collector for the first time. In a simple case it means that the seed is updated after reset at the start of the first TLS connection.

# Enabling NV seed entropy source support

You should define `MBEDTLS_ENTROPY_NV_SEED` in your configuration, as described in [this article](https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/../compiling-and-building/how-do-i-configure-mbedtls.md). This ensures the entropy pool knows it can use the NV seed entropy source. You should set the following functions to make the entropy collector call them:

    int (*mbedtls_nv_seed_write)( unsigned char *buf, size_t buf_len );
    int (*mbedtls_nv_seed_read)( unsigned char *buf, size_t buf_len );

There are several options for how to set these functions:

1. Using the standard libc functions.
1. Using platform specific functions.
1. Defining platform specific functions.

All these options require `MBEDTLS_ENTROPY_NV_SEED` to be defined.
