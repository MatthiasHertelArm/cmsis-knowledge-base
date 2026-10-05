---
id: "tfm-run-tf-m-tests-and-applications-on-execute-tf-m-example-and-regression-test"
type: "concept"
domain: "security"
title: "Run TF-M tests and applications on Arm platforms: Execute TF-M example and regression tests on MPS3 boards"
summary: "FPGA image is available to download here"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/building/run_tfm_examples_on_arm_platforms.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/building/run_tfm_examples_on_arm_platforms.html#execute-tf-m-example-and-regression-tests-on-mps3-boards"
license: "BSD-3-Clause"
mode: "V"
---

### To run the example code on CoreLink SSE-200 Subsystem for MPS3 (AN524)

FPGA image is available to download [here](https://www.arm.com/products/development-tools/development-boards/mps3)

To run BL2 bootloader and TF-M example application and tests in the MPS3 board,
it is required to have SMM-SSE-200 for MPS3 (AN524) image in the MPS3 board
SD card. The image should be located in
`<MPS3 device name>/MB/HBI<BoardNumberBoardrevision>/AN524`

And the current boot memory for AN524 is QSPI flash, so you need to set the
correct REMAP option in
`<MPS3 device name>/MB/HBI<BoardNumberBoardrevision>/AN524/an524_v1.txt`

:
```
REMAP: QSPI                 ;REMAP boot device BRAM/QSPI.  Must match REMAPVAL below.
REMAPVAL: 1                 ;REMAP register value e.g. 0-BRAM. 1-QSPI
```
The MPS3 board tested is HBI0309B.

If you change the exe names, MPS3 expects file names in 8.3 format.

#### Example application

#. Copy `bl2.bin` and `tfm_s_ns_signed.bin` files from
   build dir to `<MPS3 device name>/SOFTWARE/`
#. Open `<MPS3 device name>/MB/HBI0309B/AN524/images.txt`
#. Update the `images.txt` file as follows::
```
TITLE: Arm MPS3 FPGA prototyping board Images Configuration File

[IMAGES]
TOTALIMAGES: 2                     ;Number of Images (Max: 32)

IMAGE0UPDATE: AUTO                 ;Image Update:NONE/AUTO/FORCE
IMAGE0ADDRESS: 0x00000000          ;Please select the required executable program
IMAGE0FILE: \SOFTWARE\bl2.bin
IMAGE1UPDATE: AUTO
IMAGE1ADDRESS: 0x00040000
IMAGE1FILE: \SOFTWARE\tfm_s_ns_signed.bin
```
#. Close `<MPS3 device name>/MB/HBI0309B/AN524/images.txt`
#. Unmount/eject the `<MPS3 device name>` unit
#. Reset the board to execute the TF-M example application
#. After completing the procedure you should be able to visualize on the serial
   port (baud 115200 8n1) the following messages::
```
[INF] Starting bootloader
[INF] Image 0: magic= good, copy_done=0xff, image_ok=0xff
[INF] Scratch: magic=unset, copy_done=0x43, image_ok=0xff
[INF] Boot source: slot 0
[INF] Swap type: none
[INF] Bootloader chainload address offset: 0x40000
[INF] Jumping to the first image slot
[Sec Thread] Secure image initializing!
```

**Note:** If `-DPLATFORM_DEFAULT_PROVISIONING=OFF` is set then the provisioning bundle has to be placed on the `0x001CB000` address.


#### Regression tests

After completing the procedure you should be able to visualize on the serial
port (baud 115200 8n1) the following messages::
```
[INF] Starting bootloader
[INF] Image 0: magic= good, copy_done=0xff, image_ok=0xff
[INF] Scratch: magic=unset, copy_done=0x9, image_ok=0xff
[INF] Boot source: slot 0
[INF] Swap type: none
[INF] Bootloader chainload address offset: 0x40000
[INF] Jumping to the first image slot
[Sec Thread] Secure image initializing!

#### Execute test suites for the Secure area ####
Running Test Suite PSA protected storage S interface tests (TFM_PS_TEST_2XXX)...
> Executing 'TFM_PS_TEST_2001'
  Description: 'Set interface'
  TEST PASSED!
> Executing 'TFM_PS_TEST_2002'
  Description: 'Set interface with create flags'
  TEST PASSED!
> Executing 'TFM_PS_TEST_2003'
  Description: 'Set interface with NULL data pointer'
  TEST PASSED!
> Executing 'TFM_PS_TEST_2004'
  Description: 'Set interface with invalid data length'
  TEST PASSED!
....
```
Some of the attestation tests take a few minutes to run on the MPS3.

#### Example application without BL2 bootloader

#. Copy `tfm_s.bin` and `tfm_ns.bin` files from
   build dir to `<MPS3 device name>/SOFTWARE/`
#. Open `<MPS3 device name>/MB/HBI0309B/AN524/images.txt`
#. Update the `images.txt` file as follows::
```
TITLE: Arm MPS3 FPGA prototyping board Images Configuration File

[IMAGES]
TOTALIMAGES: 2                     ;Number of Images (Max: 32)

IMAGE0UPDATE: AUTO                 ;Image Update:NONE/AUTO/FORCE
IMAGE0ADDRESS: 0x00000000          ;Please select the required executable program
IMAGE0FILE: \SOFTWARE\tfm_s.bin
IMAGE1UPDATE: AUTO
IMAGE1ADDRESS: 0x000C0000
IMAGE1FILE: \SOFTWARE\tfm_ns.bin
```
#. Close `<MPS3 device name>/MB/HBI0309B/AN521/images.txt`
#. Unmount/eject the `<MPS3 device name>` unit
#. Reset the board to execute the TF-M example application
#. After completing the procedure you should be able to visualize on the serial
   port (baud 115200 8n1) the following messages::
```
[Sec Thread] Secure image initializing!
```

#### Regression tests without BL2 bootloader

After completing the procedure you should be able to visualize on the serial
port (baud 115200 8n1) the following messages::
```
[Sec Thread] Secure image initializing!

#### Execute test suites for the Secure area ####
Running Test Suite PSA protected storage S interface tests (TFM_PS_TEST_2XXX)...
> Executing 'TFM_PS_TEST_2001'
  Description: 'Set interface'
  TEST PASSED!
> Executing 'TFM_PS_TEST_2002'
  Description: 'Set interface with create flags'
  TEST PASSED!
> Executing 'TFM_PS_TEST_2003'
  Description: 'Set interface with NULL data pointer'
  TEST PASSED!
> Executing 'TFM_PS_TEST_2004'
  Description: 'Set interface with invalid data length'
  TEST PASSED!
....
```

### Firmware upgrade and image validation with BL2 bootloader

High level operation of BL2 bootloader and instructions for testing firmware
upgrade is described in secure boot.

--------------

*Copyright (c) 2017-2024, Arm Limited. All rights reserved.*
