---
id: "stream-common-options-for-the-code-genera-prefix-default"
type: "concept"
domain: "cmsis-stream"
title: "Common options for the code generators: prefix (default = \"\")"
summary: "Prefix to add before the FIFO buffer definitions. Those buffers are not static and are global. If you want to use several schedulers in your code, the buffer names used by each should be different."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/CodegenOptions.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/CodegenOptions.md#prefix-default"
license: "Apache-2.0"
mode: "V"
---

Prefix to add before the FIFO buffer definitions. Those buffers are not static and are global. If you want to use several schedulers in your code, the buffer names used by each should be different.

Another possibility would be to make the buffer static by redefining the macro `CG_BEFORE_BUFFER`
