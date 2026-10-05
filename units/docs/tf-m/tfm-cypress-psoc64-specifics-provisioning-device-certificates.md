---
id: "tfm-cypress-psoc64-specifics-provisioning-device-certificates"
type: "concept"
domain: "security"
title: "Cypress PSoC64 Specifics: Provisioning device certificates"
summary: "2. Create and copy rootCA files to \"certificates\" directory next to the policy directory (please refer to documentation of the used OS)"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/platform/cypress/psoc64/cypress_psoc64_spec.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/platform/cypress/psoc64/cypress_psoc64_spec.html#provisioning-device-certificates"
license: "BSD-3-Clause"
mode: "V"
---

1. If not done yet, change to the psoc64 security directory and initialize
   cysecuretools environment:

```bash

cd platform/ext/target/cypress/psoc64/security
cysecuretools -t cy8ckit-064s0s2-4343w init
```
2. Create and copy rootCA files to "certificates" directory next to the policy
   directory (please refer to documentation of the used OS)

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
