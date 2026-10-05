---
id: "stream-common-options-for-the-code-genera-dumpfifo-default-false"
type: "concept"
domain: "cmsis-stream"
title: "Common options for the code generators: dumpFIFO (default = False)"
summary: "When true, generate some code to dump the FIFO content at runtime. Only useful for debug."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/CodegenOptions.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/CodegenOptions.md#dumpfifo-default-false"
license: "Apache-2.0"
mode: "V"
---

When true, generate some code to dump the FIFO content at **runtime**. Only useful for debug.

When this mode is enabled, the first line of the scheduler file is :

`#define DEBUGSCHED 1`

and it also enable some debug code in `GenericNodes.h`
