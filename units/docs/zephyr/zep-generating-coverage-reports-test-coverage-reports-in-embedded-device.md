---
id: "zep-generating-coverage-reports-test-coverage-reports-in-embedded-device"
type: "concept"
domain: "test"
title: "Generating coverage reports: Test coverage reports in embedded devices or QEMU"
summary: "GCC GCOV <gcov> is a test coverage program used together with the GCC compiler to analyze and create test coverage reports for your programs, helping you create more efficient, faster running code and discovering untested code paths"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/test/coverage.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/test/coverage.rst"
license: "Apache-2.0"
mode: "V"
---

### Overview

GCC GCOV <gcov_> is a test coverage program
used together with the GCC compiler to analyze and create test coverage reports
for your programs, helping you create more efficient, faster running code and
discovering untested code paths

In Zephyr, gcov collects coverage profiling data in RAM (and not to a file
system) while your application is running. Support for gcov collection and
reporting is limited by available RAM size and so is currently enabled only
for QEMU emulation of embedded targets.


### Details

There are 2 parts to enable this feature. The first is to enable the coverage for the
device and the second to enable in the test application. As explained earlier the
code coverage with gcov is a function of RAM available. Therefore ensure that the
device has enough RAM when enabling the coverage for it. For example a small device
like frdm_k64f can run a simple test application but the more complex test
cases which consume more RAM will crash when coverage is enabled.

To enable the device for coverage, select `CONFIG_HAS_COVERAGE_SUPPORT`
in the Kconfig.board file.

To report the coverage for the particular test application set `CONFIG_COVERAGE`.


### Steps to generate code coverage reports


These steps will produce an HTML coverage report for a single application.

1. Build the code with CONFIG_COVERAGE=y.

#. Capture the emulator output into a log file. You may need to terminate
   the emulator with `Ctrl-A X` for this to complete after the coverage dump
   has been printed:

```console

$ ninja -Cbuild run | tee log.log
```
#. Generate the gcov `.gcda` and `.gcno` files from the log file that was
   saved:

```console

$ python3 scripts/gen_gcov_files.py -i log.log
```
#. Find the gcov binary placed in the SDK. You will need to pass the path to
   the gcov binary for the appropriate architecture when you later invoke
   `gcovr`:

```console

$ find $ZEPHYR_SDK_INSTALL_DIR -iregex ".*gcov"
```
#. Create an output directory for the reports:

```console

$ mkdir -p coverage-report
```
#. Run `gcovr` to get the reports:

```console

$ gcovr -r $ZEPHYR_BASE . --html -o coverage-report/coverage.html --html-details --gcov-executable <gcov_path_in_SDK>
```
