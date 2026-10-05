---
id: "stream-files-copied-to-the-application-cm-stream-runtime-config-hpp"
type: "concept"
domain: "cmsis-stream"
title: "Files copied to the application {#cmsis_stream_files_copied}: `stream_runtime_config.hpp`"
summary: "This header can be used to redefine macros CMSISSTREAM_LOG_ERR and CMSISSTREAM_LOG_DBG for logging."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/Doxygen/src/01_files_copied.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/Doxygen/src/01_files_copied.md#stream-runtime-config-hpp"
license: "Apache-2.0"
mode: "V"
---

This header can be used to redefine macros `CMSISSTREAM_LOG_ERR` and
`CMSISSTREAM_LOG_DBG` for logging.

All CMSIS-Stream runtime configuration macros can also be redefined in this
header. `stream_platform_config.hpp` includes it before defining platform
defaults, so values defined here override the Pack defaults.

The runtime uses this header.
