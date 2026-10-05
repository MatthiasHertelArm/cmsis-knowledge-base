---
id: "zep-babblesim-types-of-tests"
type: "concept"
domain: "test"
title: "BabbleSim: Types of tests"
summary: "The bsim boards can be used without radio activity, and in that case, it is not necessary to connect them to a physical layer simulation."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/test/bsim.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/test/bsim.rst"
license: "Apache-2.0"
mode: "V"
---

### Tests without radio activity: bsim tests with twister


The bsim boards can be used without radio activity, and in that case, it is not
necessary to connect them to a physical layer simulation. Thanks to this, these target boards can
be used just like native_sim with twister,
to run all standard Zephyr twister tests, but with models of a real SOC HW, and their drivers.


### Tests with radio activity


When there is radio activity, BabbleSim tests require at the very least a physical layer simulation
running, and most, more than 1 simulated device. Due to this, these tests are executed by running
a dedicated script for each test which starts both the needed simulated devices, and the physical
layer executable with their required parameters, and any other tool which may be required.

To be able to run them with twister, the bsim harness should be used.

These tests are kept in the `tests/bsim/` folder.

Check the sub-sections below for more information about how to build and run them, as well as the
conventions they follow.

There are two main sets of tests:

* Self checking embedded application/tests: In which some of the simulated devices applications are
  built with some checks which decide if the test is passing or failing. These embedded
  applications tests use the bs_tests system to report the pass or
  failure, and in many cases to build several tests into the same binary.

* Test using the EDTT_ tool, in which a EDTT (python) test controls the embedded applications over
  an RPC mechanism, and decides if the test passes or not.
  Today these tests include a very significant subset of the BT qualification test suite.

More information about how different tests types relate to BabbleSim and the bsim boards can be
found in the bsim boards tests section.
