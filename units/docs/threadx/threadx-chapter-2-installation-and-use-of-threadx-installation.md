---
id: "threadx-chapter-2-installation-and-use-of-threadx-installation"
type: "concept"
domain: "rtos"
title: "Chapter 2 - Installation and Use of ThreadX: ThreadX Installation"
summary: "ThreadX is installed by cloning the GitHub repository to your local machine. The following is typical syntax for creating a clone of the ThreadX repository on your PC."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter2.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter2.md#threadx-installation"
license: "MIT"
mode: "V"
---

ThreadX is installed by cloning the GitHub repository to your local machine. The following is typical syntax for creating a clone of the ThreadX repository on your PC.

```shell
    git clone https://github.com/eclipse-threadx/threadx
```

Alternatively you can download a copy of the repository using the download button on the GitHub main page.

You will also find instructions for building the ThreadX library on the front page of the online repository.

> **Note:** *Application software needs access to the ThreadX library file (usually **tx.a** or **tx.lib**) and the C include files ***tx_api.h*** and ***tx_port.h***. This is accomplished either by setting the appropriate path for the development tools or by copying these files into the application development area.*
