---
id: "stream-graph-of-events-ipc"
type: "concept"
domain: "cmsis-stream"
title: "Graph of events: IPC"
summary: "Sharing buffers without copy between processes relies on several APIs that must be implemented for your platform."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/Events.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/Events.md#ipc"
license: "Apache-2.0"
mode: "V"
---

Sharing buffers without copy between processes relies on several APIs that must be implemented for your platform. 

### MemServer 

Shared buffers are managed by a server. Communication with this server is done through the `MemServer` API. You must provide an implementation of this API (and of the corresponding server).

The server is tracking access to the shared buffers : reference counting and locking.

All CMSIS Stream nodes must use the `MemServer` to access shared buffers. Having a global view of all the shared buffers used by all the processes involved in a CMSIS Stream graph is required for the nodes to know if in-place modification of a buffer is possible or not.

`MemServer` APIs return a `Descriptor`. This class is used to identify a shared buffer on client side. It is the only way to use a shared buffer in CMSIS Stream nodes : you first get a `Descriptor` from the `MemServer` and then you create a `SharedBuffer` object from the `Descriptor` object.

### Descriptor

You must provide an implementation of `Descriptor`. 
`Descriptor` is used to map / unmap a buffer or close the corresponding `NativeHandle`.

`Descriptor` must not be used directly but only though a `SharedBuffer` that is the unique owner of a `Descriptor`.

`Descriptor` is using the `NativeHandle` datatype.

`NativeHandle` is the datatype used to represent a shared buffer on your platform. It is `int` on Unix like systems (file descriptor) and it is `void *` on Windows.

### IPC

`IPC` is the API that must be implemented to exchange events with another process.
The `SharedBuffer` are represented by a `global_id` and only the `global_id` is transmitted by the `IPC`.
The receiving process uses the `global_id` and the `MemServer` to get a `Descriptor` for this memory buffer.

`IPC` implementation is not transmitting any file descriptor.

If you're not using `SharedBuffer` but `UniquePtr`, then the buffer will be serialized before being transmitted.

Serialization / Unserialization of events is done with the class in `cg_pack.hpp`.

Not that those classes can also be used to send the event on the network to a machine using the same endianism.
In case of transmission to the network, `SharedBuffers` are ignored and you must specify to the `pack` function that you are packing for network by setting the network argument to `true`.


# Details
