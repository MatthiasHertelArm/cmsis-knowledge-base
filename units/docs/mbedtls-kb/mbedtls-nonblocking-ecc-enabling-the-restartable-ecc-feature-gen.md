---
id: "mbedtls-nonblocking-ecc-enabling-the-restartable-ecc-feature-gen"
type: "concept"
domain: "security"
title: "Nonblocking ECC: Enabling the restartable ECC feature, generic flow"
summary: "Nonblocking ECC: Enabling the restartable ECC feature, generic flow"
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/development/restartable-ecc.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/development/restartable-ecc.md#enabling-the-restartable-ecc-feature-generic-flow"
license: "Apache-2.0"
mode: "V"
---

* At configuration time, define `MBEDTLS_ECP_RESTARTABLE` in `mbedtls/mbedtls_config.h`. See [How do I configure Mbed TLS](https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/development/../compiling-and-building/how-do-i-configure-mbedtls.md) for more information.
* Set the maximal number of operations that you want to run in a row with the `ECP` module, using `mbedtls_ecp_set_max_ops()`.
* Allocate the restart context, and initialize it by calling `mbedtls_xxx_restart_init()`.
* `ECP`, `ECDSA`, `PK` and `X.509` need an explicit restart context, and `ECDH` and `SSL` don't, though `ECDH` requires an additional call to `mbedtls_ecdh_enable_restart()`.
* Call the `mbedtls_xxx_xxxx()` or `mbedtls_xxx_xxxx_restartable()` operation. As long as it returns the error `MBEDTLS_ERR_ECP_IN_PROGRESS` or `MBEDTLS_ERR_SSL_CRYPTO_IN_PROGRESS` for TLS functions, you can call it again, potentially after taking care of other system operations. It is the caller's responsibility to either call again with the same parameters until it returns 0 or an error code, or to free the restart context if the caller wishes to abort the operation.

**Note**: We strictly require all input parameters and the restart context to be the same on successive calls for the same operation. Output parameters do not need to be the same, though you must not use them until the function finally returns 0.

**Note**: Sometimes, functions need to block for a minimum number of operations and will do so even if `max_ops` is set to a lower value. That minimum depends on the curve size. You can lower it by decreasing the value of `MBEDTLS_ECP_WINDOW_SIZE`.
