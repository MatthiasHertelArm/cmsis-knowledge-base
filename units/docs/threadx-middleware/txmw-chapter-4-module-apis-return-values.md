---
id: "txmw-chapter-4-module-apis-return-values"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Module APIs: Return values"
summary: "Additional error codes are returned for some ThreadX APIs. These additional error codes are defined as follows:"
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx-modules/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx-modules/chapter4.md#return-values"
license: "MIT"
mode: "V"
---

Additional error codes are returned for some ThreadX APIs. These additional error codes are defined as follows:

- **TXM_MODULE_INVALID_PROPERTIES** (0xF3): Indicates the module does not have the correct properties to make an API call. For example, calling trace APIs in user mode.
- **TXM_MODULE_INVALID_MEMORY** (0xF4): Indicates the memory supplied by the module is invalid or is in an invalid location. For example, in memory protected modules, object control blocks are not allowed to be located in memory the module can access.
- **TXM_MODULE_INVALID_CALLBACK** (0xF5): Callback specified in the API is outside the range of the module's code and is therefore invalid.

---
