---
id: "avh-arm-tools-artifactory-license-management"
type: "concept"
domain: "test"
title: "Arm Tools Artifactory: License management"
summary: "Arm FVPs, as well as other Arm Tools provided in the Arm Tools Artifactory, require an active Arm user-based license (UBL) for their operation."
status: "draft"
collection: "avh"
source: "ARM-software/AVH@bb8431b:DoxyGen/infrastructure/src/avh_artifactory.md"
doc_source: "https://github.com/ARM-software/AVH/blob/bb8431b/DoxyGen/infrastructure/src/avh_artifactory.md#license-management"
license: "Apache-2.0"
mode: "V"
---

Arm FVPs, as well as other Arm Tools provided in the Arm Tools Artifactory, require an active
[Arm user-based license (UBL)](https://developer.arm.com/Tools%20and%20Software/User-based%20Licensing) for their
operation.

Arm tools artifacts include the license management utility `armlm` that is used to
[activate and deactivate](https://developer.arm.com/documentation/102516/1-3/Activate-and-deactivate-your-product-license)
a UBL license in your environment.

For evaluation and non-commercial use you can activate an
[MDK-Community Edition](https://www.keil.arm.com/keil-mdk/#mdk-v6-editions) that also enables Arm FVPs. Use the
following command for that:

```sh
armlm activate -product KEMDK-COM0 -server https://mdk-preview.keil.arm.com
```

For commercial use, you need to obtain a license for
[MDK-Professional edition](https://www.keil.arm.com/keil-mdk/#mdk-v6-editions) or
[Arm Success Kit](https://www.arm.com/products/development-tools/success-kits).

> **Note**
> Your use of an Arm tool is subject to your acceptance of the End User License Agreement for Arm Software Development
> Tools, located within the `license_terms` folder of the downloaded archive. By installing and using the Arm tool, you
> agree to be bound by the terms and conditions of the end user license agreement.
