---
id: "stream-writecpp-how-to-call-the-c-scheduler"
type: "concept"
domain: "cmsis-stream"
title: "WriteCPP: How to call the C++ scheduler"
summary: "It is a C API that can be used from C code."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/WriteCPP.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/WriteCPP.md#how-to-call-the-c-scheduler"
license: "Apache-2.0"
mode: "V"
---

The API to the scheduler is:

```C
extern uint32_t scheduler(int *error);
```

or

```C
extern uint32_t scheduler(int *error,void *evtQueue_);
```

It is a C API that can be used from C code.

The second form (with `evtQueue_`) is generated when initialization of FIFOs occurs inside the scheduler function.
When initialization occurs in a separate initialization function, the event queue argument is only used by the init function.
If you don't use events in your graph, this argument can be `NULL`.

In case of error, the function is returning :

* the number of schedule iterations computed since the beginning
* an error code.

It is possible, from the Python script, to add arguments to this API when there is the need to pass additional information to the nodes.
