---
id: "mbedtls-how-to-encrypt-and-decrypt-with-rs-reading-an-rsa-key-pair"
type: "concept"
domain: "security"
title: "How to encrypt and decrypt with RSA: Reading an RSA key pair"
summary: "To perform RSA encryption or decryption, you will need an RSA key. In the case of an RSA-2048 decryption, you will need a 2048-bit RSA key."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/how-to/encrypt-and-decrypt-with-rsa.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/encrypt-and-decrypt-with-rsa.md#reading-an-rsa-key-pair"
license: "Apache-2.0"
mode: "V"
---

To perform RSA encryption or decryption, you will need an RSA key. In the case of an RSA-2048 decryption, you will need a **2048-bit RSA key**.

More information on generating an RSA key pair is in our article on [RSA key pair generation](https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/../cryptography/rsa-key-pair-generator.md). For now, we assume you have **already generated one or already have one in your possession**.

You can recognize a PEM formatted RSA key pair because it starts with a line with dashes around the string `BEGIN RSA PRIVATE KEY` or `BEGIN PRIVATE KEY`. In the case of the latter, it is not necessarily an RSA key, because `BEGIN PRIVATE KEY` is also used for Elliptic Curve and other types of keys. Information on the PEM formatted key structure can be found in [this article](https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/../cryptography/asn1-key-structures-in-der-and-pem.md).

You will need to start by [adding a random number generator (RNG)](https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/add-a-random-generator.md) to your application. In this tutorial, the RNG is the CTR-DRBG generator, and the context is called `ctr_drbg`. The RSA public key is called `our-key.pub`, and the RSA private key is called `our-key.pem`.

Mbed TLS supports two ways for using RSA:

* Directly calling the [RSA module](https://github.com/rsa-source-code).
* Using the public key layer.

The example will show the second, more advised method.
