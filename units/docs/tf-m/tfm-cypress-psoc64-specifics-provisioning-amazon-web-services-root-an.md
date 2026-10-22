---
id: "tfm-cypress-psoc64-specifics-provisioning-amazon-web-services-root-an"
type: "concept"
domain: "security"
title: "Cypress PSoC64 Specifics: Provisioning Amazon Web Services root and device certificates"
summary: "Device running Amazon FreeRTOS and using Amazon Web Services (AWS) requires AWS root and unique device certificate signed with the device key for authentication. These certificates have to be provisioned into device. The process is the following:"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/platform/cypress/psoc64/cypress_psoc64_spec.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/platform/cypress/psoc64/cypress_psoc64_spec.html#provisioning-amazon-web-services-root-and-device-certificates"
license: "BSD-3-Clause"
mode: "V"
---

Device running Amazon FreeRTOS and using Amazon Web Services (AWS)
requires AWS root and unique device certificate signed with the device key
for authentication. These certificates have to be provisioned into device.
The process is the following:

1. If not done yet, change to the psoc64 security directory and initialize
   cysecuretools environment:

```bash

cd platform/ext/target/cypress/psoc64/security
cysecuretools -t cy8ckit-064s0s2-4343w init
```
2. Obtain and copy rootCA files to  "certificates" directory next to the policy
   directory (please refer to AWS documentation)

3. Switch the board in DAPLink mode by pressing the mode button or by issuing
   the following fw-loader command (fw-loader comes with Modus ToolBox software).
   Mode LED should be slowly blinking:

```bash

fw-loader --mode kp3-daplink
```
4. Run reprov_helper.py. If running the script with default parameters,
   the script can be run as is:

```bash

 python3 reprov_helper.py

Otherwise, run it with --help parameter to get the full list of options.
```
5. Confirm selected options. When prompted for a serial number, enter the board
   unique serial number (digits only, e.g. 00183).

6. Script will ask if you want to create new signing keys. Answer Yes to
   generate new signing keys in the keys directory, or No to retain and use the
   existing keys. After re-provisioning, from now on any images for
   this board will have to be signed with these keys.

7. The script will erase user images.
   Then the script will read device public key and create device certificates
   based on the board serial number, root certificate and the device public key.

--------------

*Copyright (c) 2017-2021, Arm Limited. All rights reserved.*

*Copyright (c) 2019-2020, Cypress Semiconductor Corporation. All rights reserved.*
