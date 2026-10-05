---
id: "txmw-chapter-2-installation-and-use-of-filex-installation"
type: "concept"
domain: "rtos"
title: "Chapter 2 - Installation and use of FileX: FileX Installation"
summary: "FileX is installed by cloning the GitHub repository to your local machine. The following is typical syntax for creating a clone of the FileX repository on your PC:"
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/filex/chapter2.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/filex/chapter2.md#filex-installation"
license: "MIT"
mode: "V"
---

FileX is installed by cloning the GitHub repository to your local machine. The following is typical syntax for creating a clone of the FileX repository on your PC:

```c
    git clone https://github.com/eclipse-threadx/filex
```

Alternatively you can download a copy of the repository using the download button on the GitHub main page.

You will also find instructions for building the FileX library on the front page of the online repository.

> **Important:** Application software needs access to the FileX library file (usually called* usually ***fx.a*** or ***fx.lib***) *and the C include files **fx_api.h** and **fx_port.h**. This is accomplished either by setting the appropriate path for the development tools or by copying these files into the application development area.
