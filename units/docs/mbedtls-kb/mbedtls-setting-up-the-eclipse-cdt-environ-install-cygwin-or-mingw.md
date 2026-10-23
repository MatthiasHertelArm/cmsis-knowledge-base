---
id: "mbedtls-setting-up-the-eclipse-cdt-environ-install-cygwin-or-mingw"
type: "concept"
domain: "security"
title: "Setting up the Eclipse CDT environment on Windows: Install Cygwin or MinGW"
summary: "We recommend Cygwin, so this tutorial doesn't cover the MinGW installation. For more on MinGW, look at Compiling Mbed TLS in MinGW."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/compiling-and-building/setup-eclipse-cdt-environment-on-windows.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/compiling-and-building/setup-eclipse-cdt-environment-on-windows.md#install-cygwin-or-mingw"
license: "Apache-2.0"
mode: "V"
---

We recommend Cygwin, so this tutorial doesn't cover the MinGW installation. For more on MinGW, look at [Compiling Mbed TLS in MinGW](https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/compiling-and-building/compiling-mbedtls-in-mingw.md).

  * Download and install Cygwin by following the first three steps in the [tutorial](http://www3.ntu.edu.sg/home/ehchua/programming/howto/cygwin_howto.html). Make sure that you select `gcc`, `g++`, `gdb`, and `make` packages under the `Devel` (Development) category, since these packages are not part of the default installation.

  * Add  `C:\cygwin\bin` to your **PATH Environment Variables**.

  * If you want to check if all needed packages are installed, run the Cygwin Terminal and type `cygcheck -c`.
