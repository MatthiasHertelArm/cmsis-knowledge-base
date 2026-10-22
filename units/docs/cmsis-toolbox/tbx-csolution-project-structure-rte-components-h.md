---
id: "tbx-csolution-project-structure-rte-components-h"
type: "concept"
domain: "project"
title: "CSolution Project Structure: Directory Structure / RTE_Components.h"
summary: "The file ./RTE/RTE_Components.h is created by the CMSIS Project Manager when the option --update-rte is used with cbuild setup or cbuild. For each selected software component, it contains #define statements required by the component."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/build-overview.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/#rte-components-h"
license: "Apache-2.0"
mode: "V"
---

_Part of: Directory Structure_

The file `./RTE/RTE_Components.h` is created by the CMSIS Project Manager when the option `--update-rte` is used with `cbuild setup` or `cbuild`. For each selected software component, it contains `#define` statements required by the component. These statements are defined in the `*.PDSC` file for that component. The following example shows a sample content of a RTE_Components.h file:

```c
/* Auto generated Run-Time-Environment Component Configuration File *** Do not modify ! *** */

#ifndef RTE_COMPONENTS_H
#define RTE_COMPONENTS_H

/* Define the Device Header File: */
#define CMSIS_device_header "stm32f10x.h"

#define RTE_Network_Interface_ETH_0     /* Network Interface ETH 0 */
#define RTE_Network_Socket_BSD          /* Network Socket BSD */
#define RTE_Network_Socket_TCP          /* Network Socket TCP */
#define RTE_Network_Socket_UDP          /* Network Socket UDP */

#endif /* RTE_COMPONENTS_H */
```

The `RTE_Components.h` file is typically used in other header files to control the inclusion of files related to other components of the same software pack.

```c
#include "RTE_Components.h"
#include  CMSIS_device_header

#ifdef  RTE_Network_Interface_ETH_0     // if component Network Interface ETH 0 is included
#include "Net_Config_ETH_0.h"           // add the related configuration file for this component
#endif
```
