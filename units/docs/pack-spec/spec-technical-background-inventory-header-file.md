---
id: "spec-technical-background-inventory-header-file"
type: "concept"
domain: "pack"
title: "Technical background: Inventory header file"
summary: "Frequently, the behavior or features of a software component depend on the presence of other software components in the application. For example, a network stack can interface to Ethernet or serial PPP (UART)."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/pack_creation.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/cp_Packs.html"
license: "Apache-2.0"
mode: "V"
---

Frequently, the behavior or features of a software component depend on the presence of other software components in the
application. For example, a network stack can interface to Ethernet or serial PPP (UART). Depending on the presence of
interface components, the implementation may behave differently.

To simplify application configuration, the file **RTE_Components.h** is generated before the project build step. It contains
the inventory of all selected components. For each selected software component, it contains \#define statements that are
specified by the component meta data. The following example shows an RTE_Components.h file:

```c
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

Use this information in other header files to control features that depend on the inclusion to other software components. For
example:

```
#include "RTE_Components.h" 
#ifdef  RTE_Network_Interface_ETH_0  // if component is included 
#include "Net_Config_ETH_0.h"        // add related configuration file 
#endif
```
