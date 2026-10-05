---
id: "stream-graph-of-events-use-of-several-graphs"
type: "concept"
domain: "cmsis-stream"
title: "Graph of events: Use of several graphs"
summary: "There are some difficulties if you want to build several graphs using the same kind of nodes in your application."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/Events.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/Events.md#use-of-several-graphs"
license: "Apache-2.0"
mode: "V"
---

### Reuse of selector IDs

There are some difficulties if you want to build several graphs using the same kind of nodes in your application.

First, you may want to have the same selector IDs for the selectors they have in common.

You can reuse the selectors ID of a previous graph to compute a new one.

Just set the old selectors IDs in the configuration before computing the new scheduling:

```python
newconf = Configuration()
# Reuse selectors ID definitions from previous graph
newconf.selectorsID = scheduling.selectorsID
```

Then you compute the scheduling for the new graph using those IDs:

```python
scheduling = the_graph.computeSchedule(config=newconf)
```

### Avoid redundant initializations

Selectors are initialized at class level.

If you reuse the same kind of node in different graphs in the application, you want the initialization to occur only once.

The `.cpp` generated file contains class initializations for the selectors. If several graphs use `ProcessingNode<float,7,float,7>` and you don't make anything special then the initialization of the selectors field will occur for each graph and you'll get a linker error.

To avoid this problem, you need to export the list of initializations that occured in one graph and use this to generate the scheduling for another graph.

To export the initialization that occured in your graph, you can do:

```python
scheduling.genJsonSelectorsInit(".",conf)
```

Don't confuse wtih `genJsonSelectors` that is another json files to be used to send events to the graph from an outside tool.

Then, when you compute the schedule for another graph, you can use several json files:

```python
scheduling = the_graph.computeSchedule(config=newconf,oldSelectorsInit=["scheduler_selectors_inits.json"])
```

The initializations that occured in previous graph constructions will not occur again.

**NOTE**: It is very important in this case to use the same selectors IDs for the same selector in both graphs.

Because the initialization made in one graph must also be valid for the other ones. So, you must ensure that the selectors ID of the previous graph are reused for the current graph.
