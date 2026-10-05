---
id: "stream-graphviz-generation"
type: "concept"
domain: "cmsis-stream"
title: "Graphviz generation"
summary: "A graphical representation of the graph can be generated in the graphivz format .dot. The file .dot can be processed by the graphviz dot tool to generate png, svg, pdf files ..."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/GraphvizGen.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/GraphvizGen.md"
license: "Apache-2.0"
mode: "V"
---

A graphical representation of the graph can be generated in the [graphivz](https://graphviz.org/) format `.dot`. The file `.dot` can be processed by the [graphviz](https://graphviz.org/) `dot` tool to generate `png`, `svg`, `pdf` files ...

The graph can be generated before scheduling. It is useful to debug but will miss some information (like FIFO lengths). The graph can be generated after schedule with all the information.
