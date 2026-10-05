---
id: "threadx-overview-of-threadx-threadx-footprint"
type: "concept"
domain: "rtos"
title: "Overview of ThreadX: ThreadX footprint"
summary: "ThreadX has a remarkably small 2-KB instruction area and 1 KB of RAM minimal footprint. This small size is largely due to its non-layered picokernel architecture and automatic scaling."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/overview-threadx.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/overview-threadx.md#threadx-footprint"
license: "MIT"
mode: "V"
---

ThreadX has a remarkably small 2-KB instruction area and 1 KB of RAM minimal footprint. This small size is largely due to its non-layered picokernel architecture and automatic scaling. Automatic scaling means that only the services (and supporting infrastructure) used by the application are included in the final image at link time.

Here are some typical ThreadX size characteristics.

|ThreadX Service  |Typical Size in Bytes  |
|---------|---------|
|Core Services (Require) |2,000  |
|Queue Services  |900  |
|Event Flag Services  |900  |
|Semaphore Services  |450  |
|Mutex Services  |1,200  |
|Block Memory Services  |550  |
|Byte Memory Services  |900  |
