---
id: "stream-graph-of-events-c-definition"
type: "concept"
domain: "cmsis-stream"
title: "Graph of events: C++ definition"
summary: "For each event output that you have defined in Python, you need to define a member variable of type EventOutput. This object tracks the nodes connected to the ouput."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/Events.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/Events.md#c-definition"
license: "Apache-2.0"
mode: "V"
---

For each event output that you have defined in Python, you need to define a member variable of type `EventOutput`. This object tracks the nodes connected to the ouput.

```C++
protected:
   EventOutput ev0;
```

When a node is connected to the output, the function `subscribe` will be called. Your node must provides an implementation.

The function receives:

- The output port from which you can select the right `EventOutput` object
- The destination object
- The destination event input

```C++
void subscribe(int outputPort,StreamNode &dst,int dstPort)
{
    if (outputPort == 0)
    {
        ev0.subscribe(dst,dstPort);
    }
}
```

The `EventOutput` object can only be created with an `EventQueue` argument.

Each node using `self.addEventOutput()` in the Python description has an argument 
of type `EventQueue*` in the C++ constructor. This argument follows the FIFOs arguments.
This argument must be used to instantiate the `EventOutput` member variable.
