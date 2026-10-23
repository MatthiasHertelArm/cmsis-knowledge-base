---
id: "mbedtls-arm-mbed-tls-in-microsoft-visual-s"
type: "concept"
domain: "security"
title: "Arm Mbed TLS in Microsoft Visual Studio 2015"
summary: "This tutorial shows how to get started with the Mbed TLS cryptography library in a Windows environment, using Microsoft Visual Studio 2015. This tutorial uses the sample client application (from this example)."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/compiling-and-building/using-mbedtls-in-microsoft-visual-studio-2015.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/compiling-and-building/using-mbedtls-in-microsoft-visual-studio-2015.md"
license: "Apache-2.0"
mode: "V"
---

This tutorial shows how to get started with the Mbed TLS cryptography library in a Windows environment, using Microsoft Visual Studio 2015. This tutorial uses the sample client application (from [this example](https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/compiling-and-building/../how-to/mbedtls-tutorial.md)). This application sends an HTTP request to read an HTML page from a server.This tutorial uses Mbed TLS to enable encrypting our communication with the server with TLS. Note that Mbed TLS supports Visual Studio starting from version 2010.

There are two possible ways to build Mbed TLS on Windows:

- Using the solution file supplied with the Mbed TLS source code.
- Using `cmake` to generate a Visual Studio solution file.

This step-by-step tutorial shows you how to set up Visual Studio for Mbed TLS and the sample application. It assumes that you have already installed Visual Studio for C++. If generating a solution file using `cmake`, you should also install CMake. We tested this tutorial with `cmake` version 3.10.1.

The sample application is a command-line program, written in C. You can just as easily integrate Mbed TLS in any C or C++ application, with or without a (graphical) user interface.
