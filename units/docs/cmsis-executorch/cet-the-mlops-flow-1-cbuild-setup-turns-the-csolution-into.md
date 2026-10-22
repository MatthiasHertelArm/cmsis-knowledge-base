---
id: "cet-the-mlops-flow-1-cbuild-setup-turns-the-csolution-into"
type: "concept"
domain: "edge-ai"
title: "The MLOps flow: 1. `cbuild setup` turns the csolution into `*.cbuild-mlops.yml`"
summary: "The csolution is the only place where the NPU is described:"
status: "draft"
collection: "cmsis-executorch"
source: "Arm-Examples/CMSIS-Executorch@0a243f1:documentation/mlops-flow.md"
doc_source: "https://github.com/Arm-Examples/CMSIS-Executorch/blob/0a243f1/documentation/mlops-flow.md#1-cbuild-setup-turns-the-csolution-into-cbuild-mlops-yml"
license: "Apache-2.0"
mode: "V"
---

The csolution is the only place where the NPU is described:

```yaml
solution:
  mlops:
    description: TinyCNN int8 image classifier for Ethos-U85
    npu:
      type: Ethos-U85
    vela:
      system: Ethos_U85_SYS_DRAM_Mid   # system-config from the Vela config
      memory: Shared_Sram              # memory-mode from the Vela config
    model:
      clayer: $AI-Layer$
      name: TinyCNN
      input-shape: 1x16x16x3           # passed through to create_ai_layer.py
      calibration-samples: 2
```

CMSIS-Toolbox detects the `simulator:` target (and, for a board, the
`hardware:` target) from the target-sets, and passes the extra keys under
`model:` through unchanged.

`cbuild setup cmsis-executorch.csolution.yml --active SSE-320-U85`
resolves it for the active target and writes
`cmsis-executorch.cbuild-mlops.yml`:

```yaml
cbuild-mlops:
  generated-by: csolution version 2.15.1+p3-gf46d68bf
  description: TinyCNN int8 image classifier for Ethos-U85
  processor:
    type: Cortex-M85
  npu:
    type: Ethos-U85
  vela:
    options: --system-config Ethos_U85_SYS_DRAM_Mid --memory-mode Shared_Sram
  model:
    clayer: ai_layer/ai_layer.clayer.yml
    name: TinyCNN
    input-shape: 1x16x16x3
    calibration-samples: 2
  simulator:
    active: SSE-320-U85
    cbuild-run: out/cmsis-executorch+SSE-320-U85.cbuild-run.yml
    output:
      - file: out/cmsis-executorch/SSE-320-U85/Debug/cmsis-executorch.axf
        type: elf
    model: FVP_Corstone_SSE-320
    config-file: board/Corstone-320/fvp_config.txt
```

The SSE-320 device family pack declares no NPU, so `npu:` is written out in
full here. A device pack that does (the Alif Ensemble pack, for one) supplies
the NPU type, the MAC count and its own Vela configuration file, and the
toolbox then also emits `npu.macs`, `vela.ini` and `--accelerator-config`.
The `simulator:` section is what a test runner needs to execute the image
on the FVP.

This is the hand-over point to the MLOps side: everything a model-export
pipeline needs to know about the target is in this one file, and nothing in it
is specific to this template's Python code.

`cbuild setup` writes the file even when the AI layer does not exist yet, so
the flow also works on a checkout without a generated layer.
