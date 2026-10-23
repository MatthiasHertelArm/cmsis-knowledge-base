---
id: "ethu-hello-world"
type: "concept"
domain: "edge-ai"
title: "Hello World"
summary: "A small quantized neural network that approximates sin(x)."
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@cf13d8d:examples/Test-Ethos-U/Model/hello_world/README.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/cf13d8d/examples/Test-Ethos-U/Model/hello_world/README.md"
license: "Apache-2.0"
mode: "V"
---

A small quantized neural network that approximates `sin(x)`.

- **Input/output:** one `int8` value each.
- **Test vector:** input `-55` (about 1.794 radians), expected output `124`.
- **Validation:** exact output match.

`hello_world_int8.tflite` is the original model; `hello_world_int8_vela.tflite`
and `hello_world_model.c` contain the Vela-compiled model. The supplied output
is compiled for Ethos-U85-256 with shared SRAM. Regenerate it before running
on U55 or changing the memory configuration.

See [VELA_SUMMARY.md](https://github.com/ARM-software/CMSIS-Ethos-U/blob/cf13d8d/examples/Test-Ethos-U/Model/hello_world/VELA_SUMMARY.md) for compilation and memory details.
Enable `MODEL_HELLO_WORLD` in the combined
[ML layer](https://github.com/ARM-software/CMSIS-Ethos-U/blob/cf13d8d/examples/Test-Ethos-U/Model/hello_world/../ML-MyModels.clayer.yml) to run its `TestModel_Int8` call in
[app_main.cpp](https://github.com/ARM-software/CMSIS-Ethos-U/blob/cf13d8d/examples/Test-Ethos-U/Model/hello_world/../../Source/app_main.cpp). See the
[integration guide](https://github.com/ARM-software/CMSIS-Ethos-U/blob/cf13d8d/examples/Test-Ethos-U/Model/hello_world/../../README.md#integrate-a-new-model) for conversion and
adding models.
