---
id: "tfm-cypress-psoc64-specifics-building-multi-core-tf-m-on-cypress-psoc"
type: "concept"
domain: "security"
title: "Cypress PSoC64 Specifics: Building Multi-Core TF-M on Cypress PSoC64"
summary: "The build configuration for TF-M is provided to the build system using command line arguments. Required arguments are noted below."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/platform/cypress/psoc64/cypress_psoc64_spec.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/platform/cypress/psoc64/cypress_psoc64_spec.html#building-multi-core-tf-m-on-cypress-psoc64"
license: "BSD-3-Clause"
mode: "V"
---

### Configuring the build


The build configuration for TF-M is provided to the build system using command
line arguments. Required arguments are noted below.

   * - -DTFM_PLATFORM=cypress/psoc64
     - Specifies target platform name `psoc64`

   * - -DTFM_TOOLCHAIN_FILE=<path to toolchain file>
     - Specifies the compiler toolchain
       The possible values are:

         - `<TFM root dir>/toolchain_ARMCLANG.cmake`
         - `<TFM root dir>/toolchain_GNUARM.cmake`
         - `<TFM root dir>/toolchain_IARARM.cmake`

see tfm_cmake_configuration for
more information.


### Build Instructions


The following instructions build multi-core TF-M without regression test suites
in Isolation Level 1 on Linux.
Both the compiler and the debugging type can be changed to other configurations
listed above.

```bash

cd <TF-M base folder>
cd <trusted-firmware-m folder>

mkdir <build folder>
pushd <build folder>
cmake -DTFM_PLATFORM=cypress/psoc64 \
      -DTFM_TOOLCHAIN_FILE=../toolchain_ARMCLANG.cmake \
      ../
popd
cmake --build <build folder> -- -j VERBOSE=1
```
The following instructions build multi-core TF-M with regression test suites
in Isolation Level 1 on Linux.
Both the compiler and the debugging type can be changed to other configurations
listed above.

```bash

cd <TF-M base folder>
cd <trusted-firmware-m folder>

mkdir <build folder>
pushd <build folder>
cmake -DTFM_PLATFORM=cypress/psoc64 \
      -DTFM_TOOLCHAIN_FILE=../toolchain_ARMCLANG.cmake \
      -DTEST_S=ON -DTEST_NS=ON \
      ../
popd
cmake --build <build folder> -- -j VERBOSE=1
```
The following instructions build multi-core TF-M with PSA API test suite for
the attestation service in Isolation Level 1 on Linux.
Both the compiler and the debugging type can be changed to other configurations
listed above.

```bash

cd <TF-M base folder>
cd <trusted-firmware-m folder>

mkdir <build folder>
pushd <build folder>
cmake -DTFM_PLATFORM=cypress/psoc64 \
      -DTFM_TOOLCHAIN_FILE=../toolchain_ARMCLANG.cmake \
      -DTEST_PSA_API=INITIAL_ATTESTATION \
      ../
popd
cmake --build <build folder> -- -j VERBOSE=1
```
The following instructions build multi-core TF-M without regression test suites
in Isolation Level 2 on Linux.
Both the compiler and the debugging type can be changed to other configurations
listed above.

```bash

cd <TF-M base folder>
cd <trusted-firmware-m folder>

mkdir <build folder>
pushd <build folder>
cmake -DTFM_PLATFORM=cypress/psoc64 \
      -DTFM_TOOLCHAIN_FILE=../toolchain_ARMCLANG.cmake \
      -DTFM_ISOLATION_LEVEL=2 \
      ../
popd
cmake --build <build folder> -- -j VERBOSE=1
```
The following instructions build multi-core TF-M with regression test suites
in Isolation Level 2 on Linux.
Both the compiler and the debugging type can be changed to other configurations
listed above.

```bash

cd <TF-M base folder>
cd <trusted-firmware-m folder>

mkdir <build folder>
pushd <build folder>
cmake -DTFM_PLATFORM=cypress/psoc64 \
      -DTFM_TOOLCHAIN_FILE=../toolchain_ARMCLANG.cmake \
      -DTFM_ISOLATION_LEVEL=2 \
      -DTEST_S=ON -DTEST_NS=ON \
      ../
popd
cmake --build <build folder> -- -j VERBOSE=1
```
The following instructions build multi-core TF-M with PSA API test suite for
the protected storage service in Isolation Level 2 on Linux.
Both the compiler and the debugging type can be changed to other configurations
listed above.

```bash

cd <TF-M base folder>
cd <trusted-firmware-m folder>

mkdir <build folder>
pushd <build folder>
cmake -DTFM_PLATFORM=cypress/psoc64 \
      -DTFM_TOOLCHAIN_FILE=../toolchain_ARMCLANG.cmake \
      -DTFM_ISOLATION_LEVEL=2 \
      -DTEST_PSA_API=PROTECTED_STORAGE \
      ../
popd
cmake --build <build folder> -- -j VERBOSE=1

## Signing



### Signing keys


Copy secure keys used in the board provisioning process to
platform/ext/target/cypress/psoc64/security/keys:

The keys included in the repository are for reference and development only.
DO NOT USE THESE KEYS IN ANY ACTUAL DEPLOYMENT!

Note: provisioned board in SECURE state is required, otherwise refer to
Cypress documentation for details on the provisioning process.
https://www.infineon.com/dgdl/Infineon-PSoC_64_Secure_MCU_Secure_Boot_SDK_User_Guide-Software-v07_00-EN.pdf?fileId=8ac78c8c7d0d8da4017d0f8c361a7666

If the board was previously provisioned with signing keys and policy, copy
secure signing keys used in the board provisioning process to
platform/ext/target/cypress/psoc64/security/keys:

TFM_S_KEY.json
  Private OEM key for signing CM0P image

TFM_S_KEY_PRIV.pem
  Private OEM key for signing CM0P image in PEM format

TFM_NS_KEY.json
  Private OEM key for signing CM4 image

TFM_NS_KEY_PRIV.pem
  Private OEM key for signing CM4 image in PEM format

Alternatively, you can generate a new set of signing keys using cysecuretools
create-keys command and provision the keys to the board, if the previously
provisioned policy allows board's re-provisioning.

Initialize cysecuretools environment:

```bash

cd platform/ext/target/cypress/psoc64/security
cysecuretools -t cy8ckit-064s0s2-4343w init
```
Generate a new set of keys:

```bash

cysecuretools -t cy8ckit-064s0s2-4343w -p policy/policy_multi_CM0_CM4_tfm.json create-keys
```
Re-provision the new keys to the board:

```bash

cysecuretools -t cy8ckit-064s0s2-4343w -p policy/policy_multi_CM0_CM4_tfm.json re-provision-device
```

### Signing the images


Sign the images using CySecureTools CLI tool.
Note: the tool overwrites unsigned file with a signed one, it also creates an
unsigned copy <filename>_unsigned.hex.

SPE image:

```bash

cysecuretools \
--policy platform/ext/target/cypress/psoc64/security/policy/policy_multi_CM0_CM4_tfm.json \
--target cy8ckit-064s0s2-4343w \
sign-image \
--hex <build folder>/bin/tfm_s.hex \
--image-type BOOT \
--image-id 1
```
NSPE image:

```bash

cysecuretools \
--policy platform/ext/target/cypress/psoc64/security/policy/policy_multi_CM0_CM4_tfm.json \
--target cy8ckit-064s0s2-4343w \
sign-image \
--hex <build folder>/bin/tfm_ns.hex \
--image-type BOOT \
--image-id 16
```
* CySecureTools sign-image overwrites unsigned file with a signed one,
  also it creates an unsigned copy _unsigned.hex.

* image-type option: "--image-type BOOT" creates a signed hex file with offsets
  for the primary image slot. Use "--image-type UPGRADE" if you want to create
  an image for the secondary "upgrade" slot.
  When booting, CyBootloader will validate image in the secondary slot and copy
  it to the primary boot slot.

* image-id option: Each image has its own ID. By default, SPE image running on
  CM0P core has ID=1, NSPE image running on CM4 core has ID=16. Refer to the
  policy file for the actual ID's.



## Programming the Device


After building and signing, the TFM images must be programmed into flash
memory on the PSoC64 device. There are three methods to program it.


### DAPLink mode


Using KitProg3 mode button, switch it to DAPLink mode.
Mode LED should start blinking rapidly and depending on the host computer
settings DAPLINK will be mounted as a media storage device.
Otherwise, mount it manually.

Copy tfm hex files one by one to the DAPLINK device:

```bash

cp <build folder>/bin/tfm_ns.hex <mount point>/DAPLINK/; sync
cp <build folder>/bin/tfm_s.hex <mount point>/DAPLINK/; sync
```

### OpenOCD


Using KitProg3 mode button, switch to KitProg3 CMSIS-DAP BULK. Status LED
should be ON and not blinking for CMSIS-DAP BULK.

Before programming the images, erase PS partition if needed.
This will clear all data and force PS to reformat partition.

```bash

${OPENOCD_PATH}/bin/openocd \
        -s ${OPENOCD_PATH}/scripts \
        -f interface/kitprog3.cfg \
        -f target/psoc6_2m_secure.cfg \
        -c "init; reset init" \
        -c "flash erase_address 0x101c0000 0x10000" \
        -c "shutdown"
```
Note that the `0x101C0000` in the command above must match the PS start
address of the secure primary image specified in the file:

    platform/ext/target/cypress/psoc64/partition/flash_layout.h

so be sure to change it if you change that file.

To program the signed tfm_s and tfm_ns images to the device with openocd
(assuming OPENOCD_PATH is pointing at the openocd installation directory)
run the following commands:

```bash

OPENOCD_PATH=<cyprogrammer dir>/openocd
BUILD_DIR=<build folder>

${OPENOCD_PATH}/bin/openocd \
        -s ${OPENOCD_PATH}/scripts \
        -f interface/kitprog3.cfg \
        -f target/psoc6_2m_secure.cfg \
        -c "init; reset init" \
        -c "flash write_image erase ${BUILD_DIR}/bin/tfm_s.hex" \
        -c "shutdown"

${OPENOCD_PATH}/bin/openocd \
        -s ${OPENOCD_PATH}/scripts \
        -f interface/kitprog3.cfg \
        -f target/psoc6_2m_secure.cfg \
        -c "init; reset init" \
        -c "flash write_image erase ${BUILD_DIR}/bin/tfm_ns.hex" \
        -c "reset run"
```

### PyOCD


PyOCD is installed by CySecureTools automatically. It can be used
to program TFM images into the board.

Using KitProg3 mode button, switch to KitProg3 DAPLink mode.
Mode LED should start blinking rapidly.

Optionally, erase PS partition:

```bash

pyocd erase -b CY8CKIT-064S0S2-4343W -s 0x101c0000+0x10000
```
To program the signed tfm_s and tfm_ns images to the device with pyocd
run the following commands:

```bash

pyocd flash -b CY8CKIT-064S0S2-4343W ${BUILD_DIR}/bin/tfm_s.hex

pyocd flash -b CY8CKIT-064S0S2-4343W ${BUILD_DIR}/bin/tfm_ns.hex
