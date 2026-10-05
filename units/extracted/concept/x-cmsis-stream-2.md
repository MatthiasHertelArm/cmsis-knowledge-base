---
id: "x-cmsis-stream-2"
type: "concept"
domain: "cmsis-stream"
title: "CMSIS Stream Python node base classes"
status: "draft"
extracted_from: "proc-cmsis-stream"
source: "cmsis-stream/SKILL.md"
---

If the class only has event ports, it inherits from `BaseNode`.
If the class has some dataflow ports it must inherit from `GenericSink` if those dataflow ports are only input ports, from `GenericSource` if those dataflow ports are only output ports, and from `GenericNode` if those dataflow ports are both input and output ports.
