---
id: "ethint-litert-model-converter-mlops-input"
type: "concept"
domain: "edge-ai"
title: "LiteRT model converter: MLOps input"
summary: "The generated .cbuild-mlops.yml supplies the Vela configuration and model selection:"
status: "draft"
collection: "cmsis-ethos-integration"
source: "Arm-Examples/CMSIS-Ethos-Integration@9b906f5:script/README.md"
doc_source: "https://github.com/Arm-Examples/CMSIS-Ethos-Integration/blob/9b906f5/script/README.md#mlops-input"
license: "Apache-2.0"
mode: "V"
---

The generated `*.cbuild-mlops.yml` supplies the Vela configuration and model
selection:

```yaml
cbuild-mlops:
  vela:
    ini: Model/vela.ini
    options: >-
      --accelerator-config ethos-u55-128
      --system-config Ethos_U55_High_End_Embedded
      --memory-mode Shared_Sram
    misc: --verbose-all
  model:
    dir: Model
    name: tiny_cnn/tiny_cnn_int8.tflite
```

Paths are resolved relative to the directory containing the MLOps file.

The converter uses from the `*.cbuild-mlops.yml` file the following nodes:

- `vela.ini` as Vela's configuration file when present;
- `vela.options` for generated Vela arguments;
- `vela.misc` for optional additional Vela arguments;
- `model.dir` as the model working directory; and
- `model.name` to select one or more input models.
