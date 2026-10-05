---
id: "tfm-build-tests-regression-tests"
type: "concept"
domain: "security"
title: "Build Tests: Regression Tests"
summary: "For instructions on configuring, building and executing the regression tests please refer to the documentation in tf-m-tests repository (to be added). The regression test application is located under /tests_reg folder."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/building/tests_build_instruction.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/building/tests_build_instruction.html#regression-tests"
license: "BSD-3-Clause"
mode: "V"
---

For instructions on configuring, building and executing the regression tests
please refer to the documentation in **tf-m-tests** repository (to be added).
The regression test application is located under **/tests_reg** folder.
It is recommended to build both SPE and NSPE from that folder.

The basic commands for building the regression tests will be:

```bash

cd </tf-m-tests/tests_reg>
cmake -S spe -B build_spe -DTFM_PLATFORM=arm/mps2/an521 \
      -DCONFIG_TFM_SOURCE_PATH=<TF-M source dir> \
      -DTFM_TOOLCHAIN_FILE=<Absolute path to>/toolchain_ARMCLANG.cmake \
      -DTEST_S=ON -DTEST_NS=ON
cmake --build build_spe -- install

cmake -S . -B build_test -DCONFIG_SPE_PATH=<Absolute path to>/build_spe/api_ns
cmake --build build_test
```
Instead of enable all the supported Secure (`TEST_S`) and NS (`TEST_NS`) tests, you can also
enable individual test suites by using `-DTEST_S_<SUITE>=ON` or `-DTEST_NS_<SUITE>=ON`.
For the available test suites, refer to the `default_s_test_config.cmake` and
`default_ns_test_config.cmake` files in tf-m-tests repo.

All the test suite config options should be passed to the SPE build command, including NS ones.
The SPE building command also accepts all the other config options used to build a single TF-M.
All options passing to SPE build does not have to be duplicated in NSPE build, including NS test
suite config options.
And this also applies to the below PSA API tests.
