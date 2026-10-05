---
id: "mbedtls-mbed-tls-ci-documentation-build"
type: "concept"
domain: "security"
title: "Mbed TLS CI: Documentation build"
summary: "The Mbed TLS API documentation, rendered by Doxygen, is published on readthedocs. GitHub triggers a readthedocs build on every pull request. This is controlled by .readthedocs.yaml. This check is required: a pull request cannot be merged unless it passes."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/testing/testing-ci.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/testing/testing-ci.md#documentation-build"
license: "Apache-2.0"
mode: "V"
---

The Mbed TLS API documentation, rendered by Doxygen, is published [on readthedocs](https://mbed-tls.readthedocs.io/en/latest/). GitHub triggers a readthedocs build on every pull request. This is controlled by [`.readthedocs.yaml`](https://github.com/Mbed-TLS/mbedtls/blob/development/.readthedocs.yaml). This check is required: a pull request cannot be merged unless it passes.

### Retrying a stuck or failed documentation build

If the readthedocs build fails due to a transient failure (e.g. could not communicate to GitHub), or if the status is not reported back to GitHub due to a transient failure, you can re-trigger a new build in one of the following ways:

* If you have a readthedocs account with suitable permissions, go to the build page (`https://readthedocs.org/projects/mbedtls-versioned/builds/<NUMBER>/`) and click “Rebuild this build”.
* Close and reopen the pull request. This triggers a new readthedocs build, and preserves PR tests results and GitHub review states.
