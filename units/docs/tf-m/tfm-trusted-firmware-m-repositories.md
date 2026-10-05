---
id: "tfm-trusted-firmware-m-repositories"
type: "concept"
domain: "security"
title: "Trusted Firmware M: Repositories"
summary: "TF-M is comprised of multiple repositories that supplement each other in making the project both customisable and maintainable."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/introduction/readme.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/introduction/.html#repositories"
license: "BSD-3-Clause"
mode: "V"
---

TF-M is comprised of multiple repositories that supplement each other in making the project both customisable and maintainable.


* - **Repository**
  - **Description**
* - [trusted-firmware-m](https://git.trustedfirmware.org/plugins/gitiles/TF-M/trusted-firmware-m.git/+/refs/heads/main)
  - Software implementation of TF-M with documentation and essential tools
* - [tf-m-tests](https://git.trustedfirmware.org/plugins/gitiles/TF-M/tf-m-tests.git/+/refs/heads/main)
  - Tests that focus on the functionalities of TF-M components
* - [tf-m-tools](https://git.trustedfirmware.org/plugins/gitiles/TF-M/tf-m-tools.git/+/refs/heads/main)
  - Non essential tools used for testing and verification of TF-M
* - [tf-m-extras](https://git.trustedfirmware.org/plugins/gitiles/TF-M/tf-m-extras.git/+/refs/heads/main)
  - Extension of the main repository to host examples, demonstrations, third-party modules etc

# License

The software is provided under a BSD-3-Clause License.
Contributions to this project are accepted under the same license with developer
sign-off as described in the Contributing Process.

This project contains code from other projects as listed below. The code from
external projects is limited to `bl2`, `lib` and `platform`
folders. The original license text is included in those source files.

- The `bl2` folder contains files imported from MCUBoot project and the files
  have Apache 2.0 license.
- The `lib/ext` folder may contain 3rd party projects and files with
  diverse licenses. Here are some that are different from the BSD-3-Clause and
  may be a part of the runtime image. The source code for these projects is
  fetched from upstream at build time only.

   - `CMSIS_5`    - Apache 2.0 license
   - `tf-psa-crypto` - `Apache 2.0 license TF-PSA-Crypto
     <https://github.com/Mbed-TLS/TF-PSA-Crypto/blob/development/LICENSE>`_
   - `mcuboot`    - `Apache 2.0 license MCUBoot
     <https://github.com/mcu-tools/mcuboot/blob/main/LICENSE>`_
   - `qcbor`      - `Modified BSD-3-Clause license
     <https://github.com/laurencelundblade/QCBOR/blob/master/LICENSE>`_
   - `tf-m-extras` - Set of additional components. Please check individually in
     [tf-m-extras repository](https://git.trustedfirmware.org/TF-M/tf-m-extras.git/tree/)

- The `platform` folder currently contains platforms support imported from
  the external project and the files may have different licenses.

The document Supported Platforms lists the details.


# Release Notes and Process

The Release Cadence and Process provides
release cadence and process information.

The Releases provides details of
major features of the release and platforms supported.


# Feedback and Support

For this release, feedback is requested via email to
tf-m@lists.trustedfirmware.org <tf-m@lists.trustedfirmware.org>.

A bi-weekly technical forum is available for discussion on any technical topics
online. Welcome to join [TF-M Forum](https://www.trustedfirmware.org/meetings/tf-m-technical-forum).

--------------

*SPDX-FileCopyrightText: Copyright The TrustedFirmware-M Contributors*

*SPDX-License-Identifier: BSD-3-Clause*
