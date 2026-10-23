---
id: "mbedtls-mbed-tls-ci-interface-stability-tests"
type: "concept"
domain: "security"
title: "Mbed TLS CI: Interface stability tests"
summary: "The interface stability tests compare some aspects of the pull request's code with the code in the target branch. They run a script called abi_check.py, but their scope is broader than the name indicates:"
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/testing/testing-ci.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/testing/testing-ci.md#interface-stability-tests"
license: "Apache-2.0"
mode: "V"
---

The interface stability tests compare some aspects of the pull request's code with the code in the target branch. They run a script called `abi_check.py`, but their scope is broader than the name indicates:

* [API comparison](#api-comparison) in the default configuration;
* [ABI comparison](#abi-comparison) in the default configuration;
* Storage format [test case preservation](#test-case-preservation);
* Generated [test case preservation](#test-case-preservation).

These tests have many false positives. Therefore, it is not mandatory for them to pass. If GitHub marks the checks as failed, please see the logs and verify whether the reported failures are acceptable.

### API comparison

The API comparison checks that every API element in a public header that exists on the target branch still exists and is compatible on the pull request branch. This check is performed in the default configuration. For example, if a function exists on the main branch, there must be a function of the same name in the same header with the same prototype on the target branch.

The API must be preserved between minor versions of the library (e.g. Mbed TLS 3.4.x to Mbed TLS 3.5.0). It may only change in a major release (e.g. Mbed TLS 3.6.x to Mbed TLS 4.0.0).

Some changes are not considered API breaks, as described [in `BRANCHES.md`](https://github.com/Mbed-TLS/mbedtls/blob/development/BRANCHES.md#backwards-compatibility-for-application-code). There are acceptable changes which the tool flags, such as:

* Changes to private fields in structures (declared using `MBEDTLS_PRIVATE`).
* Changes to functions and macros that do not have Doxygen documentation.
* Changes to anything that is documented as experimental.

### ABI comparison

The ABI comparison checks that every symbol in a build in the default configuration of the target branch remains present in the target branch.

The ABI must normally be preserved between patch releases of the library (e.g. Mbed TLS 3.6.0 to Mbed TLS 3.6.1). In particular, it should be preserved in long-time support (LTS) branches. The ABI may change in minor or major releases (e.g. Mbed TLS 3.5.x to 3.6.0, or 3.6.x to 4.0.0).

There are acceptable changes which the tool flags, such as changes to undocumented functions that are only meant for use inside the library.

### Test case preservation

We check that certain sets of test cases are preserved.

* Storage format tests: the goal is to ensure that new versions of the library can read persistent keys stored by a previous version. We maintain this compatibility even across major versions. If the storage format changes, we will change the storage format version number and provide an upgrade path.
* Generated tests: the goal is to ensure that we don't lose coverage without noticing, for example if a change to a test generation script causes it to emit fewer tests than expected.

The comparison is based on lines in `.data` files containing the function name and the arguments for a test case. There are acceptable changes which the tool flags, such as adding an argument to a test function, or (not applicable to storage format tests) changes to the test data which we consider acceptable in terms of coverage.
