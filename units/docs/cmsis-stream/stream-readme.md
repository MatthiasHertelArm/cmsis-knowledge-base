---
id: "stream-readme"
type: "concept"
domain: "cmsis-stream"
title: "README"
summary: "The CMSIS Pack copies the configuration files into the client project so the application can customize them. Generated schedulers include app_config.hpp and then stream_platform_config.hpp; client application source files normally do not include the files in config directly."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:platform/cmsis_rtos_runtime/README.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/platform/cmsis_rtos_runtime/README.md"
license: "Apache-2.0"
mode: "V"
---

# Files copied to the application

The CMSIS Pack copies the configuration files into the client project so the
application can customize them. Generated schedulers include `app_config.hpp`
and then `stream_platform_config.hpp`; client application source files normally
do not include the files in `config` directly.

The copied configuration files are:
- `app_config.hpp` : Application configuration
- `cstream_node.h` : C API to the nodes
- `IdentifiedNode.hpp` : Implementation of the C API
- `stream_runtime_config.hpp` : Runtime configuration
