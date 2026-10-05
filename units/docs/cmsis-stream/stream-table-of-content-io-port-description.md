---
id: "stream-table-of-content-io-port-description"
type: "concept"
domain: "cmsis-stream"
title: "Table of content: IO Port Description"
summary: "Description of an IO port on a node. There are two versions. For normal modes it is a list of input: or output: fields in the YAML."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/YAML.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/YAML.md#io-port-description"
license: "Apache-2.0"
mode: "V"
---

Description of an IO port on a node. There are two versions. For normal modes it is a list of `input:` or `output:` fields in the YAML.

But for the nodes inheriting from `GenericToManyNode`, `GenericFromManyNode`, `GenericManyToManyNode`, we can have a list of homogeneous inputs or outputs. This must be described in the YAML since those IOs are not managed in the same way in the generated C code.

### Normal input or output:

| Keyword                | Content                                |
| ---------------------- | -------------------------------------- |
| `input:` or `output:`  | Name of the IO port.                   |
| [`samples:`](#samples) | Number of samples produced or consumed |
| [`type:`](#type)       | Data type for the samples              |

**Examples:**

```yml
- input: i
  samples: 7
  type: float32_t
```

```yml
- output: o
  samples: 5
  type: float32_t
```

### `input:` or `output:`

Name of the IO port. It must be a valid Python property name that is not already used by the Python root class.

### `samples:`

Number of samples produced on an output or consumed on an input.

In case of an asynchronous scheduling, it represents the ideal or average case.

In case of cyclo-static scheduling, this is a list encoding the sequence of generated values.

**Examples**

```yml
inputs:
    - input: i
      samples: 800
      type: int16_t
```

For cyclo-static scheduling:

```yml
outputs:
    - output: o
      samples:
      - 185
      - 185
      - 185
      - 180
      type: int16_t
```

### `type:`

Data type for the samples. It can be a scalar data type as defined in CMSIS-DSP:

* `float64_t`
* `float32_t`
* `float16_t`
* `q31_t`
* `q15_t`
* `q7_t`
* `uint32_t`
* `uint16_t`
* `uint8_t`
* `sint32_t`
* `sint16_t`
* `sint8_t`

It can also be more complex datatypes defined with a C struct. More complex datatypes have to be define at the beginning of the graph description using the [`structures:`](#structures) field.

### Input or output list

| Keyword                | Content                                     |
| ---------------------- | ------------------------------------------- |
| [`samples:`](#samples) | Number of samples produced or consumed      |
| [`type:`](#type)       | Data type for the samples                   |
| names:                 | List of input names or list of output names |

**Examples**

```yml
outputs:
      samples: 5
      type: float
      names:
      - oa
      - ob
      - oc
      - od
      - oe
```

In this example, an output list is used. The YAML entry `outputs` is no more containing a list of `output:` entries that would correspond to different kind of output ports.

Here we have a list of output of the same nature : number of samples and types. The `samples:` and `type:` fields are shared between all outputs and only the list of output names is used.

A list of inputs would be described similarly in the `inputs:` section.

When a list of inputs (or list of output) is used, you cannot use any more the `input:` or `output:` entries.

When a list of inputs and/or outputs is used, the node will be recognized (at import) as a special node like `GenericManyToMany` etc ...
