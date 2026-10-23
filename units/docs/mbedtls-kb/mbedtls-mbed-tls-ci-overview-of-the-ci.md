---
id: "mbedtls-mbed-tls-ci-overview-of-the-ci"
type: "concept"
domain: "security"
title: "Mbed TLS CI: Overview of the CI"
summary: "The following checks are reported on GitHub:"
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/testing/testing-ci.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/testing/testing-ci.md#overview-of-the-ci"
license: "Apache-2.0"
mode: "V"
---

The following checks are reported on GitHub:

* [DCO](#dco): check that all commit messages have a `Signed-off-by:` line. This must pass.
* [readthedocs](#documentation-build): build the documentation for online browsing. This must pass.
* [PR tests](#pr-tests): build and test the library in over 100 different configurations and platforms, as well as a few simple static checks. This must pass.
* [Interface stability tests](#interface-stability-tests): compare some interfaces before and after the proposed changes. This has many false positives, and a pull request can be merged if this check fails, at the gatekeeper's discretion.

The PR tests and the interface stability tests run on two hosts: “Internal CI” which is only accessible to Arm employees, and “TF OpenCI” which is publicly accessible. In principle, these run the same tests, thus if you are not an Arm employee (or even if you are) you can generally ignore the internal CI. At the time of writing, OpenCI is mandatory and internal CI is optional, so intermittent failures on the internal CI can be ignored.
