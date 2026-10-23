---
id: "mbedtls-mbed-tls-tutorial-ssl-tls"
type: "concept"
domain: "security"
title: "Mbed TLS tutorial: SSL/TLS"
summary: "The SSL/TLS part of Mbed TLS provides the means to set up and communicate over a secure communication channel using SSL/TLS."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/how-to/mbedtls-tutorial.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/mbedtls-tutorial.md#ssl-tls"
license: "Apache-2.0"
mode: "V"
---

The SSL/TLS part of Mbed TLS provides the means to set up and communicate over a secure communication channel using SSL/TLS.

Its basic functionalities are:

* Initialize an SSL/TLS context.
* Perform an SSL/TLS handshake.
* Send/receive data.
* Notify a peer that a connection is being closed.

Many aspects of such a channel are set through parameters and callback functions:

* The endpoint role: client or server.
* The authentication mode: to state whether certificate verification is needed or not.
* The host-to-host communication channel: send and receive functions.
* The random number generator (RNG) function.
* The ciphers to use for encryption/decryption.
* A certificate verification function.
* Session control: session get and set functions.
* X.509 parameters for certificate handling and key exchange.

Mbed TLS can be used to create an SSL/TLS server and client by providing a framework to set up and communicate through an SSL/TLS communication channel. The SSL/TLS part relies directly on the certificate parsing, symmetric and asymmetric encryption and hashing modules of the library.
