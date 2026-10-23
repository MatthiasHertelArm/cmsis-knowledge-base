---
id: "tfm-corstone-sse-315-with-ethos-u65-ex-to-run-the-example-code-on-corstone-315"
type: "concept"
domain: "security"
title: "Corstone SSE-315 with Ethos-U65 Example Subsystem for Ecosystem FVP: To run the example code on Corstone-315 Ethos-U65 Ecosystem FVP"
summary: "FVP is available to download here"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/platform/arm/mps4/corstone315/README.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/platform/arm/mps4/corstone315/.html#to-run-the-example-code-on-corstone-315-ethos-u65-ecosystem-fvp"
license: "BSD-3-Clause"
mode: "V"
---

FVP is available to download [here](https://developer.arm.com/Tools%20and%20Software/Fixed%20Virtual%20Platforms/IoT%20FVPs)

#. Install the FVP
#. Copy `bl1_1.bin`, `cm_provisioning_bundle.bin`, `dm_provisioning_bundle.bin`,
   `bl2_signed.bin` and `tfm_s_ns_signed.bin`  files from
   build dir to `<FVP installation path>/models/Linux64_GCC-6.4/`
#. Navigate to the same directory and execute the following command to start FVP::
```
$ ./FVP_Corstone_SSE-315 --data "bl1_1.bin"@0x11000000
               --data "cm_provisioning_bundle.bin"@0x12024000
               --data "dm_provisioning_bundle.bin"@0x1202aa00
               --data "bl2_signed.bin"@0x12031400
               --data "tfm_s_ns_signed.bin"@0x38000000
```
#. After completing the procedure you should be able to see similar messages
   to this on the serial port (baud 115200 8n1)::
```
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
[INF] Starting TF-M BL1_1
[INF] Beginning provisioning
[INF] TP mode set complete, system will now reset.
[INF] Starting TF-M BL1_1
[INF] Beginning provisioning
[INF] Waiting for CM provisioning bundle
[INF] Enabling secure provisioning mode, system will now reset.
[INF] Starting TF-M BL1_1
[INF] Beginning provisioning
[INF] Waiting for CM provisioning bundle
[INF] Running CM provisioning bundle
[INF] Starting TF-M BL1_1
[INF] Beginning provisioning
[INF] Waiting for DM provisioning bundle
[INF] Enabling secure provisioning mode, system will now reset.
[INF] Starting TF-M BL1_1
[INF] Beginning provisioning
[INF] Waiting for DM provisioning bundle
[INF] Running DM provisioning bundle
[INF] Starting TF-M BL1_1
[INF] Jumping to BL1_2
[INF] starting TF-M bl1_2
[INF] Attempting to boot image 0
[INF] BL2 image decrypted successfully
[INF] BL2 image validated successfully
[INF] Jumping to BL2
[INF] Starting bootloader
[INF] Image index: 1, Swap type: none
[INF] Image index: 0, Swap type: none
[INF] Bootloader chainload address offset: 0x0
[INF] Jumping to the first image slot
Booting TF-M v2.0.0+d09934721
Non-Secure system starting...
```

**Note:** Some of the messages above are only visible when `CMAKE_BUILD_TYPE` is set to `Debug`.

-------------

*Copyright (c) 2024-2025, Arm Limited. All rights reserved.*
