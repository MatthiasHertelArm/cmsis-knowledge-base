---
id: "tfm-details-for-the-platform-folder-interfacing-with-tf-m"
type: "concept"
domain: "security"
title: "Details for the platform folder: Interfacing with TF-M"
summary: "This file should enumerate the hardware peripherals that are available for TF-M on the platform. The name of the peripheral used by a service is set in its manifest file."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/integration_guide/source_structure/platform_folder.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/source_structure/platform_folder.html#interfacing-with-tf-m"
license: "BSD-3-Clause"
mode: "V"
---

### platform/ext/target/tfm_peripherals_def.h

This file should enumerate the hardware peripherals that are available for TF-M
on the platform. The name of the peripheral used by a service is set in its
manifest file. The platform have to provide a macro for each of the provided
peripherals, that is substituted to a pointer to type
`struct platform_data_t`. The memory that the pointer points
to is allocated by the platform code. The pointer gets stored in the partitions
database in SPM, and it is provided to the SPM HAL functions.


#### Peripherals currently used by the services in TF-M

- `TFM_PERIPHERAL_UART1`-  UART1


If a platform doesn't support a peripheral, that is used by a service, then
the service cannot be used on the given platform. Using a peripheral in
TF-M that is not supported by the platform results in compile error.

### platform/include/tfm_spm_hal.h

This file contains the declarations of functions that a platform implementation
has to provide for TF-M's SPM. For details see the comments in the file.


### platform/include/tfm_platform_system.h

This file contains the declarations of functions that a platform implementation
has to provide for TF-M's Platform Service. For details see
`docs/user_guides/services/tfm_platform_integration_guide.rst`
