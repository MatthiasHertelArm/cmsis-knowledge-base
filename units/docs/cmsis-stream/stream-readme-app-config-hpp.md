---
id: "stream-readme-app-config-hpp"
type: "concept"
domain: "cmsis-stream"
title: "README: `app_config.hpp`"
summary: "This header is generally used to define CG_BEFORE_BUFFER and CG_BEFORE_NODE_EXECUTION, which customize the generated CMSIS-Stream scheduler."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:platform/cmsis_rtos_runtime/README.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/platform/cmsis_rtos_runtime/README.md#app-config-hpp"
license: "Apache-2.0"
mode: "V"
---

This header is generally used to define `CG_BEFORE_BUFFER` and
`CG_BEFORE_NODE_EXECUTION`, which customize the generated CMSIS-Stream
scheduler.

`CG_BEFORE_BUFFER` __must__ be used to enforce alignment of buffers when memory optimization feature is activated.
