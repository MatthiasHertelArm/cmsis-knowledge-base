---
id: "x-cmsis-stream-4"
type: "concept"
domain: "cmsis-stream"
title: "CMSIS Stream evtQueue argument for nodes that send events without event output ports"
status: "draft"
extracted_from: "proc-cmsis-stream"
source: "cmsis-stream/SKILL.md"
---

If the component has no event output port but must still be able to send events, the Python should define a new argument for the C++ constructor
```python
self.addVariableArg("evtQueue")
```

The name `evtQueue` is special and will be used by the code generator to set the value of this argument to the pointer of the EventQueue that is used internally by the component to send events.
