---
id: "stream-schedule-computation-api"
type: "concept"
domain: "cmsis-stream"
title: "Schedule computation: API"
summary: "This is a method on the Graph object. It can take an optional Configuration object."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/SchedOptions.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/SchedOptions.md#api"
license: "Apache-2.0"
mode: "V"
---

```python
def computeSchedule(self,config=Configuration()):
```

This is a method on the `Graph` object. It can take an optional `Configuration` object.

It returns a `Schedule` object. This object contains:

* A description of the static schedule
* The computed size of the FIFOs
* The FIFOs
* The buffers for the FIFOs (with sharing when possible if memory optimizations were enabled)
* A rewritten graph with `Duplicate` nodes inserted

```python
def generateGenericNodes(folder):
```

Create the file `GenericNodes.h` in the folder `folder`. You can also use the `GenericNodes.h` from the CMSIS-Stream repository. But, to make it easier to start, it is included in the Python wrapper.

`GenericNodes.h` contains the definitions required for CMSIS-Stream to work (FIFO, Generic nodes, sources and sinks ...)

```python
def generateCGStatus(folder):
```

Create the file `cg_enums.h` in the folder `folder`. You can also use the `cg_enums.h` from the CMSIS-Stream repository. But, to make it easier to start, it is included in the Python wrapper.

`cg_enums.h` contains error codes.
