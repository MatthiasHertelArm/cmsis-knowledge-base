---
id: "mbedtls-arm-mbed-tls-in-microsoft-visual-s-tls-explanation"
type: "concept"
domain: "security"
title: "Arm Mbed TLS in Microsoft Visual Studio 2015: Use the solution file supplied with the Mbed TLS source code / TLS explanation"
summary: "Part of: Use the solution file supplied with the Mbed TLS source code"
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/compiling-and-building/using-mbedtls-in-microsoft-visual-studio-2015.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/compiling-and-building/using-mbedtls-in-microsoft-visual-studio-2015.md#tls-explanation"
license: "Apache-2.0"
mode: "V"
---

_Part of: Use the solution file supplied with the Mbed TLS source code_

The TLS part of Mbed TLS provides the means to set up and communicate over a secure communication channel using TLS. Its basic provisions are:

- Initialize a TLS context.
- Perform a TLS handshake.
- Send and receive data.
- Notify a peer that a connection is being closed.

Many aspects of such a channel are set through parameters and callback functions:

- The endpoint role: client or server.
- The authentication mode: whether certificate verification should take place.
- The host-to-host communication channel: send and receive functions.
- The random number generator (RNG) function.
- The ciphers to use for encryption and decryption.
- A certificate verification function.
- Session control: session get and set functions.
- X.509 parameters for certificate-handling and key exchange.

You can use Mbed TLS to create a TLS server and client by providing a framework to set up and communicate through a TLS communication channel. The TLS part relies directly on the certificate parsing, symmetric and asymmetric encryption and hashing modules of the library.
