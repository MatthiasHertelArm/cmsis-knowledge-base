---
id: "stream-files-copied-to-the-application-cm"
type: "concept"
domain: "cmsis-stream"
title: "Files copied to the application {#cmsis_stream_files_copied}"
summary: "The CMSIS Pack copies the configuration files into the client project so the application can customize them. Generated schedulers include app_config.hpp and then stream_platform_config.hpp; client application source files do not include the files in folder config directly."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/Doxygen/src/01_files_copied.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/Doxygen/src/01_files_copied.md"
license: "Apache-2.0"
mode: "V"
---

The CMSIS Pack copies the configuration files into the client project so the
application can customize them. Generated schedulers include `app_config.hpp`
and then `stream_platform_config.hpp`; client application source files
do not include the files in folder `config` directly.

The copied configuration files are:

- `app_config.hpp`: Application configuration
- `cstream_node.h`: C API to the nodes
- `IdentifiedNode.hpp`: Implementation of the C API
- `stream_runtime_config.hpp`: Runtime configuration
- `stream_init.hpp`: Application startup interface
- `stream_init.cpp`: Application startup implementation
