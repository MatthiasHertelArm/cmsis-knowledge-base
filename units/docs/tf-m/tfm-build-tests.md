---
id: "tfm-build-tests"
type: "concept"
domain: "security"
title: "Build Tests"
summary: "The tests is a TF-M application which verifies TF-M functionality on both SPE and NSPE sides. Thus, tests require an extension of SPE side with test code and extra functionality for some Non-Secure test cases."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/building/tests_build_instruction.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/building/tests_build_instruction.html"
license: "BSD-3-Clause"
mode: "V"
---

The tests is a TF-M application which verifies TF-M functionality on both SPE and NSPE sides.
Thus, tests require an extension of SPE side with test code and extra functionality
for some Non-Secure test cases. To inject that test code into SPE the
`CONFIG_TFM_TEST_DIR` option is used. When SPE build system sees this option
it adds the corresponding folder via `add_subdirectory(${CONFIG_TFM_TEST_DIR} tf-m-tests)`
and includes it to SPE binary.
Also, test configurations should be passed to SPE build to include building Secure Tests.

To hide these complexities to developers, TF-M implements a wrapper CMake in **tf-m-tests**
repository [1]_ to build the SPE for testing rather than building it from the TF-M repository.

The recommended tf-m-tests repo commit to verify TF-M can be found at
`<TF-M source dir>/lib/ext/tf-m-tests/version.txt`.
It does not support auto-downloading as builds start from it.
You need to download it manually before building any tests with the following commands:

```bash

git clone https://git.trustedfirmware.org/TF-M/tf-m-tests.git
git checkout <recommended tf-m-tests commit>
```
