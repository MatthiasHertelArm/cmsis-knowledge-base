---
id: "ethu-test-ethos-u-recompile-the-models"
type: "concept"
domain: "edge-ai"
title: "Test-Ethos-U: Recompile the models"
summary: "The model converter reads the generated .cbuild-mlops.yml file and recompiles the selected quantized models with the Vela settings for that solution. For prerequisites, command-line and VS Code usage, configuration overrides, and generated files, see the LiteRT model converter documentation."
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@cf13d8d:examples/Test-Ethos-U/README.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/cf13d8d/examples/Test-Ethos-U/README.md#recompile-the-models"
license: "Apache-2.0"
mode: "V"
---

The model converter reads the generated `*.cbuild-mlops.yml` file and recompiles
the selected quantized models with the Vela settings for that solution. For
prerequisites, command-line and VS Code usage, configuration overrides, and
generated files, see the [LiteRT model converter documentation](https://github.com/ARM-software/CMSIS-Ethos-U/blob/cf13d8d/examples/Test-Ethos-U/script/README.md).

```console
python script/model-converter.py Test-Ethos-U85.cbuild-mlops.yml
```
