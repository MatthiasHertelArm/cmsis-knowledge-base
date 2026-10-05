---
id: "stream-table-of-content-graph"
type: "concept"
domain: "cmsis-stream"
title: "Table of content: `graph:`"
summary: "Description of the graph. It contains the following:"
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/YAML.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/YAML.md#graph"
license: "Apache-2.0"
mode: "V"
---

Description of the graph. It contains the following:

| `graph:`                     |              | Content                                                      |
| ---------------------------- | ------------ | ------------------------------------------------------------ |
| [`options:`](#options)       | Optional     | Option to select some default  C++ class for some nodes and edges |
| [`structures:`](#structures) | Optional     | C struct used in the graph for IO description                |
| [`nodes:`](#nodes)           | **Required** | List of nodes in the graph                                   |
| [`edges:`](#edges)           | **Required** | List of edges in the graph                                   |

**Examples:**

```yml
version: '1.0'
graph:
  nodes:
  ...
  edges:
  ...
```

### `options:`

| `options:`   |          | Content                                                      |
| ------------ | -------- | ------------------------------------------------------------ |
| `FIFO:`      | Optional | Name of the C++ class implementing FIFOs in the C++ generated code. (It can be overridden for each edge of the graph) |
| `Duplicate:` | Optional | Name of class used for `Duplicate` node if the default class is not used. |

### `custom-types:`

List of C++ custom types used in the node description.

This entry is optional in the graph description.

**Examples**

```yml
  custom-types:
    custom_type_1:
      ...
    custom_type_2:
      ...
```

```yml
  custom-types:
    complex:
      cname: complex
      bytes: 8
    quaternion:
      cname: quaternion
      bytes: 16
```

Each item in the list has following format:

| Keyword   | Description                                                  |
| --------- | ------------------------------------------------------------ |
| `cname:`  | C name of the structure                                      |
| `bytes:`  | Not used for the custom type with `cname` `Shared`. Otherwise, size of the custom type in bytes as returned by C `sizeof` |
| internal: | Only used for the custom type with `cname` `Shared`. Type of the buffer referenced by the `Shared` object |
| shared:   | Only used for the custom type `cname` `Shared. Shared status of the buffer reference by the `Shared` object. |

`Shared` types are mapped to C++ templates : ```Shared<bufferType,sharedStatus>```

**Examples**

```yml
- custom-types:
    complex:
      cname: complex
      bytes: 8
```

### `nodes:`

List of [nodes](#node-description)

**Examples:**

```yml
nodes:
  - node: source
    ...
  - node: processing
    ...
  - node: sink
    ...
```

### `edges:`

List of [edges](#edge-description).

**Examples:**

```yml
edges:
  - src:
      node: source
      ...
    dst:
      node: processing
      ...
  - src:
      node: processing
      ...
    dst:
      node: sink
      ...
```

### Node description

 It contains the following:

| nodes:                       |              | Content                                                      |
| ---------------------------- | ------------ | ------------------------------------------------------------ |
| [`node:`](#node-description) | **Required** | Identification of the node.                                  |
| [`kind:`](#kind)             | Optional     | The category of the node (when implemented with a C++ class) |
| [`c-function:`](#c-function)               | Optional     | A a pure C function |
| [`unary:`](#unary)           | Optional     | Function name for unary function (when node is a pure function with one input and one output) |
| [`binary:`](#binary)         | Optional     | Function name for binary function (when node is a pure function with two inputs and one output) |
| [`inputs:`](#inputs)         | Optional     | List of inputs for this node                                 |
| [`outputs:`](#output)        | Optional     | List of outputs for this node                                |
| [`args:`](#args)             | Optional     |                                                              |

**Examples:**

```yml
- node: processing
    kind: ProcessingNode
    inputs:
    - input: i
      samples: 7
      type: float32_t
    outputs:
    - output: o
      samples: 7
      type: float32_t
```

#### `node:`

Identification of the node. It must be a valid C variable name. It is used to identify the node in the graph and in the generated C code. It must be unique in the graph since it is the only way to identify the node,

#### `kind:`

It is the name of the `C++` class template implementing the node. It must be a valid `C++` class name.

It is optional for `Constant` nodes since those nodes just represent a C variable and don't have a corresponding C implementation.

It is not used for `Dsp`, `Unary` and `Binary` nodes that are mapped to pure C functions. A pure C function has no state and thus do not need a C++ wrapper.

#### `c-function:`

When the node is a pure C function that has no state, there is no C++ wrapper. This `c-function:` field gives the name of a C function and describes how the node IOs and additional arguments are mapped to the arguments of the C function.

This mapping is described with the field `args`:

| args:                       | Required | Content                                                      |
| ---------------------------- | ------------ | ------------------------------------------------------------ |
| `io:` | **Optional** | This argument of the C function uses a FIFO pointer generated by the CMSIS-Stream code generator. |
| `io-length:` | **Optional** | This argument of the C function is the length of a FIFO buffer generated by the CMSIS-Stream code generator. |
| `args:` | **Optional** | This argument of the C function is an additional arguments of the CMSIS-Stream node. |

The FIFO must be defined in the `inputs` or `outputs` sections. The additional arguments must be specified with a `literal` or `variable` section.

| io-length:                       |              | Content                                                      |
| ---------------------------- | ------------ | ------------------------------------------------------------ |
| `name:` | **Required** | Name of the IO                     |
| `sample-unit:` | **Required** | True when the size is expressed in samples. False when the size is expressed in bytes. |

**Examples:**

```yml
- node: myfunc1
    identified: false
    c-function:
      name: myfunc
      args:
      - io: ia
      - io-length:
          name: ia
          sample-unit: true
      - args: 0
      - io: ib
      - io-length:
          name: ib
          sample-unit: false
      - io: o
      - io-length:
          name: o
          sample-unit: true
      - args: 1
      - args: 2
    inputs:
    - input: ia
      samples: 7
      type: float
    - input: ib
      samples: 7
      type: float
    outputs:
    - output: o
      samples: 5
      type: q15_t
    args:
    - variable: testVar
    - literal: 4
    - literal: '5'
```

This will be mapped to the CMSIS-DSP function `myfunc` with header:

```C
  void myfunc(float *i0,
              int    i0_sample_length,
              char  *testVar,
              float *i1,
              int    i1_byte_length,
              q15_t *o2,
              int    o2_sample_length,
              int    arg0,
              char  *arg1);
```

The corresponding CMSIS-Stream node has an input port consuming 7 samples (ia), an input port consuming 7 samples (ib), an output port producing 5 samples (o) and three additional arguments : a variable `testVar`, an int `4` and a string `5`.

The call to the function in the generated C++ code will look like:

```C
myfunc(i0,7,testVar,i1,sizeof(float)*7,o2,5,4,"5");
```

#### `unary:`

When the node is a pure function that has no state and only one input / output, there is no C++ wrapper. This `unary:` field is the name of the function. The C function should implement a specific header.

**Examples:**

```yml
  - node: my_scale1
    unary: my_scale
    inputs:
    - input: i
      samples: 160
      type: float32_t
    outputs:
    - output: o
      samples: 160
      type: float32_t
```

**Header for a unary function:**

```C
void unary(
  const float32_t * pSrc,
        float32_t * pDst,
        uint32_t blockSize);
```

#### `binary:`

When the node is a pure function that has no state, two inputs, one output, there is no C++ wrapper. This `binary:` field is the name of the function. The C function should implement a specific header.

**Examples:**

```yml
  - node: my_binary1
    binary: my_binary
    inputs:
    - input: ia
      samples: 160
      type: float32_t
    - input: ib
      samples: 160
      type: float32_t
    outputs:
    - output: o
      samples: 160
      type: float32_t
```

**Header for a binary function:**

```C
void binary(
  const float32_t * pSrcA,
        float32_t * pSrcB,
        float32_t * pDst,
        uint32_t blockSize);
```

The type of an input argument could just be `float32_t` instead of a pointer. In that case, this input must be connected to a constant node in the graph.

#### `inputs:`

List of [inputs](#input-or-output) for the node.

A source node has no inputs. So this item is optional. 

#### `outputs:`

List of [outputs](#input-or-output) for the node.

A sink node has no outputs. So this item is optional.

#### `args:`

The `C++` implementation can have additional arguments in the constructor. Those arguments are defined with this `args:` field that is optional.

| args:                    |          | Content                  |
| ------------------------ | -------- | ------------------------ |
| [`literal:`](#literal)   | Optional | A scalar or string       |
| [`variable:`](#variable) | Optional | The name of a C variable |

**Examples:**

```yml
args:
    - literal: 4
    - literal: testString
    - variable: someVariable
```

The generated C++ constructor call may look like:

```C++
ProcessingNode<float32_t,7,float32_t,5> processing(fifo0,fifo1,4,"testString",someVariable);
```

##### `literal:`

It can be a scalar (int, float) or a string. I will be passed as it is to the API of the `C++` constructor.

##### `variable:`

It is the name of a C variable.
