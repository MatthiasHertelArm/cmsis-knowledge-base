---
id: "mbedtls-sample-applications-pkey"
type: "concept"
domain: "security"
title: "Sample Applications: *`pkey`*"
summary: "These sample applications demonstrate the usage of asymmetric cryptography APIs for key exchange and message signing, verification, encryption and decryption."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/development/sample_applications.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/development/sample_applications.md#pkey"
license: "Apache-2.0"
mode: "V"
---

These sample applications demonstrate the usage of asymmetric cryptography APIs for key exchange and message signing, verification, encryption and decryption.

- `dh_client` - A program demonstrating the [Diffie-Hellman-Merkle](https://www.ietf.org/rfc/rfc2631.txt) key exchange on the client side. (only available in versions prior to 4.0)
- `dh_genprime` - A program demonstrating the [Diffie-Hellman-Merkle](https://www.ietf.org/rfc/rfc2631.txt) key exchange prime generation. (only available in versions prior to 4.0)
- `dh_server` - A program demonstrating the [Diffie-Hellman-Merkle](https://www.ietf.org/rfc/rfc2631.txt) key exchange on the server side. (only available in versions prior to 4.0)
- `ecdh_curve25519` - A reference program that shows how to use Curve25519, a special use case of ECDHE. (only available in versions prior to 4.0)
- `ecdsa` - An example [ECDSA](https://tools.ietf.org/html/rfc6979) program. (only available in versions prior to 4.0)
- `gen_key` - An example of how to generate a private key. (only available in versions prior to 4.0)
- `key_app_writer` - An example that demonstrates how to write a key file in different formats (`PEM` and `DER`), from a given key. (only available in versions prior to 4.0)
- `key_app` - A program demonstrating how to read and parse a key. (only available in versions prior to 4.0)
- `mpi_demo` - An application demonstrating how to use the multiple precision integers (`mpi`) APIs. (only available in versions prior to 4.0)
- `pk_decrypt` - A reference application that demonstrates how to use the Public key-based decryption, using the [`pk`](https://github.com/Mbed-TLS/mbedtls/blob/development/include/mbedtls/pk.h) wrapper APIs. (only available in versions prior to 4.0)
- `pk_encrypt` - A reference application that demonstrates how to use the Public key-based encryption, using the [`pk`](https://github.com/Mbed-TLS/mbedtls/blob/development/include/mbedtls/pk.h) wrapper APIs. (only available in versions prior to 4.0)
- `pk_sign` - A reference application that demonstrates how to use the Public key-based signature creation, using the [`pk`](https://github.com/Mbed-TLS/mbedtls/blob/development/include/mbedtls/pk.h) wrapper APIs.
- `pk_verify` - A reference application that demonstrates how to use the Public key-based signature verification, using the [`pk`](https://github.com/Mbed-TLS/mbedtls/blob/development/include/mbedtls/pk.h) wrapper APIs.
- `rsa_decrypt` - An RSA decryption reference program, using the [`rsa`](https://github.com/Mbed-TLS/mbedtls/blob/development/include/mbedtls/rsa.h) APIs. (only available in versions prior to 4.0)
- `rsa_encrypt` - An RSA encryption reference program, using the [`rsa`](https://github.com/Mbed-TLS/mbedtls/blob/development/include/mbedtls/rsa.h) APIs. (only available in versions prior to 4.0)
- `rsa_genkey` - An application demonstrating how to generate an RSA key pair. (only available in versions prior to 4.0)
- `rsa_sign_pss` - An application demonstrating how to create a signature with the [PKCS #1 v2.1](https://www.ietf.org/rfc/rfc3447.txt) padding scheme.
- `rsa_sign` - An application demonstrating how create a signature with the [PKCS #1 v1.5](https://tools.ietf.org/html/rfc2313) padding scheme. (only available in versions prior to 4.0)
- `rsa_verify_pss` - An application demonstrating how to verify a signature with the [PKCS #1 v2.1](https://www.ietf.org/rfc/rfc3447.txt) padding scheme.
- `rsa_verify` - An application demonstrating how to verify a signature with the [PKCS #1 v1.5](https://tools.ietf.org/html/rfc2313) padding scheme. (only available in versions prior to 4.0)
