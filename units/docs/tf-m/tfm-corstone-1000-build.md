---
id: "tfm-corstone-1000-build"
type: "concept"
domain: "security"
title: "Corstone-1000: Build"
summary: "The platform binaries are build using Yocto. Below is the user guide:"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/platform/arm/corstone1000/readme.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/platform/arm/corstone1000/.html#build"
license: "BSD-3-Clause"
mode: "V"
---

### Platform solution


The platform binaries are build using Yocto. Below is the user guide:

Arm Corstone-1000 User Guide



#### Building TF-M


Follow the instructions in Building instructions.



##### Build instructions for the FVP

`-DTFM_PLATFORM=arm/corstone1000 -DPLATFORM_IS_FVP=TRUE`


##### Build instructions for the FPGA

`-DTFM_PLATFORM=arm/corstone1000`


### Secure Test


This section can be used to test the secure enclave software independently from
the host. The below configuration builds the secure enclave binaries with regression test
frame integrated. On boot, secure enclave software stack is brought up, and
regression tests starts executing at the end of the initialization process. In the
below configuration, host software support is disabled, and meant only
to test/verify the secure enclave software.

Follow the instructions in Building instructions.

In the case of Corstone-1000 the build and run commands are the following.


#### FVP


- Download Corstone-1000 FVP from : Arm Ecosystem FVPs
- Install FVP by running the shell script.
- Running of the binary will boot secure enclave software stack and then the enabled
  regression tests from tf-m-tests are executed. (See Enabled tests)

```bash

cd <tf-m-tests-root>/tests_reg
cmake -S spe -B build_spe -DTFM_PLATFORM=arm/corstone1000 \
    -DCONFIG_TFM_SOURCE_PATH=<tf-m-root> \
    -DTFM_TOOLCHAIN_FILE=<tf-m-root>/toolchain_GNUARM.cmake \
    -DTEST_S=ON   \
    -DCMAKE_BUILD_TYPE=Debug  \
    -DTEST_PSA_API=OFF  \
    -DTEST_S_PS=OFF  \
    -DTEST_S_ITS=OFF  \
    -DTEST_S_IPC=OFF  \
    -DPLATFORM_IS_FVP=True
cmake --build build_spe -- install
dd conv=notrunc bs=1 if=build_spe/bin/bl1_1.bin of=build_spe/bin/bl1.bin seek=0
dd conv=notrunc bs=1 if=build_spe/bin/bl1_provisioning_bundle.bin of=build_spe/bin/bl1.bin seek=59208
./<tf-m-root>/platform/ext/target/arm/corstone1000/create-flash-image.sh build_spe/bin cs1000.bin

<path-to-FVP-installation>/models/Linux64_GCC-9.3/FVP_Corstone-1000 \
      -C se.trustedBootROMloader.fname="build_spe/bin/bl1.bin"  \
      -C board.flashloader0.fname="none"  \
      -C board.xnvm_size=64  \
      -C se.trustedSRAM_config=6  \
      -C se.BootROM_config="3"  \
      -C board.smsc_91c111.enabled=0  \
      -C board.hostbridge.userNetworking=true \
      --data board.flash0=build_spe/bin/cs1000.bin@0x68000000  \
      -C diagnostics=4  \
      -C disable_visualisation=true  \
      -C board.se_flash_size=8192  \
      -C se.secenc_terminal.start_telnet=1  \
      -C se.cryptocell.USER_OTP_FILTERING_DISABLE=1
```

**Note:** The nvm_image.bin has to be deleted in-between the FVP runs in order to start from a clean state.


#### FPGA


- Follow the above pointed platform user guide to setup the FPGA board.
- Use the BL1 generated from the below commands to place it inside FPGA board SD Card.
- Use the cs1000.bin created from the below commands to place it inside FPGA board SD Card.

```bash

cd <tf-m-tests-root>/tests_reg
cmake -S spe -B build_spe -DTFM_PLATFORM=arm/corstone1000 \
    -DCONFIG_TFM_SOURCE_PATH=<tf-m-root> \
    -DTFM_TOOLCHAIN_FILE=<tf-m-root>/toolchain_GNUARM.cmake \
    -DTEST_S=ON   \
    -DCMAKE_BUILD_TYPE=Debug  \
    -DTEST_PSA_API=OFF  \
    -DTEST_S_PS=OFF  \
    -DTEST_S_ITS=OFF  \
    -DTEST_S_IPC=OFF
cmake --build build_spe -- install
dd conv=notrunc bs=1 if=build_spe/bin/bl1_1.bin of=build_spe/bin/bl1.bin seek=0
dd conv=notrunc bs=1 if=build_spe/bin/bl1_provisioning_bundle.bin of=build_spe/bin/bl1.bin seek=59208
./<tf-m-root>/platform/ext/target/arm/corstone1000/create-flash-image.sh build_spe/bin cs1000.bin
cp build_spe/bin/bl1.bin <path-to-FPGA-SD-CARD>/SOFTWARE/
cp build_spe/bin/cs1000.bin <path-to-FPGA-SD-CARD>/SOFTWARE/
```

**Note:** .. _Enabled tests: Enabled Tests: Some of the regression tests have to be disabled as adding all of them would exceed the available RAM size. So there is a need to select few tests but not all. Other test configurations can be found in the
