---
id: "mbedtls-asn-1-key-structures-in-der-and-pe-asn-1-and-der-encoding"
type: "concept"
domain: "security"
title: "ASN.1 key structures in DER and PEM: ASN.1 and DER encoding"
summary: "The RSA, PKCS#1, SSL and TLS communities use the Distinguished Encoding Rules (DER) encoding of ASN.1 to represent keys and certificates in a portable format."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/cryptography/asn1-key-structures-in-der-and-pem.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/cryptography/asn1-key-structures-in-der-and-pem.md#asn-1-and-der-encoding"
license: "Apache-2.0"
mode: "V"
---

The RSA, PKCS#1, SSL and TLS communities use the [Distinguished Encoding Rules (DER)](http://en.wikipedia.org/wiki/Distinguished_Encoding_Rules) encoding of [ASN.1](http://en.wikipedia.org/wiki/ASN.1) to represent keys and certificates in a portable format. The certificate and key information is stored in the binary DER for ASN.1, and applications providing RSA, SSL and TLS should use DER encoding to parse the data. While ASN.1 is a complex representation format and can be difficult to understand, it also has its merits.

### Some good resources on ASN.1 and DER

* [A Warm Welcome to ASN.1 and DER](https://letsencrypt.org/docs/a-warm-welcome-to-asn1-and-der/)
* [A Layman's Guide to a Subset of ASN.1, BER, and DER](http://luca.ntop.org/Teaching/Appunti/asn1.html)
* [ASN.1 Made Simple](https://www.oss.com/asn1/resources/asn1-made-simple/introduction.html)
