---
id: "mbedtls-is-mbed-tls-fips-certified-fips-test-vectors"
type: "concept"
domain: "security"
title: "Is Mbed TLS FIPS certified?: FIPS test vectors"
summary: "For a FIPS certification, cryptographic modules are normally tested against the Security Requirements for Cryptographic Modules requirements found in the FIPS PUB 140-2."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/generic/is-mbedtls-fips-certified.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/generic/is-mbedtls-fips-certified.md#fips-test-vectors"
license: "Apache-2.0"
mode: "V"
---

For a FIPS certification, cryptographic modules are normally tested against the Security Requirements for Cryptographic Modules requirements found in the FIPS PUB 140-2.

These requirements include official NIST validating and test vectors for the algorithms. These are included and used in our test suite.

The test suite that is located at `tests/` within the Mbed TLS source code often contains a subset of the available NIST test vectors. So, whenever you run the tests with `make check`, these tests will be run as well.

<!--", is-mbedtls-fips-certified,"Describes the FIPS 140-2 certification and the current status of Mbed TLS certification and presence of the validation and test vectors","NIST, FIPS, FIPS 140-2, 140-2, test vectors, validation vectors, cavp","nist, fips, test vectors, validation, cavp, certification, test suite, accreditation, security",published,"2013-06-25 08:56:00",1,7684,"2015-07-24 11:39:00","Paul Bakker"-->
