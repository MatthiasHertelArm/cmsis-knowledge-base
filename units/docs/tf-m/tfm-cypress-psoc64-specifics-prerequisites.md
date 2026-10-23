---
id: "tfm-cypress-psoc64-specifics-prerequisites"
type: "concept"
domain: "security"
title: "Cypress PSoC64 Specifics: Prerequisites"
summary: "PSoC64 must first be provisioned with SecureBoot firmware and a provisioning packet containing policy and secure keys. Please refer to the guide at https://www.infineon.com/dgdl/Infineon-PSoC_64_Secure_MCU_Secure_Boot_SDK_User_Guide-Software-v07_00-EN.pdf?fileId=8ac78c8c7d0d8da4017d0f8c361a7666 Use the following policy file for provisioning and signing: policy_multi_CM0_CM4_tfm.json"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/platform/cypress/psoc64/cypress_psoc64_spec.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/platform/cypress/psoc64/cypress_psoc64_spec.html#prerequisites"
license: "BSD-3-Clause"
mode: "V"
---

PSoC64 must first be provisioned with SecureBoot firmware and a provisioning packet
containing policy and secure keys. Please refer to the guide at
https://www.infineon.com/dgdl/Infineon-PSoC_64_Secure_MCU_Secure_Boot_SDK_User_Guide-Software-v07_00-EN.pdf?fileId=8ac78c8c7d0d8da4017d0f8c361a7666
Use the following policy file for provisioning and signing:
policy_multi_CM0_CM4_tfm.json

Please make sure you have all required software installed as explained in the
TF-M getting started.

Please also make sure that all the source code are fetched by following
general building instruction.

Install CySecureTools or update it to the newest version (2.0.0 at the time of
writing)

```bash

pip3 install --upgrade --force-reinstall cysecuretools
```
PyOCD is installed by CySecureTools as a dependency.

For more details please refer to
[CySecureTools](https://pypi.org/project/cysecuretools) page.

Install OpenOCD with PSoC6 support. Download the latest revision 4.1.0
or newer from:
https://github.com/openocd-org/openocd/releases

Lastly, the PSoC64 board KitProg firmware needs to be 2.00.744 or greater.
Please use Cypress Modus Toolbox or CyProgrammer to update it if needed.
