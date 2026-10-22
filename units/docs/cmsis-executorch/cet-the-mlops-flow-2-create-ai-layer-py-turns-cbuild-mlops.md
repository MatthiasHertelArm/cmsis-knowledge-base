---
id: "cet-the-mlops-flow-2-create-ai-layer-py-turns-cbuild-mlops"
type: "concept"
domain: "edge-ai"
title: "The MLOps flow: 2. `create_ai_layer.py` turns `*.cbuild-mlops.yml` into the AI layer"
summary: "python create_ai_layer.py cmsis-executorch.cbuild-mlops.yml stands in for an MLOps system. It reads the file and:"
status: "draft"
collection: "cmsis-executorch"
source: "Arm-Examples/CMSIS-Executorch@0a243f1:documentation/mlops-flow.md"
doc_source: "https://github.com/Arm-Examples/CMSIS-Executorch/blob/0a243f1/documentation/mlops-flow.md#2-create-ai-layer-py-turns-cbuild-mlops-yml-into-the-ai-layer"
license: "Apache-2.0"
mode: "V"
---

`python create_ai_layer.py cmsis-executorch.cbuild-mlops.yml` stands in
for an MLOps system. It reads the file and:

1. builds ExecuTorch's `EthosUCompileSpec` from `npu:` and `vela:` -- the
   accelerator (`ethos-u85-256`), system config and memory mode come from
   there, and every other option in `vela.options` (the `misc:` of the
   csolution's `vela:` node) reaches Vela as an extra flag, so the Python code
   contains no NPU configuration;
2. exports `model/model.py`: quantizes it, delegates the whole graph to the
   Ethos-U and compiles it with Vela;
3. reads the operators the resulting program still calls on the CPU and looks
   up the matching components in the `PyTorch::ExecuTorch` pack (the version
   `cbuild setup` resolved, from `*.cbuild-pack.yml`);
4. writes the layer into the directory of `model.clayer`:

| File | Content |
|------|---------|
| `ai_layer/ai_layer.clayer.yml` | runtime, kernel utilities and registration, Ethos-U backend and the operator components the program uses |
| `ai_layer/model_pte.c` / `.h` | the program as a 16-byte-aligned C array, `model_pte` / `model_pte_size` |
| `ai_layer/model.pte` | the program itself, for inspection (not committed) |

The clayer and the C array are committed, so a checkout builds without
Python. For a fully delegated model the component list is short: `Runtime`,
`Kernel Utils`, `Kernel Registration`, `Backend EthosU`, and the int8 boundary
`Quantized quantize` / `Quantized dequantize` operators. Everything else in
the pack is never compiled, let alone linked.
