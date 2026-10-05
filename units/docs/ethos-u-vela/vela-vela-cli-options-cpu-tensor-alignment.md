---
id: "vela-vela-cli-options-cpu-tensor-alignment"
type: "concept"
domain: "edge-ai"
title: "Vela CLI Options: Command Line Interface / CPU Tensor Alignment"
summary: "Controls the allocation byte alignment. This affects all CPU tensors including Ethos-U Custom operator inputs and outputs. In this instance a CPU tensor is defined as any tensor that is explicitly listed in the resulting .tflite file."
status: "draft"
collection: "ethos-u-vela"
source: "artificial-intelligence/ethos-u/ethos-u-vela@eb9cf0d:OPTIONS.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/eb9cf0d/OPTIONS.md#cpu-tensor-alignment"
license: "Apache-2.0"
mode: "V"
---

_Part of: Command Line Interface_

Controls the allocation byte alignment.  This affects all CPU tensors including
Ethos-U Custom operator inputs and outputs.  In this instance a CPU tensor is
defined as any tensor that is explicitly listed in the resulting `.tflite` file.
The Ethos-U NPU internal tensors will remain 16-byte aligned independent of this
option, these tensors are contained within the command stream.  Alignment has to
be a power of two and greater or equal to 16.  
**Type: Integer**  
**Default: 16**  

```bash
vela network.tflite --cpu-tensor-alignment 128
```
