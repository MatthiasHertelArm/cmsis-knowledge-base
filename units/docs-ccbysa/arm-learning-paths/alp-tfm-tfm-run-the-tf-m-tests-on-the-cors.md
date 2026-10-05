---
id: "alp-tfm-tfm-run-the-tf-m-tests-on-the-cors"
type: "concept"
domain: "core"
title: "Configure, build and run the TF-M example application: Run the TF-M tests on the Corstone-300 FVP"
summary: "The tests built can now be run on the Corstone-300 FVP. This is done by providing the following arguments to the FVP: - build/tests-spe/bin/bl2.axf is the MCUBoot bootloader image."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/tfm/tfm.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/tfm/tfm/#run-the-tf-m-tests-on-the-corstone-300-fvp"
license: "CC-BY-SA-4.0"
mode: "V"
---

The tests built can now be run on the Corstone-300 FVP. This is done by providing the following arguments to the FVP:
- `build/tests-spe/bin/bl2.axf` is the MCUBoot bootloader image.
- `build/tests/tfm_s_ns_signed.bin` is the combined signed image for the TF-M secure and non-secure image.
- `@<addr>` indicates where in the Corstone-300 FVP memory the image is loaded. The memory map for the FVP is documented in the [FVP Reference Guide](https://developer.arm.com/documentation/100966/1118/Arm--Corstone-SSE-300-FVP/Memory-map-overview-for-Corstone-SSE-300).
- the GUI is disabled with parameter `mps3_board.visualisation.disable-visualisation`
- the tests' outputs is redirected to the standard output with parameters `mps3_board.telnetterminal0.start_telnet` and `mps3_board.uart0.out_file`. Otherwise, the FVP will launch an `xterm` and use a `telnet` connection to display the log, which may not work if your environment does not have an X display.

```console
FVP_Corstone_SSE-300_Ethos-U55 \
  -a cpu0*=build/tests-spe/bin/bl2.axf \
  --data build/tests/tfm_s_ns_signed.bin@0x38000000 \
  -C mps3_board.visualisation.disable-visualisation=1 \
  -C mps3_board.telnetterminal0.start_telnet=0 \
  -C mps3_board.uart0.out_file=/dev/stdout
telnetterminal0: Listening for serial connection on port 5000
telnetterminal1: Listening for serial connection on port 5001
telnetterminal2: Listening for serial connection on port 5002
telnetterminal5: Listening for serial connection on port 5003

    Ethos-U rev 136b7d75 --- Apr 12 2023 13:44:01
    (C) COPYRIGHT 2019-2023 Arm Limited
    ALL RIGHTS RESERVED

[INF] Starting bootloader
[INF] Beginning BL2 provisioning
[WRN] TFM_DUMMY_PROVISIONING is not suitable for production! This device is NOT SECURE
[INF] Image index: 0, Swap type: none
[INF] Bootloader chainload address offset: 0x0
[INF] Jumping to the first image slot
[INF] Beginning TF-M provisioning
<NUL>[WRN] <NUL>TFM_DUMMY_PROVISIONING is not suitable for production! <NUL>This device is NOT SECURE<NUL>
<NUL>[WRN] <NUL>This device was provisioned with dummy keys. <NUL>This device is NOT SECURE<NUL>
<NUL>[Sec Thread] Secure image initializing!
<NUL>TF-M isolation level is: <NUL>0x00000001
Booting TF-M v2.0.0
<NUL>[SFN Test partition] SFN Test Partition initialized.
Creating an empty ITS flash layout.
[INF][Crypto] Provisioning entropy seed... complete.
[DBG][Crypto] Initialising Mbed TLS 3.5.0 as PSA Crypto backend library... complete.

#### Execute test suites for the Secure area ####
Running Test Suite PSA internal trusted storage S interface tests (TFM_S_ITS_TEST_1XXX)...
> Executing 'TFM_S_ITS_TEST_1001'
  Description: 'Set interface'
  TEST: TFM_S_ITS_TEST_1001 - PASSED!
...
TESTSUITE PASSED!
Running Test Suite Symmetric key algorithm based Initial Attestation Service non-secure interface tests (TFM_NS_ATTEST_TEST_2XXX)...
> Executing 'TFM_NS_ATTEST_TEST_2001'
  Description: 'Symmetric key algorithm based Initial Attestation test'
  TEST: TFM_NS_ATTEST_TEST_2001 - PASSED!
TESTSUITE PASSED!

*** Non-secure test suites summary ***
Test suite 'SFN Backend NS test (TFM_NS_SFN_TEST_1XXX)' has PASSED
Test suite 'PSA internal trusted storage NS interface tests (TFM_NS_ITS_TEST_1XXX)' has PASSED
Test suite 'Crypto non-secure interface test (TFM_NS_CRYPTO_TEST_1XXX)' has PASSED
Test suite 'Symmetric key algorithm based Initial Attestation Service non-secure interface tests (TFM_NS_ATTEST_TEST_2XXX)' has PASSED

*** End of Non-secure test suites ***
^C
Stopping simulation...


Info: /OSCI/SystemC: Simulation stopped by user.
```

Congratulations, you have successfully ran some of the TF-M tests (some other test suite, like the PSA tests, are also available in the `tf-m-tests` repository).

# Configure, build and run the TF-M example application

Now that the tests are passing, let's build and run the TF-M example application !

```bash
cmake -S trusted-firmware-m -B build/spe \
      -DCMAKE_BUILD_TYPE=Debug \
      -DTFM_PLATFORM=arm/mps3/corstone300/fvp \
      -DTFM_PROFILE=profile_small \
      -DTFM_TOOLCHAIN_FILE=$PWD/trusted-firmware-m/toolchain_GNUARM.cmake
cmake --build build/spe -- install
```

The `CMakeLists.txt` for the TF-M example application requires a minor fix for the build to go smoothly. In `tf-m-extras/examples/tf-m-example-ns-app/CMakeLists.txt`, move command `add_subdirectory(${CONFIG_SPE_PATH} ${CMAKE_BINARY_DIR}/spe)` (at line 36) *after* the next statement (`add_executable(tfm_ns ...)` ). Build the application with:

```bash
cmake -S tf-m-extras/examples/tf-m-example-ns-app -B build/example \
      -DCMAKE_BUILD_TYPE=Debug \
      -DCONFIG_SPE_PATH=$PWD/build/spe/api_ns
cmake --build build/example
```

To run the image on the FVP, the command line is very similar to the one used with the tests, with changes to the paths for the example application images:

```console
FVP_Corstone_SSE-300_Ethos-U55 \
  -a cpu0*=build/spe/bin/bl2.axf \
  --data build/example/tfm_s_ns_signed.bin@0x38000000 \
  -C mps3_board.visualisation.disable-visualisation=1 \
  -C mps3_board.telnetterminal0.start_telnet=0 \
  -C mps3_board.uart0.out_file=/dev/stdout
telnetterminal0: Listening for serial connection on port 5000
telnetterminal1: Listening for serial connection on port 5001
telnetterminal2: Listening for serial connection on port 5002
telnetterminal5: Listening for serial connection on port 5003

    Ethos-U rev 136b7d75 --- Apr 12 2023 13:44:01
    (C) COPYRIGHT 2019-2023 Arm Limited
    ALL RIGHTS RESERVED

[INF] Starting bootloader
[INF] Beginning BL2 provisioning
[WRN] TFM_DUMMY_PROVISIONING is not suitable for production! This device is NOT SECURE
[INF] Image index: 0, Swap type: none
[INF] Bootloader chainload address offset: 0x0
[INF] Jumping to the first image slot
[INF] Beginning TF-M provisioning
<NUL>[WRN] <NUL>TFM_DUMMY_PROVISIONING is not suitable for production! <NUL>This device is NOT SECURE<NUL>
<NUL>[WRN] <NUL>This device was provisioned with dummy keys. <NUL>This device is NOT SECURE<NUL>
<NUL>[Sec Thread] Secure image initializing!
<NUL>TF-M isolation level is: <NUL>0x00000001
Booting TF-M v2.0.0
<NUL>Creating an empty ITS flash layout.
[INF][Crypto] Provisioning entropy seed... complete.
[DBG][Crypto] Initialising Mbed TLS 3.5.0 as PSA Crypto backend library... complete.
Non-Secure system starting...
Hello TF-M world
FW  version = 257
Testing psa get random number...
1: psa_generate_random() = 254
2: psa_generate_random() = 214
3: psa_generate_random() = 129
4: psa_generate_random() = 226
5: psa_generate_random() = 102
End of TF-M example App
^C
Stopping simulation...


Info: /OSCI/SystemC: Simulation stopped by user.
[warning ][main@0][1298 ns] Simulation stopped by user
```

Congratulations, you have built and run your first TF-M application !
