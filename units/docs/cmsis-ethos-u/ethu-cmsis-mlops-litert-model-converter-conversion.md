---
id: "ethu-cmsis-mlops-litert-model-converter-conversion"
type: "concept"
domain: "edge-ai"
title: "CMSIS MLOps LiteRT model converter specification: Conversion"
summary: "For every selected model, the script invokes the equivalent of:"
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@cf13d8d:examples/Test-Ethos-U/script/model-converter-specification.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/cf13d8d/examples/Test-Ethos-U/script/model-converter-specification.md#conversion"
license: "Apache-2.0"
mode: "V"
---

For every selected model, the script invokes the equivalent of:

```console
vela --config <vela.ini> <vela.options> <model> --output-dir <temporary-directory>
```

The input path is resolved below `model.dir`. The script rejects a path that
escapes this directory. It accepts any `.tflite` filename; an `_int8` suffix is
not required.

Before invoking Vela, the script validates the MLOps YAML, Vela INI file, model
directory, and every input model. It stops with a nonzero status when
validation or conversion fails, while preserving Vela output for diagnosis.
