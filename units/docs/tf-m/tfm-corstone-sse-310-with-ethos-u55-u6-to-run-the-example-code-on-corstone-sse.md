---
id: "tfm-corstone-sse-310-with-ethos-u55-u6-to-run-the-example-code-on-corstone-sse"
type: "concept"
domain: "security"
title: "Corstone SSE-310 with Ethos-U55/U65 Example Subsystem for Arm Ecosystem FVP and for MPS3 (AN555): To run the example code on Corstone SSE-310 with Ethos-U55/U65"
summary: "FPGA image is available to download here"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/platform/arm/mps3/corstone310/README.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/platform/arm/mps3/corstone310/.html#to-run-the-example-code-on-corstone-sse-310-with-ethos-u55-u65-example-subsystem"
license: "BSD-3-Clause"
mode: "V"
---

FPGA image is available to download [here](https://developer.arm.com/downloads/view/AN555?sortBy=availableBy&revision=r3p0-00rel0-1)

If the link above is not working just go to [Arm PDH](https://developer.arm.com/downloads) and search for AN555.

To run BL2 bootloader, TF-M example application and tests in the MPS3 board,
it is required to have AN555 image in the MPS3 board SD card. The image should
be located in `<MPS3 device name>/MB/HBI<BoardNumberBoardrevision>/AN555`

The MPS3 board tested is HBI0309C.

#. Execute the following command to create the tfm.bin binary
   which fills the entire available space on the MPS3 onboard QSPI.
   This way the whole flash content (PS, ITS, OTP, NV counters) is in a known state.
   (If anything left in the QSPI, this binary will overwrite it.)
   Also, MPS3 can only handle SFN 8.3 format, so the binary name must be shortened.::
```
```
   $ cd <build dir>/bin
   $ cp tfm_s_ns_signed.bin tfm.bin
   $ truncate -s 8M tfm.bin

#. Copy `bl2.bin` and `tfm.bin` files from
   build dir to `<MPS3 device name>/SOFTWARE/`
#. Open `<MPS3 device name>/MB/HBI0309C/AN555/images.txt`
#. Update the `images.txt` file as follows::
```
[IMAGES]
TOTALIMAGES: 2

IMAGE0ADDRESS: 0x01_00_1100_0000
IMAGE0UPDATE: RAM
IMAGE0FILE: \SOFTWARE\bl2.bin

IMAGE1ADDRESS: 0x01_00_0000_0000
IMAGE1UPDATE: FORCEQSPI
IMAGE1FILE: \SOFTWARE\tfm.bin
```
#. Close `<MPS3 device name>/MB/HBI0309C/AN555/images.txt`
#. Unmount/eject the `<MPS3 device name>` unit
#. Reset the board to execute the TF-M example application
#. After completing the procedure you should be able to visualize on the serial
   port (baud 115200 8n1) the following messages::
```
[INF] Starting bootloader
[INF] Beginning BL2 provisioning
[WRN] TFM_DUMMY_PROVISIONING is not suitable for production! This device is NOT SECURE
[INF] Image index: 1, Swap type: none
[INF] Image index: 0, Swap type: none
[INF] Bootloader chainload address offset: 0x0
[INF] Jumping to the first image slot
[INF] Beginning TF-M provisioning
[WRN] TFM_DUMMY_PROVISIONING is not suitable for production! This device is NOT SECURE
[WRN] This device was provisioned with dummy keys. This device is NOT SECURE
[Sec Thread] Secure image initializing!
TF-M isolation level is: 0x00000001
Booting TF-M v1.8.1
```

**Note:** Some of the messages above are only visible when `CMAKE_BUILD_TYPE` is set to `Debug`.


**Note:** If `-DPLATFORM_DEFAULT_PROVISIONING=OFF` is set then the provisioning bundle has to be placed on the `0x11022400` address by copying `provisioning_bundle.bin` and renaming it to `prv.bin`, then extending the images.txt with:: IMAGE2UPDATE: RAM IMAGE2ADDRESS: 0x01_00_1102_2400 IMAGE2FILE: \SOFTWARE\prv.bin
