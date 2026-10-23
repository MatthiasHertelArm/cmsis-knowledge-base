---
id: "mcuboot-porting-how-to-memory-management-for-mbed-tls"
type: "concept"
domain: "boot-update"
title: "Porting how-to: Memory management for Mbed TLS"
summary: "Mbed TLS employs dynamic allocation of memory, making use of the pair calloc/free. If Mbed TLS is to be used for crypto, your target RTOS needs to provide this pair of function."
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@725d63c:docs/PORTING.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/725d63c/docs/PORTING.md#memory-management-for-mbed-tls"
license: "Apache-2.0"
mode: "V"
---

`Mbed TLS` employs dynamic allocation of memory, making use of the pair
`calloc/free`. If `Mbed TLS` is to be used for crypto, your target RTOS
needs to provide this pair of function.

To configure the what functions are called when allocating/deallocating
memory `Mbed TLS` uses the following call:

```
int mbedtls_platform_set_calloc_free (void *(*calloc_func)(size_t, size_t),
                                      void (*free_func)(void *));
```

For reference see [Mbed TLS platform.h](https://tls.mbed.org/api/platform_8h.html).
If your system already provides functions with compatible signatures, those can
be used directly here, otherwise create new functions that glue to your
`calloc/free` implementations.
