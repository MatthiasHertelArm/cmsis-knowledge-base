---
id: "zep-test-framework-quick-start-unit-testing"
type: "concept"
domain: "test"
title: "Test Framework: Quick start - Unit testing"
summary: "Ztest can be used for unit testing. This means that rather than including the entire Zephyr OS for testing a single function, you can focus the testing efforts into the specific module in question."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/test/ztest.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/test/ztest.rst"
license: "Apache-2.0"
mode: "V"
---

Ztest can be used for unit testing. This means that rather than including the
entire Zephyr OS for testing a single function, you can focus the testing
efforts into the specific module in question. This will speed up testing since
only the module will have to be compiled in, and the tested functions will be
called directly.

To setup unit tests you have to add a CMakeLists.txt, a tests.yaml and a
prj.conf to the directory containing the unit test source files. The resulting
binary from this directory is built using -DBOARD=unit_testing. When twister
is invoked the script zephyr/scripts/pylib/twister/twisterlib/testplan.py
filters out all tests.yaml in which type: unit is not set. Only unit tests
are executed with a firmware build with BOARD=unit_testing.


**Note:** Unit tests are run as **native** applications on the host and are therefore subject to similar limitations as documented for the POSIX architecture. Running unit tests is therefore only supported for Linux. To run unit tests on Windows or macOS it is necessary to use containers or Virtual Machines running a Linux guest. Follow the same instructions as for the


### The `unit_testing` board


Unit tests are built for the special `unit_testing` board
(`subsys/testsuite/boards/unit_testing`). It is not a real piece of
hardware nor a simulated target: it is a pseudo-board with `arch: unit` that
uses the host toolchain to produce a regular native executable. Selecting it
with `-DBOARD=unit_testing` (which Twister does automatically for scenarios
marked `type: unit`) builds and links only the source files you add to the
`testbinary` target together with the Ztest unit-test harness.

Crucially, **the Zephyr kernel and operating system are not built at all**.
There is no boot sequence, no scheduler, no devicetree-driven device
initialization, and no driver model. The functions under test are compiled into
the test binary and called directly. Any kernel API or other dependency that the
module under test relies on must be supplied by the test itself, usually as a
stub or a mock.


#### Difference from `native_sim` and other boards


It is easy to confuse the `unit_testing` board with
native_sim, since both run on the host. They are
fundamentally different:

* native_sim builds the
  **complete Zephyr OS** -- kernel, devicetree, Kconfig, drivers and
  subsystems -- into a host binary that boots and runs exactly like a Zephyr
  image on real hardware, only compiled for the host instead of a target SoC.
  Use it to run full applications and integration tests on the host. Tests for
  these boards do **not** set `type: unit`.

* `unit_testing` builds **none** of that. It links only the code under test
  plus Ztest, with everything else stubbed or mocked, and calls the tested
  functions directly. This makes builds and runs fast and keeps the focus on a
  single module, at the cost of having to provide stubs for every dependency.
  These tests must set `type: unit` (see below).

In short, reach for `native_sim` to exercise code in the context of a running
Zephyr system, and for `unit_testing` to test an isolated module without
pulling in the kernel.


### CMakeLists.txt


In order to declare the unit tests present in a source folder, you need to add
the relevant source files to the `testbinary` target from the CMake
`unittest <cmake/modules/unittest.cmake>` component. See a minimal
example below:

```cmake

cmake_minimum_required(VERSION 3.28.0)

project(app)
find_package(Zephyr COMPONENTS unittest REQUIRED HINTS $ENV{ZEPHYR_BASE})
target_sources(testbinary PRIVATE main.c)
```
Since you won't be including basic kernel data structures that most code
depends on, you have to provide function stubs in the test. Ztest provides
some helpers for mocking functions, as demonstrated below.

In a unit test, mock objects can simulate the behavior of complex real objects
and are used to decide whether a test failed or passed by verifying whether an
interaction with an object occurred, and if required, to assert the order of
that interaction.


### tests.yaml


You have to set the value for the key "type" to "unit" in the tests.yaml

```yaml

tests:
   testscenario.testsuite:
      tags: your_tag
      type: unit
```

### prj.conf


For unit tests this contains usually only

```kconfig

CONFIG_ZTEST=y
```
If your unit tests require additional libraries (e.g. math-lib) you will have to
add them either via the CMakeLists.txt or in the tests.yaml:

```yaml

tests:
   testscenario.testsuite:
      tags: your_tag
      type: unit
      extra_args:
         - EXTRA_LDFLAGS="-lm"
```
Examples of unit tests can be found in the `tests/unit/` folder.
