---
id: "mbedtls-mbed-tls-ci-pr-tests"
type: "concept"
domain: "security"
title: "Mbed TLS CI: PR tests"
summary: "The “PR tests” (pull request tests) check is the bulk of the CI. It runs an extensive battery of tests on many configurations and with several toolchains and platforms. The tests are hosted on Jenkins."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/testing/testing-ci.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/testing/testing-ci.md#pr-tests"
license: "Apache-2.0"
mode: "V"
---

The “PR tests” (pull request tests) check is the bulk of the CI. It runs an extensive battery of tests on many configurations and with several toolchains and platforms. The tests are hosted on Jenkins.

This check must pass on at least one of the CIs (OpenCI or Internal CI). Which one is required can vary over time (depending on which one is most reliable and most convenient).

### High-level overview of the PR tests

The PR tests check includes the following parts:

- Run most of `tests/scripts/all.sh`. The default platform is on Ubuntu 16.04 x86 (64-bit), but some components request a different platform. This script includes:
    - Some sanity checks.
    - Tests of the library in various configurations. The tests are mainly unit tests (`make test`), SSL feature tests (`tests/ssl-opt.sh`) and interoperability tests (`tests/compat.sh`).
    - Some cross compilation with GCC-arm, Arm Compiler 5 (`armcc`), Arm Compiler 6 (`armclang`) and MinGW (`i686-w64-mingw32-gcc`). These are only builds, not tests.
- Run a subset of `tests/scripts/all.sh` on FreeBSD (amd64)
- Build on Windows with MinGW and Visual Studio. We use the following Visual Studio versions:
    - Since Mbed TLS 2.19: VS 2013, 2015, 2017. As of January 2024, we expect to drop VS 2013 soon.
- A final job called [outcome analysis](#outcome-analysis), which performs sanity checks on test coverage across builds in different configurations.

The component names are:

* all_sh-//platform//-//component//: `tests/scripts/all.sh -k `//component// run on //platform//.
* `code-coverage`: `tests/scripts/basic-build-test.sh` run on Linux (currently Ubuntu 16.04).
* `win32-mingw`, `win32_msvc12_32`, `win32-msvc12_64`: ad hoc Windows jobs in the default configuration, see below.
* `Windows-`//20NN//: builds with the specified version of Visual Studio (Visual Studio 10 2010, Visual Studio 12 2013, Visual Studio 14 2015 or Visual Studio 15 2017).
    * Library configuration: `config.py full` (`config.pl full` in older branches) minus `MBEDTLS_THREADING_xxx`.
    * Visual Studio configurations: `Release` and `Debug`.
    * Architectures: `Win32` and `x64` (except no `x64` in VS 2010).
    * `PlatformToolset` property:
        * “Retargeted” build: set to the version corresponding to the Visual Studio version for “retargeted” builds.
        * “Non-retargeted” build: set to `v120` on `development` (C99 code base).
    * Testing: `selftest.exe`, plus the unit tests in the CMake builds.

The `win32-mingw` component runs the following bat script:
```
cmake . -G "MinGW Makefiles" -DCMAKE_C_COMPILER="gcc"
mingw32-make
mingw32-make test
ctest -VV
programs\test\selftest.exe
```

The `win32_msvc12_32` component runs the following bat script:
```
call "C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\vcvarsall.bat"
cmake . -G "Visual Studio 12"
MSBuild ALL_BUILD.vcxproj
programs\test\Debug\selftest.exe
```
The `win32-msvc12_64` component is identical except that it runs `cmake . -G "Visual Studio 12 Win64"`.

### Outcome analysis

Each build and test job saves a list of test cases and PASS/SKIP/FAIL information. The outcome analysis job collects this information and performs sanity checks on it. The collected data is called the outcome file, which is available as an artifact called `outcomes.csv.xz` on Jenkins. For example, you can download the outcome analysis for the first test run of pull request \#9999 at
```
https://ci.trustedfirmware.org/job/mbed-tls-pr-head/job/PR-9999-head/1/artifact/outcomes.csv.xz
```

Note that the outcome file is very large: on Mbed TLS 3.6, it is about 60MB compressed and over 2GB uncompressed.

The outcome file has a simple semicolon-separated format. The format is documented in [`docs/architecture/testing/test-framework.md`](https://github.com/Mbed-TLS/mbedtls/tree/development/docs/architecture/testing/test-framework.md#outcome-file).

If outcome analysis reports a failure, the logs can't be seen directly on the default view of Jenkins, due to a known limitation of Jenkins's BlueOcean interface. They can be accessed from the classic “Pipeline Steps” view. For convenience, they are also provided as an artifact, e.g.
```
https://ci.trustedfirmware.org/job/mbed-tls-pr-head/job/PR-999-head/1/artifact/result-analysis-analyze_outcomes.log.xz
```

Outcome analysis contains two kinds of checks:

* Every test case must be executed at least once.
* Driver builds must run the same sets of test cases as the corresponding builtin-only build (if there is one).

The script has a list of exceptions, which must be justified.
