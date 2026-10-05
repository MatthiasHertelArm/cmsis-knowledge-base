---
id: "stream-graphviz-generation-graph-generation-before-scheduling"
type: "concept"
domain: "cmsis-stream"
title: "Graphviz generation: Graph generation before scheduling"
summary: "Generating the graph before the scheduling computation can be useful to find problems. Sometimes the scheduling is failing because the graph has some issues : IOs not connected, loops without the right delays ..."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/GraphvizGen.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/GraphvizGen.md#graph-generation-before-scheduling"
license: "Apache-2.0"
mode: "V"
---

Generating the graph before the scheduling computation can be useful to find problems. Sometimes the scheduling is failing because the graph has some issues : IOs not connected, loops without the right delays ...

To generate the graph before the scheduling, you can use the `graphviz` function on the **graph** object and before using the `computeSchedule` function that is rewriting the graph

```python
def graphviz(self,f,config=Configuration())
```

This is a method of the **graph** object.
