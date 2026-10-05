---
id: "stream-table-of-content-yaml-for-the-configuration"
type: "concept"
domain: "cmsis-stream"
title: "Table of content: YAML for the configuration"
summary: "The table below explains the top-level elements of the yml configuration description."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/YAML.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/YAML.md#yaml-for-the-configuration"
license: "Apache-2.0"
mode: "V"
---

The table below explains the top-level elements of the yml configuration description.

| Keyword                                                      | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`version:`](#version)                                       | Version of the Compute graph YAML format used by this file   |
| [`schedule-options:`](#schedule-options)                     | Options used for the computation of the synchronous scheduling |
| [`code-generation-options:`](#code-generation-options)       | Common code generation options                               |
| [`c-code-generation-options:`](#c-code-generation-options)   | Options for the C++ code generation                          |
| [`python-code-generation-options:`](#python-code-generation-options) | Options for the Python code generation                       |
| [`graphviz-code-generation-options:`](#graphviz-code-generation-options) | Options for the graphviz generation                          |

### `schedule-options:`

| Keyword                                                      | Description                                              |
| ------------------------------------------------------------ | -------------------------------------------------------- |
| [`memory-optimization:`](https://github.com/ARM-software/CMSIS-DSP/blob/main/ComputeGraph/documentation/SchedOptions.md#memoryoptimization-default--false) | Enable memory optimization                               |
| [`sink-priority:`](https://github.com/ARM-software/CMSIS-DSP/blob/main/ComputeGraph/documentation/SchedOptions.md#sinkpriority-default--true) | Enable sink prioritization                               |
| [`display-fifo-sizes:`](https://github.com/ARM-software/CMSIS-DSP/blob/main/ComputeGraph/documentation/SchedOptions.md#displayfifosizes-default--false) | Display FIFO sizes during schedule computation           |
| [`dump-schedule:`](https://github.com/ARM-software/CMSIS-DSP/blob/main/ComputeGraph/documentation/SchedOptions.md#dumpschedule-default--false) | Dump the schedule at the end of the schedule computation |

### `code-generation-options:`

| Keyword                                                      | Description                                      |
| ------------------------------------------------------------ | ------------------------------------------------ |
| [`debug-limit:`](https://github.com/ARM-software/CMSIS-DSP/blob/main/ComputeGraph/documentation/CodegenOptions.md#debuglimit-default--0) | Number of schedule iterations (used for debug)   |
| [`dump-fifo:`](https://github.com/ARM-software/CMSIS-DSP/blob/main/ComputeGraph/documentation/CodegenOptions.md#dumpfifo-default--false) | Dump of FIFO content at runtime (used for debug) |
| [`scheduler-name:`](https://github.com/ARM-software/CMSIS-DSP/blob/main/ComputeGraph/documentation/CodegenOptions.md#schedname-default--scheduler) | Name of the scheduler function                   |
| [`fifo-prefix:`](https://github.com/ARM-software/CMSIS-DSP/blob/main/ComputeGraph/documentation/CodegenOptions.md#prefix-default--) | Prefix for naming FIFO global buffers.           |

### `c-code-generation-options:`

| Keyword                                                      | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`c-optional-args:`](https://github.com/ARM-software/CMSIS-DSP/blob/main/ComputeGraph/documentation/CCodeGen.md#coptionalargs-default--) | Arguments of the C API of the scheduler                      |
| [`switch-case:`](https://github.com/ARM-software/CMSIS-DSP/blob/main/ComputeGraph/documentation/CCodeGen.md#switchcase-default--true) | Don't unroll the schedule. Schedule is implemented as a switch / case |
| [`event-recorder:`](https://github.com/ARM-software/CMSIS-DSP/blob/main/ComputeGraph/documentation/CCodeGen.md#eventrecorder-default--false) | Enable event recorder calls in the generated schedule        |
| [`app-config-c-name:`](https://github.com/ARM-software/CMSIS-DSP/blob/main/ComputeGraph/documentation/CCodeGen.md#appconfigcname-default--app_config) | Name of the custom include file                              |
| [`post-custom-c-name:`](https://github.com/ARM-software/CMSIS-DSP/blob/main/ComputeGraph/documentation/CCodeGen.md#postcustomcname-default--) | Name of a custom include file following all other include files |
| [`generic-node-c-name:`](https://github.com/ARM-software/CMSIS-DSP/blob/main/ComputeGraph/documentation/CCodeGen.md#genericnodecname-default--genericnodesh) | Name of the include file containing the generic nodes (part of the pack) |
| [`app-nodes-c-name:`](https://github.com/ARM-software/CMSIS-DSP/blob/main/ComputeGraph/documentation/CCodeGen.md#appnodescname-default--appnodesh) | Name of the include file containing the application nodes    |
| [`scheduler-c-file-name:`](https://github.com/ARM-software/CMSIS-DSP/blob/main/ComputeGraph/documentation/CCodeGen.md#schedulercfilename-default--scheduler) | Name of the files containing the code for the scheduler and header for the scheduler |
| [`c-api:`](https://github.com/ARM-software/CMSIS-DSP/blob/main/ComputeGraph/documentation/CCodeGen.md#capi-default--true) | True when the API of the scheduler is callable from C        |
| [`cmsis-dsp:`](https://github.com/ARM-software/CMSIS-DSP/blob/main/ComputeGraph/documentation/CCodeGen.md#cmsisdsp-default--true) | True when CMSIS-DSP headers are included                     |
| [`asynchronous:`](https://github.com/ARM-software/CMSIS-DSP/blob/main/ComputeGraph/documentation/CCodeGen.md#asynchronous-default--false) | True when asynchronous mode is enabled                       |
| [`fifo-increase:`](https://github.com/ARM-software/CMSIS-DSP/blob/main/ComputeGraph/documentation/CCodeGen.md#fifoincrease-default-0) | In asynchronous mode, increase all FIFO sizes globally       |
| [`async-default-skip:`](https://github.com/ARM-software/CMSIS-DSP/blob/main/ComputeGraph/documentation/CCodeGen.md#asyncdefaultskip-default-true) | Behavior of `Duplicate` nodes in asynchronous mode           |
| [`heap-allocation`](https://github.com/ARM-software/CMSIS-DSP/blob/main/ComputeGraph/documentation/CCodeGen.md#heapallocation-default-false) | Enable the heap allocation mode. When enabled, FIFOs and nodes are allocated on the heap. |
| [`node-identification`](https://github.com/ARM-software/CMSIS-DSP/blob/main/ComputeGraph/documentation/CCodeGen.md#nodeidentification-default-false) | When enabled, a new API is generated. This new API enables to identify and access nodes from the outside of the scheduler. |
| fully-asynchronous:(https://github.com/ARM-software/CMSIS-DSP/blob/main/ComputeGraph/documentation/CCodeGen.md#fullyasynchronous-default-false) | True when the `fullyAsynchronous` mode is enabled.           |

### `python-code-generation-options:`

| Keyword                                                      | Description                                   |
| ------------------------------------------------------------ | --------------------------------------------- |
| [`py-optional-args:`](https://github.com/ARM-software/CMSIS-DSP/blob/main/ComputeGraph/documentation/PythonGen.md#pyoptionalargs-default--) | Arguments for the Python API of the scheduler |
| [`custom-python-name:`](https://github.com/ARM-software/CMSIS-DSP/blob/main/ComputeGraph/documentation/PythonGen.md#custompythonname-default--custom) | Name of the custom python file                |
| [`app-nodes-python-name:`](https://github.com/ARM-software/CMSIS-DSP/blob/main/ComputeGraph/documentation/PythonGen.md#appnodespythonname-default--appnodes) | Name of the python application node files     |
| [`scheduler-python-file-name:`](https://github.com/ARM-software/CMSIS-DSP/blob/main/ComputeGraph/documentation/PythonGen.md#schedulerpythonfilename-default--sched) | Name of the python scheduler file             |

### `graphviz-code-generation-options:`

| Keyword                                                      | Description                                     |
| ------------------------------------------------------------ | ----------------------------------------------- |
| [`horizontal:`](https://github.com/ARM-software/CMSIS-DSP/blob/main/ComputeGraph/documentation/GraphvizGen.md#horizontal-default--true) | Horizontal layout for the graph                 |
| [`display-fifo-buf:`](https://github.com/ARM-software/CMSIS-DSP/blob/main/ComputeGraph/documentation/GraphvizGen.md#displayfifobuf-default--false) | Display FIFO buffer ID instead of the FIFO size |
