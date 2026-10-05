---
id: "stream-graphviz-generation-options-for-the-graphviz-generator"
type: "concept"
domain: "cmsis-stream"
title: "Graphviz generation: Options for the graphviz generator"
summary: "Horizontal or vertical layout for the graph."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/GraphvizGen.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/GraphvizGen.md#options-for-the-graphviz-generator"
license: "Apache-2.0"
mode: "V"
---

### horizontal (default = True)

Horizontal or vertical layout for the graph.

### displayFIFOBuf (default = False)

By default, the graph is displaying the FIFO sizes computed as result of the scheduling. If you want to know the FIFO variable names used in the code, you can set this option to true and the graph will display the FIFO variable names.
