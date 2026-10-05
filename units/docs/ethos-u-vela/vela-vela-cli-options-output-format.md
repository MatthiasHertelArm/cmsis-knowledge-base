---
id: "vela-vela-cli-options-output-format"
type: "concept"
domain: "edge-ai"
title: "Vela CLI Options: Command Line Interface / Output format"
summary: "Selects output format. The available options are tflite and raw."
status: "draft"
collection: "ethos-u-vela"
source: "artificial-intelligence/ethos-u/ethos-u-vela@eb9cf0d:OPTIONS.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/eb9cf0d/OPTIONS.md#output-format"
license: "Apache-2.0"
mode: "V"
---

_Part of: Command Line Interface_

Selects output format. The available options are `tflite` and `raw`.

The `tflite` format produces a `.tflite` file containing Ethos-U custom
operators for each group of NPU operators​ with command streams and driver
action commands attached as well as the required tensor, buffer and operator
lists. If any operators fall back to the CPU, they are included in this file
as well.

The `raw` format produces an [`.npz`](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.html#module-numpy.lib.format)
file containing the same information as the `tflite` format, but more easily
accessible. When loaded with NumPy, the arrays can be accessed by name with the
keys listed below.  
**Raw format keys:**  
- **cmd_data** - The command stream data and metadata for the driver.
- **weight_data** - The encoded weight, scale & bias, and constant data.
- **weight_region** - Memory region identifier for the weights.
- **scratch_shape / scratch_fast_shape** - The shape of the scratch and fast
scratch buffers.
- **scratch_region / scratch_fast_region** - Memory region identifiers for the
scratch and fast scratch buffers.
- **scratch_size / scratch_fast_size** - The total size of each scratch buffer
(in bytes).
- **input_shape / output_shape / variable_shape** - Per-tensor shapes for inputs,
outputs and variable tensors.
- **input_elem_size / output_elem_size / variable_elem_size** - Element sizes (in
bytes) for each input, output and variable tensor.
- **input_region / output_region / variable_region** - Memory region identifiers
for inputs, outputs and variables.
- **input_offset / output_offset / variable_offset** - Memory offsets for each
input, output and variable tensor.
- **input_quantization / output_quantization / variable_quantization** - Per-tensor quantization entries with `quant_type` (`per_tensor`, `per_channel`, or `none`), `scale`, and `zero_point`.

For this format, it is not supported to have any operators fall back to the CPU.

**Type: String**  
**Default: tflite**  
**Choices: [tflite, raw]**  

```bash
vela network.tflite --accelerator-config ethos-u85-512 --output-format raw
```
