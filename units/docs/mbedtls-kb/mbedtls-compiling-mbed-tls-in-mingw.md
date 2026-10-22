---
id: "mbedtls-compiling-mbed-tls-in-mingw"
type: "concept"
domain: "security"
title: "Compiling Mbed TLS in MinGW"
summary: "This page explains how to compile the Mbed TLS cryptography library in the MinGW environment and the Windows command prompt."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/compiling-and-building/compiling-mbedtls-in-mingw.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/compiling-and-building/compiling-mbedtls-in-mingw.md"
license: "Apache-2.0"
mode: "V"
---

This page explains how to compile the Mbed TLS cryptography library in the MinGW environment and the Windows command prompt.

MinGW, Minimalist GNU for Windows, allows you to compile most Posix (Linux, Unix, and so on) programs to run on Microsoft Windows.

You can compile Mbed TLS in the native Windows compiler. However, if you use Mbed TLS as part of a Linux (or other) project that you would like to port to MinGW, you need a MinGW-compiled version of Mbed TLS.
