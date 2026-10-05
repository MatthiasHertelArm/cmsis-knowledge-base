---
id: "stream-graph-of-events-sharing-buffers-between-processes"
type: "concept"
domain: "cmsis-stream"
title: "Graph of events: Sharing buffers between processes"
summary: "When some nodes in the graph are communicating with different processes, it is possible (when supported by the platform) to avoid copying buffers and use shared memory instead."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/Events.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/Events.md#sharing-buffers-between-processes"
license: "Apache-2.0"
mode: "V"
---

When some nodes in the graph are communicating with different processes, it is possible (when supported by the platform) to avoid copying buffers and use shared memory instead.

The `TensorPtr` and `RawBuffer` should use a `SharedBuffer` instead of a `UniquePtr`.

The `SharedBuffer` is a unique reference to a shared buffer.

It contains a platform dependent descriptor, a `global_id` that is used to identify the buffer, the size of the buffer in bytes and a pointer to the data.

The pointer to the data may be a `nullptr` if the buffer has not been mapped in the CMSIS-Stream process. As consequence, a CMSIS Stream node do not always have to map the buffer if it is just controlling an hardware accelerator.

For more details about how to integrate this feature in your platform, see the section IPC.


# Integrate the events in your application
