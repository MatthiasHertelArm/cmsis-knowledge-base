---
id: "stream-graph-of-events-serialization-unserialization"
type: "concept"
domain: "cmsis-stream"
title: "Graph of events: Serialization / Unserialization"
summary: "The cg_pack.hpp file, generated with other default files, can be used to serialize / unserialize events and transmit them on a network."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/Events.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/Events.md#serialization-unserialization"
license: "Apache-2.0"
mode: "V"
---

The `cg_pack.hpp` file, generated with other default files, can be used to serialize / unserialize events and transmit them on a network.

To serialize an event you can do:

```C++
Pack packer;
    
packer.pack(nodeid, evt);

std::vector<uint8_t> d = packer.vector();
```

You need a destination nodeid for this event.

To unpack an event you can do:
```C++
void handleMessage(const std::vector<uint8_t> &message)
{
  uint32_t node_id;

  Unpack unpack(message.data(), message.size());

  Event evt = unpack.unpack(node_id);
...
```
