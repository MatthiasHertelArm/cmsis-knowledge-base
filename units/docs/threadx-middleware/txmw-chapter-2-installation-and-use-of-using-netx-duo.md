---
id: "txmw-chapter-2-installation-and-use-of-using-netx-duo"
type: "concept"
domain: "rtos"
title: "Chapter 2 - Installation and Use of NetX Duo: Using NetX Duo"
summary: "Using NetX Duo is easy. Basically, the application code must include nx_api.h during compilation and link with the NetX Duo library nx.a (or nx.lib)."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter2.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter2.md#using-netx-duo"
license: "MIT"
mode: "V"
---

Using NetX Duo is easy. Basically, the application code must include ***nx_api.h*** during compilation and link with the NetX Duo library ***nx.a*** (or ***nx.lib**)*.

The following are the four easy steps required to build a NetX Duo application:

| Step  | Description  |
|---|---|
|Step 1: |Include the ***nx_api.h*** file in all application files that use NetX Duo services or data structures.|
|Step 2: |Initialize the NetX Duo system by calling ***nx_system_initialize*** from the ***tx_application_define*** function or an application thread.|
|Step 3: |Create an IP instance, enable the Address Resolution Protocol (ARP), if necessary, and any sockets after ***nx_system_initialize*** is called.|
|Step 4: |Compile application source and link with the NetX Duo runtime library ***nx.a*** (or ***nx.lib***). The resulting image can be downloaded to the target and executed!|
