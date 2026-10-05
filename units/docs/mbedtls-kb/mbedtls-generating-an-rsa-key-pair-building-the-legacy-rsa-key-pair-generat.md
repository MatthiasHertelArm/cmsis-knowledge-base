---
id: "mbedtls-generating-an-rsa-key-pair-building-the-legacy-rsa-key-pair-generat"
type: "concept"
domain: "security"
title: "Generating an RSA key pair: Building the legacy RSA key pair generator"
summary: "Before 4.0, Mbed TLS shipped the source code for an RSA key pair generator application, called gen_key. To build the executable for the application, please check out the building Mbed TLS."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/cryptography/rsa-key-pair-generator.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/cryptography/rsa-key-pair-generator.md#building-the-legacy-rsa-key-pair-generator"
license: "Apache-2.0"
mode: "V"
---

Before 4.0, Mbed TLS shipped the source code for an RSA key pair generator application, called **gen_key**. To build the executable for the application, please check out the [building Mbed TLS](https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/cryptography/../compiling-and-building/how-do-i-build-compile-mbedtls.md).

After the compilation, the legacy executable is often located in the `programs/pkey` directory.

The **gen_key** application has the following arguments and options:
    
    usage: gen_key param=<>...
    
    acceptable parameters:
       type=rsa|ec        default: rsa
       rsa_keysize=%d     default: 4096
       ec_curve=%s        see below
       filename=%s        default: keyfile.key
       format=pem|der     default: pem
       use_dev_random=0|1 default: 0
    
    available ec_curve values:
       secp521r1 (default)
       brainpoolP512r1
       secp384r1
       brainpoolP384r1
       secp256r1
       secp256k1
       brainpoolP256r1
       secp224r1
       secp224k1
       secp192r1
       secp192k1
