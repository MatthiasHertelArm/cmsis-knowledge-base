---
id: "mbedtls-how-to-generate-a-self-signed-cert-generating-a-self-signed-certificate"
type: "concept"
domain: "security"
title: "How to generate a self-signed certificate: Generating a self-signed certificate"
summary: "For generating and writing certificate files, Mbed TLS includes the cert_write application (located in programs/x509)."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/how-to/generate-a-self-signed-certificate.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/generate-a-self-signed-certificate.md#generating-a-self-signed-certificate"
license: "Apache-2.0"
mode: "V"
---

For generating and writing certificate files, Mbed TLS includes the `cert_write` application (located in `programs/x509`).

Before generating the self-signed certificate, determine the different values in it.

In the case of a self-signed certificate, indicate it with `selfsign=1`.

### Key to use in the certificate

First and foremost a certificate binds a public-private key pair to an identity. To indicate which key to use to sign the certificate we use the `issuer_key` argument, like so `issuer_key=our_key.key`.

Because this is a self-signed certificate the `subject_key` is automatically identical.

### Subject name / Issuer name

Each certificate is identified with a subject name (the identity that is being signed) and an issuer name (the party doing the signing). For self-signed certificates, only the issuer name is used.

In case we want to name the issuer `myserver` from the organization `myorganization` and the country `NL`, we should use `issuer_name=CN=myserver,O=myorganization,C=NL` on the command-line.

**Note:** If you want to use a space in one of the names you have to either nullify it (`issuer_name=CN=my\ server`) or contain the entire argument in quotes (`"issuer_name=CN=my server"`).

**Note:** Commas inside names need to be nullified with a backslash as well. You need to protect the backslash from your shell, for example, `issuer_name=CN=my\\\,server` or `issuer_name='CN=my\,server'`.

The supported items in a `subject_name` are:

* C = Country
* CN = Common Name
* L = Locality
* O = Organization
* OU = Organizational Unit
* R = e-mail address
* ST = State
* serialNumber
* postalAddress
* postalCode
