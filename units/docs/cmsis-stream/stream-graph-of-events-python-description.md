---
id: "stream-graph-of-events-python-description"
type: "concept"
domain: "cmsis-stream"
title: "Graph of events: Python description"
summary: "Event inputs and outputs are defined in a similar way to the data flow inputs and outputs. The differences are:"
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/Events.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/Events.md#python-description"
license: "Apache-2.0"
mode: "V"
---

Event inputs and outputs are defined in a similar way to the data flow inputs and outputs. The differences are:

- They are not named but numbered
- They have not a "number of samples" property
- They have no type

```python
self.addEventInput()
```

This functions adds a new event input and increments the event number. The initial event input has number 0.

```python
self.addEventInput(4)
```

This function adds 4 new event inputs starting from the current event number.

Event outputs are defined in a similar way.

```python
self.addEventOutput()
```

```python
self.addEventOutput(4)
```
