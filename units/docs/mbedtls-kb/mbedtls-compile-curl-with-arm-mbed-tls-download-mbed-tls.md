---
id: "mbedtls-compile-curl-with-arm-mbed-tls-download-mbed-tls"
type: "concept"
domain: "security"
title: "Compile cURL with Arm Mbed TLS: Download Mbed TLS"
summary: "The Mbed TLS library is not included in the cURL source package, so you need to download and install Mbed TLS first. You can use the latest version by altering the version number in the URL below."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/how-to/compile-curl-with-mbedtls.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/compile-curl-with-mbedtls.md#download-mbed-tls"
license: "Apache-2.0"
mode: "V"
---

The Mbed TLS library is not included in the cURL source package, so you need to download and install Mbed TLS first. You can use the latest version by altering the version number in the URL below. Enter these statements to download and unpack the Mbed TLS source code to your `/home/Downloads` folder:

```
cd ~/Downloads
wget https://tls.mbed.org/code/releases/mbedtls-2.12.0-gpl.tgz
tar -zxf mbedtls-2.12.0-gpl.tgz
cd mbedtls-2.12.0
```
