---
id: "stream-files-copied-to-the-application-cm-other-header"
type: "concept"
domain: "cmsis-stream"
title: "Files copied to the application {#cmsis_stream_files_copied}: Other header"
summary: "Nodes of CMSIS-Stream can implement some APIs exposed to the software outside of the graph."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/Doxygen/src/01_files_copied.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/Doxygen/src/01_files_copied.md#other-header"
license: "Apache-2.0"
mode: "V"
---

Nodes of CMSIS-Stream can implement some APIs exposed to the software outside of the graph. 

The headers `cstream_node.h` and
`IdentifiedNode.hpp` provides a way to expose those API to the external world
and hide complexity of C++ multiple-inheritance.

The APIs implemented are application dependent and that's why those files must
be provided by the application. See CMSIS-Stream documentation for more
information.
