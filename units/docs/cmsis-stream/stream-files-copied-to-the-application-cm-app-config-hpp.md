---
id: "stream-files-copied-to-the-application-cm-app-config-hpp"
type: "concept"
domain: "cmsis-stream"
title: "Files copied to the application {#cmsis_stream_files_copied}: `app_config.hpp`"
summary: "This header is generally used to define CG_BEFORE_BUFFER and CG_BEFORE_NODE_EXECUTION, which customize the generated CMSIS-Stream scheduler."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/Doxygen/src/01_files_copied.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/Doxygen/src/01_files_copied.md#app-config-hpp"
license: "Apache-2.0"
mode: "V"
---

This header is generally used to define `CG_BEFORE_BUFFER` and
`CG_BEFORE_NODE_EXECUTION`, which customize the generated CMSIS-Stream
scheduler.

`CG_BEFORE_BUFFER` **must** be used to enforce alignment of buffers when memory
optimization feature is activated.

This header is only included by the generated schedulers. The runtime does not include it.
