---
id: "pyocd-architecture-object-graph"
type: "concept"
domain: "debug"
title: "Architecture: Object graph"
summary: "The diagram below shows the most interesting parts of the pyOCD object graph, i.e. those parts that a user of the Python API will interact with. The connections in the diagram represent composition, not inheritance."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@d1974ff:docs/architecture.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/d1974ff/docs/architecture.md#object-graph"
license: "Apache-2.0"
mode: "V"
---

The diagram below shows the most interesting parts of the pyOCD object graph, i.e. those parts
that a user of the Python API will interact with. The connections in the diagram represent
composition, not inheritance.




The root of the runtime object graph is a `Session` object. This object holds references to the debug
probe and the board. It is also responsible for managing per-session options that control
various features and settings.

Attached to the board is a `CoreSightTarget` instance, which represents an MCU. This owns the
CoreSight related objects for communicating with the DP and APs and a `CortexM` object for each CPU
core on the device. Both `CoreSightTarget` and `CortexM` are subclasses of the abstract `Target`
class, which is referenced below, and share most of the same APIs. `CortexM` has a memory map
comprised of `MemoryRegion` objects. The flash memory regions have a `Flash` object to control flash
programming.
