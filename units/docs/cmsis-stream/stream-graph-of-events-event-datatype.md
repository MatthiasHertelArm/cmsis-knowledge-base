---
id: "stream-graph-of-events-event-datatype"
type: "concept"
domain: "cmsis-stream"
title: "Graph of events: Event datatype"
summary: "Starting from ID 100, you can use custom events using the selectors (see below). The first selector ID is 100. Values before 100 are reserved for CMSIS-Stream."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/Events.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/Events.md#event-datatype"
license: "Apache-2.0"
mode: "V"
---

The event contains:

- An event ID
- A priority
- The data

```C++
uint32_t event_id;
uint32_t priority;
EventData data;
```

Some events are standardized:

```C++
 enum cg_standard_event
    {
        kNoEvent = 0,
        kDo = 1,
        kPause = 2,
        kResume = 3,
        kGetParam = 5,
        kValue = 6,
        kStopGraph = 7,
        kDebug = 8,
        kStartNodeInitialization = 9,     
        kNodeWasInitialized = 10,    
        kNodeWillBeDestroyed = 11,
        kNodeReadyToBeDestroyed = 12, 
        kError = 13,
        kLongRun = 14,     
        // Node selectors are starting at 100
        kSelector = 100
    };
```

Starting from ID 100, you can use custom events using the selectors (see below).
The first selector ID is 100. Values before 100 are reserved for CMSIS-Stream.

- `kDo` : Do a default action that is node dependent
- `kPause` : Pause the dataflow. The nodes stop their computations but still updates the FIFO and write output data. In case of memory optimization, the output buffer can be shared between different nodes that's why a node must always write something into the FIFO. So, the pause here is a pause of the computation but not of the flow of data
- `kResume` : Resume the computation
- `kGetParam` : Get the value of a parameter. This value will be sent as an output event on the default event output (port 0 that must be present)
- `kValue` : Send a value to an event input
- `kStopGraph` : Stop the data flow graph
- `kDebug` : Any debug action that may be implemented by the node

In generate, nodes are initialized in their C++ constructors.
Some nodes may require more complex initializations that could fail and should do those initializations with `init` method if possible.
When the initializations may take too much time, it is possible to use events to do an asynchronous initialization with some nodes.

Some events have been defined to handle this:

- `kStartNodeInitialization`:

  - Ask a node to start a complex initialization in asynchronous way

- `kNodeWasInitialized`:
  - Event sent by a node when its initialization is finished. The event should contain one value : the node ID as an `uint32_t`. If an error occurred,
  the 'kError' event should be sent with the node ID as `uint32_t` and an error code as an `int32_t`.
- `kNodeWillBeDestroyed`:
  - If a node was initialized with the previous process, the C++ destructor cannot be called before the node has had the chance to undo what has been done during the initialization. This event signals a node that its C++ destructor is going to be used
- `kNodeReadyToBeDestroyed`:
  - When the node is ready to be destroyed and the C++ destructor can be called, it should signal it.

The application can check if a node needs an asynchronous initialization using the API `bool needsAsynchronousInit()`.

- `kLongRun`:
   This event is used by a node when the node needs a thread to run a long (or forever) task. This event should be sent by the node to itself in an asynchronous way. Like that, the event handler will be executed on the thread pool managing the event queue. A long running task should use the event queue method `mustEnd` to know if the tasks must end.

**A node is free to ignore any events.**

### Event values

An event is either an atomic value or a list of value (`ListValue`).

An atomic value is of type `cg_value`.

`cg_value` is basically a variant:

```C++
using cg_value_variant = std::variant<std::monostate,
    int8_t,
    int16_t,
    int32_t,
    int64_t,
    float,
    double,
    uint8_t,
    uint16_t,
    uint32_t,
    uint64_t,
    BufferPtr,
    std::string,
    cg_any_tensor,
    cg_any_const_tensor> value;
```

`BufferPtr` is an alias for `ProtectedBuffer<RawBuffer>`

`cg_any_tensor` and `cg_any_const_tensor` are two other variants for tensors.

For instance, `cg_any_tensor` contains `TensorPtr<float>`.

`TensorPtr<T>` is an alias for `ProtectedBuffer<Tensor<T>>`

Read the section about `ProtectedBuffer` to know how to allocate raw buffers and tensors.

### ProtectedBuffer

Buffers (raw buffer or tensor) can be shared between several events because we do not want to have to copy big buffers.

As consequence, those datatype must be accessed through a `std::shared_ptr` that will manage a reference count to know how many events are referencing the buffer.

In some platforms, the events can be managed in an asynchronous way using threads. As consequence, those buffers can be accessed from different thread and the access must be protected with mutexes.

It is also important to protect the ref count.

If you want to be able to do in-place modification on some big buffers you need to know if the buffer is shared or not. It is not possible to know the sharing status if the ref count is also not protected by a mutex.

`ProtectedBuffer` is used to provide a protected access to a buffer or tensor description and its reference count.

`ProtectedBuffer` protects a buffer description : `RawBuffer` or `Tensor<T>`. A buffer descriptor describes the data (length, shape) but does not contain the data. It contains a unique pointer to the data. The unique pointer is using the class `UniquePtr` provided by `StreamNodes.hpp`.

To create a protected buffer, you first must have some data. You should create a `UniquePtr` with a deleter if needed.

```C++
UniquePtr<float> ptr(10);
```

Once the content has been created, you can get a `ProtectedBuffer` describing this content:

```C++
 TensorPtr<float> t = TensorPtr<float>::create_with((uint8_t)1,cg_tensor_dims_t{10},std::move(ptr));
```

The arguments of the `create_with` are the arguments required to create a `Tensor<float>` object.

To access the content of the `TensorPtr` you need to use the `lock` and `lock_shared` APIs.

`lock_shared` is used when you need a read access. It takes a lambda as argument:

```C++
obj.lock_shared([](CG_MUTEX_ERROR_TYPE error, const Tensor<T> &t)
{
    ...
}
```

In the lambda you have access to an error code if an error occured while trying to lock the mutex.

In the lambda, you have access to the object but if an error occured you should not access it.

The error type is defined with the macro `CG_MUTEX_ERROR_TYPE` to provide portability.

You should not raise exceptions in the lambda.

Note that the lambda is called only if there is an object in the `ProtectedBuffer`. If the object pointer is null because of previous errors, the lambda is not called.

If you want a write access. you use:

```C++
t.lock([](CG_MUTEX_ERROR_TYPE error,bool isShared, Tensor<float> &tensor)
{
    ...
}
```

There is an additional argument to the lambda : `bool isShared`.

It is true if the buffer is shared : if there are several references to the buffer.

The events are passed by rvalue reference to the handler (`processEvent` in a node or the application handler).
The reason is related to the ref count : using `const Event&` would introduce an untracked sharing that would not be reflected in the ref count. 

Events only need to be copied when they are sent to many nodes. It is done by the `EventOutput` object. In the application code, events don't have generally a reason to be copied.

You may need to __copy__ the event if you need to pass it to a function for read only processing (like displaying on stdout with iostream).

__Never pass the event by reference or pointer.__
