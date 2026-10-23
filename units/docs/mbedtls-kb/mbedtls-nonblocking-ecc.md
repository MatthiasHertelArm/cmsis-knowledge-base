---
id: "mbedtls-nonblocking-ecc"
type: "concept"
domain: "security"
title: "Nonblocking ECC"
summary: "ECC operations are expensive. They're the most expensive operations in a typical TLS handshake, which includes many of them. On small boards, for example, based on a Cortex M0 core, a TLS handshake can spend several seconds on ECC operations."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/development/restartable-ecc.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/development/restartable-ecc.md"
license: "Apache-2.0"
mode: "V"
---

ECC operations are expensive. They're the most expensive operations in a typical TLS handshake, which includes many of them. On small boards, for example, based on a Cortex M0 core, a TLS handshake can spend several seconds on ECC operations. In a threaded environment, such as Mbed OS, this is not a problem because other threads can execute concurrently. In nonthreaded environments, blocking for several seconds on an operation is not acceptable if the system needs to attend to other tasks in a timely fashion. In order to support that case, Mbed TLS provides a restartable version of `ECC` operations, and all operations that depend on them (such as TLS handshakes), through the configuration option `MBEDTLS_ECP_RESTARTABLE` in the configuration header (`mbedtls/mbedtls_config.h`). Restartable functions enable collaborative multitasking by returning after a configurable amount of computations, so that you can attend to other tasks. They then continue the operation, and so on, until it completes. The `ECP`, `ECDSA`, `ECDH`, `PK`, `X.509` and `SSL` modules support this feature. Curve25519 does not support this feature at this time.

Continue reading to learn about the workflow of the restartable ECC feature, starting with the broad concept followed by specific examples.
