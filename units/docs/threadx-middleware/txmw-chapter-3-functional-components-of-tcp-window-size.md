---
id: "txmw-chapter-3-functional-components-of-tcp-window-size"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of NetX Duo: Transmission Control Protocol (TCP) / TCP Window Size"
summary: "Part of: Transmission Control Protocol (TCP)"
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter3.md#tcp-window-size"
license: "MIT"
mode: "V"
---

_Part of: Transmission Control Protocol (TCP)_

During both the setup and data transfer phases of the connection, each port reports the amount of data it can handle, which is called its window size. As data are received and processed, this window size is adjusted dynamically. In TCP, a sender can only send an amount of data that fits into the receiver's window. In essence, the window size provides flow control for data transfer in each direction of the connection.
