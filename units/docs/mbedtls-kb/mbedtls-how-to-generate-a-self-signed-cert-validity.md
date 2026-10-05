---
id: "mbedtls-how-to-generate-a-self-signed-cert-validity"
type: "concept"
domain: "security"
title: "How to generate a self-signed certificate: Validity"
summary: "Each certificate contains within it the validity period for that certificate indicated by the not_before and not_after values."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/how-to/generate-a-self-signed-certificate.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/generate-a-self-signed-certificate.md#validity"
license: "Apache-2.0"
mode: "V"
---

Each certificate contains within it the validity period for that certificate indicated by the **not_before** and **not_after** values.

The applications accepts values of the format **YYYYMMDDHHMMSS**, so to indicate that a certificate is not valid before 2013, you can use `not_before=20130101000000` and not valid after 2015, you can use `not_after=20151231235959`.
