---
id: "pyocd-architecture-high-level-structure"
type: "concept"
domain: "debug"
title: "Architecture: High level structure"
summary: "The session and connection to the target and all aspects of the target are representated in pyOCD with a graph of objects constructed at runtime."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@d1974ff:docs/api/architecture.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/d1974ff/docs/api/architecture.md#high-level-structure"
license: "Apache-2.0"
mode: "V"
---

The session and connection to the target and all aspects of the target are representated in pyOCD with a graph of objects constructed at runtime. The diagram below shows an overview of this object graph, focusing on objects that a user of the Python API will interact with.




The connections in the diagram represent composition.

The root of the runtime object graph is a `Session` object. This object holds references to the debug probe and the board. Through the board object, the entire object graph is accessible. It is also responsible for managing per-session options that control various features and settings.

As shown in the diagram, the object graph mirrors the physical structure: board, SoC, and cores. There are many more objects connected with the ones shown here. The Arm ADI debug port (DP) and access ports (APs), other CoreSight components, the memory map, and so on.
