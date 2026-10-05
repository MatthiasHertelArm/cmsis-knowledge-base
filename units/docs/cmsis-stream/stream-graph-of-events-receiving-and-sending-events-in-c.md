---
id: "stream-graph-of-events-receiving-and-sending-events-in-c"
type: "concept"
domain: "cmsis-stream"
title: "Graph of events: Receiving and sending events in C++"
summary: "When an event is received, the function processEvent is used. It is defined in the CMSIS-Stream root class StreamNode and it must be overriden in your implementation."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/Events.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/Events.md#receiving-and-sending-events-in-c"
license: "Apache-2.0"
mode: "V"
---

### Receiving events 

When an event is received, the function `processEvent` is used. It is defined in the CMSIS-Stream root class `StreamNode` and it must be overriden in your implementation.

```C++
 cg_status processEvent(int dstPort,Event &&evt) final
```

Assume you want have an handler in your class:

```C++
cg_status myHandler(float a,int32_t b);
```

You want to use it to process an event.

The simplest way is to rely on the template functions provided by the `StreamNode.h` file and write something like that in your `processEvent` function:

```C++
if (evt.wellFormed<float,int32_t>())
{
    return evt.apply<float,int32_t>(&MyClass::myHandler, *this);
}
return CG_SUCCESS;
```

Note that an `int32_t` argument in those functions will also take into account `int16_t` and `int8_t` and introduce casts to `int32_t`.

Same with `float` that can receive an `int32_t`, `int16_t` or `int8_t` in the event.

The `apply` functions takes a pointer to a member function and the current object `*this`.

Note that the function `apply` is using `std::get<T>` from `std::variant` and will throw (if exceptions are enabled) if the type can't be found in the event. `wellFormed` should always be used before trying to use `apply`.

### Sending events

If you send an event from the `processEvent` function you can send it in a synchronous way. It will be executed immediately by another `processEvent` function in some other nodes.

It you publish the event from anywhere else you need to publish it in an asynchronous way: the events is pushed to an event queue with some priority. You'll have to provide an implementation of this event queue.

For instance, if the events are published from the `run` function of the data flow nodes, then they must be sent in an asynchronous way.

To send an event, you use the API of the `EventOutput` object.

The second argument is the event ID. Event ID are extensible using selectors (see below).

For instance:

```C++
ev0.sendSync(kNormalPriority,kDo);
```

or

```C++
res = ev0.sendAsync(kNormalPriority,kDo);
```

`res` is false is there was a queue overflow when trying to send the event in an asynchronous mode.

You can also use several arguments:

```C++
ev0.sendAsync(kNormalPriority,kValue,uint32_t(1),float(1.0),int32_t(-4));
```

It is better to give the type of constant values to avoid any ambiguity.

It is also possible to send an event to the application. 

```C++
EventOutput::sendSyncToApp(nodeIDSendingTheEvent,kNormalPriority,kDo)
```

This is a static function of the class `EventOutput` because it is not related to any specific output. The application is virtually connected to all nodes.


or

```C++
ev0->sendAsyncToApp(nodeIDSendingTheEvent,kNormalPriority,kDo)
```

For asynchronous mode, the event must be put on the event queue.
Each `EventOutput` is virtually connected to the application.
When an event is sent to the application, it is not sent to the nodes connected to the event output.

You don't have to use an `EventOutput` object to send an event to the application in an asynchronous way.
You can do it with the `EventQueue` used in the graph:

```C++
queue->push(DistantDestination{nodeIDSendingTheEvent},std::move(event));
```


You need to install an application event handler to process those events. This handler must be installed in the `EventQueue`. See the section about the `EventQueue`.
