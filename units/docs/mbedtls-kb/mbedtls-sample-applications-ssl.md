---
id: "mbedtls-sample-applications-ssl"
type: "concept"
domain: "security"
title: "Sample Applications: *`ssl`*"
summary: "These applications demonstrate common use cases for the SSL\\TLS stack APIs."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/development/sample_applications.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/development/sample_applications.md#ssl"
license: "Apache-2.0"
mode: "V"
---

These applications demonstrate common use cases for the SSL\TLS stack APIs.  

**Note: These applications use the [Mbed TLS test root certificate](https://github.com/Mbed-TLS/mbedtls/blob/development/include/mbedtls/certs.h) and are meant to work with one another. To test the client applications with an external server, the root certificate needs to be set correctly by calling the [`mbedtls_ssl_conf_ca_chain()`](https://github.com/api/ssl_8h.html#a85c3bb6b682ba361d13de1c0a1eb69fb). Alternatively, some applications allow to optionally set the CA root certificate file through the command-line. To test the server applications with external clients, they need to replace `mbedtls_x509_crt_parse()` with [`mbedtls_x509_crt_parse_file()`](https://github.com/api/group__x509__module.html#gad4da63133d3590aa311488497d4c38ec) to read the server and CA certificates, as well as replacing `mbedtls_pk_parse_key()` with [`mbedtls_pk_parse_keyfile()`](https://github.com/api/pk_8h.html#a935d710e542409462d0209f2381da83e).**

- `dtls_client` - A DTLS client demonstration program.
- `dtls_server` - A DTLS server demonstration program.
- `mini_client` - A minimal TLS client that uses minimal set of memory consumption. It should be used with `config-suite-b.h` or `config-ccm-psk-tls1_2.h` as the configuration files.
- `ssl_client1` - An SSL client demonstration program.
- `ssl_client2` - An SSL client demonstration program with certificate authentication.
- `ssl_fork_server` - An SSL server demonstration program using `fork()` for handling multiple clients.
- `ssl_mail_client` - An SSL client for SMTP servers.
- `ssl_pthread_server` - An SSL server demonstration program using `pthread` for handling multiple clients.
- `ssl_server` - An SSL server demonstration program.
- `ssl_server2` - A flexible SSL server demonstration, which accepts many different options for various use cases.
