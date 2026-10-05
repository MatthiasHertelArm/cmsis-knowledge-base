---
id: "txmw-chapter-5-netx-duo-network-drivers-driver-entry"
type: "concept"
domain: "rtos"
title: "Chapter 5 - NetX Duo Network Drivers: Driver Entry"
summary: "NetX Duo invokes the network driver entry function for driver initialization and for sending packets and for various control and status operations, including initializing and enabling the network device."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter5.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter5.md#driver-entry"
license: "MIT"
mode: "V"
---

NetX Duo invokes the network driver entry function for driver initialization and for sending packets and for various control and status operations, including initializing and enabling the network device. NetX Duo issues commands to the network driver by setting the ***nx_ip_driver_command*** field in the **NX_IP_DRIVER** request structure. The driver entry function has the following format:

```c
VOID my_driver_entry(NX_IP_DRIVER *request);
```
