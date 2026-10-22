---
id: "mbedtls-writing-a-proof-of-concept-for-a-v-structure-of-a-poc"
type: "concept"
domain: "security"
title: "Writing a proof-of-concept for a vulnerability: Structure of a PoC"
summary: "This section discusses the preferred structure of a PoC. These are guidelines, not requirements. You do not have to follow them, but they make our life easier."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/attacks/poc-guidelines.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/attacks/poc-guidelines.md#structure-of-a-poc"
license: "Apache-2.0"
mode: "V"
---

This section discusses the preferred structure of a PoC. These are guidelines, not requirements. You do not have to follow them, but they make our life easier.

Note that LLM tend to be fairly good at picking up the structure of our test code, including finding poorly documented auxiliary functions. However, without proper guidance, LLM tend to use internal functions. Internal functions should not be used in victim code, since their behavior is not part of the library's contract.

### PoC using a sample program

For parser bugs, an input that causes a sample program to crash is sufficient as a PoC. You do not need to write your own program if one already exists.

### PoC as a unit test

For TF-PSA-Crypto and Mbed TLS maintainers, the ideal form of a PoC is a non-regression test for the bug. This means a new test case in `tests/suites/test_suite_*.data` which either fails at a clearly valid assertion, or causes memory corruption inside the library. Note that if the bug causes memory corruption, you should not try to detect it in the code: instead, rely on compile-time or run-time instrumentation such as AddressSanitizer (ASan) or Valgrind.

Depending on how close the existing test functions come to reaching the bug, you might either:

* add a new test case for an existing function;
* or add an assertion to the existing code;
* or write a new test function.

If you write a new test function, it is helpful if you can provide a variant of the test that passes, to help locate the cause of the bug.

Note that unit tests have easy access to internal interfaces of individual library modules. A violation of an internal contract does not demonstrate a vulnerability. A violation of a public contract, reached by using internal functions, does not demonstrate a vulnerability either. To demonstrate a vulnerability, make sure that the victim code only uses public interfaces.

### PoC using SSL test programs

For TLS bugs, depending on the way the vulnerability can be triggered, it may be more convenient to use the test programs `programs/ssl/ssl_client2` and `programs/ssl/ssl_server2`. For bugs involving non-nominal DTLS traffic, `programs/test/udp_proxy` can be useful. These programs are normally invoked via `tests/ssl-opt.sh`. A test case in `tests/ssl-opt.sh` is a convenient way to demonstrate a TLS bug. Our tooling is set up to either run `ssl_client2` against `ssl_server2`, or run one of them against an OpenSSL or GnuTLS peer.

Note that if the bug causes memory corruption, you should not try to detect it in the code: instead, rely on compile-time or run-time instrumentation such as AddressSanitizer (ASan) or Valgrind.

Note that `ssl_client2` and `ssl_server2` have access to internal functions that can create malformed traffic or put the SSL context in unexpected states. When demonstrating a vulnerability, the attacker side may use whatever is convenient to construct malformed traffic. On the other hand, the victim side must not rely on calls to internal functions, since that would fail to demonstrate a security impact. If the vulnerability affects a client or server in the default runtime configuration, you may use `programs/ssl/ssl_client1` or `programs/ssl/ssl_server` as the victim.
