---
id: "tfm-corstone-sse-310-with-ethos-u55-u6-to-run-the-example-code-on-corstone-310"
type: "concept"
domain: "security"
title: "Corstone SSE-310 with Ethos-U55/U65 Example Subsystem for Arm Ecosystem FVP and for MPS3 (AN555): To run the example code on Corstone-310 Ethos-U55/U65 Ecosyste"
summary: "FVP is available to download here"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/platform/arm/mps3/corstone310/README.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/platform/arm/mps3/corstone310/.html#to-run-the-example-code-on-corstone-310-ethos-u55-u65-ecosystem-fvp"
license: "BSD-3-Clause"
mode: "V"
---

FVP is available to download [here](https://developer.arm.com/Tools%20and%20Software/Fixed%20Virtual%20Platforms/IoT%20FVPs)

#. Install the FVP
#. Copy `bl2.axf` and `tfm_s_ns_signed.bin` files from
   build dir to `<FVP installation path>/models/Linux64_GCC-9.3/`
#. Navigate to the same directory and execute the following command to start FVP::
```
$ ./FVP_Corstone_SSE-310 -a cpu0*="bl2.axf" --data "tfm_s_ns_signed.bin"@0x38000000
```
#. After completing the procedure you should be able to see similar messages
   to this on the serial port (baud 115200 8n1)::
```
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
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


**Note:** If `-DPLATFORM_DEFAULT_PROVISIONING=OFF` is set then the provisioning bundle has to be placed on the `0x11022000` address with:: $ ./FVP_Corstone_SSE-310 -a cpu0*="<path-to-build-directory>/bl2.axf" --data "<path-to-build-directory>/tfm_s_ns_signed.bin"@0x38000000 --data "<path-to-build-directory>/provisioning_bundle.bin"@0x11022000

-------------

*Copyright (c) 2021-2024, Arm Limited. All rights reserved.*
