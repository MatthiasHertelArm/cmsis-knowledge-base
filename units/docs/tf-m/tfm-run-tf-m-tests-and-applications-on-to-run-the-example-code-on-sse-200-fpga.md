---
id: "tfm-run-tf-m-tests-and-applications-on-to-run-the-example-code-on-sse-200-fpga"
type: "concept"
domain: "security"
title: "Run TF-M tests and applications on Arm platforms: Execute TF-M regression tests on MPS2 boards and FVP / To run the example code on SSE 200 FPGA on MPS2 board"
summary: "Part of: Execute TF-M regression tests on MPS2 boards and FVP"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/building/run_tfm_examples_on_arm_platforms.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/building/run_tfm_examples_on_arm_platforms.html#to-run-the-example-code-on-sse-200-fpga-on-mps2-board"
license: "BSD-3-Clause"
mode: "V"
---

_Part of: Execute TF-M regression tests on MPS2 boards and FVP_

FPGA image is available to download
[here](https://developer.arm.com/products/system-design/development-boards/cortex-m-prototyping-systems/mps2)

To run BL2 bootloader and TF-M example application and tests in the MPS2 board,
it is required to have SMM-SSE-200 for MPS2 (AN521) image in the MPS2 board SD
card. The image should be located in
`<MPS2 device name>/MB/HBI0263<board revision letter>/AN521`

The MPS2 board tested is HBI0263C referred also as MPS2+.


If you change the exe names, MPS2 expects file names in 8.3 format.

#### Example application

#. Copy `bl2.bin` and `tfm_s_ns_signed.bin` files from
   `<build_dir>/bin` to
   `<MPS2 device name>/SOFTWARE/`
#. Open `<MPS2 device name>/MB/HBI0263C/AN521/images.txt`
#. Update the `AN521/images.txt` file as follows::
```
TITLE: Versatile Express Images Configuration File
[IMAGES]
TOTALIMAGES: 2                     ;Number of Images (Max: 32)
IMAGE0ADDRESS: 0x10000000
IMAGE0FILE: \Software\bl2.bin  ; BL2 bootloader
IMAGE1ADDRESS: 0x10080000
IMAGE1FILE: \Software\tfm_s_ns_signed.bin ; TF-M example application binary blob
```
#. Close `<MPS2 device name>/MB/HBI0263C/AN521/images.txt`
#. Unmount/eject the `<MPS2 device name>` unit
#. Reset the board to execute the TF-M example application
#. After completing the procedure you should be able to visualize on the serial
   port (baud 115200 8n1) the following messages::
```
[INF] Starting bootloader
[INF] Image 0: magic=good, copy_done=0xff, image_ok=0xff
[INF] Scratch: magic=bad, copy_done=0x5, image_ok=0xcf
[INF] Boot source: primary slot
[INF] Swap type: none
[INF] Bootloader chainload address offset: 0x80000
[INF] Jumping to the first image slot
[Sec Thread] Secure image initializing!
```

#### Regression tests

After completing the procedure you should be able to visualize on the serial
port (baud 115200 8n1) the following messages::
```
[INF] Starting bootloader
[INF] Image 0: magic=good, copy_done=0xff, image_ok=0xff
[INF] Scratch: magic=bad, copy_done=0x5, image_ok=0xcf
[INF] Boot source: primary slot
[INF] Swap type: none
[INF] Bootloader chainload address offset: 0x80000
[INF] Jumping to the first image slot
[Sec Thread] Secure image initializing!

#### Execute test suites for the protected storage service ####
Running Test Suite PS secure interface tests (TFM_PS_TEST_2XXX)...

> Executing 'TFM_PS_TEST_2001'
  Description: 'Create interface'
  TEST PASSED!
> Executing 'TFM_PS_TEST_2002'
  Description: 'Get handle interface (DEPRECATED)'
This test is DEPRECATED and the test execution was SKIPPED
  TEST PASSED!
> Executing 'TFM_PS_TEST_2003'
  Description: 'Get handle with null handle pointer (DEPRECATED)'
This test is DEPRECATED and the test execution was SKIPPED
  TEST PASSED!
> Executing 'TFM_PS_TEST_2004'
  Description: 'Write interface'
  TEST PASSED!
> Executing 'TFM_PS_TEST_2005'
  Description: 'Read interface'
....
```

PS reliability tests take a few minutes to run on the MPS2.

#### Example application without BL2 bootloader

#. Copy `tfm_s.bin` and `tfm_ns.bin` files from
   `<build_dir>/bin` to
   `<MPS2 device name>/SOFTWARE/`
#. Open `<MPS2 device name>/MB/HBI0263C/AN521/images.txt`
#. Update the `AN521/images.txt` file as follows::
```
TITLE: Versatile Express Images Configuration File
[IMAGES]
TOTALIMAGES: 2                   ;Number of Images (Max: 32)
IMAGE0ADDRESS: 0x10000000
IMAGE0FILE: \Software\tfm_s.bin  ; Secure code
IMAGE1ADDRESS: 0x00100000
IMAGE1FILE: \Software\tfm_ns.bin ; Non-secure code
```
#. Close `<MPS2 device name>/MB/HBI0263C/AN521/images.txt`
#. Unmount/eject the `<MPS2 device name>` unit
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

#### Execute test suites for the protected storage service ####
Running Test Suite PS secure interface tests (TFM_PS_TEST_2XXX)...

> Executing 'TFM_PS_TEST_2001'
  Description: 'Create interface'
  TEST PASSED!
> Executing 'TFM_PS_TEST_2002'
  Description: 'Get handle interface (DEPRECATED)'
This test is DEPRECATED and the test execution was SKIPPED
  TEST PASSED!
> Executing 'TFM_PS_TEST_2003'
  Description: 'Get handle with null handle pointer (DEPRECATED)'
This test is DEPRECATED and the test execution was SKIPPED
  TEST PASSED!
> Executing 'TFM_PS_TEST_2004'
  Description: 'Write interface'
  TEST PASSED!
> Executing 'TFM_PS_TEST_2005'
  Description: 'Read interface'
....

## Execute TF-M regression tests on Musca test chip boards


Before executing any images on Musca-B1 board, please check the
to have the correct setup.

Install SRecord for Musca test chip boards:

- Windows: [SRecord v1.63](https://sourceforge.net/projects/srecord/)
- Linux: `sudo apt-get install -y srecord`

### Example application with BL2 bootloader


#. Create a unified hex file comprising of both `bl2.bin` and
   `tfm_s_ns_signed.bin` for Musca-B1 platforms::
```
srec_cat bin/bl2.bin -Binary -offset 0xA000000 bin/tfm_s_ns_signed.bin -Binary -offset 0xA020000 -o tfm.hex -Intel
```
#. Power up the Musca board by connecting it to a computer with a USB lead.
   Press the `PBON` button if the green `ON` LED does not immediately turn
   on. The board should appear as a USB drive.
#. Copy `tfm.hex` to the USB drive. The orange `PWR` LED should start
   blinking.
#. Once the `PWR` LED stops blinking, power cycle or reset the board to boot
   from the new image.
#. After completing the procedure you should see the following messages on the
   DAPLink UART (baud 115200 8n1)::
```
[INF] Starting bootloader
[INF] Image 0: magic=good, copy_done=0xff, image_ok=0xff
[INF] Scratch: magic=bad, copy_done=0x5, image_ok=0xd9
[INF] Boot source: primary slot
[INF] Swap type: none
[INF] Bootloader chainload address offset: 0x20000
[INF] Jumping to the first image slot
[Sec Thread] Secure image initializing!
```

### Regression tests with BL2 bootloader


**Note:** As the Internal Trusted Storage and Protected Storage tests use persistent storage, it is recommended to erase the storage area before running the tests. Existing data may prevent the tests from running to completion if, for example, there is not enough free space for the test data or the UIDs used by the tests have already been created with the write-once flag set. Repeated test runs can be done without erasing between runs. To erase the storage when flashing an image, `-fill 0xFF <start_addr> <end_addr>` can be added to the `srec_cat` command used to create the combined hex file. The `<start_addr>` and `<end_addr>` are the start and end addresses of the storage area, found in the board's `flash_layout.h` file. The board's flash can also be erased via a debugger; see your IDE's documentation for instructions.

After completing the procedure you should see the following messages on the
DAPLink UART (baud 115200 8n1)::
```
[INF] Starting bootloader
[INF] Image 0: magic=good, copy_done=0xff, image_ok=0xff
[INF] Scratch: magic=bad, copy_done=0x5, image_ok=0x9
[INF] Boot source: primary slot
[INF] Swap type: none
[INF] Bootloader chainload address offset: 0x20000
[INF] Jumping to the first image slot
[Sec Thread] Secure image initializing!

#### Execute test suites for the protected storage service ####
Running Test Suite PS secure interface tests (TFM_PS_TEST_2XXX)...
> Executing 'TFM_PS_TEST_2001'
  Description: 'Create interface'
  TEST PASSED!
> Executing 'TFM_PS_TEST_2002'
  Description: 'Get handle interface (DEPRECATED)'
This test is DEPRECATED and the test execution was SKIPPED
  TEST PASSED!
> Executing 'TFM_PS_TEST_2003'
  Description: 'Get handle with null handle pointer (DEPRECATED)'
This test is DEPRECATED and the test execution was SKIPPED
  TEST PASSED!
> Executing 'TFM_PS_TEST_2004'
  Description: 'Get attributes interface'
  TEST PASSED!
> Executing 'TFM_PS_TEST_2005'
  Description: 'Get attributes with null attributes struct pointer'
....
```

### PSA API tests

Follow the build instructions for the PSA API tests and then follow the above
procedures for flashing the image to the board. The PSA API tests are linked
into the TF-M binaries and will automatically run. A log similar to the
following should be visible on the UART; it is normal for some tests to be
skipped but there should be no failed tests::
```
[Sec Thread] Secure image initializing!
Booting TFM v1.1
Non-Secure system starting...

***** PSA Architecture Test Suite - Version 1.0 *****

Running.. Storage Suite
******************************************

TEST: 401 | DESCRIPTION: UID not found check
[Info] Executing tests from non-secure

[Info] Executing ITS tests
[Check 1] Call get API for UID 6 which is not set
[Check 2] Call get_info API for UID 6 which is not set
[Check 3] Call remove API for UID 6 which is not set
[Check 4] Call get API for UID 6 which is removed
[Check 5] Call get_info API for UID 6 which is removed
[Check 6] Call remove API for UID 6 which is removed
[Check 7] Call get API for different UID 5
[Check 8] Call get_info API for different UID 5
[Check 9] Call remove API for different UID 5

[Info] Executing PS tests
[Check 1] Call get API for UID 6 which is not set
[Check 2] Call get_info API for UID 6 which is not set
[Check 3] Call remove API for UID 6 which is not set
[Check 4] Call get API for UID 6 which is removed
[Check 5] Call get_info API for UID 6 which is removed
[Check 6] Call remove API for UID 6 which is removed
[Check 7] Call get API for different UID 5
[Check 8] Call get_info API for different UID 5
[Check 9] Call remove API for different UID 5

TEST RESULT: PASSED

******************************************

<further tests removed from log for brevity>

************ Storage Suite Report **********
TOTAL TESTS     : 17
TOTAL PASSED    : 11
TOTAL SIM ERROR : 0
TOTAL FAILED    : 0
TOTAL SKIPPED   : 6
******************************************
```

**Note:** The Internal Trusted Storage and Protected Storage flash areas must be wiped before running the Storage test suites. Many IDEs for embedded development (such as Keil µVision) offer a function to erase a device's flash. Refer to your IDE's documentation for instructions. Another way this can be achieved is by using `srec_cat` with the `-fill` parameter to fill the corresponding area in the binary with the erase value of the flash (`0xFF`). Refer to the platform flash layout for appropriate addresses to erase on other platforms. This step is not required on targets that emulate flash storage in RAM, as it will be erased each time the device is reset. Note, however, that a warm reset may not clear SRAM contents, so it may be necessary to power the device off and on again between test runs.


### Example application or regression tests on Musca-B1 without BL2 bootloader


Follow the above procedures, but create a unified hex file out of `tfm_s.bin`
and `tfm_ns.bin`:

- Windows::
```
srec_cat.exe bin\tfm_s.bin -Binary -offset 0xA000000 bin\tfm_ns.bin -Binary -offset 0xA080000 -o tfm.hex -Intel
```
- Linux::
```
srec_cat bin/tfm_s.bin -Binary -offset 0xA000000 bin/tfm_ns.bin -Binary -offset 0xA080000 -o tfm.hex -Intel
