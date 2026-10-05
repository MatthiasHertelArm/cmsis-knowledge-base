---
id: "stream-graph-of-events-json-identification"
type: "concept"
domain: "cmsis-stream"
title: "Graph of events: JSON identification"
summary: "You may want to address the nodes by name instead of ID."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/Events.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/Events.md#json-identification"
license: "Apache-2.0"
mode: "V"
---

You may want to address the nodes by name instead of ID.

```python
scheduling.genJsonIdentification(".",conf)
```

This exports a json file mapping the name of a node to its ID in a given graph. It can be used by external tools.

If you are in the C/C++ world you can just use the `#define` generated in the header of the scheduler.

You may also want to use a name for a selector rather than the global ID:

```python
scheduling.genJsonSelectors(".",conf)
```

This generates a JSON file mapping json selector names to their ID for a given graph.
