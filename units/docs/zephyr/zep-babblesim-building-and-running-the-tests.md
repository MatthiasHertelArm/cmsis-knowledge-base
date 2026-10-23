---
id: "zep-babblesim-building-and-running-the-tests"
type: "concept"
domain: "test"
title: "BabbleSim: Building and running the tests"
summary: "Check the nrf52_bsim page for instructions on how to set up the simulator."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/test/bsim.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/test/bsim.rst"
license: "Apache-2.0"
mode: "V"
---

Check the nrf52_bsim page for instructions on how to set up the
simulator.

You can build and run these tests with twister.
To run multidevice tests, you will need to pass twister the option `--fixture bsim_multi_test`.

For example, from ${ZEPHYR_BASE}, you can build and run one of the BT tests with:

```bash

twister -p nrf52_bsim/native -T tests/bsim/bluetooth/host/adv/chain/ --fixture bsim_multi_test
```
If the test binaries have already been built, you can also run a test directly using its individual
test script. For example:

```bash

BOARD=nrf52_bsim/native tests/bsim/bluetooth/host/adv/chain/tests_scripts/adv_chain.sh
```
Twister command line options like `-n, --no-clean`,
`--aggressive-no-clean`, or `-b, --build-only` are likely to be useful when debugging or
fixing issues.


### Legacy batch scripts


Until the twister bsim harness was added, building and running multidevice bsim tests relied
on two scripts in the `tests/bsim/` folder: `compile.sh` and `run_parallel.sh`.
These scripts were used by the CI system to build the needed images and execute these tests in
batch. They were also meant as utilities for users to build and execute their tests.
These scripts can still be used, but users are recommended to transition to using
twister and `tests.yaml` definitions.

These scripts expect a few environment variables to be set.
For example, from Zephyr's root folder, you can run:

```bash

# Build all the tests
${ZEPHYR_BASE}/tests/bsim/compile.sh

# Run them (in parallel)
RESULTS_FILE=${ZEPHYR_BASE}/myresults.xml \
   SEARCH_PATH=${ZEPHYR_BASE}/tests/bsim \
      ${ZEPHYR_BASE}/tests/bsim/run_parallel.sh
```
Or to build and run only a specific subset, e.g. host advertising tests:

```bash

# Build the Bluetooth host advertising tests
${ZEPHYR_BASE}/tests/bsim/bluetooth/host/adv/compile.sh

# Run them (in parallel)
RESULTS_FILE=${ZEPHYR_BASE}/myresults.xml \
   SEARCH_PATH=${ZEPHYR_BASE}/tests/bsim/bluetooth/host/adv \
      ${ZEPHYR_BASE}/tests/bsim/run_parallel.sh
```
Check the `run_parallel.sh` help for more options and examples on how to use this script to run
the tests in batch.

After building the tests' required binaries you can run a test directly using its individual test
script.

For example you can build the required binaries for the networking tests with

```bash

WORK_DIR=${ZEPHYR_BASE}/bsim_out ${ZEPHYR_BASE}/tests/bsim/net/compile.sh
```
and then directly run one of the tests:

```bash

${ZEPHYR_BASE}/tests/bsim/net/sockets/echo_test/tests_scripts/echo_test_802154.sh
```

### Conventions



#### Test code


See the `Bluetooth sample test <tests/bsim/bluetooth/host/misc/sample_test/README.rst>` for conventions that apply to test
code.


#### Test images


When adding a new test, always consider if it is possible to have that test be part of an existing
image. Each image adds CI build time, while the bs_tests system allows
sharing an image for multiple tests which are selected at runtime, as long as their Kconfig and
other global state do not conflict.


#### Test scripts


Please follow the existing conventions and do not design one-off bespoke runners (e.g. a python
script, or another shell abstraction).

The rationale is that it is easier and faster for the maintainers to perform tree-wide updates for
build system or compatibility changes if the tests are run in the same manner, with the same
variables, etc..

If you have a good idea for improving your test script, please make a PR changing *all* the test
scripts in order to benefit everyone and conserve homogeneity. You can of course discuss it first in
an RFC issue or on the babblesim discord channel.

Scripts starting with an underscore (`_`) are not automatically discovered and run. They can serve
as either helper functions for the main script, or can be used for local development utilities, e.g.
building and running tests locally, debugging, etc..

Here are the conventions:

- Each test is defined by a shell script with the extension `.sh`, in a subfolder called
  `tests_scripts/`.
- It is recommended to run a single test per script file. It allows for better parallelization of
  the runs in CI.
- Scripts expect that the binaries they require are already built. They should not compile binaries.
- Scripts will spawn the processes for every simulated device and the physical layer simulation.
- Scripts must return 0 to the invoking shell if the test passes, and not 0 if the test fails.
- Each test must have a unique simulation id, to enable running different tests in parallel.
- Neither the scripts nor the images should modify the workstation filesystem content beyond the
  `${BSIM_OUT_PATH}/results/<simulation_id>/` or `/tmp/` folders.
  That is, they should not leave stray files behind.
- Tests that require several consecutive simulations (e.g, if simulating a device pairing, powering
  off, and powering up after as a new simulation) should use separate simulation ids for each
  simulation segment, ensuring that the radio activity of each segment can be inspected a
  posteriori.
- Avoid overly long tests. If the test takes over 20 seconds of runtime, consider if it is possible
  to split it in several separate tests.
- If the test takes over 6 seconds, set `EXECUTE_TIMEOUT` to a value that is at least 5 times
  bigger than the measured run-time.
- Do not set `EXECUTE_TIMEOUT` to a value lower than the default.
- Tests should not be overly verbose: less than a hundred lines are expected on the outputs. Do make
  use of `LOG_DBG()` extensively, but don't enable the `DBG` log level by default.
- Test scripts that use the Physical layer simulation are expected to pass any extra parameters
  passed to the test script directly to the Phy executable. This is used, for example, to run the
  Phy in check mode (`-c`), in which the Phy verifies that the last simulation and this one have
  produced the exact same radio traffic.
- Only override random seeds if there is a real need for that test. Avoid designing tests which are
  overly sensitive to random seed changes.
