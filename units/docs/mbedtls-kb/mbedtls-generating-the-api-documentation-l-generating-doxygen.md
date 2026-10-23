---
id: "mbedtls-generating-the-api-documentation-l-generating-doxygen"
type: "concept"
domain: "security"
title: "Generating the API documentation locally: Generating doxygen"
summary: "Mbed TLS has full doxygen documentation in the source code which is also available on the site in the API documentation page."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/development/generating-mbedtls-api-documentation-locally.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/development/generating-mbedtls-api-documentation-locally.md#generating-doxygen"
license: "Apache-2.0"
mode: "V"
---

Mbed TLS has full doxygen documentation in the source code which is also available on the site in the [API documentation page](https://github.com/api).

To generate the documentation locally, [download](https://github.com/download) and extract the latest Mbed TLS tarball and run:

    make apidoc
    
This generates the doxygen documentation in the `apidoc` subdirectory.
