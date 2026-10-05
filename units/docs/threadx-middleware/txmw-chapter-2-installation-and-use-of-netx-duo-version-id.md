---
id: "txmw-chapter-2-installation-and-use-of-netx-duo-version-id"
type: "concept"
domain: "rtos"
title: "Chapter 2 - Installation and Use of NetX Duo: NetX Duo Version ID"
summary: "The current version of NetX Duo is available to both the user and the application software during runtime. You can obtain the NetX Duo version from examination of the nx_port.h file."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter2.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter2.md#netx-duo-version-id"
license: "MIT"
mode: "V"
---

The current version of NetX Duo is available to both the user and the application software during runtime. You can obtain the NetX Duo version from examination of the **nx_port.h** file. In addition, this file also contains a version history of the corresponding port. Application software can obtain the NetX Duo version by examining the global string _***nx_version_id*** in ***nx_port.h***.

Application software can also obtain release information from the constants shown below defined in ***nx_api.h***.

These constants identify the current product release by name and the product major and minor version.

\#define EL_PRODUCT_NETXDUO  
\#define NETXDUO_MAJOR_VERSION  
\#define NETXDUO_MINOR_VERSION
