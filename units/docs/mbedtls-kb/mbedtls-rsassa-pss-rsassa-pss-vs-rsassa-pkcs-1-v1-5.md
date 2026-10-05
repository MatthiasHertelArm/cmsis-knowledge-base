---
id: "mbedtls-rsassa-pss-rsassa-pss-vs-rsassa-pkcs-1-v1-5"
type: "concept"
domain: "security"
title: "RSASSA-PSS: RSASSA-PSS vs RSASSA (PKCS#1 v1.5)"
summary: "RSASSA-PSS is more robust than RSASSA (PKCS#1 v1.5) and you do not need to take as many precautions to use it securely as you do with the older version."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/generic/rsassa-pss.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/generic/rsassa-pss.md#rsassa-pss-vs-rsassa-pkcs-1-v1-5"
license: "Apache-2.0"
mode: "V"
---

RSASSA-PSS is more robust than RSASSA (PKCS#1 v1.5) and you do not need to take as many precautions to use it securely as you do with the older version. However, the original RSASSA is more widely supported by existing protocols and software. For example, the SSL protocol only supports RSASSA (PKCS#1 v1.5) for RSA signatures, and does not support RSASSA-PSS. So, although RSASSA-PSS is more advantageous from a security perspective, in practice, RSASSA is still more widely used.
