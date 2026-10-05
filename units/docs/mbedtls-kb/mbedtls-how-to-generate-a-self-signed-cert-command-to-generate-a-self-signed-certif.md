---
id: "mbedtls-how-to-generate-a-self-signed-cert-command-to-generate-a-self-signed-certif"
type: "concept"
domain: "security"
title: "How to generate a self-signed certificate: Command to generate a self-signed certificate"
summary: "The full command for generating a self-signed CA certificate that cannot sign other CA certificates for our_key.key with the name CN=myserver,O=myorganization,C=NL and valid only in the years 2013, 2014 and 2015 would be:"
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/how-to/generate-a-self-signed-certificate.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/generate-a-self-signed-certificate.md#command-to-generate-a-self-signed-certificate"
license: "Apache-2.0"
mode: "V"
---

**Example:**

The full command for generating a self-signed CA certificate that cannot sign other CA certificates for `our_key.key` with the name `CN=myserver,O=myorganization,C=NL` and valid only in the years 2013, 2014 and 2015 would be:
```
programs/x509/cert_write selfsign=1 issuer_key=our_key.key                    \
                         issuer_name=CN=myserver,O=myorganization,C=NL        \
                         not_before=20130101000000 not_after=20151231235959   \
                         is_ca=1 max_pathlen=0 output_file=my_crt.crt
```
The file `my_crt.crt` now contains your PEM-encoded certificate.

### Key usage and NS cert type extension

You can set the key usage extension and the NS Cert type extension in the certificate on the command-line as well with:
```
    key_usage=%s        default: (empty)
                        Comma-separated-list of values:
                          digital_signature
                          non_repudiation
                          key_encipherment
                          data_encipherment
                          key_agreement
                          key_certificate_sign
                          crl_sign
    ns_cert_type=%s     default: (empty)
                        Comma-separated-list of values:
                          ssl_client
                          ssl_server
                          email
                          object_signing
                          ssl_ca
                          email_ca
                          object_signing_ca
```
<!---generate-a-self-signed-certificate
,"Step-by-step guide on how to generate a self-signed certificate with Mbed TLS instead of OpenSSL.",,"generate, certificate generation, self-signed, cert_write, gen_key, CA certificate",published,"2013-10-31 12:13:00",2,19910,"2015-07-02 11:48:00","Paul Bakker"--->
