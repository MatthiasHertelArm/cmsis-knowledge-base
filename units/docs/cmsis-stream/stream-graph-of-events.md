---
id: "stream-graph-of-events"
type: "concept"
domain: "cmsis-stream"
title: "Graph of events"
summary: "The inputs and outputs of the CMSIS Stream nodes can be of two kind:"
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/Events.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/Events.md"
license: "Apache-2.0"
mode: "V"
---

The inputs and outputs of the CMSIS Stream nodes can be of two kind:

- Data flow
- Events

Data flow is the original CMSIS Stream concept based upon streaming of samples between nodes.

Events are a new feature : you can have both a dataflow graph and an event graph mixed.

You can even have a graph that only generates and consumes events.

An event is transmitted synchronously or asynchronously from one event output to several event inputs.

An event input can receive events from several outputs.

An event is like a function call:

- It has a name
- It has some arguments

The function call is executed by the node when it receives the event and if it has an event handler for this kind of event.

Refer to the `events` example in `Examples` folder to see a full example with:
- Data flow
- Events
- Multi-threading
- Remote procedure call (client / server)
- Custom memory allocators

# Working with events
