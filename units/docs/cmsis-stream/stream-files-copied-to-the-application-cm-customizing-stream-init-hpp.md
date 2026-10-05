---
id: "stream-files-copied-to-the-application-cm-customizing-stream-init-hpp"
type: "concept"
domain: "cmsis-stream"
title: "Files copied to the application {#cmsis_stream_files_copied}: Customizing `stream_init.hpp`"
summary: "Update NB_APPS to match the number of generated stream applications that can run in the project. A simple project generally keeps NB_APPS set to 1."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/Doxygen/src/01_files_copied.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/Doxygen/src/01_files_copied.md#customizing-stream-init-hpp"
license: "Apache-2.0"
mode: "V"
---

Update `NB_APPS` to match the number of generated stream applications that can
run in the project. A simple project generally keeps `NB_APPS` set to 1. A
project that context switches between several generated graphs should set it to
the number of available graphs.

Keep `contexts` sized with `NB_APPS`. Each entry describes one generated graph
to the runtime: its scheduler function, FIFO reset function, pause and resume
helpers, node lookup wrapper, event queue, number of identified nodes, and
scheduler length.

Keep `currentNetwork` as the index of the graph that must be started first, or
that is currently selected for execution. Application code may update it before
startup or when selecting another graph.

The public functions `stream_configure_and_start()` and `stream_free_all()` are
the application-level lifecycle API. They can be renamed or wrapped by the
client project if a different startup convention is required.
