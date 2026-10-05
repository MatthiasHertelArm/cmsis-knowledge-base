---
id: "mcuboot-bootloader-testing-in-ci-testing-in-ci"
type: "concept"
domain: "boot-update"
title: "Bootloader: [Testing in CI](#testing-in-ci)"
summary: "The CI currently tests the Fault Injection Hardening feature of MCUboot by executing instruction skip during execution, and looking at whether a corrupted image was booted by the bootloader or not."
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@ba2099f:docs/design.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/ba2099f/docs/design.md#testing-in-ci-testing-in-ci"
license: "Apache-2.0"
mode: "V"
---

### [Testing Fault Injection Hardening (FIH)](#testing-fih)

The CI currently tests the Fault Injection Hardening feature of MCUboot by
executing instruction skip during execution, and looking at whether a corrupted
image was booted by the bootloader or not.

The main idea is that instruction skipping can be automated by scripting a
debugger to automatically execute the following steps:

- Set breakpoint at specified address.
- Continue execution.
- On breakpoint hit increase the Program Counter.
- Continue execution.
- Detach from target after a timeout reached.

Whether or not the corrupted image was booted or not can be decided by looking
for certain entries in the log.

As MCUboot is deployed on a microcontroller, testing FI would not make much
sense in the simulator environment running on a host machine with different
architecture than the MCU's, as the degree of hardening depends on compiler
behavior. For example, (a bit counterintuitively) the code produced by gcc
with `-O0` optimisation is more resilient against FI attacks than the code
generated with `-O3` or `-Os` optimizations.

To run on a desired architecture in the CI, the tests need to be executed on an
emulator (as real devices are not available in the CI environment). For this
implementation QEMU is selected.

For the tests MCUboot needs a set of drivers and an implementation of a main
function. For the purpose of this test Trusted-Firmware-M has been selected as
it supports Armv8-M platforms that are also emulated by QEMU.

The tests run in a docker container inside the CI VMs, to make it more easy to
deploy build and test environment (QEMU, compilers, interpreters). The CI VMs
seems to be using quite old Ubuntu (16.04).

The sequence of the testing is the following (pseudo code):

```sh
fn main()
  # Implemented in ci/fih-tests_install.sh
  generate_docker_image(Dockerfile)

  # See details below. Implemented in ci/fih-tests_run.sh.
  # Calling the function with different parameters is done by Travis CI based on
  # the values provided in the .travis.yaml
  start_docker_image(skip_sizes, build_type, damage_type, fih_level)

fn start_docker_image(skip_sizes, build_type, damage_type, fih_level)
  # implemented in ci/fih_test_docker/execute_test.sh
  compile_mcuboot(build_type)

  # implemented in ci/fih_test_docker/damage_image.py
  damage_image(damage_type)

  # implemented in ci/fih_test_docker/run_fi_test.sh
  ranges = generate_address_ranges()
  for s in skip_sizes
    for r in ranges
      do_skip_in_qemu(s, r) # See details below
  evaluate_logs()

fn do_skip_in_qemu(size, range)
  for a in r
    run_qemu(a, size)  # See details below

# this part is implemented in ci/fih_test_docker/fi_tester_gdb.sh
fn run_qemu(a, size)
  script = create_debugger_script(a, size)
  start_qemu_in_bacground() # logs serial out to a file
  gdb_attach_to_qemu(script)
  kill_qemu()

  # This checks the debugger and the quemu logs, and decides whether the tets
  # was executed successfully, and whether the image is booted or not. Then
  # emits a yaml fragment on the standard out to be processed by the caller
  # script
  evaluate_run(qemu_log_file)
```

Further notes:

- The image is corrupted by changing its signature.
- MCUBOOT_FIH_PROFILE_MAX is not tested as it requires TRNG, and the AN521
platform has no support for it. However this profile adds the random
execution delay to the code, so should not affect the instruction skip results
too much, because break point is placed at exact address. But in practice this
makes harder the accurate timing of the attack.
- The test cases defined in .travis.yml always return `passed`, if they were
executed successfully. A yaml file is created during test execution with the
details of the test execution results. A summary of the collected results is
printed in the log at the end of the test.

An advantage of having the tests running in a docker image is that it is
possible to run the tests on a local machine that has git and docker, without
installing any additional software.

So, running the test on the host looks like the following (The commands below
are issued from the MCUboot source directory):

```sh
$ mkdir docker
$ ./ci/fih-tests_install.sh
$ FIH_LEVEL=MEDIUM BUILD_TYPE=RELEASE SKIP_SIZE=2 DAMAGE_TYPE=SIGNATURE \
     ./ci/fih-tests_run.sh
```
On the travis CI the environment variables in the last command are set based on
the configs provided in the `.travis.yaml`

This starts the tests, however the shell that it is running in is not
interactive, it is not possible to examine the results of the test run. To have
an interactive shell where the results can be examined, the following can be
done:

- The docker image needs to be built with `ci/fih-tests_install.sh` as described
  above.
- Start the docker image with the following command:
  `docker run -i -t mcuboot/fih-test`.
- Execute the test with a command similar to the following:
  `/root/execute_test.sh 8 RELEASE SIGNATURE MEDIUM`. After the test finishes,
  the shell returns, and it is possible to investigate the results. It is also
  possible to stop the test with _Ctrl+c_. The parameters to the
  `execute_test.sh` are `SKIP_SIZE`, `BUILD_TYPE`, `DAMAGE_TYPE`, `FIH_LEVEL` in
  order.
