---
id: "stream-graph-picture-styling"
type: "concept"
domain: "cmsis-stream"
title: "Graph picture styling"
summary: "When the graph is complex, it can be interesting to customize the look of the graphical representation, highlight some nodes, some edges ..."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/Styling.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/Styling.md"
license: "Apache-2.0"
mode: "V"
---

When the graph is complex, it can be interesting to customize the look of the graphical representation, highlight some nodes, some edges ...

It is possible to change lots of aspects of the style.

There are global style settings that are applied to all elements of the graph, and local style settings that are applied only to specific nodes, edges, ports (a port being an input or output of the node).

A global style setting is defined in a dictionary. A local style setting is a method of a class that must be overridden.

To generate a graph with some style you use the option `style` of the `graphviz` function:

```python
schedule.graphviz(file,config=your_config,style=your_style)
```

Two default styles are available:

* `Style.default_style()`
* `Style.dark_style()`
