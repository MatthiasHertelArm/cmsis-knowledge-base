---
id: "stream-files-copied-to-the-application-cm-stream-init-hpp-and-stream-init-cpp"
type: "concept"
domain: "cmsis-stream"
title: "Files copied to the application {#cmsis_stream_files_copied}: `stream_init.hpp` and `stream_init.cpp`"
summary: "stream_init.hpp and stream_init.cpp are CMSIS-RTOS application templates. They connect one or more generated schedulers to the shared CMSIS-Stream runtime."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/Doxygen/src/01_files_copied.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/Doxygen/src/01_files_copied.md#stream-init-hpp-and-stream-init-cpp"
license: "Apache-2.0"
mode: "V"
---

`stream_init.hpp` and `stream_init.cpp` are CMSIS-RTOS application templates.
They connect one or more generated schedulers to the shared CMSIS-Stream
runtime. They are copied into the client project because they depend on the
application graph names, generated scheduler headers, hardware initialization,
node parameters, and runtime startup policy.

The template is intentionally more complex than the other copied files. It is
the place where application code binds generated graph code to the CMSIS-RTOS
runtime.
