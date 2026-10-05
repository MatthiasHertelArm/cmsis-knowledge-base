---
id: "mbedtls-arm-mbed-tls-in-microsoft-visual-s-download-mbed-tls"
type: "concept"
domain: "security"
title: "Arm Mbed TLS in Microsoft Visual Studio 2015: Download Mbed TLS"
summary: "First, you need to get the Mbed TLS source code. Download mbedtls-<version\\>-gpl.tgz from the Mbed TLS dowload location. To unpack this file, you can use a tool like 7-zip."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/compiling-and-building/using-mbedtls-in-microsoft-visual-studio-2015.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/compiling-and-building/using-mbedtls-in-microsoft-visual-studio-2015.md#download-mbed-tls"
license: "Apache-2.0"
mode: "V"
---

First, you need to get the Mbed TLS source code. Download `mbedtls-<version\>-gpl.tgz` from [the Mbed TLS dowload location](https://github.com/download). To unpack this file, you can use a tool like [7-zip](http://www.7-zip.org/).

The default installation of Visual Studio creates this folder: My Documents\Visual Studio 2015\Projects. Extract the contents of the .tgz file to this location. Make sure to extract the second occurrence of the `mbedtls-<version>` folder. Otherwise, the paths given later in this tutorial won't match.

**Note:** You can extract the contents to any location you want, but for the purpose of this tutorial, the download location is the Visual Studio projects folder.
