---
id: "stream-table-of-content-edge-description"
type: "concept"
domain: "cmsis-stream"
title: "Table of content: Edge description"
summary: "Source port for an edge. It contains the following:"
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/YAML.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/YAML.md#edge-description"
license: "Apache-2.0"
mode: "V"
---

It contains the following:

| Keyword            |              | Content                                                      |
| ------------------ | ------------ | ------------------------------------------------------------ |
| [`src:`](#src)     | **Required** | Source port for the edge                                     |
| [`dst:`](#dst)     | **Required** | Destination port for the edge                                |
| `class:`           | Optional     | Name of the C++ class template implementing this FIFO. The template arguments must be the same than in original FIFO template. The C++ class must inherit from `FIFOBase` |
| `scale:`           | Optional     | Used in asynchronous scheduling only. It is a float used to scale the synchronous FIFO size to have more margin in asynchronous mode. **deprecated** since the `asynchronous` mode is deprecated and replaced by a `fullyAsynchronous` |
| `fifoAsyncLength:` | Optional     | Used in `fullyAsynchronous` mode to specify the length of the FIFO in sample units |
| `weak:`            | Optional     | Used in `fullyAsynchronous` to break loops for the topological ordering of the graph that is used to compute the schedule. |

**Examples:**

```yml
- src:
      node: source
      output: o
  dst:
      node: processing
      input: i
```

```yml
- src:
      node: sourceOdd
      output: o
  dst:
      node: debug
      input: i
  class: MyFIFO
  scale: 3.0
```

### `src:`

Source port for an edge. It contains the following:

| `src:`                       | Content                                                     |
| ---------------------------- | ----------------------------------------------------------- |
| [`node:`](#node-description) | Source node                                                 |
| `output:`                    | Name of the [Output port](#io-port-description) of the node |

**Examples:**

```yml
- src:
      node: source
      output: o
```

### `dst:`

Destination port for an edge. It contains the following:

| `dst:`           | Content                                                     |
| ---------------- | ----------------------------------------------------------- |
| [`node:`](#node) | Destination node                                            |
| `input:`         | Name of the [Input port](#io-port-description) for the node |

**Examples:**

```yml
dst:
      node: processing
      input: i
```
