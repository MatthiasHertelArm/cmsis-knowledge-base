---
id: "mbedtls-asn-1-key-structures-in-der-and-pe-useful-tools"
type: "concept"
domain: "security"
title: "ASN.1 key structures in DER and PEM: Useful tools"
summary: "To customize which OIDs are recognized, you can use an OID file — see NOTES in man asn1parse."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/cryptography/asn1-key-structures-in-der-and-pem.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/cryptography/asn1-key-structures-in-der-and-pem.md#useful-tools"
license: "Apache-2.0"
mode: "V"
---

### OpenSSL

```
openssl asn1parse -inform DER
```

Limitation: gives up on invalid ASN.1.

To customize which OIDs are recognized, you can use an OID file — see [NOTES in `man asn1parse`](https://www.openssl.org/docs/man3.0/man1/openssl-asn1parse.html#NOTES).

Also, many subcommands that work with ASN.1 formatted data (`openssl x509`, `openssl pkey`, etc.) have a `-text` option to dump a text representation of most of the data.

### dumpasn1

`dumpasn1` is a [utility by Peter Gutmann](https://www.cs.auckland.ac.nz/~pgut001/#standards). It is available as a Debian/Ubuntu package. It's a standalone single-file C program plus a configuration file with a list of OIDs.

### LAPO ASN.1 JavaScript decoder

Highlights the correspondence between the hex data and pieces of the decoded tree.

* [Online version](https://lapo.it/asn1js/).
* Offline version: Unpack the [zip](http://lapo.it/asn1js/asn1js.zip) in an empty directory and point a browser at the `index.html` file.

### `asn1_indent`

[`asn1_indent`](https://raw.githubusercontent.com/Mbed-TLS/mbedtls-docs/main/tools/bin/asn1_indent) is a home-made script that just splits the nested SEQUENCES from ASN.1 data. Useful when inspecting or tweaking data to form bad-case test cases.
