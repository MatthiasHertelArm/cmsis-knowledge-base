---
id: "mbedtls-arm-mbed-tls-in-microsoft-visual-s-further-notes"
type: "concept"
domain: "security"
title: "Arm Mbed TLS in Microsoft Visual Studio 2015: Further notes"
summary: "This sample is for example use only. It doesn't authenticate the server with a trusted root certificate."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/compiling-and-building/using-mbedtls-in-microsoft-visual-studio-2015.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/compiling-and-building/using-mbedtls-in-microsoft-visual-studio-2015.md#further-notes"
license: "Apache-2.0"
mode: "V"
---

This sample is for example use only. It doesn't authenticate the server with a trusted root certificate. In a larger project, you may want to wrap the code to call Mbed TLS in functions like: `InitializeSSL`, `OpenSSLConnection`, `ExecuteSSLRequest`, `ReadSSLResponse` and `CloseSSL`. You could also use a C++ class with which you can place the initialize and close functions in the constructor and destructor.

To ease the rollout of your application, you can copy the `mbedTLS.lib` files to the Debug and Release folders of your project.

<!-- using-mbedtls-in-microsoft-visual-studio-2015,"Walkthrough for compiling Mbed TLS with Visual Studio 2015","Visual Studio 2010, Visual Studio, MSVS2015","Microsoft, visual studio, msvc, windows, tutorial, snippet, VS2015, explanation,",published,"2012-10-09 00:00:00",6,12129,"2015-07-24 11:36:00","Paul Bakker" -->
