---
id: "txmw-chapter-2-installation-and-use-of-host-considerations"
type: "concept"
domain: "rtos"
title: "Chapter 2 - Installation and use of FileX: Host Considerations"
summary: "Embedded development is usually performed on Windows or Linux (Unix) host computers. After the application is compiled, linked, and located on the host, it is downloaded to the target hardware for execution."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/filex/chapter2.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/filex/chapter2.md#host-considerations"
license: "MIT"
mode: "V"
---

### Computer Type

Embedded development is usually performed on Windows or Linux (Unix) host computers. After the application is compiled, linked, and located on the host, it is downloaded to the target hardware for execution.

### Download Interfaces

Usually the target download is done from within the development tool's debugger. After download, the debugger is responsible for providing target execution control (go, halt, breakpoint, etc.) as well as access to memory and processor registers.

### Debugging Tools

Most development tool debuggers communicate with the target hardware via on-chip debug (OCD) connections such as JTAG (IEEE 1149.1) and Background Debug Mode (BDM). Debuggers also communicate with target hardware through In-Circuit Emulation (ICE) connections. Both OCD and ICE connections provide robust solutions with minimal intrusion on the target resident software.

### Required Hard Disk Space

The source code for FileX is delivered in ASCII format and requires approximately 500 KBytes of space on the host computer's hard disk
