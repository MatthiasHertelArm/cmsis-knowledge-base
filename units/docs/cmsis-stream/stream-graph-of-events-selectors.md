---
id: "stream-graph-of-events-selectors"
type: "concept"
domain: "cmsis-stream"
title: "Graph of events: Selectors"
summary: "Without selectors, a node can decide what to do based upon:"
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/Events.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/Events.md#selectors"
license: "Apache-2.0"
mode: "V"
---

Without selectors, a node can decide what to do based upon:

- The predefined event IDs
- The event input that received the event
- The datatype of the value

It is already flexible but it should also be
possible for a node to define new kind of events.

A selector is a name for an event that is mapped to a unique number used at runtime to receive and send those events.

The Python description of a node lists the events that can be received or sent by the node by giving their names as strings.

The python scheduling is generating unique identification number for those event names.

Those unique numbers are used to initialize a class member variables in the C++ class implementing the node.

The C++ for the node is using those global
numbers to communicate with other nodes.


### Defining selectors in the Python

You can use the argument `selectors` to pass the name of the events you want to use in your node (receiving or sending).

```python
GenericNode.__init__(self,name,selectors=["reset","increment"])
```

The events have a local ID : the position in the list.
`reset` will have local ID 0 and `increment` will have local ID 1.

### Initialization of selectors in C++

In the generated scheduler code, a class member is initialized with the custom global selectors ID.

You should define a public class variable like:

```C++
static std::array<uint16_t,N> selectors;
```

where `N` is the number of selectors you can receive or send.

The class variable is initialized like:

```C++
template<>
std::array<uint16_t,2> ProcessingNode<float,7,float,7>::selectors = {SEL_RESET_ID, SEL_INCREMENT_ID};
```

`SEL_RESET_ID` and `SEL_INCREMENT_ID` are global unique identifiers. They are unique for a given graph and are computed by the Python script that is computing the graph scheduling.

Internally, in your node implementation you can use the local ID : position in the `selectors` array.

It is also a good idea to define an enum in your class to more easily track the events using their local IDs:

```C++
enum selector {selReset=0,
               selIncrement=1};
```

### Use of selectors in C++

To use the selectors, you should always use their global ID.

If you want to test if you have received the message `increment`, you should compare the received global ID with `selectors[selIncrement]`.

If you want to send the event `increment`, you should use the global ID `selectors[selIncrement]`

```C++
ev0.sendAsync(kNormalPriority,selectors[selIncrement]);
```

In below code, an event taking 3 arguments is built and sent.

```C++
ev0.sendAsync(kNormalPriority,selectors[selComplexEvent],1,1.0,-4);
```

If you have 0 or 1 arguments, a normal event will be created.

If you have more than 1 arguments, a list event will be created.

Note that NO CHECK is done on the number of arguments or their types.

If you sent an event with the wrong number of arguments or types it will likely be ignored in the destination node.

The `processEvent` functions should check that the event received if well formed and ignore it if it is not the case.
