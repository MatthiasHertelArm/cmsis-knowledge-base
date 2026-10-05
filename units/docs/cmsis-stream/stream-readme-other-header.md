---
id: "stream-readme-other-header"
type: "concept"
domain: "cmsis-stream"
title: "README: Other header"
summary: "Nodes of CMSIS Stream can implement some APIs. The header cstream_node.h and IdentifiedNode.hpp provides a way to expose those API to the external world and hide complexity of C++ multiple-inheritance."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:platform/cmsis_rtos_runtime/README.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/platform/cmsis_rtos_runtime/README.md#other-header"
license: "Apache-2.0"
mode: "V"
---

Nodes of CMSIS Stream can implement some APIs.
The header `cstream_node.h` and `IdentifiedNode.hpp` provides a way to expose those API to the external world and hide complexity of C++ multiple-inheritance.

The APIs implemented are application dependent and that's why those files must be provided by the application. See CMSIS Stream documentation for more information.

# How to start CMSIS Stream

The `stream_runtime_init.hpp` is a convenience header to start CMSIS Stream.
It is possible to start CMSIS Stream manually but the APIs in this header takes care of creating the memory pools, the event queues and the threads.

They also provide a way to pause / resume a graph and to context switch to another graph.

1. Call `stream_init_memory`
2. Allocate event queues for each of your apps with `stream_new_event_queue`
3. Init the scheduler for each of your app (using functions in the generated scheduler header)
4. Resume the app you want to start first with `resume_scheduler_app`
5. Create the CMSIS Stream runtime threads with `stream_start_threads`
6. Starts this RTOS scheduling with `osKernelStart`

To context switch between two app use:

1. `pause_scheduler_app`
2. `resume_scheduler_app`


# Configuration values
Default configuration values that can be modified when building.
You can redefine any of those values:

- By redefining them on the command line
- By redefining them in the copied `stream_runtime_config.hpp` file.
