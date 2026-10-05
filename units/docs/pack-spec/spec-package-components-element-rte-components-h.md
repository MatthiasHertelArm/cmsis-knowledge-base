---
id: "spec-package-components-element-rte-components-h"
type: "concept"
domain: "pack"
title: "/package/components element: RTE_Components.h"
summary: "The build environment should generate a C/C++ include file with the name RTE_Components.h that contains: - The statements of the related <RTE_Components_h> element for all selected software components."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/components_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html"
license: "Apache-2.0"
mode: "V"
---

The build environment should generate a C/C++ include file with the name **RTE_Components.h** that contains:
  - The statements of the related `<RTE_Components_h>` element for all selected software components.
  - The header file name specified in the `<compile>` element of the pdsc_devices_pg.

**Example**

The following example shows a sample content of a file **RTE_Components.h**.
It contains the statements that are specified with the element **RTE_Components_h** of four software components.

```
/*
Auto generated Run-Time-Environment Component Configuration File
     *** Do not modify ! ***
/

#ifndef RTE_COMPONENTS_H
#define RTE_COMPONENTS_H

/*
Define the Device Header File:
/
#define CMSIS_device_header "stm32f10x.h"

#define RTE_Network_Interface_ETH_0     /* Network Interface ETH 0 */
#define RTE_Network_Socket_BSD          /* Network Socket BSD */
#define RTE_Network_Socket_TCP          /* Network Socket TCP */
#define RTE_Network_Socket_UDP          /* Network Socket UDP */

#endif /* RTE_COMPONENTS_H */
```

The **RTE_Components.h** file allows to create software that works with any supported device as it gives access to the
**CMSIS_device_header.**  The **CMSIS_device_header** reflects the current selected device and gives you for example access
to the processor configuration.  Refer to **"Device Header File `<device.h>`"** in **CMSIS-Core(M)**
or **CMSIS-Core(A)** for more information.

```
#include CMSIS_device_header            /* header file of the selected device in the project */

#if (defined (__MPU_PRESENT)) && (__MPU_PRESENT == 1)
  // device has MPU, start the related code
#else
  #error "Software Component requires a device with MPU"
#endif
```

**Note:** __MPU_PRESENT must not be used for non-Arm MPUs!

Another typical usage of the **RTE_Components.h** file is in header files to control for example the inclusion of files
that are related to other components for the same Software Pack.

```
#include "RTE_Components.h"

#ifdef  RTE_Network_Interface_ETH_0    // generated when software component Network Interface ETH 0 is included
#include "Net_Config_ETH_0.h"          // add the related configuration file for these component
#endif
```
