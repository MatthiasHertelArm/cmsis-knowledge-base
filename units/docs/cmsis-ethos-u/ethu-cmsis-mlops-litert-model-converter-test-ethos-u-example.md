---
id: "ethu-cmsis-mlops-litert-model-converter-test-ethos-u-example"
type: "concept"
domain: "edge-ai"
title: "CMSIS MLOps LiteRT model converter specification: Test-Ethos-U example"
summary: "Test-Ethos-U55.csolution.yml illustrates the input that CMSIS-Toolbox copies to the generated .cbuild-mlops.yml file:"
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@cf13d8d:examples/Test-Ethos-U/script/model-converter-specification.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/cf13d8d/examples/Test-Ethos-U/script/model-converter-specification.md#test-ethos-u-example"
license: "Apache-2.0"
mode: "V"
---

`Test-Ethos-U55.csolution.yml` illustrates the input that CMSIS-Toolbox copies
to the generated `*.cbuild-mlops.yml` file:

```yaml
model:
  dir: Model
  name:
    - hello_world/hello_world_int8.tflite
    - tiny_cnn/tiny_cnn_int8.tflite
```

The example uses a sequence because it always converts both models. Other
projects may use a string-valued `name` when converting one model.
