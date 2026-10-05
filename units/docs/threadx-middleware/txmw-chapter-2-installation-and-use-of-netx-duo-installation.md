---
id: "txmw-chapter-2-installation-and-use-of-netx-duo-installation"
type: "concept"
domain: "rtos"
title: "Chapter 2 - Installation and Use of NetX Duo: NetX Duo Installation"
summary: "NetX Duo is installed by cloning the GitHub repository to your local machine. The following is typical syntax for creating a clone of the NetX Duo repository on your PC:"
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter2.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter2.md#netx-duo-installation"
license: "MIT"
mode: "V"
---

NetX Duo is installed by cloning the GitHub repository to your local machine. The following is typical syntax for creating a clone of the NetX Duo repository on your PC:

```c
    git clone https://github.com/eclipse-threadx/netxduo
```

Alternatively you can download a copy of the repository using the download button on the GitHub main page.

You will also find instructions for building the NetX Duo library on the front page of the online repository.

> **Important:** *Application software needs access to the NetX Duo library file (usually **nx.a** or **nx.lib**) and the C include files **nx_api.h, and nx_port.h**. This is accomplished either by setting the appropriate path for the development tools or by copying these files into the application development area.*
