---
id: "vela-vela-cli-options-verbose-print-options"
type: "concept"
domain: "edge-ai"
title: "Vela CLI Options: Verbose Print Options"
summary: "All of the options below are disabled by default and enabling them will add prints to standard out without any functional changes."
status: "draft"
collection: "ethos-u-vela"
source: "artificial-intelligence/ethos-u/ethos-u-vela@eb9cf0d:OPTIONS.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/eb9cf0d/OPTIONS.md#verbose-print-options"
license: "Apache-2.0"
mode: "V"
---

All of the options below are disabled by default and enabling them will add
prints to standard out without any functional changes.  

### Show Cpu Operations

Show the operations that fall back to the CPU.  

```bash
vela network.tflite --show-cpu-operations
```

### Show Subgraph IO Summary

**Deprecation notice:**
This option will be removed in next major release.

Prints a summary of all the subgraphs and their inputs and outputs.  

```bash
vela network.tflite --show-subgraph-io-summary
```

### Verbose All

Enable all `--verbose-*` options.  

```bash
vela network.tflite --verbose-all
```

### Verbose Config

Verbose system configuration and memory mode.  If no `--system-config` or
`--memory-mode` CLI options are specified then default values will be
displayed.  

```bash
vela network.tflite --verbose-config
```

### Verbose Graph

Displays two lists of operators. The first lists all of the operators that exist
in Vela's internal representation (Graph IR) of the Neural Network Graph (NNG)
before the graph optimisation process has run.  The second lists all of the
operators after that process.  The lists do not show the connectivity
information of the NNG and are unordered, therefore the execution order may
differ.  Each line in the list is of the format:  
`<num> <op_type> <op_name>`, where;  
num = an increasing operator count  
op_type = the Graph IR Operator Type  
op_name = the Graph IR Operator Name (this may have been derived from the
corresponding TFLite operator name)  

```bash
vela network.tflite --verbose-graph
```

### Verbose Quantization

Displays quantization information of all *weight*, *bias*, *input* and *output*
tensors for each operator in the Neural Network Graph (NNG).  The quantization
approximates floating point values as:
`approx_float_value = (integer_value - zero_point) * scale`
The information of each tensor is displayed in the format:
`<idx> <data_type> <min> <max> <scale> <zero_point> <name>`, where;  
idx = the tensor index on each operator  
min = the minimum floating point value before quantization  
max = the maximum floating point value before quantization  
scale = the quantization scaling, zero_point = the quantization zero point  
name = the name of the tensor  

```bash
vela network.tflite --verbose-quantization
```

### Verbose Packing

**Deprecation notice:**
This option will be removed in next major release.

Displays a list of passes where a pass represents one or more Graph IR operators
that are run together as one hardware operation e.g. a pass could be a
convolution operator fused with a hardswish activation.  Each line of the list
has the format:  
`<id> <pass>`, where;  
id = an increasing pass count  
pass = name of the pass (usually derived from the first operator in the pass)  

```bash
vela network.tflite --verbose-packing
```

### Verbose Performance

Verbose per-layer Performance. Please see
[Vela Performance Estimation Summary](https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/eb9cf0d/PERFORMANCE.md)
for a detailed explanation.  

```bash
vela network.tflite --verbose-performance
```

### Verbose Tensor Purpose

**Deprecation notice:**
This option will be removed in next major release.

Displays a list of all operators and the tensors that are connected to them.
Additional information is shown about the tensors. The format is:
`<num> `<op_type>` `<op_name>` `<direction>` `<idx>` 
 `<mem_area>` `<mem_type>`
<tens>`, where;  
num = an increasing operator count  
op_type = the Graph IR Operator Type  
op_name = the Graph IR Operator Name (this may have been derived from the
corresponding TFLite operator name)  
direction = either *Input* or *Output* and indicates the connection direction of
the tensor with respect 
idx = the index position where on each operator  
purpose = purpose of the tensor (weight, bias, feature map, etc.)  
mem_area = assigned memory area (for example SRAM or Flash)  
mem_type = memory type (i.e. Scratch or Permanent NPU)  
tens = string representation of the tensor containing its name, shape and data
type  

```bash
vela network.tflite --verbose-tensor-purpose
```

### Verbose Schedule

Display all schedule operations which contain information about the operator
type, block config, stripe sizes, size of encoded weights, size of weight
buffers, depth slices, cascade assignment and SRAM usage. The purpose of the
scheduler is to come up with an execution plan for the network. It will make
decisions on how to split an operator execution into stripes, group operators
together in cascades to either reduce SRAM footprint or, in a multi-level
memory system, better utilize the SRAM. The scheduler will also decide in what
memory to put tensors as well as how to buffer data from a slower memory like
Flash/DRAM to SRAM.

Feature maps can be split up into horizontal subsections called stripes that
allow us to apply operators independently to smaller sections of feature maps.
The output stripes that are produced can fit into a smaller buffer than the
output of a full feature map would, which combined with cascading can reduce
memory usage.

A cascade is a group of operators that will be computed interleaved in stripes.
Instead of storing the full output of an operator applied on a whole feature
map, we calculate the smallest possible buffer that allows storing intermediate
results of enough output stripes of one operator to allow the consecutive
operator to calculate one output stripe. Then, the consumed parts of the buffer
that is no longer needed by the consecutive operator in the cascade can be
overwritten by a new output stripe of the first operator, allowing us to reuse
and reduce the memory usage.  

```bash
vela network.tflite --verbose-schedule
```

### Verbose Allocation

This option displays tensor allocation information in separate tables for each
type of memory area. Each table contains information about each tensor's start
and end time, address, size and purpose as well as the memory usage during the
each tensors live range. The start- and end time denotes the time steps during
when the tensor needs to be allocated in the memory. After the end time, the
addresses are allowed to be overwritten by other tensors. The reported memory
usage is the peak usage at any time step of the tensors live range, which means
that the maximum memory usage value of all tensors will be the minimum required
size to fit the proposed allocation.  

```bash
vela network.tflite --verbose-allocation
```

### Verbose High Level Command Stream

Display an enumerated list of High-Level (HL) commands in execution
order.  There are three types of command and each one displays individual
information:

* NPU Stripe = `<name> `<ifm_box>` `<ifm2_box>` `<ofm_box>` `<weight_box>`
<block_config>`, represents a data processing operation that maps directly to
a single Ethos-U operation where;  
name = name of the pass that corresponds to this HL command (not unique)  
ifm_box = part of the IFM in NHWC format  
ifm2_box = part of the IFM2 in NHWC format (is empty [] when not present)  
ofm_box = part of the OFM in NHWC format  
weight_box = part of the filter kernel in NHWC format  
block_config = block processing size in HWIO format

* DMA = `<in> <out> <box>`, represents a memory copy operation from source to
destination where;  
name = name of the pass that corresponds to this HL command (not unique)  
in = name of the source tensor  
out = name of the destination tensor  
box = part of the source tensor in NHWC format

* NOP = `<in> <out>`, represents a memory copy operation that has source equal
to destination and therefore does nothing, where;  
name = name of the pass that corresponds to this HL command (not unique)  
in = name of the input tensor  
out = name of the output tensor

```bash
vela network.tflite --verbose-high-level-command-stream
```

### Verbose Register Command Stream

Display two groups of information.  The first group is the input to the register
command stream generator.  The second group is the output of the register
command stream generator:

* Input = an enumerated list of the High-Level commands that are the input to
the generator.  Each command details all of its attributes.

* Output = a disassembly of the Ethos-U command stream (referred to as the
register command stream).  More information about the commands listed in the
register command stream can be found in the Arm Ethos-U NPU Technical Reference
Manuals that are available from the Arm Developer website (see
[README - Resources](https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/eb9cf0d/README.md#resources)).

```bash
vela network.tflite --verbose-register-command-stream
```

### Verbose Operators

**Deprecation notice:**
This option will be removed in next major release.

Display a list of all operators in the neural network graph along with their
attributes before any optimization is made by Vela.  

```bash
vela network.tflite --verbose-operators
```

### Verbose Weights

Displays the size of the *Original* and *Ethos-U NPU Encoded* weights as part of
the final summary information.  The *original* weights size refers to the size
of the weights as read from the input `.tflite` file.  The *NPU Encoded* weights
size refers to the total size of all of the weight tensors after they have been
reordered, padded and encoded for the operators that run on the Ethos-U.  

```bash
vela network.tflite --verbose-weights
```

### Verbose cycle estimate

Displays the cycle estimate of inference as part of the final summary information.  
The estimates include number of cycles per batch for NPU, memory accesses and in
total.  
__NOTE: This is only an estimate. For performance numbers we recommend running
the compiled network on an FVP Model or FPGA.__  

```bash
vela network.tflite --verbose-cycle-estimate
```

### Verbose Progress

**Deprecation notice:**
This option will be removed in next major release.

This option displays progress information of the most time consuming parts of
the compiler driver and scheduler.  

```bash
vela network.tflite --verbose-progress
```

### Experimental: int16 Softmax negative exponential range

Adjusts the negative-exponential lookup table (LUT) range used by the int16
Softmax graph optimisation.

**Note:** The default value is `10.0`. Values other than `10.0` are
experimental, have not been validated, and may reduce numerical correlation
with the reference kernel. The value must be greater than `0` and
less than `65535`.

**Type: Float**  
**Default: 10.0**  
**Range: (0, 65535)**

```bash
vela network.tflite --experimental-softmax-int16-neg-exp-range 10.0
````

### Debug force legacy core

**Deprecation notice:**
This option will be removed in next major release.

Force Ethos-U55 or Ethos-U65 to use the deprecated legacy compilation path
(TFLite only).

```bash
vela network.tflite --debug-force-legacy-core
```

### Debug force regor

**Deprecation notice:**
This option will be removed in next major release.

Regor is the default for all targets, and this option no longer has any effect.
Use `--debug-force-legacy-core` to force the legacy compilation path
(Ethos-U55 or Ethos-U65 and TFLite only).

```bash
vela network.tflite --debug-force-regor
```

### Disable chaining

Disable use of chaining buffers when using the Regor compilation path.

```bash
vela network.tflite --disable-chaining
```

### Disable Fast Weight Decoder

Disable use of the Fast Weight Decoder core when using the Regor compilation path.

```bash
vela network.tflite --disable-fwd
```

### Disable cascading

Disable cascading of operators when using the Regor compilation path.

```bash
vela network.tflite --disable-cascading
```

### Disable Buffering

Disable buffering of weights to faster memory when using the Regor compilation path.

```bash
vela network.tflite --disable-buffering
```
