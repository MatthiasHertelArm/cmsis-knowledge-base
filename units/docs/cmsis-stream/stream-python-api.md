---
id: "stream-python-api"
type: "concept"
domain: "cmsis-stream"
title: "Python API"
summary: "When you describe a graph and generate a scheduler there are 4 mandatory steps and one optional one:"
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/PythonAPI.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/PythonAPI.md"
license: "Apache-2.0"
mode: "V"
---

When you describe a graph and generate a scheduler there are 4 mandatory steps and one optional one:

* Describing the nodes
* Adding the nodes to the graph
* Computing the schedule
* Generating the C++ and/or Python scheduler implementation
* Optional : Generating a graphviz `.dot` file with the graphical representation of the graph

1. ## [Description of new nodes](https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/Generic.md)

2. ## [Adding nodes to the graph](https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/Graph.md)

3. ## [Schedule computation and generation](https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/SchedOptions.md)

4. ## [SDS Nodes (experimental)](https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/PythonSDS.md)

5. ## Generation

   1. #### [C++ Code generation](https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/CCodeGen.md)

   2. #### [Python code generation (deprecated)](https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/PythonGen.md)

   3. #### [Graphviz generation](https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/GraphvizGen.md)

   4. #### [Common options for all generators](https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/CodegenOptions.md)
