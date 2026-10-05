---
id: "mbedtls-fuzzing-of-mbed-tls-oss-fuzz"
type: "concept"
domain: "security"
title: "Fuzzing of Mbed TLS: OSS-Fuzz"
summary: "OSS-Fuzz is a software project that combines fuzzing-related tools with scripts to run those fuzzers on a large set of security-critical programs, including Mbed TLS. OSS-Fuzz also runs these programs on a regular basis."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/testing/fuzzing.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/testing/fuzzing.md#oss-fuzz"
license: "Apache-2.0"
mode: "V"
---

[OSS-Fuzz](https://github.com/google/oss-fuzz) is a software project that combines fuzzing-related tools with scripts to run those fuzzers on a large set of security-critical programs, including Mbed TLS. OSS-Fuzz also runs these programs on a regular basis.

### OSS-Fuzz reports

When the OSS-Fuzz infrastructure notices a fuzzer crash, the maintainers of the offending module are notified. For fuzzers where Mbed TLS is integrated, this includes the Mbed TLS security team.

Fuzzing crash reports become public after 90 days or when the crash is noticed as fixed.

### OSS-Fuzz integration

Mbed TLS is integrated in four Cryptofuzz projects:

* [bignum-fuzzer](https://github.com/google/oss-fuzz/tree/master/projects/bignum-fuzzer) (obsoleted by Cryptofuzz?)
* [cryptofuzz](https://github.com/google/oss-fuzz/tree/master/projects/cryptofuzz) — see [“Cryptofuzz”](#cryptofuzz)
* [ecc-diff-fuzzer](https://github.com/google/oss-fuzz/tree/master/projects/ecc-diff-fuzzer) (obsoleted by Cryptofuzz?)
* [mbedtls](https://github.com/google/oss-fuzz/tree/master/projects/mbedtls) — see [“Mbed TLS fuzz programs”](#mbed-tls-fuzz-programs)

### Mbed TLS fuzz programs

The [`program/fuzz`](https://github.com/Mbed-TLS/mbedtls/tree/development/programs/fuzz) directory contains several programs to fuzz key parsing in the PK module, X.509 certificate/CRL/CRT parsing, and TLS/DTLS handshakes and communication.

These programs, as well as a corpuse, were contributed by Philippe Antoine (catenacyber) and are now mostly maintained by Arm.

To reproduce a crash, just run `programs/fuzz/xxx_fuzz crash-aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa`, preferably in a debug build to understand what's going on.
