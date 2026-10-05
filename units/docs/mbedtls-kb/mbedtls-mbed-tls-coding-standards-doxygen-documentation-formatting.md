---
id: "mbedtls-mbed-tls-coding-standards-doxygen-documentation-formatting"
type: "concept"
domain: "security"
title: "Mbed TLS coding standards: Doxygen documentation formatting"
summary: "The header files should be documented with Doxygen-style code comments. Use the '\\' character as a separator."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/development/mbedtls-coding-standards.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/development/mbedtls-coding-standards.md#doxygen-documentation-formatting"
license: "Apache-2.0"
mode: "V"
---

The header files should be documented with Doxygen-style code comments. Use the **'\'** character as a separator.

|Function|Description|
|---|---|
|\brief|A useless function present for documentation purposes.|
|\note|This function has no influence on code security.|
|\param buf|Buffer to ignore.|
|\param len|Length of buffer.|
|\return|0 if successfully ignored, otherwise, a module-specific error code.|
