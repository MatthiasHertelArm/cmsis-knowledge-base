---
id: "tfm-tests-configuration-psa-tests"
type: "concept"
domain: "security"
title: "Tests configuration: PSA tests"
summary: "PSA tests are configured by using the TEST_PSA_API cmake variable. The variable should be set to the name of the test suite that is desired. It is not supported to set both TEST_PSA_API and TEST_S or TEST_NS."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/configuration/test_configuration.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/configuration/test_configuration.html#psa-tests"
license: "BSD-3-Clause"
mode: "V"
---

PSA tests are configured by using the `TEST_PSA_API` cmake variable. The
variable should be set to the name of the test suite that is desired. It is
_not_ supported to set both `TEST_PSA_API` and `TEST_S` or `TEST_NS`.

The Functional API tests are:
 - `CRYPTO`
 - `INITIAL_ATTESTATION`
 - `STORAGE` (INTERNAL_TRUSTED_STORAGE and PROTECTED_STORAGE)
 - `INTERNAL_TRUSTED_STORAGE`
 - `PROTECTED_STORAGE`

The Firmware Framework test suites are:
 - `IPC`

Note that these map directly to the `SUITE` cmake variable used in the
psa-arch-tests documentation.

--------------

*SPDX-FileCopyrightText: Copyright The TrustedFirmware-M Contributors*

*SPDX-License-Identifier: BSD-3-Clause*
