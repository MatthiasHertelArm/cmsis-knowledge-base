---
id: "txmw-chapter-3-functional-components-of-mss-validation"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of NetX Duo: Transmission Control Protocol (TCP) / MSS Validation"
summary: "Part of: Transmission Control Protocol (TCP)"
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter3.md#mss-validation"
license: "MIT"
mode: "V"
---

_Part of: Transmission Control Protocol (TCP)_

The Maximum Segment Size (MSS) is the maximum amount of bytes a TCP host can receive without being fragmented by the underlying IP layer. During TCP connection establishment phase, both ends exchanges its own TCP MSS value, so that the sender does not send a TCP data segment that is larger than the receiver's MSS. NetX Duo TCP module will optionally validate its peer's advertised MSS value before establishing a connection. By default NetX Duo does not enable such a check. Applications wishing to perform MSS validation shall define ***NX_ENABLE_TCP_MSS_CHECK*** when building the NetX Duo library, and the minimum value shall be defined in ***NX_TCP_MSS_MINIMUM***. Incoming TCP connections with MSS values below ***NX_TCP_MSS_MINIMUM*** are dropped.
