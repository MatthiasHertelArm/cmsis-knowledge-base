---
id: "mbedtls-using-dtls-defaults"
type: "concept"
domain: "security"
title: "Using DTLS: Defaults"
summary: "The cookie callbacks that are registered by default always fail. The rationale is as follows:"
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/how-to/dtls-tutorial.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/dtls-tutorial.md#defaults"
license: "Apache-2.0"
mode: "V"
---

The cookie callbacks that are registered by default always fail. The rationale is as follows:

* You cannot register working callbacks by default since you cannot create and setup the cookie context in an automated way (it needs to be shared among SSL contexts).
* You do not want to silently disable the feature by default, as that would mean insecure defaults.
* Failing callbacks force you to notice something needs to be done.

You can, **if you are sure that amplification attacks against third parties are not an issue** in your particular deployment, disable `ClientHello` verification at run-time:

* Register `NULL` callbacks.
* Alternatively, at compilation: Undefine **MBEDTLS_SSL_DTLS_HELLO_VERIFY** in `mbedtls_config.h`.

<!---",dtls-tutorial,"Article on the DTLS implementation inside Mbed TLS",,"dtls, tutorial",published,"2015-07-24 08:51:00",2,17496,"2016-02-17 17:31:00","Manuel PÃgouriÃ-Gonnard"--->
