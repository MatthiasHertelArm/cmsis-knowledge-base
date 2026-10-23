---
id: "ethint-litert-model-converter-exit-status-and-errors"
type: "concept"
domain: "edge-ai"
title: "LiteRT model converter: Exit status and errors"
summary: "The converter validates configuration files, directories, and models before starting Vela. Common errors include:"
status: "draft"
collection: "cmsis-ethos-integration"
source: "Arm-Examples/CMSIS-Ethos-Integration@9b906f5:script/README.md"
doc_source: "https://github.com/Arm-Examples/CMSIS-Ethos-Integration/blob/9b906f5/script/README.md#exit-status-and-errors"
license: "Apache-2.0"
mode: "V"
---

- `0`: all models were converted.
- `1`: Vela or output generation failed.
- `2`: command-line or YAML configuration is invalid.

The converter validates configuration files, directories, and models before
starting Vela. Common errors include:

- Vela is missing from `PATH`;
- `model.dir`, a model, or the Vela INI file does not exist;
- `model.name` is missing, empty, or malformed; and
- a model path escapes `model.dir`.
