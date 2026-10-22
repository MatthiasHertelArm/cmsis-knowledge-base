---
id: "cet-executorch-on-ethos-u-how-ml-model-generation-works"
type: "concept"
domain: "edge-ai"
title: "ExecuTorch on Ethos-U: How ML model generation works"
summary: "The target is described by the mlops: node in cmsis-executorch.csolution.yml:"
status: "draft"
collection: "cmsis-executorch"
source: "Arm-Examples/CMSIS-Executorch@0a243f1:README.md"
doc_source: "https://github.com/Arm-Examples/CMSIS-Executorch/blob/0a243f1/README.md#how-ml-model-generation-works"
license: "Apache-2.0"
mode: "V"
---

The target is described by the `mlops:` node in
`cmsis-executorch.csolution.yml`:

```yaml
mlops:
  npu:
    type: Ethos-U85
  vela:
    system: Ethos_U85_SYS_DRAM_Mid
    memory: Shared_Sram
  model:
    clayer: $AI-Layer$
    name: TinyCNN
    input-shape: 1x16x16x3
    calibration-samples: 2
```

`cbuild setup --active SSE-320-U85` resolves it into
`cmsis-executorch.cbuild-mlops.yml`, which contains the processor, NPU
and Vela options, and the FVP simulation target-set as the `simulator:` to test
on.
`create_ai_layer.py` reads those options and passes all of them to ExecuTorch's
`EthosUCompileSpec`, so the target configuration is never duplicated in
Python. The two extra keys under `model:` are parameters of the ML model itself;
the toolbox passes them through and the script hands them to `model/model.py`.
The script then writes:

- `ai_layer/ai_layer.clayer.yml`: the CMSIS components required by the ML model.
- `ai_layer/model_pte.c` and `model_pte.h`: the ExecuTorch program embedded as a C array.
- `ai_layer/model.pte`: the program itself, for inspection.

See [the MLOps flow](https://github.com/Arm-Examples/CMSIS-Executorch/blob/0a243f1/documentation/mlops-flow.md) for a detailed walkthrough.
