---
id: "x-cmsis-stream-1"
type: "concept"
domain: "cmsis-stream"
title: "CMSIS Stream C++ dataflow base class by port count"
status: "draft"
extracted_from: "proc-cmsis-stream"
source: "cmsis-stream/SKILL.md"
license: "Apache-2.0"
---

Select the C++ dataflow base class according to the number of dataflow input and output ports. Event ports do not count toward this selection. Set its template parameters according to the type and length of each dataflow port.

| Dataflow inputs | Dataflow outputs | C++ base class |
| --- | --- | --- |
| 1 | 1 | `GenericNode` |
| 1 | 2 | `GenericNode12` |
| 1 | 3 | `GenericNode13` |
| 2 | 1 | `GenericNode21` |
| 3 | 1 | `GenericNode31` |
| 1 | 0 | `GenericSink` |
| 0 | 1 | `GenericSource` |
