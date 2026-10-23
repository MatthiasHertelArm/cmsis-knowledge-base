---
id: "ethu-cmsis-mlops-litert-model-converter-input-from-cbuild-mlops-yml"
type: "concept"
domain: "edge-ai"
title: "CMSIS MLOps LiteRT model converter specification: Input from `*.cbuild-mlops.yml`"
summary: "Paths in the generated file are relative to the directory containing the .cbuild-mlops.yml file."
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@cf13d8d:examples/Test-Ethos-U/script/model-converter-specification.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/cf13d8d/examples/Test-Ethos-U/script/model-converter-specification.md#input-from-cbuild-mlops-yml"
license: "Apache-2.0"
mode: "V"
---

The script reads these nodes:

```text
cbuild-mlops.vela.ini
cbuild-mlops.vela.options
cbuild-mlops.vela.misc
cbuild-mlops.model.dir
cbuild-mlops.model.name
```

Paths in the generated file are relative to the directory containing the
`*.cbuild-mlops.yml` file.

`model.dir` is the working directory for model conversion. It contains the
input models and receives the Vela output.

`model.name` selects the models to convert and shall be either:

- a non-empty string selecting one model; or
- a non-empty list of strings selecting multiple models.

Each model path is relative to `model.dir`. Lists are processed in their
declared order. For example:

```yaml
model:
  name:
    - hello_world/hello_world_int8.tflite
    - tiny_cnn/tiny_cnn_int8.tflite
```
