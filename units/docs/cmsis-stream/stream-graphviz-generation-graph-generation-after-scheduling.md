---
id: "stream-graphviz-generation-graph-generation-after-scheduling"
type: "concept"
domain: "cmsis-stream"
title: "Graphviz generation: Graph generation after scheduling"
summary: "The below method can be used to generate the .dot file representing the graph."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/GraphvizGen.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/GraphvizGen.md#graph-generation-after-scheduling"
license: "Apache-2.0"
mode: "V"
---

The below method can be used to generate the `.dot` file representing the graph.

```python
def graphviz(self,f,config=Configuration())
```

It is a method of the **schedule** object returned by `computeSchedule`.

* `f` : Opened file where to write the graphviz description
* `config` : An optional configuration object
